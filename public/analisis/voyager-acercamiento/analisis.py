# importo herramientas de la biblioteca estándar para evitar dependencias externas
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import math
import statistics
import hashlib

# fijo el directorio de trabajo y conservo separados datos, fuentes y resultados
raiz = Path.cwd()
resultados = raiz / "resultados"
resultados.mkdir(exist_ok=True)
nombres = ["jd", "x", "y", "z", "vx", "vy", "vz", "lt", "distancia", "radial"]

def leer_horizons(nombre):
    # leo las columnas originales y convierto el día juliano UTC a fecha civil
    respuesta = json.loads((raiz / "fuentes" / nombre).read_text(encoding="utf-8"))
    texto = respuesta["result"]
    bloque = texto.split("$$SOE")[1].split("$$EOE")[0].strip()
    filas = []
    for linea in bloque.splitlines():
        campos = [campo.strip() for campo in linea.split(",")]
        valores = [float(campos[0])] + [float(campo) for campo in campos[2:11]]
        fila = dict(zip(nombres, valores))
        fila["fecha"] = datetime.fromtimestamp((fila["jd"] - 2440587.5) * 86400, timezone.utc).isoformat()
        fila["anio"] = int(fila["fecha"][:4])
        filas.append(fila)
    return filas

def guardar_csv(nombre, filas):
    # conservo todas las columnas utilizadas para que pueda auditar cada cálculo
    with (raiz / "datos" / nombre).open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0]))
        escritor.writeheader()
        escritor.writerows(filas)

tierra = leer_horizons("horizons_tierra.json")
sol = leer_horizons("horizons_sol.json")
horas = leer_horizons("horizons_tierra_2026_horario.json")
control_tierra = leer_horizons("horizons_tierra_heliocentrica_2026.json")
assert len(tierra) == len(sol) == 17969
assert len(horas) == 7657
assert all(a["jd"] == b["jd"] for a, b in zip(tierra, sol))
assert all(b["jd"] - a["jd"] == 1 for a, b in zip(tierra, tierra[1:]))
assert len({fila["jd"] for fila in tierra}) == len(tierra)
assert all(math.isfinite(fila[col]) for fila in tierra + sol + horas for col in nombres)
assert tierra[-1]["fecha"] == "2026-11-16T00:00:00+00:00"
guardar_csv("voyager_tierra_diario.csv", tierra)
guardar_csv("voyager_sol_diario.csv", sol)
guardar_csv("voyager_tierra_2026_horario.csv", horas)
print(f"Leo {len(tierra):,} instantes diarios por referencia y {len(horas):,} instantes horarios de 2026.")
print("Cobertura:", tierra[0]["fecha"], "a", tierra[-1]["fecha"])

# cruzo las dos referencias en el mismo instante antes de clasificar
cruce = []
for geo, helio in zip(tierra, sol):
    fila = {"fecha": geo["fecha"], "jd": geo["jd"], "anio": geo["anio"],
            "distancia_tierra_km": geo["distancia"], "distancia_sol_km": helio["distancia"],
            "radial_tierra_km_s": geo["radial"], "radial_sol_km_s": helio["radial"],
            "acerca_tierra_aleja_sol": geo["radial"] < 0 < helio["radial"]}
    cruce.append(fila)
guardar_csv("comparacion_diaria.csv", cruce)
actual = [fila for fila in cruce if fila["anio"] == 2026]
negativos = [fila for fila in actual if fila["acerca_tierra_aleja_sol"]]
print("Instantes diarios de 2026 que cumplen la hipótesis:", len(negativos))
print("Primero y último muestreo negativos:", negativos[0]["fecha"], negativos[-1]["fecha"])
print("Menor variación respecto a la Tierra:", round(min(f["radial_tierra_km_s"] for f in actual), 3), "km/s")
print("Menor variación respecto al Sol:", round(min(f["radial_sol_km_s"] for f in actual), 3), "km/s")

def cambios_signo(filas):
    # interpolo entre vecinos de signo contrario, sin extrapolar fuera del archivo
    limites = []
    for anterior, posterior in zip(filas, filas[1:]):
        if anterior["radial"] * posterior["radial"] < 0:
            fraccion = -anterior["radial"] / (posterior["radial"] - anterior["radial"])
            limites.append({campo: anterior[campo] + fraccion * (posterior[campo] - anterior[campo])
                            for campo in ["jd", "distancia"]})
    return limites

def interpolar(filas, jd, columna):
    # uso únicamente los dos registros que encierran el instante solicitado
    for anterior, posterior in zip(filas, filas[1:]):
        if anterior["jd"] <= jd <= posterior["jd"]:
            fraccion = (jd - anterior["jd"]) / (posterior["jd"] - anterior["jd"])
            return anterior[columna] + fraccion * (posterior[columna] - anterior[columna])
    raise ValueError("instante fuera de cobertura")

