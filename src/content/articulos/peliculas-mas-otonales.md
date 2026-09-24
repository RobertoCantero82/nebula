---
imagenPortada: "/nebula/imagenes/pelis_otono_portada.png"
titulo: "¿Cuál es la película más otoñal? Un índice entre hojas, lluvia y melancolía"
descripcion: "Un índice aplicado a 265 películas revela cuáles capturan mejor el paisaje, los rituales y la melancolía del otoño."
tema: "CINE"
fecha: 2026-09-24
cifraDestacada: "96,7"
etiquetaCifra: "puntos sobre 100: un empate entre dos películas inesperadas"
metodologia: "Índice construido a partir de 265 películas candidatas y cinco dimensiones puntuadas entre 0 y 3: presencia del otoño, paisaje y paleta, clima y vestuario, rituales y espacios, y tono emocional. Se excluyeron las películas en las que Halloween era central, se realizó un cribado inicial de 264 títulos y una revisión individual con incrementos de medio punto de 112 candidatas. Las cinco dimensiones tienen el mismo peso y el resultado se transforma a una escala de 0 a 100."
---

Hay películas que parecen otoñales antes incluso de que caiga la primera hoja. Basta una librería, un abrigo, una carretera húmeda o una conversación ligeramente melancólica para que la estación se instale en la pantalla. Pero ¿cuánto hay de otoño real y cuánto de prejuicio cinematográfico?

Para responder he construido un índice de otoñalidad y lo he aplicado a una lista inicial de **265 películas**. La condición era importante: buscar cine de otoño **sin convertir la selección en otra lista de Halloween**. El resultado tiene dos ganadoras, un empate enorme en el tercer puesto y una conclusión inesperada: el otoño cinematográfico depende menos del frío que de cómo se siente una película.

## Medir una estación sin confundirla con Halloween

El índice combina cinco dimensiones. Cada una recibe entre 0 y 3 puntos, donde 0 significa ausencia y 3 indica que el elemento es dominante o esencial:

- **Presencia del otoño:** si la estación aparece de forma explícita y relevante en la historia.
- **Paisaje y paleta:** hojas, bosques y colores ocres, marrones, rojos o naranjas.
- **Clima y vestuario:** lluvia, niebla, viento, frío, abrigos, jerséis y bufandas.
- **Rituales y espacios:** cosechas, vuelta al colegio, Acción de Gracias, cafeterías, librerías o chimeneas.
- **Tono emocional:** nostalgia, melancolía, intimidad, reflexión o calidez.

Las cinco dimensiones pesan lo mismo. La suma, cuyo máximo es 15, se transforma después a una escala de 0 a 100. Halloween no resta puntos: cuando constituye el centro de la trama, la película queda fuera del análisis. Así se evita que el índice mezcle dos preguntas distintas.

La primera codificación permitió revisar 264 películas, pero produjo demasiados perfiles idénticos. Por eso realicé una segunda evaluación individual de **112 candidatas**, incluidas las 46 situadas justo por debajo del corte provisional. Esa revisión recuperó cuatro títulos que también alcanzaban los 90 puntos y evitó que el primer filtro decidiera por sí solo la clasificación.

Es un proceso parecido al que utilicé en [el análisis de las secuelas de *Matrix*](/nebula/articulos/matrix-secuelas/): empezar con una intuición reconocible, convertirla en variables y comprobar si los datos sostienen la historia que creíamos conocer.

## Dos películas comparten el otoño perfecto

***La tormenta de hielo*** y ***Las normas de la casa de la sidra*** encabezan el índice con **96,7 puntos**. La primera convierte Acción de Gracias, el clima y la crisis de una familia en la estructura misma del relato. La segunda se apoya en el huerto, la sidra, la cosecha y el paisaje de Maine.

Justo después aparece ***Cuando cae el otoño***, con 93,3 puntos. A partir de ahí llega el gran empate: **quince películas comparten los 90 puntos**. El orden alfabético dentro de ese grupo sirve únicamente para mostrar los títulos, pero no existe diferencia de posición entre ellos.

