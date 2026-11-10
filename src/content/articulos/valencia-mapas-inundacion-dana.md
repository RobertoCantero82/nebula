---
titulo: "Valencia tenía mapas de inundación: la mitad de las viviendas afectadas quedó fuera"
descripcion: "La cifra provincial oculta dos realidades opuestas: municipios casi enteros dentro del riesgo previsto y otros que apenas aparecían."
tema: "SOCIEDAD"
fecha: 2026-11-09
imagenPortada: "/nebula/imagenes/valencia_mapas_inundacion_portada.png"
cifraDestacada: "51,1 %"
etiquetaCifra: "de las viviendas fuera de toda zona oficial"
textoContinuo: "El 51,1 % de las viviendas afectadas por la DANA en Valencia estaba fuera de las zonas que los mapas oficiales señalaban como inundables"
metodologia: "EDA de los agregados municipales publicados por EasyxLab a partir de Copernicus EMS, Catastro, SNCZI, PATRICOVA e IGN. Analizo 84.789 viviendas dentro de la huella observada y la concentración territorial del desfase. La cifra cambia con la huella y la regla espacial: los escenarios centrales van del 38,9 % al 61,9 %."
---

**Un mapa puede avisar del peligro y dejar fuera el lugar donde termina entrando el agua.** La Comunitat Valenciana tenía desde hacía años cartografía de inundaciones cuando llegó la DANA del 29 de octubre de 2024. Sin embargo, el agua no siguió obedientemente las líneas dibujadas.

<figure class="video-nebula">
  <div class="video-nebula__marco">
    <iframe
      src="https://www.youtube-nocookie.com/embed/_DLb1YpQlFY"
      title="Qué es una DANA: depresión aislada en niveles altos"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
  </div>

  <figcaption>
    Qué es una DANA y cómo se forma este fenómeno meteorológico.
  </figcaption>
</figure>

<style>
.video-nebula {
  margin: 2.2rem 0;
  padding: clamp(1rem, 4vw, 1.6rem);
  border: 1px solid #c7d3f4;
  border-radius: 18px;
  background: #f5f7fd;
  box-shadow: 0 10px 28px rgba(40, 66, 125, 0.08);
}

.video-nebula__marco {
  position: relative;
  overflow: hidden;
  width: 100%;
  padding-top: 56.25%;
  border-radius: 12px;
  background: #dfe5f5;
}

.video-nebula__marco iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.video-nebula figcaption {
  margin-top: 0.8rem;
  color: #596477;
  font-size: 0.85em;
  line-height: 1.5;
}

@media (max-width: 520px) {
  .video-nebula {
    border-radius: 14px;
  }
}
</style>

Para comprobarlo necesitamos una fotografía de lo que ocurrió. La proporciona **Copernicus**, el servicio de emergencias de la Unión Europea. Cuando sucede una catástrofe, analiza imágenes de satélite y fotografías aéreas para ayudar a los equipos que trabajan sobre el terreno. En este caso dibujó la **huella de la inundación**: la superficie donde las imágenes mostraban agua o señales de que había pasado.

La pregunta es sencilla: ¿cuántas viviendas situadas dentro de esa huella aparecían también en alguna zona oficial de peligro? La respuesta central es incómoda. De **84.789 viviendas**, **43.359 quedaron fuera de todas las zonas consultadas**. Son el **51,1 %**.

