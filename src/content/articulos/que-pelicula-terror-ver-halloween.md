---
titulo: "¿Qué película de terror deberías ver este Halloween?"
descripcion: "Este recomendador contiene decenas de películas y tiene en cuenta tus gustos y el tiempo que tienes."
tema: "CINE"
fecha: 2026-10-26T00:00:00+01:00
imagenPortada: "/nebula/imagenes/halloween_cine_portada.png"
cifraDestacada: "120"
etiquetaCifra: "películas para encontrar la que encaja en tu noche"
metodologia: "EDA de una selección editorial de 120 títulos de 1922 a 2022, incluido el mediometraje La cabina. 1.074.778 votos de MovieLens 32M hasta octubre de 2023. Países y géneros de Wikidata; duraciones contrastadas con fichas de Wikipedia, utilizando el mayor valor cuando la ficha recoge varios. Familias, tono e intensidad son etiquetas editoriales subjetivas. Recomendación por filtros exactos y orden por nota media o número de votos, sin aprendizaje automático ni predicciones. No representa todo el género, no mide miedo, no indica clasificación por edades y no verifica disponibilidad en plataformas."
---

Son las diez de la noche. Hay algo para picar, el sofá está libre y alguien propone ver una película de terror. Media hora después seguís mirando menús. Uno quiere fantasmas, otro pide que no sea demasiado gore y alguien recuerda que mañana madruga. El problema no es que falten películas. Es ponerse de acuerdo.

Para este Halloween he reunido **120 títulos**, desde *Nosferatu* hasta *Háblame*, y he cruzado sus características con más de un millón de votos. La pregunta no es cuál gana una clasificación universal, sino cuál encaja en la noche que quieres tener. Prueba a elegir antes de seguir leyendo.


<section id="halloween-recomendador" aria-labelledby="halloween-titulo">
<p class="halloween-kicker">TU SESIÓN DE HALLOWEEN</p>
<h2 id="halloween-titulo">¿Qué te apetece esta noche?</h2>
<p>120 películas de 1922 a 2022. Selección editorial y votos históricos de MovieLens hasta octubre de 2023.</p>
<form>
<div class="halloween-campos">
<label>¿Qué tipo de terror buscas?<select name="familia"><option value="">Me da igual</option><option value="fantasmas">Fantasmas</option><option value="asesinos">Asesinos</option><option value="monstruos">Monstruos</option><option value="psicologico">Terror psicológico</option><option value="ciencia-ficcion">Ciencia ficción</option><option value="zombis">Zombis</option><option value="vampiros">Vampiros</option><option value="ocultismo">Brujería y posesiones</option></select></label>
<label>¿Cuánto tiempo tienes?<select name="minutos"><option value="">Sin límite</option><option value="90">Hasta 90 minutos</option><option value="100">Hasta 100 minutos</option><option value="120">Hasta dos horas</option></select></label>
<label>¿Hasta qué intensidad?<select name="intensidad" aria-describedby="halloween-intensidad"><option value="">Cualquier intensidad</option><option value="1">1 · Amenaza sugerida</option><option value="2">Hasta 2 · Tensión intermedia</option><option value="3">Hasta 3 · Violencia o angustia intensa</option></select></label>
<label>¿Clásica o moderna?<select name="epoca"><option value="">Cualquier época</option><option value="clasica">Anterior a 2000</option><option value="moderna">Desde 2000</option></select></label>
<label>¿Seria o con humor?<select name="tono"><option value="">Me da igual</option><option value="serio">Tono serio</option><option value="humor">Con humor</option></select></label>
<label>¿Alguna procedencia?<select name="pais"><option value="">Cualquier país</option><option value="España">España, incluidas coproducciones</option><option value="Japón">Japón</option><option value="Corea del Sur">Corea del Sur</option><option value="Estados Unidos">Estados Unidos</option></select></label>
<label>Ordenar coincidencias por<select name="orden"><option value="nota">Nota media</option><option value="votos">Número de votos</option></select></label>
</div>
<p id="halloween-intensidad" class="halloween-detalle">Intensidad editorial orientativa: no mide tu miedo ni indica una edad recomendada. El humor puede incluir violencia. Las duraciones dependen de la versión.</p>
<div class="halloween-acciones"><button type="submit" disabled>Encontrar mi película</button><button type="reset">Reiniciar</button></div>
</form>
<p id="halloween-estado" role="status" aria-live="polite" tabindex="-1">Preparando el catálogo…</p>
<div id="halloween-resultados"></div>
<button id="halloween-mas" type="button" hidden>Ver otras tres coincidencias</button>
<noscript>Necesitas activar JavaScript para usar el recomendador. Puedes consultar el <a href="/nebula/analisis/halloween_cine/peliculas_analizadas.csv">catálogo en CSV</a> o el notebook al final del artículo.</noscript>
<details><summary>Cómo elijo las recomendaciones</summary><p>Aplico todos tus filtros sin cambiarlos. Entre las coincidencias, ordeno por media de estrellas sin redondear; los empates se resuelven por votos y después por identificador. Si eliges votos, ordeno primero por participación. Muestro tres resultados y puedes pedir más. Las familias, el tono y la intensidad son etiquetas editoriales. No utilizo un modelo predictivo.</p></details>
</section>
<script type="module" src="/nebula/analisis/halloween_cine/recomendador_halloween.js"></script>


