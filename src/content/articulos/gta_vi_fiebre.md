---
titulo: "¿Cuánto durará la fiebre de GTA VI? He intentado predecirlo con 28 videojuegos"
descripcion: "La atención ya está cayendo. Un modelo experimental anticipa cuánto podría quedar en diciembre y deja una previsión que podremos comprobar."
tema: "TECNOLOGÍA"
fecha: 2026-11-23T15:00:00+01:00
imagenPortada: "/imagenes/gta_vi_fiebre_portada.png"
cifraDestacada: "12 %"
etiquetaCifra: "del estreno: previsión para la tercera semana"
textoContinuo: "¿Cuánto dura la curiosidad cuando por fin llega el juego que llevabas años esperando?"
metodologia: "Machine learning experimental con consultas diarias de Wikipedia en inglés, all-access y user, días UTC. Muestra de conveniencia: 30 lanzamientos, 28 utilizados; 14 para entrenamiento, 7 para validación y 7 para prueba por fecha. Regresión ridge con dos variables disponibles hasta el día +3; objetivos: medias de +14 a +20 y +28 a +34 respecto al día 0. Elijo la penalización solo en validación y comparo con mediana histórica y persistencia. Mejora del 16,25 % en error absoluto logarítmico frente a la mediana en la prueba. Bandas orientativas basadas en errores de validación, sin cobertura probabilística garantizada. Corte: 23 de noviembre de 2026; último dato GTA VI: 22 de noviembre. No predice ventas ni jugadores."
---

**Durante años, GTA VI ha sido un juego del que hablar incluso cuando todavía no se podía jugar.** Ahora que ha llegado, la pregunta cambia: ¿cuánto tiempo seguirá despertando la misma curiosidad? He usado los primeros días de su estreno y el comportamiento de otros videojuegos para intentar anticiparlo.

La respuesta de mi modelo es que las consultas de su página en Wikipedia en inglés podrían quedarse alrededor del **12 % del nivel del estreno durante la tercera semana**, y cerca del **7 % durante la quinta**. Es una previsión experimental, con un margen amplio. No significa que vaya a perder esa proporción de jugadores.

## Hablar de un juego y jugarlo son cosas distintas

Rockstar sitúa el lanzamiento el 19 de noviembre. Al día siguiente, Take-Two anunció 3.790 millones de dólares en ventas al público durante la primera jornada, según estimaciones de la empresa. Ese dinero describe una dimensión del fenómeno. Mi pregunta se refiere a otra: la curiosidad que lleva a consultar información sobre él.

Para observarla he elegido una medida pública y repetible: las consultas de Wikipedia. La página inglesa de GTA VI recibió **750.227 el día del estreno**. El 22 de noviembre registró 308.867. Entre el primero y el cuarto día, la caída fue del **58,8 %**.

Imagina una tienda cuya inauguración atrae una cola enorme. Que unos días después haya menos gente mirando el escaparate no demuestra que quienes compraron hayan dejado de usar el producto. Con un videojuego ocurre algo parecido: bajar las consultas puede reflejar que muchas personas ya encontraron la información que buscaban.

<figure class="gta-observado"><svg viewBox="0 0 560 310" role="img" aria-labelledby="gta-curva-t gta-curva-d"><title id="gta-curva-t">Las consultas de GTA VI en sus primeros cuatro días</title><desc id="gta-curva-d">Wikipedia en inglés: 750.227 consultas el 19 de noviembre, 540.793 el 20, 393.338 el 21 y 308.867 el 22. Caída del 58,8 por ciento entre el primero y el cuarto día.</desc><path d="M80 40V245H510" fill="none" stroke="#8a95a9"/><text x="8" y="55" font-size="14" fill="#243047">750.000</text><text x="54" y="245" font-size="14" fill="#243047">0</text><polyline points="80,55.00 220,108.04 360,145.38 500,166.78" fill="none" stroke="#446ddf" stroke-width="4"/><circle cx="80" cy="55.00" r="5" fill="#446ddf"/><text x="80" y="275" text-anchor="middle" font-size="14" fill="#243047">19 nov.</text><circle cx="220" cy="108.04" r="5" fill="#446ddf"/><text x="220" y="275" text-anchor="middle" font-size="14" fill="#243047">20 nov.</text><circle cx="360" cy="145.38" r="5" fill="#446ddf"/><text x="360" y="275" text-anchor="middle" font-size="14" fill="#243047">21 nov.</text><circle cx="500" cy="166.78" r="5" fill="#446ddf"/><text x="500" y="275" text-anchor="middle" font-size="14" fill="#243047">22 nov.</text></svg><figcaption>Consultas diarias de Wikipedia en inglés. Datos observados, días UTC. Fuente: Wikimedia Analytics API.</figcaption></figure>