<div class="grafico-interactivo" style="overflow-x: auto;">
  <div style="height: 720px; min-width: 675px;">
    <canvas id="grafico-peliculas-otonales" role="img" aria-label="Clasificación de las 18 películas con mayor índice de otoñalidad"></canvas>
  </div>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-peliculas-otonales');
    if (!ctx || !window.Chart) return;

    const etiquetas = [
      'La tormenta de hielo',
      'Las normas de la casa de la sidra',
      'Cuando cae el otoño',
      'Ana de las Tejas Verdes',
      'Beneath the Harvest Sky',
      'Cuento de otoño',
      'El mito de las huellas dactilares',
      'Esencia de mujer',
      'Hannah y sus hermanas',
      'La casa del sí',
      'Lejos del cielo',
      'Mejor solo que mal acompañado',
      'Otoño en Nueva York',
      'Petite maman',
      'Prácticamente magia',
      'Quédate a mi lado',
      'Sólo el cielo lo sabe',
      'Tienes un e-mail',
    ];

    const puntuaciones = [96.7, 96.7, 93.3, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90];

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: etiquetas,
        datasets: [{
          label: 'Índice de otoñalidad',
          data: puntuaciones,
          backgroundColor: puntuaciones.map((valor) => {
            if (valor > 95) return '#74341F';
            if (valor > 90) return '#AD562E';
            return '#D28743';
          }),
          borderWidth: 0,
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        interaction: { mode: 'index', intersect: false },
        scales: {
          x: {
            beginAtZero: true,
            max: 100,
            title: { display: true, text: 'Índice de otoñalidad' },
          },
          y: {
            grid: { display: false },
            ticks: { autoSkip: false, font: { size: 10 } },
          },
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => `Índice: ${context.parsed.x.toFixed(1)} puntos`,
            },
          },
        },
      },
    });
  });
</script>

El empate no es un defecto que haya que romper a toda costa. Es información: películas muy diferentes pueden producir una sensación otoñal igual de intensa mediante combinaciones distintas. *Esencia de mujer* llega a ella a través de Acción de Gracias, el campus y la nostalgia; *Petite maman*, mediante el bosque y la intimidad; *Tienes un e-mail*, con Nueva York, las librerías y el romance.

## El otoño no solo entra por los ojos

Entre las 18 películas del grupo superior, el **tono emocional** es la dimensión más intensa, con una media de 2,92 sobre 3. Le sigue la **presencia explícita del otoño**, con 2,89. El clima y el vestuario quedan en último lugar, con 2,56.

La diferencia es pequeña, pero cambia la interpretación. Una película no necesita encadenar lluvia, bufandas y tazas humeantes para ser otoñal. Resulta más importante que la estación tenga peso narrativo y que el relato transmita intimidad, transición o melancolía.

El siguiente gráfico permite recorrer la composición de cada película. Cuanto más oscura es una celda, mayor es la puntuación de esa dimensión. Al pasar el cursor se muestra el valor exacto.

