---
titulo: 'El satélite Swift iba a caer a la Tierra: ¿con cuánta antelación pude predecir el momento exacto?'
descripcion: 'Reconstruí sus últimas semanas en órbita. Al principio, el modelo falló por más de cuatro días; poco antes de la reentrada, rozó el acierto.'
tema: 'CIENCIA'
fecha: 2026-11-06
imagenPortada: '/nebula/imagenes/swift_reentrada_portada.png'
cifraDestacada: '4 minutos'
etiquetaCifra: 'entre la predicción y la caída'
textoContinuo: "La predicción de la caída de Swift se desvió solo cuatro minutos"
metodologia: 'Predicción retrospectiva con 1.594 conjuntos de elementos orbitales TLE de Swift entre el 1 de enero de 2025 y el 3 de noviembre de 2026, solicitados al archivo histórico de CelesTrak. Convierto el movimiento medio en altura aproximada y conservo la última observación de cada día. Entreno hasta el 31 de agosto de 2026, valido del 1 de septiembre al 15 de octubre y reservo 18 observaciones desde el 16 de octubre como prueba. Comparo una regresión lineal de referencia con una relación de potencia entre el margen sobre 120 kilómetros y las horas restantes. La reentrada de referencia es la confirmada por NASA: 4 de noviembre de 2026 a las 12:39 UTC. Es un modelo retrospectivo de un solo satélite, no una herramienta de seguridad ni un predictor general.'
---

El 16 de octubre, m**i modelo creía que al observatorio Swift le quedaban 23 días y medio en órbita**. En realidad, le quedaban 19. Se equivocaba por más de cuatro días. Dos semanas después, el error había bajado a menos de dos horas. El reloj parecía estar aprendiendo a toda velocidad.

Swift terminó cayendo sobre la atmósfera el 4 de noviembre de 2026 a las 12:39 UTC, después de casi 22 años observando [estallidos de rayos gamma, algunas de las explosiones más violentas del universo](/nebula/articulos/estallidos-rayos-gamma-cielo/), y otros fenómenos fugaces. La mayor parte del satélite se quemó durante la entrada. Su final dejó una pregunta bastante terrenal: ¿cuándo podemos saber que una máquina que gira alrededor del planeta está a punto de caer?

He intentado responderla con **1.594 observaciones orbitales** publicadas entre enero de 2025 y la víspera de la reentrada.

<figure class="video-swift">
  <div class="video-swift__contenedor">
    <iframe
      src="https://www.youtube-nocookie.com/embed/uTv-P7py_c8?rel=0"
      title="La NASA no pudo salvar a Swift: el final de un observatorio legendario"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>

  <figcaption>
    Qué era el observatorio Swift, qué descubrió durante casi 22 años y por qué terminó cayendo hacia la Tierra.
  </figcaption>
</figure>

<style>
.video-swift {
  margin: 2rem 0;
}

.video-swift__contenedor {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 14px;
  background: #101626;
}

.video-swift__contenedor iframe {
  width: 100%;
  height: 100%;
  border: 0;
}

.video-swift figcaption {
  margin-top: 0.65rem;
  color: #586174;
  font-size: 0.85rem;
  line-height: 1.5;
}
</style>

## Una caída que no se parece a una rampa

**Un satélite bajo no viaja por un vacío perfecto**. Encuentra partículas de la atmósfera, pierde energía y desciende. Cuanto más baja, más denso es el aire y mayor puede ser el frenazo. La actividad solar añade otra complicación: calienta y expande las capas altas de la atmósfera.

Por eso una **línea recta es una mala brújula**. La utilicé como modelo de referencia y fracasó de forma espectacular. Al proyectar hacia alturas que todavía no había visto, llegó a devolver tiempos negativos. Era como calcular cuándo se detendrá una bicicleta suponiendo que mantendrá siempre la misma velocidad.

**El segundo modelo utiliza una curva de potencia**. Relaciona la altura aproximada con las horas que faltan, pero permite que la caída se acelere. No es un simulador orbital de NASA: es una fórmula sencilla elegida antes de abrir el periodo final de prueba.

<figure class="grafico-interactivo grafico-swift">
  <svg viewBox="0 0 680 330" role="img" aria-label="La altura media aproximada de Swift baja desde 304 kilómetros el 16 de octubre hasta 184 kilómetros el 3 de noviembre">
    <title>La órbita de Swift se deshace al final</title>
    <text x="20" y="30" class="grafico-titulo">La órbita se deshace al final</text>
    <text x="20" y="54" class="grafico-subtitulo">Altura media aproximada en las últimas observaciones</text>
    <g class="grafico-rejilla"><line x1="70" y1="95" x2="650" y2="95"/><line x1="70" y1="168" x2="650" y2="168"/><line x1="70" y1="241" x2="650" y2="241"/></g>
    <g class="grafico-eje"><text x="58" y="100" text-anchor="end">300 km</text><text x="58" y="173" text-anchor="end">250 km</text><text x="58" y="246" text-anchor="end">200 km</text><text x="70" y="305" text-anchor="middle">16 oct</text><text x="343" y="305" text-anchor="middle">25 oct</text><text x="479" y="305" text-anchor="middle">29 oct</text><text x="650" y="305" text-anchor="middle">3 nov</text></g>
    <polyline class="grafico-linea" points="70,89 104,95 138,105 172,110 206,117 241,126 275,133 309,146 343,151 377,157 411,166 445,172 479,179 514,188 548,199 582,214 616,230 650,265"/>
    <g class="grafico-puntos"><circle cx="70" cy="89" r="5"><title>16 de octubre: 304,3 km</title></circle><circle cx="343" cy="151" r="5"><title>25 de octubre: 261,5 km</title></circle><circle cx="479" cy="179" r="5"><title>29 de octubre: 242,2 km</title></circle><circle cx="650" cy="265" r="5"><title>3 de noviembre: 183,5 km</title></circle></g>
    <text x="82" y="80" class="grafico-anotacion">304 km</text><text x="640" y="254" text-anchor="end" class="grafico-anotacion">184 km</text>
  </svg>
