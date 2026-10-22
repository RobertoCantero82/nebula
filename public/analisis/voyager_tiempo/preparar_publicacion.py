from pathlib import Path
import json
import html
import re
import shutil

base=Path(__file__).resolve().parent
datos=json.loads((base/'datos_web.json').read_text(encoding='utf-8'))
def fmt(s):
    if s < 60: return f'{s:.1f} s'.replace('.',',')
    if s >= 3600:
        minutos=round(s/60)
        return f'{minutos//60} h {minutos%60} min'
    s=round(s)
    if s < 3600: return f'{s//60} min {s%60} s'
    return f'{s//3600} h {(s%3600)//60} min'

filas=''.join(f'<tr><th scope="row">{r["destino"]}</th><td>{fmt(r["segundos_ida"])}</td><td>{fmt(2*r["segundos_ida"])}</td></tr>' for r in datos['comparacion'])
opciones=''.join(f'<option value="{i}" '+('selected ' if i==5 else '')+f'>{r["destino"]}</option>' for i,r in enumerate(datos['comparacion']))
comparador=f'''<section class="voy-bloque" aria-labelledby="voy-compara-titulo">
<h3 id="voy-compara-titulo">Elige a qué distancia quieres conversar</h3>
<label for="voy-destino">Destino</label> <select id="voy-destino">{opciones}</select>
<p id="voy-espera" role="status" aria-live="polite">Voyager 1: 23 h 56 min de ida; unas 47 h 52 min para ida y vuelta.</p>
<p class="voy-nota">Fotografía del 22 de octubre de 2026 a las 00:00 UTC. La ida y vuelta duplica la distancia actual: no incluye movimiento durante la señal, procesamiento ni turnos de antena.</p>
<details><summary>Comparar todos los destinos</summary><div class="voy-tabla"><table><thead><tr><th>Destino</th><th>Ida</th><th>Ida y vuelta aprox.</th></tr></thead><tbody>{filas}</tbody></table></div></details></section>'''

def svg_historia():
    serie=datos['historia']
    points=' '.join(f'{64+i/(len(serie)-1)*650:.2f},{238-r["horas"]/24*200:.2f}' for i,r in enumerate(serie))
    grid=''.join(f'<line x1="64" x2="714" y1="{238-v/24*200}" y2="{238-v/24*200}" stroke="#ddd"/><text x="54" y="{243-v/24*200}" text-anchor="end">{v}</text>' for v in [0,6,12,18,24])
    years=''.join(f'<text x="{64+(y-1977)/(2026-1977)*650:.1f}" y="265" text-anchor="middle">{y}</text>' for y in [1977,1990,2000,2010,2026])
    return f'''<figure class="voy-figura"><figcaption><strong>Casi medio siglo para alejarse un día luz</strong><br>Horas de ida de la señal desde la Tierra. La curva acaba el 19 de octubre de 2026; el muestreo salta 30 días.</figcaption><svg viewBox="0 0 760 285" role="img" aria-label="La demora de ida crece desde casi cero en 1977 hasta casi 24 horas en octubre de 2026.">{grid}<polyline points="{points}" stroke="#446ddf" stroke-width="3" fill="none"/>{years}</svg></figure>'''

apuesta='''<fieldset class="voy-bloque" id="voy-apuesta"><legend>Haz tu apuesta</legend><p>Si Voyager se aleja del Sol, ¿la señal tarda cada día más en llegar a la Tierra?</p><div class="voy-opciones"><button type="button" data-voy="si" aria-pressed="false">Sí, siempre</button><button type="button" data-voy="no" aria-pressed="false">No necesariamente</button></div><p id="voy-respuesta" role="status" aria-live="polite">Elige una respuesta o abre la explicación que hay debajo.</p><details id="voy-explicacion"><summary>Descubrir la explicación</summary><p>No necesariamente. La Tierra también se mueve. Entre el 21 de enero y el 24 de abril, la demora de ida bajó unos 136 segundos mientras la distancia al Sol seguía creciendo.</p></details></fieldset>'''

