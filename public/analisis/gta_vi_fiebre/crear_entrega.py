from pathlib import Path
from datetime import date, timedelta
from urllib.parse import quote
import contextlib
import hashlib
import io
import json
import re
import sys
import numpy as np
from modelo import ejecutar, preparar

RAIZ=Path(__file__).resolve().parent
r=ejecutar();juegos,gta=preparar()

def md(t):
    return dict(cell_type='markdown',metadata={},source=t.splitlines(keepends=True))

def code(t):
    return dict(cell_type='code',metadata={},source=t.splitlines(keepends=True),execution_count=None,outputs=[])

def notebook(nombre,celdas):
    # ejecuto mis celdas en orden y conservo sus salidas reales
    entorno={'__name__':'__main__'}
    for i,c in enumerate(celdas):
        c['id']=f'nebula-gta-{i:02d}'
        if c['cell_type']=='code':
            salida=io.StringIO()
            with contextlib.redirect_stdout(salida):
                exec(compile(''.join(c['source']),nombre,'exec'),entorno)
            c['execution_count']=sum(x['cell_type']=='code' for x in celdas[:i+1])
            c['outputs']=[dict(output_type='stream',name='stdout',text=salida.getvalue().splitlines(keepends=True))]
    obj=dict(nbformat=4,nbformat_minor=5,metadata=dict(kernelspec=dict(display_name='Python 3',language='python',name='python3'),language_info=dict(name='python',version=sys.version.split()[0])),cells=celdas)
    (RAIZ/nombre).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')

