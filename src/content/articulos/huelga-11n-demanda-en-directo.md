---
titulo: "¿Se ha parado España? La curva eléctrica mide en directo el impacto de la huelga del 11N"
descripcion: "La demanda de electricidad se actualiza cada cinco minutos y permite observar cuánto se separa la actividad real de una jornada normal."
tema: "TECNOLOGÍA"
fecha: 2026-11-11
imagenPortada: "/nebula/imagenes/huelga_11n_demanda_portada.png"
cifraDestacada: "5 MIN"
etiquetaCifra: "entre cada actualización de la demanda eléctrica"
textoContinuo: "La curva eléctrica mide en directo el impacto de la huelga general del 11N"
metodologia: "EDA en directo de la demanda eléctrica nacional publicada por Red Eléctrica cada cinco minutos. Comparo demanda real y prevista para el mismo instante y calculo su diferencia porcentual y la energía acumulada por debajo de la previsión. Los resultados son provisionales durante la jornada. La diferencia mide actividad eléctrica, no seguimiento individual de la huelga. La meteorología, el teletrabajo, el autoconsumo y el error de previsión limitan la interpretación."
---

*España vive este 11 de noviembre su primera huelga general en catorce años. Cerca de 19 millones de asalariados están llamados a parar. Pero entre las cifras de sindicatos, empresas y administraciones hay un dato que no necesita preguntar a nadie: cuánta electricidad está consumiendo el país en cada momento.*