## Lo difícil empieza después de la primera semana

He reunido treinta lanzamientos y utilizado veintiocho, desde Fallout 4 hasta Spider-Man 2. He descartado dos comparaciones problemáticas: Dark Souls III tuvo un estreno japonés anterior al mundial y el título consultado de Baldur’s Gate 3 presenta un problema de cobertura en sus primeros días.

Para comparar juegos de tamaños distintos, doy valor cien a las consultas del día del estreno. Después observo cuánto conservan. No comparo ventas ni doy por hecho que un juego pequeño pueda explicar por completo uno como GTA VI.

El modelo aprende de dos señales: cuánto ha caído la atención en los primeros cuatro días y cuánta había durante la semana anterior. Con ellas estima la media diaria de dos semanas completas, evitando que un sábado aislado decida el resultado.

La prueba consiste en hacer como si aquellos juegos acabasen de salir: el modelo solo recibe sus primeros días y tiene que anticipar semanas que le he ocultado. Después comparo sus respuestas con los datos reales. Así puedo comprobar si ha aprendido un patrón útil o si simplemente hace cuentas que suenan convincentes.

Pero antes de aplicarlo a GTA VI tenía que demostrar que aportaba algo. **En siete juegos reservados para la prueba, redujo un 16 % el error de una regla que aplica la retención mediana de estrenos anteriores.** La mejora existe en esta muestra; no convierte el método en una máquina de acertar.

<section class="gta-explorador" aria-labelledby="gta-ex-t">
<h3 id="gta-ex-t">¿Cuánto queda después del estreno?</h3>
<p>El día de estreno de cada juego vale 100. Compara la previsión experimental de GTA VI con lo que ocurrió de verdad en otro lanzamiento.</p>
<label for="gta-juego">Juego con el que comparar</label>
<select id="gta-juego"><option value="0">Red Dead Redemption 2</option><option value="1">Fallout 4</option><option value="2">Uncharted 4: A Thief's End</option><option value="3">No Man's Sky</option><option value="4">Final Fantasy XV</option><option value="5">Horizon Zero Dawn</option><option value="6">The Legend of Zelda: Breath of the Wild</option><option value="7">Super Mario Odyssey</option><option value="8">Assassin's Creed Origins</option><option value="9">God of War (2018 video game)</option><option value="10">Spider-Man (2018 video game)</option><option value="11">Resident Evil 2 (2019 video game)</option><option value="12">Sekiro: Shadows Die Twice</option><option value="13">Death Stranding</option><option value="14">Doom Eternal</option><option value="15">Animal Crossing: New Horizons</option><option value="16">The Last of Us Part II</option><option value="17">Ghost of Tsushima</option><option value="18">Cyberpunk 2077</option><option value="19">Resident Evil Village</option><option value="20">Ratchet & Clank: Rift Apart</option><option value="21">Horizon Forbidden West</option><option value="22">Elden Ring</option><option value="23">God of War Ragnarök</option><option value="24">Resident Evil 4 (2023 video game)</option><option value="25">The Legend of Zelda: Tears of the Kingdom</option><option value="26">Final Fantasy XVI</option><option value="27">Spider-Man 2 (2023 video game)</option></select>
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
(()=>{const juegos=[{"t":"Red Dead Redemption 2","y":[21.547945,15.786822]},{"t":"Fallout 4","y":[18.007714,8.83553]},{"t":"Uncharted 4: A Thief's End","y":[19.600637,9.600065]},{"t":"No Man's Sky","y":[16.912878,4.958782]},{"t":"Final Fantasy XV","y":[15.43883,13.504701]},{"t":"Horizon Zero Dawn","y":[23.599655,11.099599]},{"t":"The Legend of Zelda: Breath of the Wild","y":[16.038266,8.675937]},{"t":"Super Mario Odyssey","y":[13.883421,9.600679]},{"t":"Assassin's Creed Origins","y":[25.036947,17.290507]},{"t":"God of War (2018 video game)","y":[14.242355,6.749365]},{"t":"Spider-Man (2018 video game)","y":[18.12347,8.769114]},{"t":"Resident Evil 2 (2019 video game)","y":[19.583714,10.331288]},{"t":"Sekiro: Shadows Die Twice","y":[16.173574,7.434325]},{"t":"Death Stranding","y":[12.476863,5.954104]},{"t":"Doom Eternal","y":[12.301256,7.456911]},{"t":"Animal Crossing: New Horizons","y":[28.351644,20.562748]},{"t":"The Last of Us Part II","y":[11.481497,5.326214]},{"t":"Ghost of Tsushima","y":[17.943103,8.446771]},{"t":"Cyberpunk 2077","y":[8.254614,3.411953]},{"t":"Resident Evil Village","y":[10.632494,4.542386]},{"t":"Ratchet & Clank: Rift Apart","y":[15.166051,6.672493]},{"t":"Horizon Forbidden West","y":[14.001,8.257582]},{"t":"Elden Ring","y":[21.709593,11.473761]},{"t":"God of War Ragnarök","y":[15.444164,10.863213]},{"t":"Resident Evil 4 (2023 video game)","y":[17.4582,8.345286]},{"t":"The Legend of Zelda: Tears of the Kingdom","y":[11.552989,6.215336]},{"t":"Final Fantasy XVI","y":[13.592011,7.149562]},{"t":"Spider-Man 2 (2023 video game)","y":[13.248784,6.789116]}];const previsiones=[12.2846689588,6.8489406005];const juego=document.getElementById('gta-juego'),semana=document.getElementById('gta-semana'),salida=document.getElementById('gta-ex-resultado'),a=document.getElementById('gta-barra-a'),b=document.getElementById('gta-barra-b'),nb=document.getElementById('gta-nombre-b');if(!juego||!semana||!salida||!a||!b||!nb)return;const f=n=>n.toLocaleString('es-ES',{maximumFractionDigits:1,minimumFractionDigits:1});function actualizar(){const h=Number(semana.value),s=juegos[Number(juego.value)],p=previsiones[h],v=s.y[h];salida.textContent=`GTA VI: previsión del ${f(p)} % para la ${h===0?'tercera':'quinta'} semana. ${s.t} conservó el ${f(v)} % de las consultas del estreno.`;a.style.width=Math.min(p,100)+'%';b.style.width=Math.min(v,100)+'%';nb.textContent=s.t+' · dato observado';}juego.addEventListener('change',actualizar);semana.addEventListener('change',actualizar);actualizar();})();
</script>

