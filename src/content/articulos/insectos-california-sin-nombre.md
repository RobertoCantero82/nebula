---
titulo: "California tiene miles de insectos que la ciencia reconoce, pero no sabe cómo llamar"
descripcion: "El índice de anonimato creado por Nebula revela que el 93 % de los grupos genéticos no está identificado hasta la especie."
tema: "BIODIVERSIDAD"
fecha: 2026-11-13
cifraDestacada: "93 de cada 100"
etiquetaCifra: "grupos genéticos no tienen identificación de especie"
textoContinuo: "El ADN distingue 42.305 grupos de insectos en California, pero el 93,3 % no tiene identificación de especie."
metodologia: "EDA de 892.274 ejemplares con código BIN, procedentes de la tabla suplementaria publicada por la California Insect Barcoding Initiative. Reduzco los registros a 42.305 grupos genéticos únicos y defino el índice de anonimato como el porcentaje de BIN sin identificación válida en la columna de especie. Comparo órdenes, familias, ecorregiones y tramos de abundancia observada. Un BIN funciona como aproximación operativa a una especie, pero no demuestra por sí solo que sea una especie nueva."
imagenPortada: "/nebula/imagenes/insectos_california_anonimato_portada.png"
---

*En California hay miles de insectos que la ciencia puede distinguir sin saber cómo llamarlos. Tienen fotografía, lugar de captura y un código genético propio. Lo que falta, muchas veces, es el nombre de la especie.*

