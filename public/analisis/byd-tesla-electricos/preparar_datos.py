from __future__ import annotations

import csv
import re
import sys
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path


ANCHOS_INICIALES = [8, 1, 8, 30, 22, 1, 21, 2, 1, 5, 6, 6, 6, 3, 2, 2, 2, 2, 24, 2, 2, 1, 8, 5, 8, 1]
NOMBRES_INICIALES = [
    "fecha_matricula",
    "clase_matricula",
    "fecha_tramitacion",
    "marca",
    "modelo",
    "procedencia",
    "bastidor",
    "tipo",
    "propulsion",
    "cilindrada",
    "potencia",
    "tara",
    "peso_maximo",
    "plazas",
    "indicador_precinto",
    "indicador_embargo",
    "numero_transmisiones",
    "numero_titulares",
    "localidad",
    "provincia",
    "provincia_matriculacion",
    "clave_tramite",
    "fecha_tramite",
    "codigo_postal",
    "fecha_primera_matriculacion",
    "nuevo_usado",
]


def normalizar(texto: str) -> str:
    """Normalizo una etiqueta para comparar marcas sin depender de tildes o espacios."""
    limpio = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^A-Z0-9]+", " ", limpio.upper()).strip()


def cortar(linea: str) -> dict[str, str]:
    """Corto únicamente el tramo inicial del registro que necesito para el análisis."""
    salida: dict[str, str] = {}
    inicio = 0
    for nombre, ancho in zip(NOMBRES_INICIALES, ANCHOS_INICIALES):
        salida[nombre] = linea[inicio : inicio + ancho].strip()
        inicio += ancho
    return salida


def marca_objetivo(marca: str) -> str | None:
    """Agrupo las variantes de las dos marcas y dejo fuera el resto."""
    etiqueta = normalizar(marca)
    if etiqueta.startswith("TESLA"):
        return "Tesla"
    if etiqueta.startswith("BYD"):
        return "BYD"
    return None


def main(carpeta_raw: Path, salida: Path) -> None:
    salida.mkdir(parents=True, exist_ok=True)
    detalle_path = salida / "matriculaciones_byd_tesla.csv"
    mensual_path = salida / "matriculaciones_mensuales.csv"
    control_path = salida / "control_extraccion.csv"
    conteos: Counter[tuple[str, str]] = Counter()
    controles: list[dict[str, object]] = []

    with detalle_path.open("w", newline="", encoding="utf-8") as detalle:
        campos = ["fecha", "mes", "marca", "marca_dgt", "modelo", "nuevo_usado", "archivo"]
        escritor = csv.DictWriter(detalle, fieldnames=campos)
        escritor.writeheader()

        candidatos: dict[str, Path] = {}
        for archivo in sorted(carpeta_raw.glob("*.zip")):
            coincidencia = re.search(r"(20\d{4})", archivo.stem)
            if coincidencia:
                periodo = coincidencia.group(1)
                # si hay una copia duplicada, conservo el nombre oficial de la descarga
                if periodo not in candidatos or archivo.name.startswith("export_mensual"):
                    candidatos[periodo] = archivo

        for archivo in [candidatos[periodo] for periodo in sorted(candidatos)]:
            vistos = turismos_bev_nuevos = objetivos = errores = 0
            with zipfile.ZipFile(archivo) as comprimido:
                nombres = [nombre for nombre in comprimido.namelist() if nombre.lower().endswith(".txt")]
                if len(nombres) != 1:
                    raise RuntimeError(f"Esperaba un TXT en {archivo.name} y encontré {len(nombres)}")
                with comprimido.open(nombres[0]) as bruto:
                    for numero, bytes_linea in enumerate(bruto, start=1):
                        if numero == 1:
                            continue
                        vistos += 1
                        linea = bytes_linea.decode("latin-1").rstrip("\r\n")
                        if len(linea) < sum(ANCHOS_INICIALES):
                            errores += 1
                            continue
                        fila = cortar(linea)
                        if fila["tipo"] != "40" or fila["propulsion"] != "2" or fila["nuevo_usado"] != "N":
                            continue
                        turismos_bev_nuevos += 1
                        marca = marca_objetivo(fila["marca"])
                        if marca is None:
                            continue
                        fecha = fila["fecha_matricula"]
                        if len(fecha) != 8 or not fecha.isdigit():
                            errores += 1
                            continue
                        mes = f"{fecha[4:8]}-{fecha[2:4]}"
                        conteos[(mes, marca)] += 1
                        objetivos += 1
                        escritor.writerow(
                            {
                                "fecha": f"{fecha[4:8]}-{fecha[2:4]}-{fecha[0:2]}",
                                "mes": mes,
                                "marca": marca,
                                "marca_dgt": fila["marca"],
                                "modelo": fila["modelo"],
                                "nuevo_usado": fila["nuevo_usado"],
                                "archivo": archivo.name,
                            }
                        )
            controles.append(
                {
                    "archivo": archivo.name,
                    "registros": vistos,
                    "turismos_bev_nuevos": turismos_bev_nuevos,
                    "byd_tesla": objetivos,
                    "errores": errores,
                }
            )
            print(f"{archivo.name}: {objetivos:,} registros BYD/Tesla")

    meses = sorted({mes for mes, _ in conteos})
    with mensual_path.open("w", newline="", encoding="utf-8") as mensual:
        escritor = csv.DictWriter(mensual, fieldnames=["mes", "marca", "matriculaciones"])
        escritor.writeheader()
        for mes in meses:
            for marca in ("BYD", "Tesla"):
                escritor.writerow({"mes": mes, "marca": marca, "matriculaciones": conteos[(mes, marca)]})

    with control_path.open("w", newline="", encoding="utf-8") as control:
        escritor = csv.DictWriter(control, fieldnames=list(controles[0]))
        escritor.writeheader()
        escritor.writerows(controles)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Uso: preparar_datos.py CARPETA_RAW CARPETA_SALIDA")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