## Tu reloj también tiene sus propios gustos

Empecemos por una preferencia que rara vez aparece en las listas de imprescindibles: a qué hora quieres acostarte. Si dispones de **90 minutos, tienes disponibles 27 películas**. Con dos horas, las opciones suben a **104**. Media hora de margen cambia bastante más el menú que discutir si una nota debería tener una décima adicional.

El gráfico cuenta las películas que caben en cada límite. Los grupos se acumulan: una historia de 85 minutos también entra en la barra de dos horas. Entre las más breves está *La cabina*, un mediometraje televisivo de 35 minutos. Porque no todo el terror tiene que tener el tamaño de un largometraje.

<figure class="halloween-grafico"><figcaption>Media hora más abre muchas puertas</figcaption><svg viewBox="0 0 600 205" role="img" aria-label="Películas de la selección que caben: 27 en 90 minutos, 56 en 100 minutos y 104 en 120 minutos. Máximo posible: 120."><g fill="currentColor" font-family="sans-serif" font-size="16"><text x="0" y="48">90 min</text><rect x="88" y="30" width="430" height="27" rx="3" fill="#e9edf7"/><rect x="88" y="30" width="96.75" height="27" rx="3" fill="#446ddf"/><text x="533" y="49">27</text><text x="0" y="103">100 min</text><rect x="88" y="85" width="430" height="27" rx="3" fill="#e9edf7"/><rect x="88" y="85" width="200.66666666666666" height="27" rx="3" fill="#446ddf"/><text x="533" y="104">56</text><text x="0" y="158">120 min</text><rect x="88" y="140" width="430" height="27" rx="3" fill="#e9edf7"/><rect x="88" y="140" width="372.6666666666667" height="27" rx="3" fill="#446ddf"/><text x="533" y="159">104</text></g></svg><p>Conteo acumulado sobre 120 títulos. Duraciones de referencia contrastadas; se incluye un mediometraje.</p></figure>

Eso permite decisiones bastante concretas. Para una sesión de humor de hasta hora y media, *Lo que hacemos en las sombras* aparece por delante de *Tucker y Dale contra el mal* y *Terroríficamente muertos*. No significa que los vampiros sean mejores protagonistas. Significa que esas películas cumplen las condiciones y ese es su orden por nota.

Las duraciones son referencias, no promesas sobre cualquier copia. Hay montajes distintos, restauraciones y fichas que discrepan. He contrastado los datos y, cuando una ficha enumera varias duraciones, utilizo la mayor. Antes de darle al botón de reproducir, conviene mirar cuánto dura tu versión. Por si acaso.

## Los clásicos no ganan por decreto

La nostalgia suele entrar en estas conversaciones, casi sin querer. Ya cuestioné algunas ideas recibidas en [el análisis de *Matrix* y sus secuelas](/nebula/articulos/matrix-secuelas/). Si te preguntas si se hacía mejor terror antes, la respuesta es difusa. En esta selección, la película situada en el centro de las notas anteriores al año 2000 obtiene **3,61 estrellas sobre cinco**. Entre las estrenadas desde entonces, la cifra es **3,62**. Prácticamente un empate.

