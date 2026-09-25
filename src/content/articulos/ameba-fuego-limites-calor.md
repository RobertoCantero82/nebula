---
imagenPortada: "/nebula/imagenes/ameba_portada.png"
titulo: "Esta ameba resiste 70 °C, se reproduce a 63 °C y ha hecho tropezar a la propia NASA"
descripcion: "Los datos de la ameba de fuego muestran cómo pierde capacidades a medida que sube la temperatura y aclaran un error de NASA en español."
tema: "CIENCIA"
fecha: 2026-09-23
cifraDestacada: "3,25 veces"
etiquetaCifra: "más tarda en duplicarse a 63 °C que a 57 °C"
metodologia: "Análisis de 924 observaciones de crecimiento de _Incendiamoeba cascadensis_, con 864 recuentos válidos, 116 cultivos y 17 temperaturas. Cada cultivo se normalizó respecto a su densidad del día 0. Los tiempos de duplicación proceden de los lotes de referencia seleccionados por los autores. Los ensayos de movimiento y resistencia térmica se contrastaron con el estudio original y las publicaciones de NASA."
---

*Una ameba descubierta en un arroyo volcánico de California se divide a 63 °C, todavía se mueve a 64 °C, conserva algo de actividad a 66 °C y puede recuperarse después de pasar cinco minutos a 70 °C. Parece un solo récord, pero en realidad son pruebas diferentes. Los datos cuentan cómo el calor le va quitando capacidades una por una. Y, en medio de la historia, la versión española de NASA confunde 80 grados Celsius con 80 Fahrenheit.*

Las noticias científicas adoran los números redondos. Una temperatura, un récord y una criatura capaz de hacer algo que parecía imposible. La nueva *Incendiamoeba cascadensis*, apodada **ameba de fuego**, ofrece todo eso. El problema aparece cuando intentamos resumir su vida con una única cifra.

[Live Science](https://www.livescience.com/planet-earth/evolution/newfound-fire-amoeba-from-the-cascades-sets-record-for-the-hottest-temperature-complex-life-can-survive-at) presenta el hallazgo como el récord de temperatura a la que puede sobrevivir la vida compleja. La frase es llamativa, pero mezcla dos preguntas distintas. **¿A qué temperatura puede reproducirse la ameba? ¿Y hasta qué temperatura puede evitar la muerte durante unos minutos?**

Y no tienen la misma respuesta.

El [estudio publicado en *Cell*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12697723/) sitúa el verdadero récord en la **reproducción a 63 °C**. A partir de ahí comienza otra historia: la ameba deja de multiplicarse, pero no pierde todas sus funciones a la vez.

## 1. Un termómetro y cinco puertas

La manera más sencilla de entender el experimento es imaginar que el calor va cerrando puertas.

| Temperatura | Qué conserva la ameba | Qué no demuestra |
|---:|---|---|
| **63 °C** | Crece y se divide | Que lo haga con la misma facilidad que a su temperatura óptima |
| **64 °C** | Mantiene movimiento medible | Que la población siga creciendo |
| **66 °C** | Permanece parcialmente activa y comienza a redondearse | Que pueda vivir así de forma estable |
| **70 °C** | Se enquista y puede recuperarse después | Que crezca a 70 °C: la exposición duró cinco minutos |
| **80 °C** | No se recuperó en el ensayo | Que 80 °C sea una frontera universal para cualquier eucariota |

<div class="grafico-interactivo">
  <canvas id="grafico-limites-ameba" height="340"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-limites-ameba');
    if (!ctx || !window.Chart) return;

    const explicaciones = [
      'Crece y se divide.',
      'Mantiene movimiento medible, pero ya no crece.',
      'Permanece parcialmente activa y comienza a redondearse.',
      'Se enquista y puede recuperarse tras una exposición de cinco minutos.',
      'No se recuperó después del ensayo.',
    ];

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          'Reproducción',
          'Movimiento',
          'Actividad parcial',
          'Recuperación',
          'Sin recuperación',
        ],
        datasets: [{
          label: 'Límite observado (°C)',
          data: [63, 64, 66, 70, 80],
          borderColor: '#446DDF',
          backgroundColor: 'rgba(68, 109, 223, 0.12)',
          pointBackgroundColor: [
            '#D85A30',
            '#446DDF',
            '#8B85C4',
            '#9A6BB5',
            '#8D897E',
          ],
          pointBorderColor: '#FFFFFF',
          pointBorderWidth: 2,
          pointRadius: 8,
          pointHoverRadius: 11,
          borderWidth: 3,
          stepped: 'after',
          fill: true,
        }],
      },
      options: {
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false,
        },
        plugins: {
          legend: {
            position: 'bottom',
          },
          tooltip: {
            callbacks: {
              label: (context) =>
                `${context.dataset.label}: ${context.parsed.y} °C`,
              afterLabel: (context) =>
                explicaciones[context.dataIndex],
            },
          },
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Capacidad observada',
            },
          },
          y: {
            min: 60,
            max: 82,
            ticks: {
              stepSize: 2,
              callback: (valor) => `${valor} °C`,
            },
            title: {
              display: true,
              text: 'Temperatura',
            },
          },
        },
      },
    });
  });