notebook('01_preparacion_datos.ipynb',[
md('# Mi medida de la fiebre de GTA VI\n\n**Roberto Cantero · Nebula · 23 de noviembre de 2026**\n\n## Mi pregunta\n\nQuiero anticipar las consultas de la página de GTA VI en Wikipedia en inglés durante las semanas tercera y quinta tras su lanzamiento. Mido consultas, no lectores únicos, jugadores ni ventas. Separo esta preparación de mi modelo y su evaluación. Uso días UTC y conservo todos los datos necesarios para repetir el trabajo sin conexión.\n\nNecesito Python 3.10+ y NumPy. Ejecuto los cuadernos en esta carpeta, con modelo.py y los JSON al lado. Las salidas incluidas se han ejecutado en orden mediante Python, sin un servidor de Jupyter.'),
code("# leo mis datos conservados y genero el csv sin imputar ausencias\nfrom modelo import preparar, RAIZ, EXCLUSIONES\nfrom collections import Counter\nimport hashlib, json\nimport numpy as np\njuegos, gta = preparar()\nprint('NumPy:', np.__version__)\nprint('Juegos conservados: 30; juegos utilizados:', len(juegos))\nprint('Mi reparto:', dict(Counter(s['grupo'] for s in juegos)))\nprint('Mis exclusiones:', EXCLUSIONES)\nfor nombre in ['series_consultadas.json','gta_vi_consultado.json']:\n    print(nombre, hashlib.sha256((RAIZ/nombre).read_bytes()).hexdigest())"),
md('## Mi procedencia y mis decisiones\n\nHe extraído las series del JSON visible del servicio oficial de Wikimedia, con proyecto en.wikipedia.org, all-access, user y frecuencia diaria. Conservo los números extraídos, no afirmo haber conservado el cuerpo bruto completo de cada respuesta. En series_consultadas.json guardo título, fecha de estreno y 43 consultas diarias consecutivas desde siete días antes hasta 35 días después. En fuentes_metodologia.md dejo las peticiones exactas y las páginas consultadas para las fechas.\n\nElijo una muestra de conveniencia de grandes videojuegos de pago de 2015 a 2023; no es representativa de todos los videojuegos. Conservo treinta series y excluyo dos por criterios de comparabilidad y cobertura. No incluyo GTA V: su estreno de 2013 precede a la cobertura diaria de este servicio. Dark Souls III tuvo un estreno japonés anterior al mundial; el título consultado de Baldur’s Gate 3 muestra consultas casi nulas al principio y un salto posterior, compatible con un cambio de título o redirección. No lo interpreto como ausencia de interés.'),
code("# compruebo la integridad de mis ventanas y las fechas de cada día\nimport csv\nfrom datetime import date, timedelta\nfilas = list(csv.DictReader((RAIZ/'consultas_diarias.csv').open(encoding='utf-8')))\nassert len(filas)==30*43\nassert len({(s['titulo'],s['fecha']) for s in filas})==len(filas)\nassert all(int(s['consultas'])>0 for s in filas)\nassert len(gta['v'])==22\nassert date.fromisoformat(gta['start'])+timedelta(days=21)==date(2026,11,22)\nprint('Filas conservadas:',len(filas))\nprint('Consultas de GTA VI del 19 al 22 de noviembre:',gta['v'][18:22])\nprint('Mis objetivos usan días +14 a +20 y +28 a +34; mis entradas solo -7 a +3.')"),
md('## Mis límites antes de modelar\n\nUna consulta no equivale a una persona. El idioma inglés no representa un país. El filtro user excluye agentes automatizados identificados, sin garantizar ausencia de toda automatización. Consultar un solo título no suma automáticamente las visitas de sus redirecciones históricas. Las fechas de estreno regionales y las nuevas versiones pueden afectar las curvas; no interpreto las diferencias como efectos causales de la calidad del juego. No convierto una caída de consultas en abandono del juego. Continúo en 02_prediccion.ipynb.')
])
notebook('02_prediccion.ipynb',[
md('# ¿Cuánto durará la fiebre de GTA VI?\n\n**Roberto Cantero · Nebula · Machine learning experimental**\n\n## Mi objetivo y mi protocolo\n\nEstimo la media diaria de consultas en las semanas tercera y quinta, como fracción de las consultas del día de estreno. No estimo cuándo se deja de jugar. Mi protocolo está en protocolo.md, escrito antes de calcular el modelo. Uso dos señales disponibles al cuarto día: la caída entre el estreno y el día +3, y el interés previo relativo al estreno. Ajusto una regresión ridge sobre el logaritmo de la retención. Regularizo para limitar ajustes excesivos con pocos juegos.'),
code("# reproduzco mi preparación y mi ajuste\nfrom modelo import ejecutar, preparar, ajustar, predecir, referencia, medir\nimport numpy as np\nimport json\nr=ejecutar()\njuegos,gta=preparar()\nprint(json.dumps(r['muestra'],ensure_ascii=False,indent=2))\nprint('Mi penalización elegida solo en validación:',r['alpha_elegido'])"),
md('## Cómo compruebo si mi modelo aporta algo\n\nEntreno con catorce juegos hasta 2019. Elijo entre dos penalizaciones con siete juegos de 2020–2021. Después reajusto con esos veintiuno y evalúo una vez en siete juegos de 2022–2023. Mantengo cada videojuego entero en su grupo. No mezclo días del mismo juego entre entrenamiento y prueba. Mi criterio de selección es el error absoluto medio del logaritmo de retención: penaliza desviaciones proporcionales. Lo acompaño con errores en puntos porcentuales, más fáciles de interpretar.\n\nMis referencias son conservar el nivel del cuarto día y aplicar la mediana histórica de retención de cada horizonte. Esta segunda referencia ya sabe que la atención suele caer: superarla es una comparación más exigente.'),
code("# examino mi validación sin usar la prueba para escoger la penalización\nprint(json.dumps(r['seleccion_validacion'],ensure_ascii=False,indent=2))\nprint('Mi prueba final:')\nprint(json.dumps(r['metricas_prueba'],ensure_ascii=False,indent=2))\nprint('Mi mejora relativa en el error logarítmico:',round(100*r['mejora_relativa_mae_log'],2),'%')\nprint('Resultados por juego:')\nfor s in r['prueba_por_juego']:\n    print(s['titulo'], 'real',np.round(100*np.array(s['real']),2), 'modelo',np.round(100*np.array(s['ridge']),2),'mediana',np.round(100*np.array(s['mediana']),2))"),
md('## Lo que encuentro en mi prueba\n\nMi modelo mejora un 16,25 % el error logarítmico de la mediana histórica en siete juegos de prueba. El error absoluto medio es de 2,26 puntos de retención para la tercera semana y 1,48 para la quinta. Son puntos sobre el nivel del estreno, no un error relativo del 2,26 % o 1,48 %. La prueba es pequeña y no demuestra una mejora universal. No atribuyo significación estadística al resultado. El conjunto de validación fue más difícil; no uso solo el buen resultado final para esconderlo.'),
code("# aplico el mismo modelo evaluado sin añadir datos futuros de gta vi\nprint(json.dumps(r['gta'],ensure_ascii=False,indent=2))\nassert r['supera_referencia']\nassert r['gta']['periodos'][0]['inicio']=='2026-12-03'\nassert r['gta']['periodos'][1]['fin']=='2026-12-23'\nprint('Mi modelo usa solo los cuatro primeros días observados de GTA VI y la semana anterior.')"),
md('## Mi previsión experimental y su incertidumbre\n\nEstimo alrededor de 92.000 consultas diarias para el 3–9 de diciembre, un 12,3 % del día de estreno. Para el 17–23 de diciembre obtengo unas 51.000, un 6,8 %. Mi banda orientativa va de unas 46.000 a 186.000 consultas en la primera ventana y de 16.000 a 163.000 en la segunda. La construyo aplicando a la previsión el mayor error logarítmico de mis siete juegos de validación para cada horizonte.\n\nNo es un intervalo con cobertura del 80 %, 90 % o 95 % garantizada. Reajusto después de esa validación y GTA VI puede no ser intercambiable con los juegos anteriores. Las bandas son una traducción de errores históricos a escala de GTA VI, no probabilidades calibradas.\n\nEl estreno de GTA VI supera en consultas al mayor estreno de mi entrenamiento y validación. Además, su caída inicial, 58,8 %, es algo mayor que la más intensa de esos veintiún juegos. Estoy extrapolando ligeramente una variable; normalizar las curvas no elimina ese límite. No interpreto la magnitud del estreno como una cantidad de jugadores.'),
code("# compruebo mi extrapolación y comparo con el registro más sencillo\nprevios=[s for s in juegos if s['grupo']!='prueba']\nprint('Mayor estreno previo:',max(s['dia0'] for s in previos),'frente a GTA VI:',gta['dia0'])\nprint('Caída inicial de GTA VI:',round(100*(gta['dia3']/gta['dia0']-1),2),'%')\nprint('Mayor caída inicial en mis datos de ajuste:',round(100*(min(s['dia3']/s['dia0'] for s in previos)-1),2),'%')\nprint('Referencia de mediana aplicada a GTA VI:',np.round(referencia(previos,[gta],'mediana')[0]*gta['dia0']))\nprint('Mi prueba no contiene los datos futuros de GTA VI: todavía no han ocurrido.')"),
md('## Mi conclusión y cómo contrastarla después\n\nMi previsión es experimental: la mejora sobre la mediana existe en esta prueba, pero es modesta y la muestra es pequeña. Publico tanto la cifra central como un rango amplio. No predigo ventas, jugadores, calidad ni el fin del éxito de GTA VI. Mi predicción se refiere a las consultas de una página concreta.\n\nDespués del 9 y del 23 de diciembre descargaré las ventanas completas, conservaré esta previsión sin modificarla y calcularé su error. Si cambian títulos o redirecciones, documentaré el cambio en vez de sustituir silenciosamente la serie. Las instrucciones de repetición y las peticiones están en fuentes_metodologia.md. Mi código solo necesita NumPy y los archivos conservados.')
])