<div class="grafico-interactivo" style="overflow-x: auto;">
  <div style="height: 760px; min-width: 675px;">
    <canvas id="grafico-composicion-otonal" role="img" aria-label="Composición del índice de otoñalidad por película y dimensión"></canvas>
  </div>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-composicion-otonal');
    if (!ctx || !window.Chart) return;

    const peliculas = [
      'La tormenta de hielo',
      'Las normas de la casa de la sidra',
      'Cuando cae el otoño',
      'Ana de las Tejas Verdes',
      'Beneath the Harvest Sky',
      'Cuento de otoño',
      'El mito de las huellas dactilares',
      'Esencia de mujer',
      'Hannah y sus hermanas',
      'La casa del sí',
      'Lejos del cielo',
      'Mejor solo que mal acompañado',
      'Otoño en Nueva York',
      'Petite maman',
      'Prácticamente magia',
      'Quédate a mi lado',
      'Sólo el cielo lo sabe',
      'Tienes un e-mail',
    ];

    const dimensiones = [
      'Presencia del otoño',
      'Paisaje y paleta',
      'Clima y vestuario',
      'Rituales y espacios',
      'Tono emocional',
    ];

    const valores = [
      [3, 2.5, 3, 3, 3],
      [3, 3, 2.5, 3, 3],
      [3, 3, 2.5, 2.5, 3],
      [2.5, 3, 2.5, 2.5, 3],
      [3, 2.5, 2.5, 3, 2.5],
      [3, 3, 2, 3, 2.5],
      [3, 2, 2.5, 3, 3],
      [3, 2, 2.5, 3, 3],
      [3, 2, 2.5, 3, 3],
      [3, 1.5, 3, 3, 3],
      [3, 3, 2.5, 2, 3],
      [3, 2, 3, 3, 2.5],
      [3, 3, 2.5, 2, 3],
      [3, 3, 2.5, 2, 3],
      [2.5, 3, 2.5, 2.5, 3],
      [2.5, 3, 2.5, 2.5, 3],
      [3, 3, 2.5, 2, 3],
      [2.5, 3, 2.5, 2.5, 3],
    ];

    const datos = valores.flatMap((fila, y) =>
      fila.map((valor, x) => ({
        x,
        y,
        valor,
        pelicula: peliculas[y],
        dimension: dimensiones[x],
      }))
    );

    const colorCelda = (valor) => {
      if (valor === 3) return '#74341F';
      if (valor === 2.5) return '#A84F24';
      if (valor === 2) return '#E46C0A';
      return '#F5A13A';
    };

    const celdas = {
      id: 'celdasComposicion',
      beforeDatasetsDraw(chart) {
        const { ctx: dibujo, scales } = chart;
        const dataset = chart.data.datasets[0].data;

        dibujo.save();
        dataset.forEach((dato) => {
          const x1 = scales.x.getPixelForValue(dato.x - 0.48);
          const x2 = scales.x.getPixelForValue(dato.x + 0.48);
          const y1 = scales.y.getPixelForValue(dato.y - 0.48);
          const y2 = scales.y.getPixelForValue(dato.y + 0.48);
          const izquierda = Math.min(x1, x2);
          const arriba = Math.min(y1, y2);

          dibujo.fillStyle = colorCelda(dato.valor);
          dibujo.fillRect(izquierda, arriba, Math.abs(x2 - x1), Math.abs(y2 - y1));
        });
        dibujo.restore();
      },
      afterDatasetsDraw(chart) {
        const { ctx: dibujo, scales } = chart;
        const dataset = chart.data.datasets[0].data;

        dibujo.save();
        dibujo.font = '11px Fira Code, monospace';
        dibujo.textAlign = 'center';
        dibujo.textBaseline = 'middle';

        dataset.forEach((dato) => {
          dibujo.fillStyle = dato.valor >= 2.5 ? '#FFFFFF' : '#1B1836';
          dibujo.fillText(
            dato.valor.toFixed(1),
            scales.x.getPixelForValue(dato.x),
            scales.y.getPixelForValue(dato.y)
          );
        });
        dibujo.restore();
      },
    };

    new Chart(ctx, {
      type: 'scatter',
      data: {
        datasets: [{
          data: datos,
          pointRadius: 0,
          pointHitRadius: 42,
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        parsing: false,
        interaction: { mode: 'nearest', intersect: false },
        scales: {
          x: {
            type: 'linear',
            min: -0.5,
            max: 4.5,
            afterBuildTicks: (escala) => {
              escala.ticks = dimensiones.map((_, indice) => ({ value: indice }));
            },
            grid: { display: false },
            ticks: {
              stepSize: 1,
              autoSkip: false,
              callback: (valor) => dimensiones[valor] ?? '',
              font: { size: 10 },
            },
          },
          y: {
            type: 'linear',
            min: -0.5,
            max: 17.5,
            reverse: true,
            afterBuildTicks: (escala) => {
              escala.ticks = peliculas.map((_, indice) => ({ value: indice }));
            },
            grid: { display: false },
            ticks: {
              stepSize: 1,
              autoSkip: false,
              callback: (valor) => peliculas[valor] ?? '',
              font: { size: 10 },
            },
          },
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title: (elementos) => elementos[0].raw.pelicula,
              label: (context) => `${context.raw.dimension}: ${context.raw.valor.toFixed(1)}`,
            },
          },
        },
      },
      plugins: [celdas],
    });
  });
</script>

El mapa también explica por qué existe un empate tan amplio. *La casa del sí* compensa su paisaje menos otoñal con clima, rituales y tono máximos. *Mejor solo que mal acompañado* obtiene un 3 en clima y rituales, pero se queda en 2 en paisaje. *Lejos del cielo* hace lo contrario: su paleta es esencial, mientras los rituales tienen menos peso.

## Una clasificación estable, un umbral discutible

Para comprobar cuánto dependía el resultado de las decisiones del índice, repetí el cálculo eliminando una dimensión cada vez. Las correlaciones entre las clasificaciones alternativas y la original se mantuvieron entre **0,896 y 0,986**. El orden general, por tanto, es razonablemente estable.

La frontera de los 90 puntos lo es menos. Quince películas están exactamente en ese valor, de modo que pequeños cambios en la definición pueden hacerlas entrar o salir del grupo superior. Los 90 puntos deben leerse como **un umbral editorial**, no como una ley natural.