La [California Insect Barcoding Initiative](https://doi.org/10.1002/ecog.08572) reunió más de un millón de ejemplares. Los investigadores estudiaron un fragmento de ADN que funciona de manera parecida al código de barras de un producto: permite separar organismos con secuencias distintas, incluso cuando parecen casi iguales a simple vista.

El proyecto encontró **42.305 grupos genéticos**, conocidos como BIN. Cada uno sirve como aproximación práctica a una especie. Sin embargo, tener un código propio no implica que el catálogo sepa relacionarlo con un nombre como *Apis mellifera* o *Danaus plexippus*.

Para medir esa distancia he creado para Nebula el **índice de anonimato**. No aparece en el estudio original, sino que es una medida propia para responder una pregunta sencilla. De cada cien BIN, ¿cuántos no tienen una identificación de especie?

<section class="insectos-apuesta" data-insectos-apuesta>
  <p class="insectos-etiqueta">ANTES DE VER EL RESULTADO</p>
  <h2>¿Qué grupo crees que tiene más anonimato?</h2>
  <div class="insectos-opciones">
    <button type="button" data-respuesta="moscas">Moscas y mosquitos</button>
    <button type="button" data-respuesta="mariposas">Mariposas y polillas</button>
    <button type="button" data-respuesta="escarabajos">Escarabajos</button>
  </div>
  <p class="insectos-resultado" aria-live="polite">Elige una opción para revelar la comparación.</p>
</section>

## Un catálogo capaz de reconocer desconocidos

El resultado general es **93,3 sobre 100**. De los 42.305 grupos genéticos, solo **2.817** tienen una identificación de especie en la tabla. Los otros 39.488 se quedan en el género, la familia, el orden o una clasificación todavía más general.

La forma de contar importa. Si cada ejemplar pesara por separado, los insectos más frecuentes dominarían el resultado. El índice cuenta una sola vez cada BIN: una especie aproximada con miles de capturas vale lo mismo que otra encontrada en una única ocasión. Así aparece con mayor claridad la parte menos conocida del inventario.

**Esto no significa que California esconda 39.488 especies nuevas**. Un insecto puede estar descrito y conservar un nombre científico, pero no disponer aún de una referencia genética fiable que permita unir ambas piezas. Un BIN también puede agrupar o separar organismos de una forma que no coincida perfectamente con una especie biológica.

La cifra sí muestra la magnitud del trabajo pendiente. En tres de cada cuatro grupos, la identificación más precisa disponible es únicamente la familia. Sería como reconocer que un animal es un felino sin poder aclarar si se trata de un gato, un lince o un leopardo.

<div class="grafico-interactivo insectos-grafico" role="img" aria-label="De los 42.305 grupos genéticos, el 6,7 por ciento llega a especie, el 9,7 por ciento a género, el 75,6 por ciento a familia y el resto solo a orden o un nivel más general.">
  <h3>Solo el 6,7 % llega a tener nombre de especie</h3>
  <div class="insectos-barra-apilada">
    <span style="--ancho:6.7%;--tono:#446ddf">6,7 %</span>
    <span style="--ancho:9.7%;--tono:#7592e8">9,7 %</span>
    <span style="--ancho:75.6%;--tono:#a8b9ef">75,6 %</span>
    <span style="--ancho:8%;--tono:#d9e1fa">8 %</span>
  </div>
  <div class="insectos-leyenda"><span>Especie</span><span>Género</span><span>Familia</span><span>Orden o menos</span></div>
  <p>Porcentaje de los 42.305 BIN según el nivel más preciso alcanzado.</p>
</div>

## Moscas y avispas llenan el cajón sin etiquetar

Las moscas y los mosquitos forman el orden más diverso del conjunto: **16.181 BIN**. Su índice de anonimato alcanza el **94,6 %**. Las avispas, abejas y hormigas llegan aún más lejos, al **95,9 %**, entre 13.966 grupos.

Los escarabajos se sitúan en el 93 %. Mariposas y polillas bajan al 81,2 %. Siguen teniendo un vacío enorme, pero cuentan con una ventaja histórica: son más visibles, atraen más atención y han recibido un esfuerzo taxonómico mayor que muchas moscas diminutas o avispas parasitoides.

La familia más numerosa del gran cajón sin etiquetar es Cecidomyiidae, unas moscas minúsculas conocidas como mosquitos de las agallas. El conjunto contiene 4.816 BIN y **4.804 carecen de identificación de especie**: un 99,8 %.

## Encontrarlo una vez complica ponerle nombre

El anonimato también cambia con el número de ejemplares. Entre los 15.417 BIN observados una sola vez, el índice alcanza el **98,1 %**. En los grupos con más de veinte registros desciende al 80,7 %.

<div class="grafico-interactivo insectos-grafico insectos-rareza" role="img" aria-label="El índice de anonimato baja del 98,1 por ciento en los grupos con un ejemplar al 80,7 por ciento en los grupos con más de veinte.">
  <h3>Cuanto menos aparece un grupo, más probable es que siga sin nombre</h3>
  <div data-rareza></div>
  <p>Índice de anonimato según el número de ejemplares observados por BIN.</p>
</div>

La relación no demuestra que la rareza sea la causa. Un insecto puede aparecer una sola vez porque vive en un lugar poco muestreado, vuela en otra época o evita las trampas utilizadas. Pero el patrón señala un problema práctico: cuanto menos se encuentra un organismo, menos oportunidades existen de compararlo, estudiarlo y conectarlo con una especie conocida.

California ya posee una biblioteca genética capaz de separar decenas de miles de formas de vida. Ahora queda la parte lenta: revisar ejemplares, compararlos con colecciones históricas y describir especies cuando corresponda. El código de barras permite saber que dos insectos son distintos. **Ponerles nombre sigue necesitando tiempo y especialistas.**

Puedes consultar el [notebook completo](/nebula/analisis/insectos-california-anonimato/insectos_california_indice_anonimato_eda.ipynb), los [resultados procesados](/nebula/analisis/insectos-california-anonimato/catalogo_bins.csv) y la [tabla original en Dryad](https://doi.org/10.5061/dryad.qrfj6q5zs).

Fuentes: [artículo científico en Ecography](https://doi.org/10.1002/ecog.08572), [datos originales en Dryad](https://doi.org/10.5061/dryad.qrfj6q5zs), [código de los investigadores](https://github.com/Austin-Baker/CIBI-biodiversity) y [Natural History Museum of Los Angeles County](https://nhmlac.org/press/scientists-discover-there-are-way-more-bugs-california-you-thought).

<style>
.insectos-apuesta{border:1px solid #d9d7e2;margin:2.5rem 0;padding:clamp(1.2rem,4vw,2rem)}.insectos-etiqueta{color:#446ddf;font:600 10px var(--font-mono);letter-spacing:.08em}.insectos-apuesta h2,.insectos-grafico h3{font-size:clamp(1.5rem,3vw,2.2rem);margin:.5rem 0 1.5rem}.insectos-opciones{display:flex;flex-wrap:wrap;gap:.65rem}.insectos-opciones button{background:#fff;border:1px solid #1b1836;color:#1b1836;cursor:pointer;font:600 11px var(--font-mono);padding:.8rem 1rem}.insectos-opciones button:hover,.insectos-opciones button:focus-visible,.insectos-opciones button.activo{background:#1b1836;color:#fff}.insectos-resultado{border-top:1px solid #d9d7e2;margin:1.4rem 0 0;padding-top:1.2rem}.insectos-barra-apilada{display:flex;min-height:76px;overflow:hidden}.insectos-barra-apilada span{align-items:center;background:var(--tono);display:flex;flex:0 0 var(--ancho);font:600 10px var(--font-mono);justify-content:center;overflow:hidden}.insectos-leyenda{display:grid;font:10px var(--font-mono);grid-template-columns:6.7fr 9.7fr 75.6fr 8fr;margin-top:.6rem;text-align:center}.insectos-grafico>p{color:var(--color-secondary-text);font-size:.85rem;margin:1rem 0 0}.insectos-rareza [data-rareza]{display:grid;gap:.7rem}.insectos-fila{align-items:center;display:grid;gap:1rem;grid-template-columns:120px 1fr 48px}.insectos-fila span{font:10px var(--font-mono)}.insectos-pista{background:#dfe5f5;height:18px}.insectos-pista i{background:#446ddf;display:block;height:100%;width:var(--valor)}@media(max-width:600px){.insectos-leyenda{display:none}.insectos-fila{grid-template-columns:95px 1fr 40px}}
</style>

<script>
const textos={moscas:'Correcto. Moscas y mosquitos alcanzan un 94,6 % de anonimato. Las avispas los superan ligeramente, pero no estaban entre las opciones.',mariposas:'Mariposas y polillas tienen el índice más bajo de las tres opciones: 81,2 %.',escarabajos:'Los escarabajos alcanzan un 93 %, pero moscas y mosquitos llegan al 94,6 %.'};
document.querySelectorAll('[data-insectos-apuesta]').forEach((bloque)=>{bloque.querySelectorAll('button').forEach((boton)=>boton.addEventListener('click',()=>{bloque.querySelectorAll('button').forEach((b)=>b.classList.toggle('activo',b===boton));bloque.querySelector('.insectos-resultado').textContent=textos[boton.dataset.respuesta];}));});
const datosRareza=[['1 ejemplar',98.1],['2–5',95.1],['6–20',89.1],['Más de 20',80.7]];
document.querySelectorAll('[data-rareza]').forEach((raiz)=>{datosRareza.forEach(([etiqueta,valor])=>{const fila=document.createElement('div');fila.className='insectos-fila';fila.innerHTML=`<span>${etiqueta}</span><div class="insectos-pista"><i style="--valor:${valor}%"></i></div><strong>${valor.toLocaleString('es-ES')} %</strong>`;raiz.append(fila);});});
</script>