peticiones=[]
for s in json.loads((RAIZ/'series_consultadas.json').read_text(encoding='utf-8')):
    d=date.fromisoformat(s['d'])
    url='https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/'+quote(s['t'],safe='')+'/daily/'+(d-timedelta(days=7)).strftime('%Y%m%d00')+'/'+(d+timedelta(days=35)).strftime('%Y%m%d00')
    peticiones.append(f"| {s['t'].replace('_',' ')} | {s['d']} | [Fecha consultada](https://en.wikipedia.org/wiki/{quote(s['t'],safe='')}) · [Serie]({url}) |")
fuentes='''# Mis fuentes, unidades y límites

Autor: Roberto Cantero · Nebula. Corte: 23 de noviembre de 2026.

## Mi fuente numérica

Wikimedia Analytics API: https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/

Uso consultas de páginas en inglés, todos los accesos, agente user, días UTC. No cuento personas únicas ni búsquedas. Cada serie histórica guarda 43 números en orden, de -7 a +35 respecto a la fecha declarada. Los JSON son una transcripción estructurada de los números extraídos del JSON visible en el navegador; no son las respuestas HTTP originales completas. Conservo títulos, fechas, peticiones y huellas para auditar esta copia. Los redireccionamientos no se agregan automáticamente y son una limitación. He comprobado las fechas en las fichas visibles de cada artículo de Wikipedia, fuente secundaria para esas fechas; no afirmo que todas las fechas se hayan contrastado con la editora.

GTA VI: https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Grand_Theft_Auto_VI/daily/2026110100/2026112200

## Mi contexto original

- Tienda de Rockstar, lanzamiento el 19 de noviembre: https://store.rockstargames.com/game/buy-gta-vi?drm=playstation
- Comunicado de Take-Two del 20 de noviembre, también depositado en la SEC: https://www.sec.gov/Archives/edgar/data/946581/000162828026075217/exhibit9918k.htm . Los 3.790 millones de dólares son ventas al público estimadas por la empresa hasta el final del 19 de noviembre, no ingresos netos de Take-Two ni un dato usado para entrenar mi modelo.

## Mi muestra y sus fechas

Muestra de conveniencia de treinta grandes videojuegos de pago; no es un censo. El protocolo documenta mis dos exclusiones, las particiones temporales, las métricas y el tratamiento de incertidumbre. Los otros veintiocho juegos siguen incluidos, aun con controversias, pandemia o estrenos regionales próximos. No ajusto la selección a los resultados.

| Juego | Día 0 utilizado | Procedencia |
|---|---|---|
'''+ '\n'.join(peticiones)+'''

## Cómo reproduzco mi trabajo

1. Uso Python 3.10 o posterior e instalo NumPy. El entorno de ejecución y la versión efectiva aparecen en el primer notebook.
2. Mantengo modelo.py, protocolo.md, series_consultadas.json y gta_vi_consultado.json juntos.
3. Ejecuto `python modelo.py`. Regenero consultas_diarias.csv y resultados.json sin conexión.
4. Ejecuto los dos notebooks en orden en esa carpeta. Alternativamente, `python crear_entrega.py` ejecuta secuencialmente sus celdas mediante Python y guarda sus salidas; no utiliza un servidor de Jupyter.

La expresión de ridge es B=(ZᵀZ+diag(0,α,α))⁻¹Zᵀlog(Y), con intercepto sin penalizar y entradas estandarizadas solo con el conjunto de ajuste. Pruebo α=1 y α=10 en validación. Cada juego aporta una fila y dos objetivos. La prueba final permanece fuera del ajuste. Conservo el modelo ajustado con veintiún juegos para aplicarlo a GTA VI.

Mi banda orientativa usa el máximo error absoluto logarítmico por horizonte en los siete juegos de validación: predicción × exp(±error). No es un intervalo de confianza ni de predicción con cobertura probabilística garantizada. No uso los errores de prueba para ajustar la banda. La extrapolación de GTA VI y la pequeña muestra limitan su interpretación.

## Cómo contrastaré la previsión

Para el primer horizonte consultaré 2026120300–2026120900 y para el segundo 2026121700–2026122300, siempre con los mismos proyecto, título, accesos y agente. Compararé su media con las previsiones congeladas, 92.162,90 y 51.382,60 consultas diarias. Estas cifras sin redondear son para reproducir el cálculo; el artículo las redondea. No he creado una automatización ni programado una revisión.

## Huellas de los archivos

'''+ '\n'.join(f'- {n}: `{v}`' for n,v in r['huellas'].items())+'\n'
(RAIZ/'fuentes_metodologia.md').write_text(fuentes,encoding='utf-8')