def svg_distancias():
    serie=datos['diario']; amplitud=500
    def curva(col):return ' '.join(f'{68+i/(len(serie)-1)*645:.2f},{250-(r[col]+50)/amplitud*210:.2f}' for i,r in enumerate(serie))
    grid=''.join(f'<line x1="68" x2="713" y1="{250-(v+50)/amplitud*210}" y2="{250-(v+50)/amplitud*210}" stroke="#ddd"/><text x="58" y="{255-(v+50)/amplitud*210}" text-anchor="end">{v}</text>' for v in [-50,0,150,300,450])
    labels=''.join(f'<text x="{68+i/294*645:.1f}" y="280" text-anchor="middle">{s}</text>' for i,s in [(0,'Ene'),(90,'Abr'),(181,'Jul'),(294,'22 oct')])
    return f'''<figure class="voy-figura"><figcaption><strong>Alejarse del Sol no siempre significa alejarse de la Tierra</strong><br>Cambio de distancia desde el 1 de enero de 2026, en millones de kilómetros. Ambas curvas parten de cero para comparar el cambio, no la distancia total.</figcaption><p class="voy-leyenda"><span>Azul continuo: desde la Tierra</span><span>Marrón discontinuo: desde el Sol</span></p><svg viewBox="0 0 760 300" role="img" aria-label="La distancia al Sol aumenta todo el periodo; la distancia a la Tierra desciende entre enero y abril antes de aumentar de nuevo.">{grid}<polyline points="{curva('sol')}" stroke="#a76d3c" stroke-dasharray="8 5" stroke-width="3" fill="none"/><polyline points="{curva('tierra')}" stroke="#446ddf" stroke-width="3" fill="none"/>{labels}</svg></figure>'''