def fecha_jd(jd):
    # expreso los límites aproximados en utc para evitar ambigüedad de calendario
    return datetime.fromtimestamp((jd - 2440587.5) * 86400, timezone.utc).isoformat()

limites = cambios_signo(horas)
assert len(limites) == 2
inicio, fin = limites
duracion = fin["jd"] - inicio["jd"]
reduccion = inicio["distancia"] - fin["distancia"]
aumento_sol = interpolar(sol, fin["jd"], "distancia") - interpolar(sol, inicio["jd"], "distancia")
resumen = {"inicio_utc_aproximado": fecha_jd(inicio["jd"]), "fin_utc_aproximado": fecha_jd(fin["jd"]),
           "duracion_dias": duracion, "reduccion_tierra_km": reduccion, "aumento_sol_km": aumento_sol,
           "reduccion_porcentaje": reduccion / inicio["distancia"] * 100,
           "reduccion_distancia_dividida_c_segundos": reduccion / 299792.458,
           "muestreos_diarios_negativos_2026": len(negativos)}
print(json.dumps(resumen, ensure_ascii=False, indent=2))

# separo contribuciones a la variación de distancia sobre una misma línea de visión
control_por_jd = {fila["jd"]: fila for fila in control_tierra}
contribuciones = []
errores_posicion = []
errores_velocidad = []
for geo, helio in zip(tierra, sol):
    if geo["anio"] != 2026:
        continue
    direccion = [geo[eje] / geo["distancia"] for eje in ["x", "y", "z"]]
    velocidad_voyager = [helio[eje] for eje in ["vx", "vy", "vz"]]
    velocidad_tierra = [helio[eje] - geo[eje] for eje in ["vx", "vy", "vz"]]
    aporte_voyager = sum(a * b for a, b in zip(velocidad_voyager, direccion))
    aporte_tierra = -sum(a * b for a, b in zip(velocidad_tierra, direccion))
    control = control_por_jd[geo["jd"]]
    errores_posicion.append(max(abs((helio[eje] - geo[eje]) - control[eje]) for eje in ["x", "y", "z"]))
    errores_velocidad.append(max(abs((helio[eje] - geo[eje]) - control[eje]) for eje in ["vx", "vy", "vz"]))
    contribuciones.append({"fecha": geo["fecha"], "jd": geo["jd"],
                           "aporte_voyager_km_s": aporte_voyager,
                           "aporte_tierra_km_s": aporte_tierra,
                           "suma_km_s": aporte_voyager + aporte_tierra,
                           "radial_publicada_km_s": geo["radial"]})
error_cierre = max(abs(f["suma_km_s"] - f["radial_publicada_km_s"]) for f in contribuciones)
assert error_cierre < 1e-9
assert max(errores_posicion) < 0.01
assert max(errores_velocidad) < 1e-8
guardar_csv("contribuciones_2026.csv", contribuciones)
mas_cercana = min(contribuciones, key=lambda fila: fila["radial_publicada_km_s"])
print("Día de mayor acercamiento por segundo (muestreo diario):", mas_cercana)
print("Error máximo al recomponer la velocidad radial:", error_cierre, "km/s")
print("Diferencia máxima con la consulta terrestre independiente:", max(errores_posicion), "km y", max(errores_velocidad), "km/s")

# resumo cada año sin mezclar periodos completos y parciales
anuales = []
for anio in sorted({f["anio"] for f in cruce}):
    grupo = [f for f in cruce if f["anio"] == anio]
    anuales.append({"anio": anio, "muestreos": len(grupo),
                    "muestreos_acercamiento": sum(f["acerca_tierra_aleja_sol"] for f in grupo),
                    "radial_tierra_min_km_s": min(f["radial_tierra_km_s"] for f in grupo),
                    "radial_sol_min_km_s": min(f["radial_sol_km_s"] for f in grupo)})
historico = [f for f in anuales if 1990 <= f["anio"] <= 2025]
assert len(historico) == 36
assert all(f["muestreos"] in [365, 366] for f in historico)
assert all(f["muestreos_acercamiento"] > 0 and f["radial_sol_min_km_s"] > 0 for f in historico)
limites_diarios = cambios_signo([f for f in tierra if f["anio"] == 2026])
diferencia_limites_minutos = [abs(a["jd"] - b["jd"]) * 1440 for a, b in zip(limites, limites_diarios)]
errores_diferencias = []
for anterior, central, posterior in zip(tierra, tierra[1:], tierra[2:]):
    if central["anio"] >= 1990:
        aproximacion = (posterior["distancia"] - anterior["distancia"]) / ((posterior["jd"] - anterior["jd"]) * 86400)
        errores_diferencias.append(abs(aproximacion - central["radial"]))