</script>

El récord científico está en la primera fila. La ameba no se limita a permanecer intacta a 63 °C: **se alimenta, crece y divide su célula**. El equipo también observó la mitosis, el proceso con el que una célula reparte su material genético antes de dividirse.

Los otros números describen resistencias cada vez más precarias. El movimiento fue cuantificado hasta 64 °C. A 66 °C las células se redondearon, permanecieron parcialmente activas y parecieron comenzar a formar un quiste protector. A 70 °C llegaron a enquistarse y recuperaron la actividad cuando volvieron a 60 °C, pero solo después de una exposición de cinco minutos. Tras el tratamiento a 80 °C ya no regresaron.

La publicación de NASA permite ver ese comportamiento, no solo leerlo:

<div style="max-width: 560px; margin: 2rem auto;">
  <blockquote class="twitter-tweet" data-dnt="true">
    <a href="https://x.com/NASA_es/status/2102480581103681568">Ver la publicación y el vídeo de NASA en español sobre la ameba de fuego.</a>
  </blockquote>
</div>

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Sobrevivir cinco minutos, seguir moviéndose y reproducirse durante días no son sinónimos.** Presentarlos como un único límite borra precisamente la parte más interesante del descubrimiento.

## 2. A 63 °C vive, pero no cómodamente

**He analizado los datos de crecimiento publicados por los investigadores**. El archivo contiene 924 observaciones tomadas en 116 cultivos individuales y 17 temperaturas. Sesenta registros no tienen un recuento celular válido, por lo que el análisis utiliza las 864 mediciones restantes.

Como en [el análisis de la cadencia espacial de China](/nebula/articulos/articulo_lanzamientos_china_2026/), una cifra llamativa adquiere sentido cuando se observa la serie completa y no solo su valor máximo.

Los cultivos no empezaban siempre con la misma cantidad de células. Para compararlos, dividí cada recuento por la densidad de ese mismo cultivo en el día 0. Un resultado de 1 significa que termina igual que comenzó; por encima de 1 hay crecimiento neto y por debajo de 1 hay pérdida.

El patrón forma una montaña. A temperaturas bajas la ameba apenas crece. Acelera al acercarse a los 55-57 °C y después pierde rendimiento mientras se aproxima a su límite.

<div class="grafico-interactivo">
  <canvas id="grafico-ameba-crecimiento" height="340"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-ameba-crecimiento');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['30', '40', '42', '43', '44', '45', '50', '51,5', '54', '55', '57', '61,5', '62', '62,5', '63', '64'],
        datasets: [{
          label: 'Densidad mediana al día 7 respecto al día 0',
          data: [0.55, 0.98, 1.44, 1.45, 1.73, 2.21, 2.46, 5.28, 3.33, 3.83, 4.80, 1.58, 2.58, 2.64, 1.23, 0.41],
          borderColor: '#D85A30',
          backgroundColor: 'rgba(216, 90, 48, 0.14)',
          pointBackgroundColor: [
            '#D85A30', '#D85A30', '#D85A30', '#D85A30', '#D85A30', '#D85A30',
            '#D85A30', '#D85A30', '#D85A30', '#D85A30', '#D85A30', '#D85A30',
            '#D85A30', '#D85A30', '#8B85C4', '#446DDF'
          ],
          pointRadius: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 7, 7],
          borderWidth: 3,
          tension: 0.22,
          fill: true,
        }],
      },
      options: {
        responsive: true,
        interaction: { mode: 'index', intersect: false },
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              title: (items) => `${items[0].label} °C`,
              label: (context) => `${context.parsed.y.toFixed(2)} veces la densidad inicial`,
            },
          },
        },
        scales: {
          x: { title: { display: true, text: 'Temperatura (°C)' } },
          y: {
            beginAtZero: true,
            title: { display: true, text: 'Factor de crecimiento mediano' },
          },
        },
      },
    });
  });
