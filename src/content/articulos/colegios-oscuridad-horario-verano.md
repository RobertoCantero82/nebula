---
titulo: '¿Te gusta el horario de verano? Hay 83 mañanas que pueden hacerte cambiar de opinión'
descripcion: 'La tarde ganaría una hora de luz, pero mantenerla durante el invierno extendería las salidas antes del amanecer a toda España.'
tema: 'SOCIEDAD'
fecha: 2026-11-04
imagenPortada: '/nebula/imagenes/colegios_oscuridad_horario_verano_portada.png'
cifraDestacada: '6,2 millones de menores'
etiquetaCifra: 'afectados al menos una mañana'
textoContinuo: "Cambiar al horario de verano podría afectar a 6,2 millones de menores"
metodologia: 'EDA de 6.248.054 residentes de 5 a 17 años registrados por el INE en 2025 en 8.131 municipios con coordenadas del IGN. Usansolo, con 623, queda fuera por no aparecer todavía en esa capa. Calculo el amanecer local durante un calendario escolar común de 2026-2027 y comparo tres relojes para salidas a las 8:00, 8:30 y 9:00. La cifra es un escenario, no un recuento de trayectos observados.'
---

**A las ocho y media de una mañana de enero, una mochila puede salir de casa antes que el sol.** Ahora ocurre sobre todo en el oeste de España. Si mantuviésemos el horario de verano durante todo el año, dejaría de ser una rareza geográfica y llegaría a todo el país.

La pregunta nació en Estados Unidos. Un estudio publicado en *Current Biology* calculó que mantener allí el horario de verano añadiría más de 2.000 millones de trayectos escolares antes del amanecer cada año. Pero ese resultado no se puede trasladar directamente a España. Como ya ocurrió cuando [el reloj parecía contradecir el viaje de Voyager 1](/nebula/articulos/voyager-un-dia-luz/), hablar de tiempo sin fijarse en el lugar desde el que se mide puede engañar. Por eso he repetido el cálculo con datos españoles: 8.131 municipios y **6.248.054 residentes de 5 a 17 años**. Usansolo queda fuera porque todavía no aparece en la capa geográfica utilizada.

<figure class="video-horario-verano">
  <div class="video-horario-verano__marco">
    <iframe
      src="https://www.youtube-nocookie.com/embed/k1gcEDoC9wc"
      title="Vídeo sobre el horario de verano"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
  </div>

  <figcaption>
    Cómo influye el cambio de hora en nuestras mañanas y tardes.
  </figcaption>
</figure>

<style>
  .video-horario-verano {
    margin: 2rem 0;
  }

  .video-horario-verano__marco {
    position: relative;
    overflow: hidden;
    width: 100%;
    padding-top: 56.25%;
    border-radius: 14px;
    background: #eef2fc;
  }

  .video-horario-verano__marco iframe {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }

  .video-horario-verano figcaption {
    margin-top: 0.65rem;
    color: #596477;
    font-size: 0.9em;
    line-height: 1.5;
  }
</style>

No significa que todos entren a la misma hora ni que recorran el mismo camino. Esa información no existe reunida para cada estudiante. Por eso el análisis no esconde el supuesto: permite mover la hora de salida y ver cuánto cambia la historia.

## La hora que le robamos a la mañana

El cambio de octubre no crea ni destruye luz. Mueve las manillas del reloj. Cuando atrasamos una hora, el amanecer que habría aparecido a las 9:00 vuelve a marcar las 8:00. Mantener el horario de verano durante el invierno haría justo lo contrario.

**Prueba con las tres salidas de casa**. Las cifras representan mañanas escolares oscuras por menor durante el curso.

<section class="reloj-escolar" id="reloj-escolar" aria-labelledby="reloj-titulo">
  <h3 id="reloj-titulo">¿A qué hora sale de casa?</h3>
  <div class="reloj-botones" role="group" aria-label="Hora de salida">
    <button type="button" data-hora="08:00" aria-pressed="false">8:00</button>
    <button type="button" data-hora="08:30" aria-pressed="true">8:30</button>
    <button type="button" data-hora="09:00" aria-pressed="false">9:00</button>
  </div>
  <div class="reloj-comparacion" aria-live="polite">
    <div><span>Sistema actual</span><strong id="reloj-actual">15,4</strong><i id="barra-actual"></i></div>
    <div><span>Verano permanente</span><strong id="reloj-verano">83,0</strong><i id="barra-verano"></i></div>
  </div>
  <p id="reloj-lectura">Serían 67,5 mañanas oscuras adicionales por menor.</p>
  <small>Escenario calculado con población de 5 a 17 años. “Oscura” significa que la salida elegida ocurre antes del amanecer oficial.</small>