</figure>

## Dieciocho oportunidades para equivocarse

Separé los datos como separaría el tiempo: primero 566 días para entrenar, después 34 para escoger el método y, finalmente, 18 observaciones que el modelo no podía mirar. En esas últimas semanas, el error absoluto medio fue de 32,5 horas. El número parece grande, pero esconde una transformación.

**El 16 de octubre la predicción se retrasaba 103,7 horas**. El 25 de octubre, solo 14,9. El día 29, modelo y realidad quedaron separados por apenas cuatro minutos. A partir de ahí empezó a adelantarse: **el último cálculo** disponible situaba la caída **8,4 horas antes de lo que ocurrió**.

<figure class="grafico-interactivo grafico-swift">
  <svg viewBox="0 0 680 330" role="img" aria-label="El error de la predicción baja desde 103,7 horas el 16 de octubre hasta casi cero el 29 de octubre y termina adelantándose 8,4 horas el 3 de noviembre">
    <title>La predicción fue cerrando el margen</title>
    <text x="20" y="30" class="grafico-titulo">La predicción fue cerrando el margen</text>
    <text x="20" y="54" class="grafico-subtitulo">Horas de diferencia respecto a la reentrada real</text>
    <g class="grafico-rejilla"><line x1="70" y1="95" x2="650" y2="95"/><line x1="70" y1="168" x2="650" y2="168"/><line x1="70" y1="241" x2="650" y2="241" class="linea-cero"/></g>
    <g class="grafico-eje"><text x="58" y="100" text-anchor="end">100 h</text><text x="58" y="173" text-anchor="end">50 h</text><text x="58" y="246" text-anchor="end">0 h</text><text x="70" y="305" text-anchor="middle">16 oct</text><text x="343" y="305" text-anchor="middle">25 oct</text><text x="479" y="305" text-anchor="middle">29 oct</text><text x="650" y="305" text-anchor="middle">3 nov</text></g>
    <polyline class="grafico-linea" points="70,89 104,108 138,131 172,141 206,154 241,170 275,183 309,210 343,219 377,225 411,231 445,235 479,241 514,244 548,251 582,258 616,259 650,254"/>
    <g class="grafico-puntos"><circle cx="70" cy="89" r="5"><title>16 de octubre: 103,7 horas tarde</title></circle><circle cx="343" cy="219" r="5"><title>25 de octubre: 14,9 horas tarde</title></circle><circle cx="479" cy="241" r="6"><title>29 de octubre: unos cuatro minutos de diferencia</title></circle><circle cx="650" cy="254" r="5" class="punto-adelanto"><title>3 de noviembre: 8,4 horas antes</title></circle></g>
    <text x="82" y="80" class="grafico-anotacion">4,3 días tarde</text><text x="479" y="228" text-anchor="middle" class="grafico-anotacion">casi exacta</text><text x="640" y="278" text-anchor="end" class="grafico-anotacion">8,4 h antes</text>
    <text x="650" y="322" text-anchor="end" class="grafico-nota">Sobre cero: tarde · Bajo cero: antes</text>
  </svg>
</figure>

La mejora no fue mágica. Cada nueva observación revelaba cuánto se había acelerado la pérdida de altura. Cuando Swift bajó de unos 260 kilómetros, la curva empezó a doblarse con claridad. El modelo recibía información mucho más cercana al desenlace.

<section class="swift-bloque" aria-labelledby="swift-selector-titulo"><h3 id="swift-selector-titulo">Mueve el reloj de la predicción</h3><label for="swift-fecha">Observación utilizada</label><input id="swift-fecha" type="range" min="0" max="17" value="17" step="1"><p id="swift-resultado" role="status" aria-live="polite"></p><div class="swift-relojes"><div><span>Modelo</span><strong id="swift-modelo"></strong></div><div><span>Realidad</span><strong id="swift-real"></strong></div></div><p class="swift-nota">Las horas se cuentan desde la observación hasta la reentrada. Un error positivo significa que el modelo esperaba una caída más tardía.</p></section>

## Acertar la hora no basta para señalar el lugar

