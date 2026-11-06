---
titulo: 'El satélite Swift iba a caer a la Tierra: ¿con cuánta antelación pude predecir el momento exacto?'
descripcion: 'Reconstruí sus últimas semanas en órbita. Al principio, el modelo falló por más de cuatro días; poco antes de la reentrada, rozó el acierto.'
tema: 'CIENCIA'
fecha: 2026-11-06
imagenPortada: '/nebula/imagenes/swift_reentrada_portada.png'
cifraDestacada: '4 minutos'
etiquetaCifra: 'entre la predicción y la caída'
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

<figure class="swift-figura"><figcaption><strong>La órbita se deshace al final</strong><br>Altura media aproximada de Swift en las últimas observaciones disponibles.</figcaption><div id="swift-altura" class="swift-grafico" role="img" aria-label="La altura de Swift desciende lentamente y acelera hasta unos 183 kilómetros el 3 de noviembre"></div></figure>

## Dieciocho oportunidades para equivocarse

Separé los datos como separaría el tiempo: primero 566 días para entrenar, después 34 para escoger el método y, finalmente, 18 observaciones que el modelo no podía mirar. En esas últimas semanas, el error absoluto medio fue de 32,5 horas. El número parece grande, pero esconde una transformación.

**El 16 de octubre la predicción se retrasaba 103,7 horas**. El 25 de octubre, solo 14,9. El día 29, modelo y realidad quedaron separados por apenas cuatro minutos. A partir de ahí empezó a adelantarse: **el último cálculo** disponible situaba la caída **8,4 horas antes de lo que ocurrió**.

<figure class="swift-figura"><figcaption><strong>La predicción fue cerrando el margen</strong><br>Diferencia entre la hora calculada y la reentrada real. Por encima de cero, el modelo esperaba una caída más tardía; por debajo, la adelantaba.</figcaption><div id="swift-error" class="swift-error-grafico" role="img" aria-label="El error de la predicción baja desde 103,7 horas el 16 de octubre hasta casi cero el 29 de octubre y termina adelantándose 8,4 horas el 3 de noviembre"></div></figure>

<section class="swift-bloque" aria-labelledby="swift-selector-titulo"><h3 id="swift-selector-titulo">Mueve el reloj de la predicción</h3><label for="swift-fecha">Observación utilizada</label><input id="swift-fecha" type="range" min="0" max="17" value="17" step="1"><p id="swift-resultado" role="status" aria-live="polite"></p><div class="swift-relojes"><div><span>Modelo</span><strong id="swift-modelo"></strong></div><div><span>Realidad</span><strong id="swift-real"></strong></div></div><p class="swift-nota">Las horas se cuentan desde la observación hasta la reentrada. Un error positivo significa que el modelo esperaba una caída más tardía.</p></section>