El cálculo procede de un [estudio de EasyxLab](https://github.com/easybytehub/easyxlab/tree/main/studies/s19-dana-flood-mapped-vs-observed). Sus autores superpusieron tres piezas: la huella de Copernicus, los edificios del Catastro y los mapas que ya señalaban dónde podía haber inundaciones.

Ahí entran dos nombres poco amables. El **SNCZI** es el mapa estatal de zonas inundables. El **PATRICOVA** es el plan valenciano que añade su propia cartografía del riesgo. Estar fuera de ambos no significa que una vivienda fuera segura, ilegal o desconocida para la Administración. Solo significa que su edificio no entraba en las zonas de peligro utilizadas en la comparación.

Mi análisis parte de los resultados municipales publicados para responder otra pregunta: **¿ese agujero del mapa se repartió por igual?**

## La mitad no fue igual para todos

No. La cifra provincial mezcla municipios con historias opuestas. En Sedaví, las 1.878 viviendas contabilizadas dentro de la huella quedaron fuera de las zonas oficiales. En Picanya fueron el 95,8 % y en Alberic, el 93,7 %.

En Paiporta, el porcentaje bajó al 71,9 %, pero el tamaño del golpe lo cambia todo: hablamos de **8.619 viviendas**. Es la misma precaución que necesitaba [la supuesta concentración mundial de muertes en la alta velocidad española](/nebula/articulos/accidentes-alta-velocidad-espana-mitad/): un porcentaje puede cambiar de significado cuando miramos cuántos casos hay detrás.

En el extremo contrario, Massanassa y Beniparrell tenían prácticamente todas las viviendas de la huella dentro de una zona estatal de peligro. Albalat de la Ribera y Alcàntera de Xúquer tampoco registran viviendas fuera en los datos publicados.

**Elige un municipio y observa cuánto cambia el mapa.**

<section class="selector-municipio" id="selector-municipio" aria-labelledby="selector-titulo">
  <h3 id="selector-titulo">¿Qué parte quedó fuera de toda zona oficial?</h3>
  <div role="group" aria-label="Municipio">
    <button type="button" data-lugar="Sedaví" aria-pressed="true">Sedaví</button>
    <button type="button" data-lugar="Picanya" aria-pressed="false">Picanya</button>
    <button type="button" data-lugar="Paiporta" aria-pressed="false">Paiporta</button>
    <button type="button" data-lugar="Alfafar" aria-pressed="false">Alfafar</button>
    <button type="button" data-lugar="Aldaia" aria-pressed="false">Aldaia</button>
  </div>
  <strong id="selector-porcentaje">100 %</strong>
  <i><b id="selector-barra" style="width:100%"></b></i>
  <p id="selector-lectura">1.878 de 1.878 viviendas situadas dentro de la huella.</p>
  <small>Escenario central de EasyxLab. “Fuera” significa que la planta del edificio no toca ninguna de las zonas oficiales utilizadas.</small>
</section>

## Tres municipios concentran casi la mitad

Los porcentajes extremos llaman la atención, pero pueden describir lugares pequeños. Por eso también he ordenado los municipios por el número de viviendas fuera de zona. Paiporta encabeza la lista, seguida de València, con 6.795, y Picanya, con 4.674.

Solo esas tres reúnen **20.088 viviendas**, el **46,3 %** de todas las que quedaron fuera en la provincia. Si añadimos Alberic y Xirivella, las cinco primeras concentran el 67,2 %. El problema no fue uniforme: una parte enorme se acumuló en unos pocos puntos.

<figure class="concentracion-mapas">
  <figcaption><strong>Dos de cada tres viviendas fuera de zona se concentran en cinco municipios</strong><br>Parte de las 43.359 viviendas del escenario central.</figcaption>
  <div role="img" aria-label="Paiporta, València y Picanya concentran el 46,3 por ciento; Alberic y Xirivella elevan el grupo de cinco al 67,2 por ciento; el resto suma el 32,8 por ciento">
    <span style="width:46.3%"><b>46,3 %</b></span><i style="width:20.9%"><b>20,9 %</b></i><em style="width:32.8%"><b>32,8 %</b></em>
  </div>
  <p>Los tres primeros son Paiporta, València y Picanya. Alberic y Xirivella completan el grupo de cinco.</p>
</figure>

## Una línea no es una verdad exacta

El **51,1 %** no debe leerse como si alguien hubiera contado casas con una libreta. **Depende de dos decisiones**.

La primera es **dónde termina la inundación**. Copernicus reconstruyó su huella con imágenes tomadas en distintos días. La Generalitat hizo otra delimitación con fuentes y criterios diferentes. Ninguna línea puede capturar a la perfección un fenómeno que cambia con las horas.

La segunda es **qué hacemos con una casa atravesada por el borde**. Podemos contarla cuando cualquier parte del edificio toca la zona de peligro o exigir que su punto central quede dentro. Parece un detalle, pero miles de edificios están cerca de esas fronteras.

Al combinar dos huellas y tres reglas razonables, el resultado se mueve entre **el 38,9 % y el 61,9 %**. No es un margen de error estadístico. Es una [prueba de sensibilidad, como la utilizada para comparar los horarios escolares](/nebula/articulos/colegios-oscuridad-horario-verano/): repetimos la cuenta con decisiones distintas para comprobar cuánto depende de ellas la conclusión.

Hay una cautela todavía mayor. La capa estatal utilizada figura actualizada el 20 de diciembre de 2024, después de la catástrofe. La versión vigente el día de la DANA estaba fechada en 2022, pero no pudo recuperarse. Por eso este análisis no demuestra con precisión qué sabía cada mapa aquel 29 de octubre.

Sí demuestra que la frase «Valencia sabía dónde se inundaría» necesita muchos matices. La revisión anunciada en 2026 aumenta un 61,2 % la superficie peligrosa en la zona de la DANA, de 27.162 a 43.779 hectáreas. El riesgo no solo estaba en el territorio. También estaba en lo que las líneas todavía no alcanzaban a contar.

## Fuentes y análisis

- [Copernicus EMSR773: huella de la inundación](https://storymaps.arcgis.com/stories/9ff57e9320dd440eb2ce8d20e62c92cd).
- [EasyxLab: método, datos agregados y limitaciones](https://github.com/easybytehub/easyxlab/tree/main/studies/s19-dana-flood-mapped-vs-observed).
- [Revisión del PATRICOVA anunciada en 2026](https://www.europapress.es/comunitat-valenciana/noticia-nuevo-patricova-aumenta-61-superficie-inundable-zona-dana-fija-medidas-elevar-nuevas-viviendas-20261015122611.html).
- [Notebook ejecutado](/nebula/analisis/valencia-mapas-inundacion/analisis_mapas_inundacion_valencia.ipynb), [datos municipales](/nebula/analisis/valencia-mapas-inundacion/municipios.csv) y [guía de reproducción](/nebula/analisis/valencia-mapas-inundacion/README.md).

<style>
.selector-municipio{margin:2rem 0;padding:clamp(1rem,4vw,1.6rem);border:1px solid #c7d3f4;border-radius:16px;background:#f5f7fd;color:#24304a}.selector-municipio h3{margin-top:0}.selector-municipio>div{display:flex;gap:.55rem;flex-wrap:wrap}.selector-municipio button{font:inherit;padding:.58rem .85rem;border:1px solid #446ddf;border-radius:999px;background:#fff;color:#274ba9;cursor:pointer}.selector-municipio button[aria-pressed="true"]{background:#446ddf;color:#fff}.selector-municipio>strong{display:block;margin:1.3rem 0 .5rem;font-size:clamp(2.4rem,9vw,4rem);color:#3157bd}.selector-municipio>i{display:block;overflow:hidden;height:15px;border-radius:10px;background:#dfe5f5}.selector-municipio>i b{display:block;height:100%;border-radius:inherit;background:#446ddf;transition:width .35s ease}.selector-municipio p{margin:.8rem 0}.selector-municipio small{color:#596477;line-height:1.45}.concentracion-mapas{margin:2.2rem 0;padding:clamp(1.2rem,4vw,2rem);border:1px solid #c7d3f4;border-radius:18px;background:#f5f7fd;color:#24304a;box-shadow:0 10px 28px rgba(40,66,125,.08)}.concentracion-mapas figcaption{margin-bottom:1.25rem;line-height:1.5}.concentracion-mapas>div{display:flex;overflow:hidden;height:52px;border-radius:12px}.concentracion-mapas span,.concentracion-mapas i,.concentracion-mapas em{display:flex;align-items:center;justify-content:center;font-style:normal}.concentracion-mapas span{background:#446ddf;color:#fff}.concentracion-mapas i{background:#7f9be8;color:#fff}.concentracion-mapas em{background:#dfe5f5;color:#354052}.concentracion-mapas b{font-size:.78em}.concentracion-mapas p{margin-bottom:0;font-size:.78em;line-height:1.45;color:#596477}@media(prefers-reduced-motion:reduce){.selector-municipio>i b{transition:none}}@media(max-width:520px){.concentracion-mapas{border-radius:14px}.concentracion-mapas i b{display:none}}
</style>

<script>
document.addEventListener('DOMContentLoaded',()=>{
 const datos={"Sedaví":{p:100,n:'1.878 de 1.878 viviendas situadas dentro de la huella.'},"Picanya":{p:95.8,n:'4.674 de 4.880 viviendas situadas dentro de la huella.'},"Paiporta":{p:71.9,n:'8.619 de 11.987 viviendas situadas dentro de la huella.'},"Alfafar":{p:49.8,n:'1.414 de 2.837 viviendas situadas dentro de la huella.'},"Aldaia":{p:24.3,n:'841 de 3.454 viviendas situadas dentro de la huella.'}};
 const bloque=document.getElementById('selector-municipio');if(!bloque)return;
 const actualizar=lugar=>{const d=datos[lugar];bloque.querySelectorAll('[data-lugar]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.lugar===lugar)));document.getElementById('selector-porcentaje').textContent=d.p.toLocaleString('es-ES',{maximumFractionDigits:1})+' %';document.getElementById('selector-barra').style.width=d.p+'%';document.getElementById('selector-lectura').textContent=d.n;};
 bloque.querySelectorAll('[data-lugar]').forEach(b=>b.addEventListener('click',()=>actualizar(b.dataset.lugar)));actualizar('Sedaví');
});
</script>