editorial=(base/'editorial.md').read_text(encoding='utf-8')
for clave,valor in {'comparador':comparador,'historia':svg_historia(),'apuesta':apuesta,'distancias':svg_distancias()}.items():editorial=editorial.replace('{'+clave+'}',valor)
front='''---
titulo: 'Voyager 1 está a casi un día luz. ¿Por qué a veces tarda menos en contestar?'
descripcion: 'La sonda se aleja del Sol, pero durante parte de 2026 se acercó a la Tierra. Los datos de NASA explican esa aparente contradicción.'
tema: 'CIENCIA'
fecha: 2026-10-22
imagenPortada: '/nebula/imagenes/voyager_tiempo_portada.png'
cifraDestacada: '47 h 52 min'
etiquetaCifra: 'ida y vuelta aproximada de la señal de Voyager 1'
metodologia: 'EDA de efemérides geométricas de JPL Horizons. Comparo seis destinos el 22 de octubre de 2026 a las 00:00 UTC, 599 posiciones de Voyager 1 cada 30 días desde 1977 y 295 posiciones diarias de 2026 desde la Tierra y desde el Sol. Distancia dividida por la velocidad de la luz y doble demora como aproximación de ida y vuelta. No son mensajes observados ni una predicción propia. Excluyo filas posteriores al corte. El hito del 18 de noviembre es una previsión publicada por NASA.'
---

'''
fuentes='''
## Fuentes y análisis

- [NASA: el próximo día luz de Voyager 1](https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/).
- [JPL Horizons: posiciones y distancias](https://ssd.jpl.nasa.gov/horizons/) y [definiciones de las tablas](https://ssd.jpl.nasa.gov/horizons/manual.html).
- [Notebook ejecutado](/nebula/analisis/voyager_tiempo/analisis_voyager.ipynb), [datos de comparación](/nebula/analisis/voyager_tiempo/comparacion.csv), [serie diaria](/nebula/analisis/voyager_tiempo/diario_2026.csv) y [guía de reproducción](/nebula/analisis/voyager_tiempo/README.md).
'''
script='''
<style>
.voy-bloque{border:1px solid #becbec;border-radius:14px;padding:1.2rem;margin:1.8rem 0;background:#f5f7fd;min-width:0}.voy-bloque legend{font-weight:700;padding:0 .5rem}.voy-bloque select,.voy-bloque button{font:inherit;padding:.65rem .8rem;border:1px solid #446ddf;border-radius:8px;background:white;color:#23439b}.voy-bloque button[aria-pressed="true"]{background:#446ddf;color:white}.voy-opciones{display:flex;gap:.65rem;flex-wrap:wrap}.voy-bloque :focus-visible{outline:3px solid #a76d3c;outline-offset:3px}.voy-nota{font-size:.85em;color:#535d70}.voy-tabla{overflow-x:auto}.voy-tabla table{width:100%;border-collapse:collapse;font-size:.9em}.voy-tabla td,.voy-tabla th{padding:.6rem;text-align:left;border-bottom:1px solid #d5def1}.voy-figura{margin:2rem 0}.voy-figura svg{width:100%;height:auto;display:block}.voy-figura text{font-size:15px;fill:#536075;font-family:system-ui,sans-serif}.voy-figura figcaption{font-size:.95em;line-height:1.5}.voy-leyenda{font-size:.85em;display:flex;flex-wrap:wrap;gap:.3rem 1rem}.voy-leyenda span:first-child{color:#446ddf}.voy-leyenda span:last-child{color:#946039}
</style>
<script>
document.addEventListener('DOMContentLoaded',()=>{
 const destinos=__DATOS__;
 const formato=(segundos)=>{if(segundos<60)return `${segundos.toFixed(1).replace('.',',')} segundos`;const s=Math.round(segundos);if(s<3600)return `${Math.floor(s/60)} min ${s%60} s`;const m=Math.round(segundos/60);return `${Math.floor(m/60)} h ${m%60} min`;};
 const selector=document.getElementById('voy-destino');
 const actualizar=()=>{const d=destinos[Number(selector.value)];document.getElementById('voy-espera').textContent=`${d.destino}: ${formato(d.segundos_ida)} de ida; ${formato(d.segundos_ida*2)} para ida y vuelta aproximada.`;};
 if(selector){selector.addEventListener('change',actualizar);actualizar();}
 document.querySelectorAll('[data-voy]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-voy]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));document.getElementById('voy-respuesta').textContent=b.dataset.voy==='no'?'Exacto. La distancia también depende del movimiento de la Tierra.':'La intuición engaña: la Tierra también se mueve y puede reducir la separación.';document.getElementById('voy-explicacion').open=true;}));
});
</script>
'''.replace('__DATOS__',json.dumps(datos['comparacion'],ensure_ascii=False))
(base/'voyager-un-dia-luz.md').write_text(front+editorial+fuentes+script,encoding='utf-8')
(base/'README.md').write_text('''# Voyager: una conversación de casi dos días

**Categoría: EDA. Corte: 22 de octubre de 2026, 00:00 UTC.**

Comparo seis destinos, una serie de Voyager 1 cada 30 días desde 1977 y series diarias de 2026 desde el centro de la Tierra y del Sol. Trabajo con efemérides calculadas por JPL, no registros observados de comunicaciones. El hito futuro del 18 de noviembre procede de NASA; no hago una predicción propia.

## Reproducir

Instalo `requirements.txt`, abro `analisis_voyager.ipynb` desde esta carpeta y ejecuto todas las celdas. Los CSV y `fuentes/` permiten repetir el análisis sin conexión. `fuentes.json` conserva consultas, fechas de descarga y SHA-256 de cada respuesta. `descargar.py` permite renovar la extracción en Windows con conexión; no reemplaza copias ya descargadas. Para obtener otra versión, uso una carpeta nueva y conservo la anterior. `ejecutar.py` automatiza la ejecución si dispongo de un kernel Python y las dependencias.

## Archivos

- `comparacion.csv`: seis destinos en un mismo corte.
- `historia.csv`: extracción histórica cada 30 días.
- `diario_2026.csv`, `diario_sol_2026.csv`: distancias diarias con dos centros distintos.
- `comparacion_limpia.csv`, `resultados.json`, `datos_web.json`: resultados reproducibles.
- `fuentes/`, `fuentes.json`: respuestas originales y trazabilidad.

## Limitaciones

Excluyo filas posteriores al corte aunque la API incluya el extremo solicitado del 23 de octubre. Uso vectores geométricos sin corrección por movimiento durante el vuelo de la señal. La ida y vuelta es el doble de distancia/c, una aproximación explicativa; no incluye ejecución de órdenes, planificación de antenas ni incidencias. No atribuyo las distancias de los centros planetarios a vehículos concretos. Los 93 intervalos de descenso son comparaciones entre medianoches, no una determinación subdiaria de los extremos. No presupongo comunicación disponible con todos los destinos. El muestreo de 30 días no resuelve oscilaciones diarias.
''',encoding='utf-8')
post='''Una nave de 1977 está a punto de quedar a un día luz de la Tierra. Mandarle una orden y recibir respuesta ya roza los dos días.

Pero sus datos esconden un detalle curioso: aunque Voyager 1 se aleja del Sol, hubo una parte de este año en la que la espera se acortó.

Lo cuento en Nebula, con datos de NASA y una pequeña apuesta antes de descubrir la explicación.

https://robertocantero82.github.io/nebula/articulos/voyager-un-dia-luz/

#Voyager #Espacio #Ciencia #Tecnología #OpenToWork #BuscandoTrabajo #Periodista #Redactor #CienciaDeDatos
'''
(base/'linkedin.md').write_text(post,encoding='utf-8')
print('Artículo, interacciones, README y LinkedIn preparados')