La mejora no fue mágica. Cada nueva observación revelaba cuánto se había acelerado la pérdida de altura. Cuando Swift bajó de unos 260 kilómetros, la curva empezó a doblarse con claridad. El modelo recibía información mucho más cercana al desenlace.

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
.swift-figura{margin:2rem 0}.swift-figura figcaption{font-size:.95em;line-height:1.5;margin-bottom:.8rem}.swift-grafico{height:250px;border-left:1px solid #cbd3e5;border-bottom:1px solid #cbd3e5;display:flex;align-items:flex-end;gap:2px;padding:12px 6px 0}.swift-barra{flex:1;min-width:5px;background:#446ddf;border-radius:3px 3px 0 0}.swift-bloque{border:1px solid #becbec;border-radius:14px;padding:1.2rem;margin:1.8rem 0;background:#f5f7fd}.swift-bloque input{width:100%;accent-color:#446ddf}.swift-relojes{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}.swift-relojes div{background:white;border-radius:10px;padding:1rem}.swift-relojes span{display:block;font-size:.85em;color:#586174}.swift-relojes strong{font-size:1.2em;color:#23439b}.swift-nota{font-size:.82em;color:#586174}.swift-error-grafico{width:100%;margin-top:1rem}.swift-error-grafico svg{display:block;width:100%;height:auto;overflow:visible}.swift-error-rejilla{stroke:#dfe4f0;stroke-width:1}.swift-error-cero{stroke:#77829a;stroke-width:1.5;stroke-dasharray:5 5}.swift-error-linea{fill:none;stroke:#446ddf;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}.swift-error-punto{fill:#446ddf;stroke:#fff;stroke-width:2}.swift-error-adelanto{fill:#d46a3a}.swift-error-eje{fill:#697386;font-size:13px}.swift-error-anotacion{fill:#243451;font-size:13px;font-weight:700}
</style>
<script>
document.addEventListener('DOMContentLoaded',()=>{
 const datos=[['16 oct',562.9,459.2,304.3],['17 oct',525.8,435.2,299.6],['18 oct',478.5,403.7,292.8],['19 oct',456.9,388.7,289.5],['20 oct',425.5,366.2,284.5],['21 oct',390.9,342.3,278.7],['22 oct',361.1,321.3,273.7],['24 oct',294.7,273.5,265.0],['25 oct',263.1,248.2,261.5],['26 oct',227.7,216.8,257.1],['27 oct',187.8,181.1,251.4],['28 oct',162.5,158.8,247.3],['29 oct',135.1,135.0,242.2],['30 oct',107.9,109.8,236.3],['31 oct',78.7,86.1,228.5],['1 nov',50.6,62.4,218.5],['2 nov',29.0,41.7,207.1],['3 nov',6.9,15.3,183.5]];
 const grafico=document.getElementById('swift-altura');if(grafico)datos.forEach(d=>{const b=document.createElement('div');b.className='swift-barra';b.style.height=`${Math.max(4,(d[3]-170)/140*100)}%`;b.title=`${d[0]}: ${d[3].toFixed(1).replace('.',',')} km`;grafico.appendChild(b);});
 const graficoError=document.getElementById('swift-error');if(graficoError){const ancho=760,alto=330,m={arriba:25,derecha:25,abajo:50,izquierda:58},min=-20,max=110;const errores=datos.map(d=>d[1]-d[2]);const x=i=>m.izquierda+i*((ancho-m.izquierda-m.derecha)/(datos.length-1));const y=v=>m.arriba+(max-v)*((alto-m.arriba-m.abajo)/(max-min));const niveles=[100,75,50,25,0,-20];const rejilla=niveles.map(v=>`<line x1="${m.izquierda}" y1="${y(v)}" x2="${ancho-m.derecha}" y2="${y(v)}" class="${v===0?'swift-error-cero':'swift-error-rejilla'}"/><text x="${m.izquierda-10}" y="${y(v)+4}" text-anchor="end" class="swift-error-eje">${v} h</text>`).join('');const puntos=errores.map((v,i)=>`${x(i)},${y(v)}`).join(' ');const circulos=errores.map((v,i)=>`<circle cx="${x(i)}" cy="${y(v)}" r="${i===12?6:4}" class="swift-error-punto ${v<0?'swift-error-adelanto':''}"><title>${datos[i][0]}: ${Math.abs(v).toFixed(1).replace('.',',')} horas ${v>=0?'tarde':'antes'}</title></circle>`).join('');const etiquetas=[0,8,12,17].map(i=>`<text x="${x(i)}" y="${alto-18}" text-anchor="middle" class="swift-error-eje">${datos[i][0]}</text>`).join('');graficoError.innerHTML=`<svg viewBox="0 0 ${ancho} ${alto}" aria-hidden="true">${rejilla}<polyline points="${puntos}" class="swift-error-linea"/>${circulos}${etiquetas}<text x="${x(0)+8}" y="${y(errores[0])-12}" class="swift-error-anotacion">4,3 días tarde</text><text x="${x(12)}" y="${y(errores[12])-14}" text-anchor="middle" class="swift-error-anotacion">casi exacta</text><text x="${x(17)-6}" y="${y(errores[17])+24}" text-anchor="end" class="swift-error-anotacion">8,4 h antes</text></svg>`;}
 const control=document.getElementById('swift-fecha');const actualizar=()=>{const d=datos[Number(control.value)];document.getElementById('swift-resultado').textContent=`Con los datos del ${d[0]}, el error fue de ${Math.abs(d[1]-d[2]).toFixed(1).replace('.',',')} horas.`;document.getElementById('swift-modelo').textContent=`${d[1].toFixed(1).replace('.',',')} h`;document.getElementById('swift-real').textContent=`${d[2].toFixed(1).replace('.',',')} h`;};if(control){control.addEventListener('input',actualizar);actualizar();}
});
</script>