g0=gta['dia0']; vals=gta['v'][18:22]
points=' '.join(f'{80+i*140},{245-v/g0*190:.2f}' for i,v in enumerate(vals))
svg=f'''<svg viewBox="0 0 560 310" role="img" aria-labelledby="gta-curva-t gta-curva-d"><title id="gta-curva-t">Las consultas de GTA VI en sus primeros cuatro días</title><desc id="gta-curva-d">Wikipedia en inglés: 750.227 consultas el 19 de noviembre, 540.793 el 20, 393.338 el 21 y 308.867 el 22. Caída del 58,8 por ciento entre el primero y el cuarto día.</desc><path d="M80 40V245H510" fill="none" stroke="#8a95a9"/><text x="8" y="55" font-size="14" fill="#243047">750.000</text><text x="54" y="245" font-size="14" fill="#243047">0</text><polyline points="{points}" fill="none" stroke="#446ddf" stroke-width="4"/>{''.join(f'<circle cx="{80+i*140}" cy="{245-v/g0*190:.2f}" r="5" fill="#446ddf"/><text x="{80+i*140}" y="275" text-anchor="middle" font-size="14" fill="#243047">{19+i} nov.</text>' for i,v in enumerate(vals))}</svg>'''
datos=[dict(t=s['titulo'].replace('_',' '),y=[round(100*x,6) for x in s['y']]) for s in juegos]
datos_script=json.dumps(datos,ensure_ascii=False,separators=(',',':'))
interaccion='''<section class="gta-explorador" aria-labelledby="gta-ex-t">
<h3 id="gta-ex-t">¿Cuánto queda después del estreno?</h3>
<p>El día de estreno de cada juego vale 100. Compara la previsión experimental de GTA VI con lo que ocurrió de verdad en otro lanzamiento.</p>
<label for="gta-juego">Juego con el que comparar</label>
<select id="gta-juego">'''+''.join(f'<option value="{i}">{s["titulo"].replace("_"," ")}</option>' for i,s in enumerate(juegos))+'''</select>
<label for="gta-semana">Periodo desde el estreno</label>
<select id="gta-semana"><option value="0">Tercera semana: días 14–20</option><option value="1">Quinta semana: días 28–34</option></select>
<p id="gta-ex-resultado" role="status" aria-live="polite" aria-atomic="true">GTA VI: previsión del 12,3 % para la tercera semana. Red Dead Redemption 2 conservó el 21,5 %.</p>
<p id="gta-nombre-a">GTA VI · previsión experimental</p><div class="gta-pista" aria-hidden="true"><div id="gta-barra-a" class="gta-prevista" style="width:12.284669%"></div></div>
<p id="gta-nombre-b">Red Dead Redemption 2 · dato observado</p><div class="gta-pista" aria-hidden="true"><div id="gta-barra-b" style="width:21.547945%"></div></div>
<p><small>Las dos barras usan una escala de 0 a 100 % del estreno. La barra rayada es una estimación; la lisa, un dato histórico. Cada periodo es una media de siete días. Un descenso aquí no equivale a perder jugadores.</small></p>
<div class="gta-tabla" tabindex="0" role="region" aria-label="Previsión y rangos orientativos de GTA VI"><table><caption>Previsión congelada el 23 de noviembre de 2026</caption><thead><tr><th scope="col">Periodo</th><th scope="col">Media diaria prevista</th><th scope="col">Rango orientativo</th></tr></thead><tbody><tr><th scope="row">3–9 diciembre</th><td>92.000 consultas · 12,3 % del estreno</td><td>46.000–186.000</td></tr><tr><th scope="row">17–23 diciembre</th><td>51.000 consultas · 6,8 % del estreno</td><td>16.000–163.000</td></tr></tbody></table></div>
<p><small>El rango traslada errores históricos de validación a esta previsión. No tiene una probabilidad de cobertura garantizada.</small></p>
<noscript>La comparación interactiva necesita JavaScript. La tabla conserva las dos previsiones y sus rangos.</noscript>
</section>
<style>
.gta-observado,.gta-explorador{margin:2rem 0;padding:clamp(1rem,4vw,2rem);background:#faf8f2;color:#243047;border:1px solid #7b8ba8;border-radius:12px}.gta-observado svg{display:block;width:100%;height:auto}.gta-explorador label{display:block;margin:1rem 0 .35rem;font-weight:700}.gta-explorador select{display:block;max-width:100%;min-height:44px;padding:.6rem;background:#fff;color:#243047;font:inherit;border:1px solid #697994}.gta-explorador :focus-visible{outline:3px solid #244fae;outline-offset:4px}.gta-pista{height:24px;background:#e0e5f0;border-radius:5px;overflow:hidden}.gta-pista>div{height:100%;background:#446ddf}.gta-pista>.gta-prevista{background:repeating-linear-gradient(45deg,#446ddf,#446ddf 5px,#bccbf4 5px,#bccbf4 8px)}.gta-tabla{overflow-x:auto;max-width:100%}.gta-tabla table{width:100%;font-size:.9rem}.gta-tabla caption{text-align:left;font-weight:700;margin:1.2rem 0 .5rem}.gta-tabla td,.gta-tabla th{padding:.65rem .5rem;text-align:left;border-bottom:1px solid #bec8d8}.gta-explorador small{font-size:.9rem}
</style>
<script>
(()=>{const juegos=DATOS_JUEGOS;const previsiones=[12.2846689588,6.8489406005];const juego=document.getElementById('gta-juego'),semana=document.getElementById('gta-semana'),salida=document.getElementById('gta-ex-resultado'),a=document.getElementById('gta-barra-a'),b=document.getElementById('gta-barra-b'),nb=document.getElementById('gta-nombre-b');if(!juego||!semana||!salida||!a||!b||!nb)return;const f=n=>n.toLocaleString('es-ES',{maximumFractionDigits:1,minimumFractionDigits:1});function actualizar(){const h=Number(semana.value),s=juegos[Number(juego.value)],p=previsiones[h],v=s.y[h];salida.textContent=`GTA VI: previsión del ${f(p)} % para la ${h===0?'tercera':'quinta'} semana. ${s.t} conservó el ${f(v)} % de las consultas del estreno.`;a.style.width=Math.min(p,100)+'%';b.style.width=Math.min(v,100)+'%';nb.textContent=s.t+' · dato observado';}juego.addEventListener('change',actualizar);semana.addEventListener('change',actualizar);actualizar();})();
</script>'''.replace('DATOS_JUEGOS',datos_script)