El índice tampoco dice si una película es buena ni si te va a gustar. Mide una característica concreta. Para la otra pregunta está [Indy](https://robertocantero-agente-indy.hf.space/), mi agente de recomendación cinematográfica: allí puedes consultar si una película encaja contigo antes de decidir la sesión. Si aún no lo has probado, no sé a qué estás esperando.

## El análisis, abierto

**Todo el proceso está disponible** para quien quiera revisar las decisiones, reproducir los cálculos o proponer otros pesos. Puedes [descargar el notebook de Jupyter](/nebula/analisis/indice-otonalidad-peliculas.ipynb) y consultar también el [CSV con las evaluaciones refinadas](/nebula/analisis/evaluaciones-otonalidad-refinadas.csv).

El cuaderno documenta el cribado inicial, la revisión de posibles falsos negativos, la construcción del ranking y el análisis de sensibilidad. La codificación incluye inevitablemente juicio humano; hacerla visible permite discutirla en lugar de esconderla detrás de una cifra.

## Las 18 películas más otoñales y dónde verlas

La disponibilidad cambia con frecuencia. Cada enlace abre la ficha actualizada en la plataforma JustWatch. Dentro del empate a 90 puntos, como te comentaba anteriormente, los títulos aparecen en orden alfabético. Esta es la lista definitiva de películas más otoñales. ¡Disfútala!

- **La tormenta de hielo** (1997) — **96,7 puntos**. Acción de Gracias, tormenta y crisis familiar. [Dónde verla en España](https://www.justwatch.com/es/pelicula/la-tormenta-de-hielo).
- **Las normas de la casa de la sidra** (1999) — **96,7 puntos**. Huerto, sidra, cosecha y paisaje de Maine. [Dónde verla en España](https://www.justwatch.com/es/pelicula/the-cider-house-rules).
- **Cuando cae el otoño** (2024) — **93,3 puntos**. El otoño rural francés determina la imagen y la narración. [Consultar disponibilidad](https://www.justwatch.com/es/buscar?q=When%20Fall%20Is%20Coming).
- **Ana de las Tejas Verdes** (1985) — **90 puntos**. Paisaje rural, calidez y sensibilidad melancólica. [Consultar disponibilidad](https://www.justwatch.com/es/buscar?q=Anne%20of%20Green%20Gables%201985).
- **Beneath the Harvest Sky** (2013) — **90 puntos**. Cosecha, adolescencia y paisaje rural de Maine. [Consultar disponibilidad](https://www.justwatch.com/es/buscar?q=Beneath%20the%20Harvest%20Sky).
- **Cuento de otoño** (1998) — **90 puntos**. Viñedo, vendimia y vida rural en la Provenza. [Dónde verla en España](https://www.justwatch.com/es/pelicula/autumn-tale).
- **El mito de las huellas dactilares** (1997) — **90 puntos**. Una reunión de Acción de Gracias organiza el drama familiar. [Consultar disponibilidad](https://www.justwatch.com/es/buscar?q=The%20Myth%20of%20Fingerprints).
- **Esencia de mujer** (1992) — **90 puntos**. Acción de Gracias, campus, ciudad y nostalgia. [Dónde verla en España](https://www.justwatch.com/es/pelicula/esencia-de-mujer).
- **Hannah y sus hermanas** (1986) — **90 puntos**. Acción de Gracias, reuniones familiares y melancolía neoyorquina. [Dónde verla en España](https://www.justwatch.com/es/pelicula/hannah-y-sus-hermanas).
- **La casa del sí** (1997) — **90 puntos**. Tormenta, encierro doméstico y una incómoda reunión de Acción de Gracias. [Consultar disponibilidad](https://www.justwatch.com/es/buscar?q=The%20House%20of%20Yes).
- **Lejos del cielo** (2002) — **90 puntos**. El follaje de Connecticut y una paleta cálida sostienen el melodrama. [Dónde verla en España](https://www.justwatch.com/es/pelicula/far-from-heaven).
- **Mejor solo que mal acompañado** (1987) — **90 puntos**. Viaje de Acción de Gracias, clima tardío y calidez emocional. [Dónde verla en España](https://www.justwatch.com/es/pelicula/mejor-solo-que-mal-acompanado).
- **Otoño en Nueva York** (2000) — **90 puntos**. La estación domina el romance y la identidad visual. [Dónde verla en España](https://www.justwatch.com/es/pelicula/autumn-in-new-york).
- **Petite maman** (2021) — **90 puntos**. Bosque otoñal, duelo e intimidad entre generaciones. [Dónde verla en España](https://www.justwatch.com/es/pelicula/petite-maman).
- **Prácticamente magia** (1998) — **90 puntos**. Nueva Inglaterra, botánica, interiores y vínculos familiares; lo sobrenatural no convierte Halloween en el centro de la trama. [Dónde verla en España](https://www.justwatch.com/es/pelicula/practicamente-magia).
- **Quédate a mi lado** (1998) — **90 puntos**. Paisaje, vestuario, vida familiar y una melancolía decisiva. [Dónde verla en España](https://www.justwatch.com/es/pelicula/stepmom).
- **Sólo el cielo lo sabe** (1955) — **90 puntos**. Un otoño dominante en la Nueva Inglaterra suburbana. [Dónde verla en España](https://www.justwatch.com/es/pelicula/solo-el-cielo-lo-sabe).
- **Tienes un e-mail** (1998) — **90 puntos**. Nueva York, librerías, ropa de entretiempo y romance. [Dónde verla en España](https://www.justwatch.com/es/pelicula/tienes-un-e-mail).