Ese valor central se llama mediana: ordeno las notas y miro la del medio, dando el mismo peso a cada película. Así evito que un título muy conocido decida por todos los demás. Son 70 películas en el primer grupo y 50 en el segundo.

Lo que sí cambia es la participación. La cifra central pasa de **6.014 votos por película** entre las antiguas a **2.949** entre las modernas. Haber acumulado más opiniones no convierte una obra en mejor, pero recuerda que las notas no llegan con el mismo respaldo.

<figure class="halloween-grafico"><figcaption>Notas casi iguales, participación desigual</figcaption><div class="halloween-comparacion"><div><strong>Antes de 2000</strong><p>70 películas</p><p><b>3,61</b> / 5 · nota central</p><div class="halloween-barra" role="img" aria-label="Nota central 3,61 sobre cinco"><span style="width:72.15165879859025%"></span></div><p><b>6.014</b> votos · cifra central</p></div><div><strong>Desde 2000</strong><p>50 películas</p><p><b>3,62</b> / 5 · nota central</p><div class="halloween-barra" role="img" aria-label="Nota central 3,62 sobre cinco"><span style="width:72.47075381915262%"></span></div><p><b>2.949</b> votos · cifra central</p></div></div><p>Medianas por película. Escala de las barras: de 0 a 5 estrellas. MovieLens 32M, votos hasta octubre de 2023.</p></figure>

Tampoco estamos viendo el marcador de hoy. Los votos proceden de MovieLens y llegan hasta octubre de 2023. Es una fotografía histórica de sus usuarios, no una encuesta al público español. Por eso esta herramienta sirve para descubrir películas, pero no pretende cubrir los estrenos más recientes ni decir dónde están disponibles.

## Reírse no evita la sangre

Otra trampa aparece al pedir algo divertido. **He marcado 18 títulos con humor, pero diez también están en el escalón editorial más intenso**. *Zombies Party* puede hacerte reír y seguir mostrando violencia. La comedia y la suavidad son cuestiones diferentes.

Estas etiquetas son orientaciones mías basadas en los argumentos: distingo amenaza, tensión intermedia y violencia explícita o angustia especialmente dura. No he medido pulsaciones ni puedo saber qué te quitará el sueño. Una aparición apenas visible puede afectarte más que una criatura llena de dientes afilados. Tampoco son recomendaciones por edades.

El mecanismo no esconde inteligencia artificial ni una fórmula de afinidad. Primero aplica tus filtros y después ordena las coincidencias por la media de estrellas. Puedes cambiar el orden al número de votos. Si no encuentra nada, lo dice. No sustituye tus preferencias por otras para fabricar una respuesta.

## Una invitación, no un veredicto

La **selección** mezcla clásicos, cine español y asiático, monstruos y suspense. No representa todo el género: la he **construido para ofrecer variedad**. Como en [la búsqueda de la película más otoñal](/nebula/articulos/peliculas-mas-otonales/), definir qué busco condiciona lo que encuentro. Las comparaciones describen estas 120 películas, y cambiar la selección o la frontera entre épocas puede cambiar el resultado.

Los datos ayudan a descartar una película demasiado larga y a encontrar otra que quizá no tenías presente. La última decisión sigue siendo bastante humana: qué te apetece ver, con quién y cuánta oscuridad quieres llevarte después a la cama.

## Fuentes y análisis