editorial='''**Durante años, GTA VI ha sido un juego del que hablar incluso cuando todavía no se podía jugar.** Ahora que ha llegado, la pregunta cambia: ¿cuánto tiempo seguirá despertando la misma curiosidad? He usado los primeros días de su estreno y el comportamiento de otros videojuegos para intentar anticiparlo.

La respuesta de mi modelo es que las consultas de su página en Wikipedia en inglés podrían quedarse alrededor del **12 % del nivel del estreno durante la tercera semana**, y cerca del **7 % durante la quinta**. Es una previsión experimental, con un margen amplio. No significa que vaya a perder esa proporción de jugadores.

## Hablar de un juego y jugarlo son cosas distintas

Rockstar sitúa el lanzamiento el 19 de noviembre. Al día siguiente, Take-Two anunció 3.790 millones de dólares en ventas al público durante la primera jornada, según estimaciones de la empresa. Ese dinero describe una dimensión del fenómeno. Mi pregunta se refiere a otra: la curiosidad que lleva a consultar información sobre él.

Para observarla he elegido una medida pública y repetible: las consultas de Wikipedia. La página inglesa de GTA VI recibió **750.227 el día del estreno**. El 22 de noviembre registró 308.867. Entre el primero y el cuarto día, la caída fue del **58,8 %**.

Imagina una tienda cuya inauguración atrae una cola enorme. Que unos días después haya menos gente mirando el escaparate no demuestra que quienes compraron hayan dejado de usar el producto. Con un videojuego ocurre algo parecido: bajar las consultas puede reflejar que muchas personas ya encontraron la información que buscaban.

GRAFICO_OBSERVADO

## Lo difícil empieza después de la primera semana

He reunido treinta lanzamientos y utilizado veintiocho, desde Fallout 4 hasta Spider-Man 2. He descartado dos comparaciones problemáticas: Dark Souls III tuvo un estreno japonés anterior al mundial y el título consultado de Baldur’s Gate 3 presenta un problema de cobertura en sus primeros días.

Para comparar juegos de tamaños distintos, doy valor cien a las consultas del día del estreno. Después observo cuánto conservan. No comparo ventas ni doy por hecho que un juego pequeño pueda explicar por completo uno como GTA VI.

El modelo aprende de dos señales: cuánto ha caído la atención en los primeros cuatro días y cuánta había durante la semana anterior. Con ellas estima la media diaria de dos semanas completas, evitando que un sábado aislado decida el resultado.

La prueba consiste en hacer como si aquellos juegos acabasen de salir: el modelo solo recibe sus primeros días y tiene que anticipar semanas que le he ocultado. Después comparo sus respuestas con los datos reales. Así puedo comprobar si ha aprendido un patrón útil o si simplemente hace cuentas que suenan convincentes.

Pero antes de aplicarlo a GTA VI tenía que demostrar que aportaba algo. **En siete juegos reservados para la prueba, redujo un 16 % el error de una regla que aplica la retención mediana de estrenos anteriores.** La mejora existe en esta muestra; no convierte el método en una máquina de acertar.

INTERACCION

## Una cifra central y mucho espacio para equivocarse

Para el periodo del **3 al 9 de diciembre**, la previsión ronda las **92.000 consultas diarias**. Para el **17 al 23 de diciembre**, unas **51.000**. Son medias previstas de consultas de una página, no personas distintas, búsquedas en Google o jugadores conectados.

Los errores de los juegos usados para validar el método obligan a dejar bastante espacio alrededor: aproximadamente **46.000–186.000 consultas** en la primera ventana y **16.000–163.000** en la segunda. Estos rangos orientativos no garantizan una probabilidad de acierto concreta.

Además, GTA VI parte de un estreno mayor que cualquiera de los juegos con los que he ajustado el modelo. Su caída inicial también es algo más intensa. Es una pequeña salida fuera del terreno conocido que hace la predicción más incierta, aunque comparemos proporciones.

Una actualización, una polémica o un anuncio pueden volver a disparar las consultas. El modelo no sabe qué noticia llegará mañana. Tampoco representa a todos los países: una página en inglés es solo una ventana al fenómeno.

Lo interesante será volver cuando terminen ambas semanas y enfrentar la previsión con lo ocurrido, conservando estas cifras. **Si las consultas caen, eso no demostrará que GTA VI ha dejado de importar.** Habrá cambiado una forma concreta de prestarle atención. La vida del juego sigue fuera de ese contador.
'''
texto=editorial.replace('GRAFICO_OBSERVADO','').replace('INTERACCION','')
palabras=len(re.findall(r"\b[\wÀ-ÿ]+\b",texto))
assert 700<=palabras<=800,palabras
articulo='''---
titulo: "¿Cuánto durará la fiebre de GTA VI? He intentado predecirlo con 28 videojuegos"
descripcion: "La atención ya está cayendo. Un modelo experimental anticipa cuánto podría quedar en diciembre y deja una previsión que podremos comprobar."
tema: "TECNOLOGÍA"
fecha: 2026-11-23
imagenPortada: "/nebula/imagenes/gta_vi_fiebre_portada.png"
cifraDestacada: "12 %"
etiquetaCifra: "del estreno: previsión para la tercera semana"
textoContinuo: "¿Cuánto dura la curiosidad cuando por fin llega el juego que llevabas años esperando?"
metodologia: "Machine learning experimental con consultas diarias de Wikipedia en inglés, all-access y user, días UTC. Muestra de conveniencia: 30 lanzamientos, 28 utilizados; 14 para entrenamiento, 7 para validación y 7 para prueba por fecha. Regresión ridge con dos variables disponibles hasta el día +3; objetivos: medias de +14 a +20 y +28 a +34 respecto al día 0. Elijo la penalización solo en validación y comparo con mediana histórica y persistencia. Mejora del 16,25 % en error absoluto logarítmico frente a la mediana en la prueba. Bandas orientativas basadas en errores de validación, sin cobertura probabilística garantizada. Corte: 23 de noviembre de 2026; último dato GTA VI: 22 de noviembre. No predice ventas ni jugadores."
---

'''+editorial.replace('GRAFICO_OBSERVADO','<figure class="gta-observado">'+svg+'<figcaption>Consultas diarias de Wikipedia en inglés. Datos observados, días UTC. Fuente: Wikimedia Analytics API.</figcaption></figure>').replace('INTERACCION',interaccion)+'''
## Fuentes y archivos

- [Fecha de lanzamiento en la tienda de Rockstar](https://store.rockstargames.com/game/buy-gta-vi?drm=playstation).
- [Comunicado original de Take-Two depositado en la SEC, 20 de noviembre](https://www.sec.gov/Archives/edgar/data/946581/000162828026075217/exhibit9918k.htm).
- [Documentación oficial de Wikimedia Analytics API](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/).
- [Notebook de preparación](/nebula/analisis/gta_vi_fiebre/01_preparacion_datos.ipynb) y [notebook de predicción y evaluación](/nebula/analisis/gta_vi_fiebre/02_prediccion.ipynb).
- [Datos diarios en CSV](/nebula/analisis/gta_vi_fiebre/consultas_diarias.csv), [serie de GTA VI](/nebula/analisis/gta_vi_fiebre/gta_vi_consultado.json), [treinta series conservadas](/nebula/analisis/gta_vi_fiebre/series_consultadas.json), [código del modelo](/nebula/analisis/gta_vi_fiebre/modelo.py) y [resultados completos](/nebula/analisis/gta_vi_fiebre/resultados.json).
- [Protocolo previo al cálculo](/nebula/analisis/gta_vi_fiebre/protocolo.md) y [fuentes, peticiones exactas, decisiones y limitaciones](/nebula/analisis/gta_vi_fiebre/fuentes_metodologia.md).

La previsión se conserva con fecha de corte del 23 de noviembre. Los datos futuros se añadirán en una revisión identificada; no están presentes en este análisis.
'''
(RAIZ/'gta_vi_fiebre.md').write_text(articulo,encoding='utf-8')
post='''GTA VI lleva años despertando curiosidad. Ahora que se puede jugar, ¿cuánto durará esa fiebre?

Con datos públicos de Wikimedia Foundation, he comparado 28 lanzamientos para intentar anticiparlo. La previsión ya está fijada; en diciembre podremos comprobar cuánto se ha equivocado.

https://robertocantero82.github.io/nebula/articulos/gta_vi_fiebre/

#GTA6 #Videojuegos #OpenToWork #BuscandoTrabajo #Periodista #Redactor #CienciaDeDatos
'''
(RAIZ/'post_linkedin_gta_vi.md').write_text(post,encoding='utf-8')
(RAIZ/'requirements.txt').write_text('numpy=='+np.__version__+'\n',encoding='utf-8')
print(json.dumps(dict(palabras_editoriales=palabras,notebooks_ejecutados=2,archivos=[p.name for p in RAIZ.iterdir() if p.is_file()]),ensure_ascii=False,indent=2))