Predecir el momento tampoco equivale a marcar un punto en el mapa. Swift completaba una vuelta aproximadamente cada 88 minutos. Un error de ocho horas representa más de cinco órbitas: miles de kilómetros de posibles diferencias sobre la superficie terrestre.

Además, **este ejercicio conoce el final porque mira hacia atrás**. He ocultado cronológicamente las últimas semanas para reproducir una predicción, pero solo dispongo de una caída. El resultado no demuestra que la fórmula funcione con otros satélites. Tampoco incorpora la orientación de Swift, la densidad real de la termosfera ni las previsiones solares que utilizan los modelos profesionales.

Ahí está precisamente la lección. Tres semanas antes, una cifra concreta podía aparentar una seguridad que los datos no tenían. En los últimos días, el reloj se estrechó, pero nunca dejó de moverse.

Swift pasó dos décadas reaccionando en segundos a explosiones situadas a miles de millones de años luz. Era una misión muy distinta a [Voyager 1, que necesita casi un día para que su señal alcance la Tierra](/nebula/articulos/voyager-un-dia-luz/), pero ambas recuerdan **lo difícil que resulta medir el tiempo en el espacio**. Para anticipar las últimas horas de Swift hubo que esperar hasta tenerlo casi encima.

## Fuentes y análisis

- [NASA: reentrada del observatorio Swift](https://science.nasa.gov/blogs/swift/2026/11/02/nasas-swift-observatory-to-re-enter-atmosphere/) y [reto de modelización de la termosfera](https://ccmc.gsfc.nasa.gov/challenges/swift-challenge/).
- [Archivo histórico de elementos orbitales de CelesTrak](https://celestrak.org/norad/archives/).
- [Notebook ejecutado](/nebula/analisis/swift_reentrada/analisis_swift_reentrada.ipynb), [datos TLE originales](/nebula/analisis/swift_reentrada/datos/sat000028485.json) y [guía de reproducción](/nebula/analisis/swift_reentrada/README.md).

<style>
.grafico-swift{margin:2.4rem 0}.grafico-swift svg{display:block;width:100%;height:auto;font-family:var(--font-body);overflow:visible}.grafico-swift .grafico-titulo{fill:currentColor;font-family:var(--font-heading);font-size:20px;font-weight:600}.grafico-swift .grafico-subtitulo{fill:#555;font-size:13px}.grafico-swift .grafico-rejilla line{stroke:#dfe4f0;stroke-width:1}.grafico-swift .grafico-rejilla .linea-cero{stroke:#77829a;stroke-width:1.5;stroke-dasharray:5 5}.grafico-swift .grafico-eje{fill:#697386;font-size:12px}.grafico-swift .grafico-linea{fill:none;stroke:#446ddf;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}.grafico-swift .grafico-puntos circle{fill:#446ddf;stroke:#fff;stroke-width:2}.grafico-swift .grafico-puntos .punto-adelanto{fill:#314ea4}.grafico-swift .grafico-anotacion{fill:currentColor;font-size:13px;font-weight:700}.grafico-swift .grafico-nota{fill:#697386;font-size:11px}.swift-bloque{border:1px solid #446ddf;border-radius:14px;padding:1.4rem;margin:2.4rem 0;background:rgba(68,109,223,.05)}.swift-bloque input{width:100%;accent-color:#446ddf}.swift-relojes{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.swift-relojes div{background:#fff;border-radius:10px;padding:1rem}.swift-relojes span{display:block;font-size:.85em;color:#586174}.swift-relojes strong{font-size:1.2em;color:#23439b}.swift-nota{font-size:.82em;color:#586174}@media(max-width:620px){.grafico-swift{margin:2rem 0}.swift-relojes{grid-template-columns:1fr}}
</style>
<script>
document.addEventListener('DOMContentLoaded',()=>{
 const datos=[['16 oct',562.9,459.2,304.3],['17 oct',525.8,435.2,299.6],['18 oct',478.5,403.7,292.8],['19 oct',456.9,388.7,289.5],['20 oct',425.5,366.2,284.5],['21 oct',390.9,342.3,278.7],['22 oct',361.1,321.3,273.7],['24 oct',294.7,273.5,265.0],['25 oct',263.1,248.2,261.5],['26 oct',227.7,216.8,257.1],['27 oct',187.8,181.1,251.4],['28 oct',162.5,158.8,247.3],['29 oct',135.1,135.0,242.2],['30 oct',107.9,109.8,236.3],['31 oct',78.7,86.1,228.5],['1 nov',50.6,62.4,218.5],['2 nov',29.0,41.7,207.1],['3 nov',6.9,15.3,183.5]];
 const control=document.getElementById('swift-fecha');const actualizar=()=>{const d=datos[Number(control.value)];document.getElementById('swift-resultado').textContent=`Con los datos del ${d[0]}, el error fue de ${Math.abs(d[1]-d[2]).toFixed(1).replace('.',',')} horas.`;document.getElementById('swift-modelo').textContent=`${d[1].toFixed(1).replace('.',',')} h`;document.getElementById('swift-real').textContent=`${d[2].toFixed(1).replace('.',',')} h`;};if(control){control.addEventListener('input',actualizar);actualizar();}
});
</script>