</section>

Salir a las 8:00 eleva los dos resultados: 69 mañanas con el reloj actual y 113,5 con el verano permanente. Salir a las 9:00 casi elimina la oscuridad actual, pero todavía deja 48,4 mañanas bajo el verano permanente. **La hora elegida importa mucho, pero ninguna de las tres borra el efecto.**

En el caso central, el salto nacional equivale a unos **422 millones de menor-días adicionales**. La expresión parece extraña, pero es sencilla: diez menores expuestos durante dos mañanas suman veinte menor-días. Sirve para reunir la repetición del fenómeno sin fingir que conozco cada trayecto.

## Galicia ya vive parte de ese futuro

España comparte reloj, pero no amanecer. La Tierra gira de este a oeste y el sol llega antes al Mediterráneo que al Atlántico. La latitud también alarga las mañanas de invierno en el norte.

Con una salida a las 8:30, **Galicia** ya registra unas **65,9 mañanas oscuras por menor** en el sistema actual. El verano permanente las elevaría a 109,4. Asturias pasaría de 49,4 a 99,2 y Castilla y León, de 37,1 a 94,9.

En el este, la situación parte de otro lugar. Cataluña, la Comunitat Valenciana, Murcia y Baleares no registran mañanas anteriores al amanecer a las 8:30 en el calendario común utilizado. Con el horario de verano permanente pasarían, respectivamente, a 67,6, 74,7, 76 y 60,6.

<figure class="grafico-territorial"><figcaption><strong>El oeste ya parte con desventaja, pero el cambio alcanzaría también al este</strong><br>Media de mañanas anteriores al amanecer por menor, con salida a las 8:30.</figcaption><div class="territorial-leyenda"><span><i></i>Sistema actual</span><span><i></i>Verano permanente</span></div><div class="territorial-lista" role="img" aria-label="Comparación de mañanas oscuras por menor en siete comunidades con el sistema actual y con horario de verano permanente"><div class="territorial-fila"><span>Galicia</span><div class="territorial-pista"><i style="left:54.9%"></i><b style="left:91.2%"></b></div><strong>65,9 → 109,4</strong></div><div class="territorial-fila"><span>Asturias</span><div class="territorial-pista"><i style="left:41.2%"></i><b style="left:82.7%"></b></div><strong>49,4 → 99,2</strong></div><div class="territorial-fila"><span>Castilla y León</span><div class="territorial-pista"><i style="left:30.9%"></i><b style="left:79.1%"></b></div><strong>37,1 → 94,9</strong></div><div class="territorial-fila"><span>Cataluña</span><div class="territorial-pista"><i style="left:0%"></i><b style="left:56.3%"></b></div><strong>0 → 67,6</strong></div><div class="territorial-fila"><span>C. Valenciana</span><div class="territorial-pista"><i style="left:0%"></i><b style="left:62.3%"></b></div><strong>0 → 74,7</strong></div><div class="territorial-fila"><span>Murcia</span><div class="territorial-pista"><i style="left:0%"></i><b style="left:63.3%"></b></div><strong>0 → 76,0</strong></div><div class="territorial-fila"><span>Baleares</span><div class="territorial-pista"><i style="left:0%"></i><b style="left:50.5%"></b></div><strong>0 → 60,6</strong></div></div><p class="grafico-nota">La posición muestra una escala común de 0 a 120 mañanas. El salto es importante incluso donde ahora no hay ninguna.</p></figure>