</script>

A 57 °C, el cultivo mediano termina el séptimo día con **4,8 veces** su densidad inicial. A 63 °C todavía queda por encima del punto de partida, pero solo alcanza **1,23 veces**. A 64 °C cae hasta **0,41**.

Las réplicas muestran el mismo salto. A 63 °C, 12 de los 16 cultivos terminan con más células que al comenzar. A 64 °C solo lo consigue 1 de 8. Puede quedar movimiento, pero el conjunto ya no mantiene el crecimiento.

Este cálculo no sustituye la prueba estadística del estudio. Los autores fijaron el límite mediante modelos aplicados a las curvas completas de crecimiento. El análisis del día 7 sirve para hacer visible el cambio con una pregunta mucho más sencilla: **¿cuánta población queda al final?**

## 3. El récord cuesta casi cuatro días por duplicación

La ameba crece mejor entre 55 y 57 °C. A 57 °C, el lote de referencia seleccionado por los autores tarda una media de **29,8 horas** en duplicar su población. Al llevarla hasta 63 °C necesita **96,8 horas**.

Eso son cuatro días para hacer lo que, cerca de su temperatura favorita, resuelve en poco más de uno. El récord existe, pero tiene un precio: **a 63 °C la duplicación es 3,25 veces más lenta que a 57 °C**.

<div class="grafico-interactivo">
  <canvas id="grafico-ameba-duplicacion" height="320"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-ameba-duplicacion');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['42', '43', '44', '45', '50', '51,5', '54', '55', '57', '61', '61,5', '62', '62,5', '63'],
        datasets: [{
          label: 'Horas necesarias para duplicar la población',
          data: [126, 86.4, 105.5, 81, 64.8, 51.4, 35, 36.9, 29.8, 39.4, 73.6, 90, 55.7, 96.8],
          borderColor: '#446DDF',
          pointBackgroundColor: [
            '#446DDF', '#446DDF', '#446DDF', '#446DDF', '#446DDF', '#446DDF',
            '#446DDF', '#446DDF', '#D85A30', '#446DDF', '#446DDF', '#446DDF',
            '#446DDF', '#8B85C4'
          ],
          pointRadius: [4, 4, 4, 4, 4, 4, 4, 4, 7, 4, 4, 4, 4, 7],
          borderWidth: 3,
          tension: 0.2,
        }],
      },
      options: {
        responsive: true,
        interaction: { mode: 'index', intersect: false },
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              title: (items) => `${items[0].label} °C`,
              label: (context) => `${context.parsed.y.toFixed(1)} horas`,
            },
          },
        },
        scales: {
          x: { title: { display: true, text: 'Temperatura (°C)' } },
          y: {
            beginAtZero: true,
            title: { display: true, text: 'Tiempo de duplicación (horas)' },
          },
        },
      },
    });
  });
</script>

Este es el matiz que desaparece cuando un titular utiliza únicamente la palabra «sobrevive». La ameba no cruza una línea y continúa como si nada. **Se acerca al límite perdiendo velocidad, capacidad de crecer y, finalmente, movimiento.**

## 4. Vida compleja no significa un animal diminuto

La expresión 'vida compleja' puede despistar. La *Incendiamoeba cascadensis* es un organismo **unicelular**. No tiene órganos, tejidos ni cerebro. La complejidad a la que se refieren los artículos es celular.

Las bacterias y arqueas son procariotas, es decir, sus células no guardan el ADN dentro de un núcleo ni poseen la misma colección de compartimentos internos. Esta ameba es eucariota. Su célula sí contiene núcleo, mitocondrias y otros orgánulos rodeados por membranas. Los animales, las plantas y los hongos también pertenecemos a ese gran grupo.

Por eso el hallazgo importa. El calor desestabiliza proteínas, membranas y material genético. Durante décadas, el límite conocido de crecimiento para los eucariotas rondaba los 60 °C. La ameba lo empuja tres grados más arriba y demuestra que una célula con esa organización interna puede seguir dividiéndose en condiciones que se consideraban demasiado destructivas.