EDA con selección editorial de 120 películas. Consulta de metadatos: 26 de octubre de 2026. Valoraciones históricas: [MovieLens 32M, GroupLens](https://grouplens.org/datasets/movielens/32m/), con votos hasta el 12 de octubre de 2023. Referencia: Harper y Konstan (2015), [The MovieLens Datasets: History and Context](https://doi.org/10.1145/2827872). Los datos transformados conservan la [licencia de MovieLens](/nebula/analisis/halloween_cine/LICENCIA_MOVIELENS.txt); GroupLens no respalda este proyecto.

Países y géneros: [Wikidata](https://www.wikidata.org/), datos estructurados CC0. Duraciones contrastadas y argumentos: fichas de Wikipedia enlazadas individualmente en los resultados y los datos. Sinopsis propias; familias, tono e intensidad de elaboración editorial. No utilizo la nota como medida del miedo ni el número de votos como popularidad mundial.

[Notebook ejecutado](/nebula/analisis/halloween_cine/halloween_cine_eda.ipynb) · [Datos analizados](/nebula/analisis/halloween_cine/peliculas_analizadas.csv) · [Votos agregados](/nebula/analisis/halloween_cine/votos_histograma.csv) · [Descargar análisis reproducible completo](/nebula/analisis/halloween_cine/halloween_cine_reproducible.zip) · [Metodología y guía](/nebula/analisis/halloween_cine/README.md).

<style>
#halloween-recomendador {margin:2rem 0;padding:clamp(18px,4vw,30px);background:#f5f6fb;border:1px solid #dce2f3;border-radius:10px;color:#24243b}
#halloween-recomendador h2 {margin:0 0 12px;font-size:1.6rem}
#halloween-recomendador .halloween-kicker {font-size:.72rem;letter-spacing:.1em;font-weight:700;color:#446ddf;margin:0 0 8px}
.halloween-campos {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:24px 0}
.halloween-campos label {font-size:.92rem;font-weight:600;display:flex;flex-direction:column;gap:7px;min-width:0}
.halloween-campos select {width:100%;min-width:0;min-height:46px;border:1px solid #bcc6df;border-radius:5px;background:white;color:#24243b;font:inherit;font-weight:400;padding:9px}
.halloween-acciones {display:flex;flex-wrap:wrap;gap:10px}
#halloween-recomendador button {border:1px solid #446ddf;border-radius:5px;padding:12px 16px;min-height:44px;background:#446ddf;color:white;font:inherit;font-size:.95rem;cursor:pointer}
#halloween-recomendador button[type=reset] {background:transparent;color:#314ea4}
#halloween-recomendador button:disabled {opacity:.55;cursor:wait}
#halloween-recomendador button:hover:not(:disabled) {background:#324fac;color:white}
#halloween-recomendador :focus-visible {outline:3px solid #446ddf;outline-offset:4px}
#halloween-recomendador [hidden] {display:none!important}
#halloween-recomendador #halloween-estado {font-size:.95rem;margin:22px 0 14px;line-height:1.6}
.halloween-tarjeta {padding:20px;background:white;border:1px solid #dce2f3;border-left:4px solid #446ddf;border-radius:6px;margin:0 0 16px;overflow-wrap:anywhere}
#halloween-recomendador .halloween-tarjeta h3 {font-size:1.25rem;margin:0 0 8px;line-height:1.4}
#halloween-recomendador .halloween-tarjeta p {margin:8px 0;line-height:1.6}
#halloween-recomendador .halloween-dato {font-size:.93rem;font-weight:600;color:#314ea4}
#halloween-recomendador .halloween-porque {font-size:.94rem}
#halloween-recomendador .halloween-detalle,#halloween-recomendador .halloween-aviso {font-size:.82rem;color:#505569}
#halloween-recomendador .halloween-aviso {color:#7a4a16}
#halloween-recomendador details {margin-top:22px;font-size:.85rem;line-height:1.6}
#halloween-recomendador summary {cursor:pointer;font-weight:600;padding:6px 0}
.halloween-grafico {margin:2rem 0;padding:20px;background:#f7f8fc;border-radius:7px}
.halloween-grafico figcaption {font-size:1.1rem;font-weight:700;margin-bottom:10px}
.halloween-grafico svg {display:block;width:100%;height:auto}
.halloween-grafico>p {font-size:.8rem;line-height:1.5;margin-bottom:0;color:#505569}
.halloween-comparacion {display:grid;grid-template-columns:1fr 1fr;gap:24px;margin:20px 0}
.halloween-comparacion p {font-size:.9rem;margin:7px 0}
.halloween-comparacion b {font-size:1.4rem;color:#314ea4}
.halloween-barra {height:9px;background:#e0e6f5;border-radius:4px;margin:10px 0 16px;overflow:hidden}
.halloween-barra span {display:block;height:100%;background:#446ddf}
@media(max-width:540px){.halloween-campos{grid-template-columns:1fr}.halloween-grafico{padding:12px}.halloween-comparacion{gap:12px}.halloween-comparacion p{font-size:.8rem}.halloween-comparacion b{font-size:1.2rem}}
</style>