<style>.grafico-territorial{margin:2.2rem 0}.grafico-territorial figcaption{margin-bottom:1rem;line-height:1.5}.territorial-leyenda{display:flex;gap:1.2rem;flex-wrap:wrap;margin-bottom:1.2rem;font-size:.82em;color:#596477}.territorial-leyenda span{display:flex;align-items:center;gap:.35rem}.territorial-leyenda i{display:inline-block;width:.7rem;height:.7rem;border-radius:50%;background:#9aa4b2}.territorial-leyenda span:last-child i{background:#446ddf}.territorial-lista{display:grid;gap:1rem}.territorial-fila{display:grid;grid-template-columns:minmax(115px,155px) 1fr minmax(92px,auto);gap:.8rem;align-items:center}.territorial-fila>span{font-size:.88em}.territorial-fila strong{font-size:.82em;color:#596477;white-space:nowrap}.territorial-pista{position:relative;height:3px;background:#d8ddea}.territorial-pista:before{content:"";position:absolute;left:0;right:0;top:1px;border-top:1px solid #d8ddea}.territorial-pista i,.territorial-pista b{position:absolute;top:50%;width:12px;height:12px;border-radius:50%;transform:translate(-50%,-50%);z-index:1}.territorial-pista i{background:#9aa4b2}.territorial-pista b{background:#446ddf}.grafico-nota{margin-top:1.2rem;font-size:.78em;line-height:1.45;color:#596477}@media(max-width:600px){.territorial-fila{grid-template-columns:1fr auto;gap:.35rem .8rem}.territorial-pista{grid-column:1/-1;grid-row:2}}</style>

La paradoja es que **el mayor aumento no siempre aparece donde amanece más tarde**. Galicia ya soporta parte de la oscuridad con el reloj actual. Murcia o Valencia saltarían desde cero porque perderían de golpe la protección del cambio de otoño.

## Un escenario, no seis millones de rutas

El cálculo utiliza la población municipal de 5 a 17 años, no una lista de matrículas. Tampoco sabe a qué hora comienza cada colegio, cuánto dura el trayecto ni si se hace andando, en coche o en autobús. Usé un calendario escolar común y excluí fines de semana, Navidad, Semana Santa y festivos nacionales; los días autonómicos y locales pueden recortar algunas mañanas.

Además, **oscuridad no significa accidente**. El estudio estadounidense que inspiró esta pregunta encontró más presencia de peatones menores en siniestros mortales antes del amanecer, pero ese riesgo no se puede trasladar automáticamente a España. Es la misma precaución que exigía [el supuesto 30 % de mejora del algoritmo penitenciario de Michigan](/nebula/articulos/algoritmos-prision-michigan/): una cifra llamativa pierde su significado cuando cambian la población, la definición o los datos disponibles. Aquí haría falta analizar por separado los registros de la DGT y las formas de desplazamiento españolas.

<figure class="grafico-afectados"><figcaption><strong>El verano permanente extendería la oscuridad a todo el país</strong><br>Residentes de 5 a 17 años con al menos una mañana anterior al amanecer, si salen de casa a las 8:30.</figcaption><div class="afectados-barras" role="img" aria-label="Con el horario de invierno permanente habría 3,45 millones de menores afectados; con el sistema actual, 3,48 millones; y con el horario de verano permanente, 6,25 millones"><div class="afectados-fila"><span>Invierno permanente</span><div class="afectados-pista"><i style="width:55.3%"></i></div><strong>3,45 millones</strong></div><div class="afectados-fila"><span>Sistema actual</span><div class="afectados-pista"><i style="width:55.7%"></i></div><strong>3,48 millones</strong></div><div class="afectados-fila destacada"><span>Verano permanente</span><div class="afectados-pista"><i style="width:100%"></i></div><strong>6,25 millones</strong></div></div><p class="grafico-nota">“Afectado” significa que la salida de las 8:30 ocurre antes del amanecer al menos una mañana del calendario analizado. No representa un trayecto observado.</p></figure>

<style>.grafico-afectados{margin:2.2rem 0}.grafico-afectados figcaption{margin-bottom:1.3rem;line-height:1.5}.afectados-barras{display:grid;gap:1.2rem}.afectados-fila{display:grid;grid-template-columns:minmax(145px,190px) 1fr minmax(95px,auto);gap:.8rem;align-items:center}.afectados-fila>span{font-size:.88em}.afectados-fila strong{color:#596477;font-size:.9em;white-space:nowrap}.afectados-pista{overflow:hidden;height:16px;border-radius:10px;background:#e8ebf2}.afectados-pista i{display:block;height:100%;border-radius:inherit;background:#9aa4b2}.afectados-fila.destacada .afectados-pista i{background:#446ddf}.afectados-fila.destacada strong{color:#3157bd}@media(max-width:600px){.afectados-fila{grid-template-columns:1fr auto;gap:.4rem .8rem}.afectados-pista{grid-column:1/-1;grid-row:2}}</style>

Lo que sí permiten responder los datos es la pregunta del reloj. El horario de invierno permanente reduce la media central a 12,3 mañanas, algo menos que el sistema actual. El de verano la dispara a 83 y extiende al conjunto del país una situación que hoy conocen mejor las familias del oeste.

La tarde ganaría una hora de luz en el reloj. **La mañana escolar la pagaría exactamente con la misma moneda.**

## Fuentes y análisis

- [INE: Censo anual de población, tabla municipal 68542](https://www.ine.es/dynt3/inebase/index.htm?capsel=11531&padre=11555).
- [IGN: Nomenclátor y coordenadas municipales](https://centrodedescargas.cnig.es/CentroDescargas/nomenclator-geografico-municipios-entidades-poblacion).
- [Estudio original sobre trayectos escolares oscuros en Estados Unidos](https://pubmed.ncbi.nlm.nih.gov/42956752/).
- [Notebook ejecutado](/nebula/analisis/colegios-oscuridad-horario-verano/analisis_horario_escolar_oscuridad.ipynb), [población municipal procesada](/nebula/analisis/colegios-oscuridad-horario-verano/municipios_poblacion_5_17.csv), [resultados por municipio](/nebula/analisis/colegios-oscuridad-horario-verano/resultados_municipios.csv) y [guía de reproducción](/nebula/analisis/colegios-oscuridad-horario-verano/README.md).

<style>
.reloj-escolar{margin:2rem 0;padding:clamp(1rem,4vw,1.6rem);border:1px solid #c7d3f4;border-radius:16px;background:#f5f7fd;color:#24304a}.reloj-escolar h3{margin-top:0}.reloj-botones{display:flex;gap:.6rem;flex-wrap:wrap}.reloj-botones button{font:inherit;padding:.65rem 1rem;border:1px solid #446ddf;border-radius:999px;background:#fff;color:#274ba9;cursor:pointer}.reloj-botones button[aria-pressed="true"]{background:#446ddf;color:#fff}.reloj-botones button:focus-visible{outline:3px solid #c58a2b;outline-offset:3px}.reloj-comparacion{display:grid;gap:1rem;margin:1.4rem 0}.reloj-comparacion div{display:grid;grid-template-columns:minmax(140px,1fr) auto;gap:.3rem 1rem;align-items:end}.reloj-comparacion strong{font-size:1.5rem;color:#446ddf}.reloj-comparacion i{grid-column:1/-1;display:block;height:12px;border-radius:8px;background:#446ddf;transition:width .35s ease}.reloj-comparacion div:first-child i{background:#9aa4b2}.reloj-escolar small{display:block;line-height:1.45;color:#596477}@media (prefers-reduced-motion:reduce){.reloj-comparacion i{transition:none}}
</style>

<script>
document.addEventListener('DOMContentLoaded',()=>{
 const datos={'08:00':{actual:69.0,verano:113.5},'08:30':{actual:15.4,verano:83.0},'09:00':{actual:0.45,verano:48.4}};
 const bloque=document.getElementById('reloj-escolar');
 if(!bloque)return;
 const formato=n=>n.toLocaleString('es-ES',{minimumFractionDigits:n<1?2:1,maximumFractionDigits:n<1?2:1});
 const actualizar=hora=>{const d=datos[hora];bloque.querySelectorAll('[data-hora]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.hora===hora)));document.getElementById('reloj-actual').textContent=formato(d.actual);document.getElementById('reloj-verano').textContent=formato(d.verano);document.getElementById('barra-actual').style.width=`${d.actual/1.2}%`;document.getElementById('barra-verano').style.width=`${d.verano/1.2}%`;document.getElementById('reloj-lectura').textContent=`Serían ${formato(d.verano-d.actual)} mañanas oscuras adicionales por menor.`;};
 bloque.querySelectorAll('[data-hora]').forEach(b=>b.addEventListener('click',()=>actualizar(b.dataset.hora)));
 actualizar('08:30');
});
</script>