Decir 'vida compleja' no es falso si se explica así. Sin esa explicación, puede sugerir algo que el estudio no ha encontrado: **un organismo multicelular viviendo alegremente a 63 °C**.

## 5. La NASA explica mejor el récord y tropieza con el termómetro

La [publicación de NASA en español](https://x.com/NASA_es/status/2102480581103681568) conduce a un artículo mucho más preciso que el titular de Live Science. NASA distingue la reproducción a 63 °C del movimiento a 64 °C, la actividad parcial a 66 °C y la recuperación tras cinco minutos a 70 °C.

Pero la [versión española](https://ciencia.nasa.gov/ciencias-terrestres/investigacion-financiada-por-la-nasa-descubre-vida-compleja-que-desafia-un-calor-record/) de ese artículo contiene una errata en el texto que acompaña al vídeo. Afirma que **«176 grados Celsius (80 grados Fahrenheit)»** fueron demasiado para la ameba. 

Las unidades están intercambiadas. La [versión inglesa de NASA](https://science.nasa.gov/earth/nasa-funded-research-finds-complex-life-defying-record-heat/) ofrece la equivalencia correcta: **176 °F son 80 °C**. El estudio ensayó 80 °C, no 176 °C.

Y no estamos hablando de una diferencia pequeña. Al convertir correctamente:

- 80 °C equivalen a 176 °F.
- 80 °F equivalen aproximadamente a 26,7 °C.
- 176 °C equivalen aproximadamente a 348,8 °F.

La errata no cambia el experimento, porque el dato original y el resto del artículo apuntan a 80 °C. Sin embargo, sí demuestra algo útil para cualquier artículo científico: **una fuente oficial también puede equivocarse al traducir una unidad**.

## 6. Por qué una ameba terrestre interesa a la NASA

La investigación recibió financiación del programa de Exobiología de NASA. No porque la ameba venga del espacio, sino porque **ayuda a revisar las condiciones en las que buscamos vida fuera de la Tierra**.

Si una célula eucariota puede dividirse a 63 °C, el rango de ambientes potencialmente habitables es algo mayor de lo que creíamos. Eso sí, esto no convierte cualquier mundo caliente en un hogar. La propia NASA recuerda que también hacen falta agua, alimento, una acidez adecuada, oxígeno, presión y un ecosistema capaz de sostener a la ameba.

La criatura, de hecho, no vive sola. Se alimenta de bacterias termófilas. Encontrar una célula resistente no basta: **para mantener vida compleja también hace falta todo lo que esa vida necesita comer**.

## 7. El récord

La ameba de fuego sí ha superado un hito. Es el eucariota conocido capaz de reproducirse a mayor temperatura: 63 °C. Pero la cifra solo se entiende cuando observamos lo que sucede alrededor.

A 57 °C se duplica con rapidez. A 63 tarda más de cuatro días. A 64 conserva movimiento, aunque la población cae. A 66 apenas mantiene actividad mientras cambia de forma. A 70 resiste durante cinco minutos dentro de un quiste. A 80 ya no regresa.

El calor no encuentra un interruptor. Encuentra una escalera y va apagando funciones peldaño a peldaño.

Esa es una historia más precisa que 'la vida compleja sobrevive a una temperatura récord'. También es más extraña y más interesante. **La gran hazaña de esta ameba no consiste en ser indestructible, sino en seguir siendo una célula funcional cuando casi todas las puertas ya se han cerrado.**

**Puedes reproducir las comparaciones de crecimiento y tiempo de duplicación** en el [notebook de Jupyter de la ameba de fuego](/nebula/analisis/analisis-ameba-fuego.ipynb).

Fuentes: [estudio original en *Cell*](https://doi.org/10.1016/j.cell.2026.08.043), [versión de acceso abierto en PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12697723/), [datos y código de los autores](https://github.com/hbrappaport/incendiamoeba_manuscript), [NASA Science](https://science.nasa.gov/earth/nasa-funded-research-finds-complex-life-defying-record-heat/), [NASA Ciencia](https://ciencia.nasa.gov/ciencias-terrestres/investigacion-financiada-por-la-nasa-descubre-vida-compleja-que-desafia-un-calor-record/) y [Live Science](https://www.livescience.com/planet-earth/evolution/newfound-fire-amoeba-from-the-cascades-sets-record-for-the-hottest-temperature-complex-life-can-survive-at).

---