assert max(errores_diferencias) < 0.02
assert max(diferencia_limites_minutos) < 15
resumen.update({"anios_completos_con_episodio": len(historico),
                "min_muestreos_1990_2025": min(f["muestreos_acercamiento"] for f in historico),
                "max_muestreos_1990_2025": max(f["muestreos_acercamiento"] for f in historico),
                "diferencia_limites_diario_horario_minutos": diferencia_limites_minutos,
                "error_max_derivada_central_km_s": max(errores_diferencias),
                "error_max_cierre_km_s": error_cierre})
guardar_csv("resumen_anual.csv", anuales)
(resultados / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
print("Años completos con acercamiento:", len(historico), "de", len(historico))
print("Muestreos negativos por año:", resumen["min_muestreos_1990_2025"], "a", resumen["max_muestreos_1990_2025"])
print("Diferencia entre límites diarios y horarios (minutos):", diferencia_limites_minutos)
print("Mayor diferencia de velocidad frente a la derivada numérica:", max(errores_diferencias), "km/s")

from html import escape

# dibujo gráficos vectoriales a partir de todos los registros diarios de 2026
def grafico_svg(titulo, descripcion, series, etiquetas_y, minimo, maximo, nombre):
    ancho, alto = 900, 480
    izquierda, derecha, arriba, abajo = 82, 26, 96, 85
    x = lambda jd: izquierda + (jd - actual[0]["jd"]) / (actual[-1]["jd"] - actual[0]["jd"]) * (ancho - izquierda - derecha)
    y = lambda valor: arriba + (maximo - valor) / (maximo - minimo) * (alto - arriba - abajo)
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" role="img" aria-labelledby="{nombre}-titulo {nombre}-desc">',
              f'<title id="{nombre}-titulo">{escape(titulo)}</title><desc id="{nombre}-desc">{escape(descripcion)}</desc>',
              '<rect width="900" height="480" fill="#faf8f2"/>',
              f'<text x="28" y="32" font-family="sans-serif" font-size="22" fill="#172342">{escape(titulo)}</text>',
              f'<text x="28" y="58" font-family="sans-serif" font-size="15" fill="#46506a">{escape(descripcion)}</text>']
    for valor in etiquetas_y:
        partes += [f'<path d="M {izquierda} {y(valor):.2f} H {ancho-derecha}" stroke="#d9dce4"/>',
                   f'<text x="{izquierda-12}" y="{y(valor)+5:.2f}" text-anchor="end" font-family="sans-serif" font-size="15" fill="#46506a">{valor:g}</text>']
    partes.append(f'<path d="M {izquierda} {y(0):.2f} H {ancho-derecha}" stroke="#172342" stroke-dasharray="4 4"/>')
    for indice, (etiqueta, color, datos) in enumerate(series):
        puntos = " ".join(f'{x(jd):.2f},{y(valor):.2f}' for jd, valor in datos)
        partes.append(f'<polyline fill="none" stroke="{color}" stroke-width="3" points="{puntos}"/>')
        partes.append(f'<text x="{82+indice*340}" y="448" font-family="sans-serif" font-size="16" fill="{color}">{escape(etiqueta)}</text>')
    for mes, etiqueta in [(1,"ene"),(3,"mar"),(5,"may"),(7,"jul"),(9,"sep"),(11,"nov")]:
        fecha = f"2026-{mes:02d}-01"
        fila = next(f for f in actual if f["fecha"].startswith(fecha))
        partes.append(f'<text x="{x(fila["jd"]):.2f}" y="420" text-anchor="middle" font-family="sans-serif" font-size="15" fill="#46506a">{etiqueta}</text>')
    partes.append('</svg>')
    texto = "".join(partes)
    (resultados / f"{nombre}.svg").write_text(texto, encoding="utf-8")
    return texto

svg_velocidad = grafico_svg("La distancia a la Tierra disminuye durante parte del año", "Variación de distancia en km/s · 1 de enero a 16 de noviembre de 2026", [
    ("Respecto a la Tierra", "#446ddf", [(f["jd"],f["radial_tierra_km_s"]) for f in actual]),
    ("Respecto al Sol", "#785c34", [(f["jd"],f["radial_sol_km_s"]) for f in actual])], [-10,0,10,20,30,40], -12, 45, "variacion_distancia")
# separo el acercamiento de la Tierra de un regreso hacia el Sol
print("Escribo resultados/variacion_distancia.svg con ambas referencias y la línea cero.")
print("Resultado: 40,7 millones de km menos hasta la Tierra y 136,4 millones más hasta el Sol durante el episodio.")