La convocatoria no responde a una sola decisión. [CCOO y UGT la resumen en tres palabras: salarios, vivienda y precios](https://www.ugt.es/11n-huelga-general-salarios-vivienda-precios). Los sindicatos reclaman desbloquear la negociación colectiva, mejorar los sueldos y los servicios públicos y frenar el peso que la vivienda y el coste de la vida tienen sobre los hogares. **La crisis de acceso a la vivienda aparece como el principal detonante**.

También intervienen otras organizaciones, entre ellas CGT, CNT y sindicatos de inquilinas. El [BOE confirma dos convocatorias estatales](https://boe.es/diario_boe/txt.php?id=BOE-A-2026-23371&lang=es) para toda la jornada, desde las 00:00 hasta las 23:59. Eso describe quién convoca y por qué. Otra pregunta distinta es cuánto se ha detenido realmente la actividad.

## Haz tu apuesta antes de mirar la curva

<section class="h11-apuesta" aria-labelledby="h11-apuesta-titulo">
  <h3 id="h11-apuesta-titulo">¿Cuál será la mayor caída del día?</h3>
  <p>Elige cuánto crees que se separará la demanda real de la prevista. Después verás el dato actualizado.</p>
  <div class="h11-apuesta__opciones">
    <button type="button" data-apuesta="5">Menos del 5 %</button>
    <button type="button" data-apuesta="10">Entre el 5 % y el 10 %</button>
    <button type="button" data-apuesta="15">Entre el 10 % y el 15 %</button>
    <button type="button" data-apuesta="99">Más del 15 %</button>
    <button type="button" data-apuesta="ver">Ver sin apostar</button>
  </div>
  <p class="h11-apuesta__respuesta" aria-live="polite">El gráfico permanece oculto hasta que elijas.</p>
</section>

<section class="h11-directo" id="h11-directo" aria-labelledby="h11-directo-titulo" hidden>
  <div class="h11-directo__cabecera">
    <div><span class="h11-pulso" aria-hidden="true"></span><strong id="h11-estado">Cargando datos</strong></div>
    <p id="h11-actualizacion">Consultando Red Eléctrica…</p>
  </div>
  <div class="h11-metricas">
    <article><span>Ahora</span><strong id="h11-ahora">—</strong><small>frente a la previsión</small></article>
    <article><span>Mayor caída</span><strong id="h11-maximo">—</strong><small id="h11-maximo-hora">durante la jornada</small></article>
    <article><span>Diferencia actual</span><strong id="h11-mw">—</strong><small>megavatios</small></article>
  </div>
  <figure class="h11-grafico">
    <svg id="h11-svg" viewBox="0 0 720 390" role="img" aria-labelledby="h11-grafico-titulo h11-grafico-desc">
      <title id="h11-grafico-titulo">Demanda eléctrica real y prevista durante el 11N</title>
      <desc id="h11-grafico-desc">La línea gris muestra la previsión completa del día y la azul la demanda real publicada hasta el último dato disponible.</desc>
      <text x="22" y="30" class="h11-titulo">La curva eléctrica del 11N</text>
      <text x="22" y="52" class="h11-subtitulo">Demanda nacional en megavatios. La línea real termina en el último dato disponible.</text>
      <g id="h11-rejilla"></g>
      <path id="h11-prevista" class="h11-linea h11-linea--prevista"></path>
      <path id="h11-real" class="h11-linea h11-linea--real"></path>
      <g id="h11-ejes"></g>
    </svg>
    <figcaption><span><i class="h11-leyenda h11-leyenda--real"></i>Real</span><span><i class="h11-leyenda h11-leyenda--prevista"></i>Prevista</span>. Fuente: Red Eléctrica. Datos provisionales.</figcaption>
  </figure>
  <p id="h11-lectura" class="h11-lectura" aria-live="polite"></p>
  <p id="h11-error" class="h11-error" hidden></p>
</section>

**La [curva de Red Eléctrica](https://www.ree.es/es/operacion/sistema-electrico/demanda-y-produccion-en-tiempo-real) se actualiza cada cinco minutos**. La línea gris representa lo que el operador esperaba para una jornada normal. La azul enseña lo que está ocurriendo. La distancia entre ambas es la pista que seguimos durante todo el día.

## La luz no cuenta huelguistas

Una caída del 10 % no significa que el 10 % de los trabajadores haya parado. Una fábrica consume muchísimo más que una oficina pequeña. Un comercio abierto puede necesitar menos energía que una vivienda con calefacción. Además, el teletrabajo no elimina el consumo: lo traslada desde el centro de trabajo hasta casa.

La comparación tampoco puede hacerse simplemente con ayer. La borrasca Charles está alterando temperaturas, desplazamientos y horarios. Por eso utilizo la previsión de Red Eléctrica, que ya tiene en cuenta el calendario, la actividad esperada y la meteorología. Aun así, una previsión puede equivocarse.

Tampoco estamos midiendo una falta de electricidad. El Gobierno ha fijado servicios mínimos para que sigan funcionando la generación, el transporte y la distribución. Si la curva baja, no es porque las centrales hayan decidido dejar al país sin suministro, sino porque hogares, comercios, oficinas e industrias están pidiendo menos energía de la esperada. La red se limita a seguir esa demanda y mantener el equilibrio.

Hay otra pieza que antes pesaba mucho menos. Parte de la electricidad producida por placas solares se consume dentro de viviendas y empresas sin pasar por la red. Red Eléctrica advierte de que su demanda no incluye todo ese autoconsumo. El termómetro sigue siendo útil, pero ya no mide exactamente el mismo país que en 2012.

## El espejo de las huelgas anteriores

Durante la huelga del 29 de marzo de 2012, la demanda diaria quedó aproximadamente un **14,8 % por debajo de la prevista**. En la del 14 de noviembre, la diferencia rondaba el **12 % a primera hora de la tarde**. En septiembre de 2010 terminó alrededor de un 14 % por debajo.

Son referencias, no una clasificación perfecta. Unas cifras corresponden al promedio completo y otras a horas concretas. También han cambiado la economía, la eficiencia energética, el autoconsumo y la posibilidad de trabajar desde casa. Compararlas sirve para dar escala al 11N, no para proclamar qué huelga tuvo más seguimiento.

El gráfico seguirá cambiando hasta el final de la jornada. Cuando llegue el último dato, quedará congelado como una fotografía eléctrica del 11N. Entonces podremos responder con precisión cuánto se separó España de la actividad prevista. Lo que la curva nunca podrá decir, por sí sola, es cuántas personas decidieron no trabajar ni cuáles fueron sus motivos.

## Fuentes y análisis

- [REData API de Red Eléctrica](https://www.ree.es/es/datos/apidatos) y [explicación de sus curvas en tiempo real](https://www.ree.es/es/operacion/sistema-electrico/demanda-y-produccion-en-tiempo-real).
- [Convocatoria y reivindicaciones de CCOO](https://huelga.ccoo.es/) y [UGT](https://www.ugt.es/11n-huelga-general-salarios-vivienda-precios).
- [Servicios mínimos del sector eléctrico publicados en el BOE](https://boe.es/diario_boe/txt.php?id=BOE-A-2026-23371&lang=es).
- [Notebook ejecutado](/nebula/analisis/huelga-11n-demanda/huelga_11n_demanda.ipynb), [datos de respaldo](/nebula/analisis/huelga-11n-demanda/datos/demanda_11n_respaldo.json) y [serie procesada](/nebula/analisis/huelga-11n-demanda/resultados/demanda_11n_procesada.csv).

<style>
.h11-apuesta,.h11-directo{margin:2.2rem 0;padding:1.35rem;border:1px solid #446ddf;border-radius:14px;background:rgba(68,109,223,.045)}.h11-apuesta h3{margin-top:0}.h11-apuesta__opciones{display:flex;flex-wrap:wrap;gap:.6rem}.h11-apuesta button{font:inherit;padding:.65rem .9rem;border:1px solid #446ddf;border-radius:999px;background:#fff;color:#294da9;cursor:pointer}.h11-apuesta button:hover,.h11-apuesta button:focus-visible,.h11-apuesta button[aria-pressed="true"]{background:#446ddf;color:#fff}.h11-apuesta__respuesta{min-height:1.5em;margin-bottom:0;font-weight:600}.h11-directo__cabecera{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding-bottom:1rem;border-bottom:1px solid #446ddf33}.h11-directo__cabecera p{margin:0;color:#586174;font-size:.86rem}.h11-pulso{display:inline-block;width:.65rem;height:.65rem;margin-right:.5rem;border-radius:50%;background:#d84a3a;box-shadow:0 0 0 0 rgba(216,74,58,.5);animation:h11-pulso 1.8s infinite}.h11-metricas{display:grid;grid-template-columns:repeat(3,1fr);gap:.8rem;margin:1.1rem 0}.h11-metricas article{padding:1rem;border-radius:10px;background:#fff}.h11-metricas span,.h11-metricas small{display:block;color:#626b7c}.h11-metricas strong{display:block;margin:.2rem 0;font-size:1.65rem;color:#1b1836;font-variant-numeric:tabular-nums}.h11-grafico{margin:1.4rem 0 0}.h11-grafico svg{display:block;width:100%;height:auto;overflow:visible;font-family:var(--font-body)}.h11-titulo{font:600 20px var(--font-heading);fill:currentColor}.h11-subtitulo,.h11-eje{font-size:12px;fill:#697386}.h11-rejilla{stroke:#dfe4f0;stroke-width:1}.h11-linea{fill:none;stroke-linecap:round;stroke-linejoin:round}.h11-linea--prevista{stroke:#aeb5c2;stroke-width:3}.h11-linea--real{stroke:#446ddf;stroke-width:4}.h11-grafico figcaption{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:.5rem;color:#586174;font-size:.84rem}.h11-leyenda{display:inline-block;width:1.4rem;height:3px;margin-right:.3rem;vertical-align:middle}.h11-leyenda--real{background:#446ddf}.h11-leyenda--prevista{background:#aeb5c2}.h11-lectura{padding:1rem;border-left:4px solid #446ddf;background:#fff;font-weight:600}.h11-error{color:#8a342b}.h11-directo[hidden]{display:none}@keyframes h11-pulso{70%{box-shadow:0 0 0 9px rgba(216,74,58,0)}100%{box-shadow:0 0 0 0 rgba(216,74,58,0)}}@media(max-width:620px){.h11-apuesta__opciones{display:grid}.h11-apuesta button{width:100%}.h11-directo__cabecera{display:block}.h11-directo__cabecera p{margin-top:.35rem}.h11-metricas{grid-template-columns:1fr}.h11-metricas article{display:grid;grid-template-columns:1fr auto;align-items:end}.h11-metricas small{grid-column:1/-1}.h11-metricas strong{font-size:1.4rem}}
</style>

<script>
(() => {
  const API='https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date=2026-11-11T00:00&end_date=2026-11-11T23:59&time_trunc=hour';
  const RESPALDO='/nebula/analisis/huelga-11n-demanda/datos/demanda_11n_respaldo.json';
  const directo=document.getElementById('h11-directo');
  const apuesta=document.querySelector('.h11-apuesta');
  if(!directo||!apuesta)return;
  let mayorActual=null;
  const numero=(n,d=1)=>new Intl.NumberFormat('es-ES',{minimumFractionDigits:d,maximumFractionDigits:d}).format(n);
  const hora=s=>new Intl.DateTimeFormat('es-ES',{hour:'2-digit',minute:'2-digit'}).format(new Date(s));
  const revelar=boton=>{
    apuesta.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b===boton)));
    directo.hidden=false;
    const salida=apuesta.querySelector('.h11-apuesta__respuesta');
    if(boton.dataset.apuesta==='ver')salida.textContent='Aquí tienes la curva actualizada.';
    else if(mayorActual===null)salida.textContent='Apuesta guardada. Cargando la curva actualizada…';
    else {
      const v=Math.abs(mayorActual),lim=Number(boton.dataset.apuesta),acierta=(lim===5&&v<5)||(lim===10&&v>=5&&v<10)||(lim===15&&v>=10&&v<15)||(lim===99&&v>=15);
      salida.textContent=(acierta?'Por ahora has acertado. ':'Por ahora la curva dice otra cosa. ')+`La mayor caída observada es del ${numero(v)} %.`;
    }
    directo.scrollIntoView({behavior:'smooth',block:'start'});
  };
  apuesta.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>revelar(b)));
  const extraer=datos=>Object.fromEntries(datos.included.filter(s=>['Real','Prevista'].includes(s.type)).map(s=>[s.type,s.attributes.values.map(v=>({t:new Date(v.datetime),v:Number(v.value),iso:v.datetime}))]));
  const camino=(serie,x,y)=>serie.map((p,i)=>`${i?'L':'M'}${x(p.t).toFixed(1)},${y(p.v).toFixed(1)}`).join(' ');
  const dibujar=series=>{
    const previstas=new Map(series.Prevista.map(p=>[p.iso,p.v]));
    const filas=series.Real.filter(p=>previstas.has(p.iso)).map(p=>({...p,prev:previstas.get(p.iso),dif:p.v-previstas.get(p.iso),pct:(p.v-previstas.get(p.iso))/previstas.get(p.iso)*100}));
    if(!filas.length)throw new Error('Sin observaciones reales comparables');
    const ultima=filas.at(-1),peor=filas.reduce((a,b)=>b.pct<a.pct?b:a);mayorActual=peor.pct;
    document.getElementById('h11-ahora').textContent=`${ultima.pct>0?'+':''}${numero(ultima.pct)} %`;
    document.getElementById('h11-maximo').textContent=`${numero(Math.abs(peor.pct))} %`;
    document.getElementById('h11-maximo-hora').textContent=`a las ${hora(peor.iso)}`;
    document.getElementById('h11-mw').textContent=`${ultima.dif>0?'+':''}${numero(ultima.dif,0)}`;
    document.getElementById('h11-actualizacion').textContent=`Actualizado a las ${hora(ultima.iso)} · se renueva cada 5 minutos`;
    const final=ultima.t.getHours()===23&&ultima.t.getMinutes()>=50;
    document.getElementById('h11-estado').textContent=final?'Jornada completa':'Datos en directo';
    document.getElementById('h11-lectura').textContent=`A las ${hora(ultima.iso)}, la demanda real es de ${numero(ultima.v,0)} MW: ${numero(Math.abs(ultima.dif),0)} MW ${ultima.dif<0?'por debajo':'por encima'} de lo previsto. La mayor caída observada hasta ahora es del ${numero(Math.abs(peor.pct))} % a las ${hora(peor.iso)}.`;
    const todas=[...series.Prevista,...series.Real],min=Math.min(...todas.map(p=>p.v))*0.96,max=Math.max(...todas.map(p=>p.v))*1.04,x0=64,x1=700,y0=76,y1=330;
    const inicio=new Date('2026-11-11T00:00:00+01:00'),fin=new Date('2026-11-12T00:00:00+01:00');
    const x=t=>x0+(t-inicio)/(fin-inicio)*(x1-x0),y=v=>y1-(v-min)/(max-min)*(y1-y0);
    document.getElementById('h11-prevista').setAttribute('d',camino(series.Prevista,x,y));document.getElementById('h11-real').setAttribute('d',camino(series.Real,x,y));
    const rejilla=document.getElementById('h11-rejilla'),ejes=document.getElementById('h11-ejes');rejilla.textContent='';ejes.textContent='';
    [0,6,12,18,24].forEach(h=>{const xx=x0+h/24*(x1-x0);rejilla.insertAdjacentHTML('beforeend',`<line class="h11-rejilla" x1="${xx}" y1="${y0}" x2="${xx}" y2="${y1}"/>`);ejes.insertAdjacentHTML('beforeend',`<text class="h11-eje" x="${xx}" y="355" text-anchor="middle">${String(h).padStart(2,'0')}:00</text>`)});
    [min,(min+max)/2,max].forEach(v=>{const yy=y(v);rejilla.insertAdjacentHTML('beforeend',`<line class="h11-rejilla" x1="${x0}" y1="${yy}" x2="${x1}" y2="${yy}"/>`);ejes.insertAdjacentHTML('beforeend',`<text class="h11-eje" x="56" y="${yy+4}" text-anchor="end">${numero(v/1000,0)}k</text>`)});
  };
  const cargar=async()=>{let respaldo=false;try{let r=await fetch(API,{cache:'no-store'});if(!r.ok)throw new Error();dibujar(extraer(await r.json()))}catch{respaldo=true;try{let r=await fetch(RESPALDO,{cache:'no-store'});dibujar(extraer(await r.json()))}catch{document.getElementById('h11-error').hidden=false;document.getElementById('h11-error').textContent='No ha sido posible cargar la curva. Puedes consultarla directamente en Red Eléctrica.'}}if(respaldo&&document.getElementById('h11-error').hidden){document.getElementById('h11-error').hidden=false;document.getElementById('h11-error').textContent='La API no responde: mostramos la última copia guardada.'}};
  cargar();setInterval(cargar,300000);
})();
</script>
