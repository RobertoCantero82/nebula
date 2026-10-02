---
imagenPortada: "/nebula/imagenes/google_datos_portada.png"
titulo: "Google quiere llevar la IA al espacio: el problema son 1.800 lanzamientos"
descripcion: "Project Suncatcher ya ha enviado una TPU a órbita, pero convertir el experimento en un centro de datos exige una cadencia de Starship difícil de imaginar."
tema: "TECNOLOGÍA"
fecha: 2026-10-02
cifraDestacada: "1.800 vuelos"
etiquetaCifra: "de Starship durante una década para acercar el lanzamiento a 200 dólares por kilogramo"
metodologia: "Análisis de escenarios basado en las estimaciones públicas de Google Research, contrastadas con los 14 vuelos integrados de Starship realizados hasta septiembre de 2026. Se estudian la cadencia anual, la carga útil y la reducción del coste por kilogramo. Los escenarios muestran condiciones necesarias, no probabilidades estadísticas."
---

*Google ya ha enviado uno de sus chips de inteligencia artificial al espacio. El experimento quiere demostrar que una TPU puede trabajar en órbita, alimentada por el Sol y sometida a radiación, vacío y cambios extremos de temperatura. Es un primer paso real. Sin embargo, el salto entre encender un chip durante unos minutos y construir un centro de datos espacial se mide en miles de cohetes.*

El proyecto se llama **[Suncatcher](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/)**. Google imagina grupos de 81 satélites situados a unos 650 kilómetros de altura, conectados mediante enlaces láser y volando a pocos cientos de metros unos de otros. Cada aparato llevaría varios chips y paneles solares. Juntos podrían repartir cargas de inteligencia artificial como hacen los servidores de un centro de datos terrestre.

<div style="position: relative; width: 100%; aspect-ratio: 16 / 9; margin: 2rem 0; overflow: hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/8NPgswgbTnE?cc_load_policy=1&cc_lang_pref=es&hl=es"
    title="Vídeo sobre los centros de datos espaciales de Google"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;"
  ></iframe>
</div>

La propuesta tiene una **ventaja** atractiva. En la órbita adecuada, **un panel puede producir hasta ocho veces más energía que en la Tierra** y recibir luz casi continuamente. No necesita suelo, grandes conexiones eléctricas ni millones de litros de agua. Pero la abundancia de energía no resuelve el transporte, la refrigeración ni el mantenimiento.

## La cuenta detrás del titular

El [análisis de Google Research](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) sitúa el punto de competitividad cerca de **200 dólares por kilogramo** a mediados de la década de 2030. Un reciente artículo en el medio TechCrunch tradujo esa curva de costes a una escala más fácil de visualizar: Starship tendría que colocar unas **370.000 toneladas en órbita** mediante aproximadamente **1.800 lanzamientos en diez años**.

La cifra fue corregida después de publicarse: el titular inicial decía 1.600. Incluso 1.800 es un redondeo optimista. Si cada vuelo transportara 200 toneladas, el total sería de 360.000. Para llegar exactamente a 370.000 harían falta 1.850 misiones, o una carga media de 205,6 toneladas.

La utilización real importa mucho. Con 150 toneladas por misión serían necesarios 2.467 vuelos. Con 100 toneladas, 3.700. Starship no solo tendría que volar a menudo: tendría que hacerlo cargada casi al máximo.

## De cinco vuelos al año a más de dos al día

El contraste con la historia reciente es enorme. Starship ha realizado 14 vuelos integrados desde 2023. Su récord anual es de cinco misiones y solo [alcanzó la órbita en septiembre de 2026](/nebula/articulos/starship-de-prototipo-a-orbita/).

Una media de 180 lanzamientos anuales tampoco explica toda la dificultad. Si la década comienza con cinco vuelos y la actividad crece de forma constante, la cadencia tendría que aumentar alrededor de un **75% cada año**. La trayectoria acabaría con unos **775 lanzamientos en 2035**, algo más de dos diarios.

<div class="grafico-interactivo">
  <canvas id="grafico-escenarios-suncatcher" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-escenarios-suncatcher');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Conservador', 'Central', 'Umbral matemático', 'Acelerado'],
        datasets: [{
          label: 'Lanzamientos acumulados entre 2026 y 2035',
          data: [349, 814, 1800, 1938],
          backgroundColor: ['#AAB2C3', '#446DDF', '#D89B30', '#54A24B'],
        }],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => `${context.parsed.y.toLocaleString('es-ES')} lanzamientos`,
            },
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 2000,
            title: { display: true, text: 'Lanzamientos acumulados' },
          },
        },
      },
    });
  });
</script>

Mi escenario central ya supone un crecimiento anual del 60% y capacidad para realizar 250 vuelos en un año. Aun así, termina con **814 lanzamientos**, menos de la mitad del objetivo. Solo las trayectorias extremas alcanzan la cifra de Google.

## Un satélite todavía no es un centro de datos

El prototipo actual suministra alrededor de un kilovatio a la TPU y la activará en intervalos de quince minutos para no sobrecargar la energía ni el sistema térmico. Es suficiente para comprobar errores, pero está muy lejos de entrenar un gran modelo.

El siguiente ensayo, previsto para 2027, conectará dos satélites mediante láser. Google ya ha conseguido 1,6 terabits por segundo en una prueba terrestre, aunque **un centro de datos necesitaría enlaces de decenas de terabits** y una puntería extraordinaria entre objetos que se desplazan a gran velocidad.

También queda el calor. En el vacío no existe aire que lo arrastre; debe salir mediante radiadores. A eso se añaden la radiación, las reparaciones imposibles y la renovación de unos chips que envejecen mucho más deprisa que un satélite.

## La predicción más razonable

Antes de 2036 probablemente veremos pequeños grupos orbitales capaces de ejecutar tareas especializadas: procesar imágenes de la Tierra, filtrar datos científicos o realizar inferencias cerca de los sensores. Es mucho menos probable que compitan de forma general con los grandes centros terrestres.

<div style="position: relative; width: 100%; aspect-ratio: 16 / 9; margin: 2rem 0; overflow: hidden;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/EthkNLasUa8?cc_load_policy=1&cc_lang_pref=es&hl=es"
    title="Vídeo sobre Project Suncatcher y la computación espacial"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;"
  ></iframe>
</div>

La predicción cambiará si Starship supera tres pruebas: reutilización rápida, más de cien vuelos anuales y un coste verificable próximo a 200 dólares por kilogramo. Hasta entonces, **Suncatcher es un experimento serio construido sobre una infraestructura que todavía no existe a la escala necesaria**.

Puedes reproducir los escenarios, modificar la carga útil y revisar todas las hipótesis en el [notebook de Jupyter del análisis de los centros de datos orbitales](/nebula/analisis/analisis-centros-datos-orbitales.ipynb).

Fuentes: [Google Research](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/), [actualización de Project Suncatcher](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) y [TechCrunch](https://techcrunch.com/2026/10/01/google-thinks-spacexs-starship-has-to-launch-1600-times-before-space-data-centers-get-off-the-ground/).