## Una cifra central y mucho espacio para equivocarse

Para el periodo del **3 al 9 de diciembre**, la previsión ronda las **92.000 consultas diarias**. Para el **17 al 23 de diciembre**, unas **51.000**. Son medias previstas de consultas de una página, no personas distintas, búsquedas en Google o jugadores conectados.

Los errores de los juegos usados para validar el método obligan a dejar bastante espacio alrededor: aproximadamente **46.000–186.000 consultas** en la primera ventana y **16.000–163.000** en la segunda. Estos rangos orientativos no garantizan una probabilidad de acierto concreta.

Además, GTA VI parte de un estreno mayor que cualquiera de los juegos con los que he ajustado el modelo. Su caída inicial también es algo más intensa. Es una pequeña salida fuera del terreno conocido que hace la predicción más incierta, aunque comparemos proporciones.

Una actualización, una polémica o un anuncio pueden volver a disparar las consultas. El modelo no sabe qué noticia llegará mañana. Tampoco representa a todos los países: una página en inglés es solo una ventana al fenómeno.

Lo interesante será volver cuando terminen ambas semanas y enfrentar la previsión con lo ocurrido, conservando estas cifras. **Si las consultas caen, eso no demostrará que GTA VI ha dejado de importar.** Habrá cambiado una forma concreta de prestarle atención. La vida del juego sigue fuera de ese contador.

## Fuentes y archivos

- [Fecha de lanzamiento en la tienda de Rockstar](https://store.rockstargames.com/game/buy-gta-vi?drm=playstation).
- [Comunicado original de Take-Two depositado en la SEC, 20 de noviembre](https://www.sec.gov/Archives/edgar/data/946581/000162828026075217/exhibit9918k.htm).
- [Documentación oficial de Wikimedia Analytics API](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/).
- [Notebook de preparación](/analisis/gta_vi_fiebre/01_preparacion_datos.ipynb) y [notebook de predicción y evaluación](/analisis/gta_vi_fiebre/02_prediccion.ipynb).
- [Datos diarios en CSV](/analisis/gta_vi_fiebre/consultas_diarias.csv), [serie de GTA VI](/analisis/gta_vi_fiebre/gta_vi_consultado.json), [treinta series conservadas](/analisis/gta_vi_fiebre/series_consultadas.json), [código del modelo](/analisis/gta_vi_fiebre/modelo.py) y [resultados completos](/analisis/gta_vi_fiebre/resultados.json).
- [Protocolo previo al cálculo](/analisis/gta_vi_fiebre/protocolo.md) y [fuentes, peticiones exactas, decisiones y limitaciones](/analisis/gta_vi_fiebre/fuentes_metodologia.md).

La previsión se conserva con fecha de corte del 23 de noviembre. Los datos futuros se añadirán en una revisión identificada; no están presentes en este análisis.
