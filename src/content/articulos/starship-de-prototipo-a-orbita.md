---
imagenPortada: "/nebula/imagenes/starship_portada.png"
titulo: "De explotar en el aire a desplegar 26 satélites: los datos que explican la evolución de Starship"
descripcion: "Los datos de sus 14 vuelos revelan el accidentado camino de SpaceX hasta la órbita."
tema: "TECNOLOGÍA"
fecha: 2026-09-29
cifraDestacada: "1.257 días"
etiquetaCifra: "entre el primer vuelo integrado de Starship y su llegada a órbita"
metodologia: "Análisis exploratorio de los 14 vuelos integrados de Starship y Super Heavy realizados entre abril de 2023 y septiembre de 2026. Se estudiaron diez capacidades observables a partir de los resúmenes de SpaceX y fuentes periodísticas independientes. Los hitos tienen el mismo peso y no constituyen una clasificación oficial de éxito."
---

*Starship ha alcanzado por fin la órbita terrestre. El hito parece un salto repentino, pero los datos cuentan una historia más accidentada: SpaceX necesitó 14 vuelos, tres generaciones del vehículo y numerosos retrocesos para reunir las capacidades necesarias en una misma misión.*

El 20 de abril de 2023, el primer conjunto integrado de Starship y Super Heavy despegó desde Texas. No logró separar sus etapas, comenzó a girar sin control y terminó destruido por su sistema de seguridad.

El 28 de septiembre de 2026, 1.257 días después, el [vuelo 14 alcanzó la órbita](https://x.com/SpaceX/status/2104354931595423762) y desplegó 26 satélites Starlink V3. SpaceX acortó la misión por precaución tras el apagado prematuro de un motor, pero la nave regresó de forma controlada.

Entre ambos vuelos hubo explosiones, amerizajes, capturas del booster y cambios de arquitectura. Para entender esa evolución he analizado diez capacidades: separación de etapas, llegada al espacio, ascenso completo, retorno y captura del booster, reentrada, amerizaje de la nave, despliegue de carga, reencendido espacial e inserción orbital.

Es el mismo enfoque utilizado para estudiar [la aceleración de los lanzamientos chinos](/nebula/articulos/articulo_lanzamientos_china_2026/): sustituir una impresión tecnológica por medidas que puedan compararse.

## El progreso no suele ir en línea recta

**Starship avanzó rápidamente durante sus primeras misiones**. La separación de etapas y la llegada al espacio aparecieron en el segundo vuelo. El tercero completó el ascenso de la nave y comenzó la reentrada. En el cuarto, tanto el booster como Starship regresaron de manera controlada.

El vuelo 5 añadió la primera captura de Super Heavy, el enorme propulsor que la impulsa durante el despegue, mediante los brazos de la torre. Un mes después, el sexto consiguió reencender un motor Raptor en el espacio.

Al terminar la primera generación, el programa ya había demostrado ocho de las diez capacidades estudiadas. Sin embargo, ninguna misión las había reunido todas a la vez.

<div class="grafico-interactivo">
  <canvas id="grafico-evolucion-starship" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-evolucion-starship');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          'Vuelo 1', 'Vuelo 2', 'Vuelo 3', 'Vuelo 4',
          'Vuelo 5', 'Vuelo 6', 'Vuelo 7', 'Vuelo 8',
          'Vuelo 9', 'Vuelo 10', 'Vuelo 11', 'Vuelo 12',
          'Vuelo 13', 'Vuelo 14'
        ],
        datasets: [
          {
            label: 'Hitos demostrados en el vuelo',
            data: [0, 2, 4, 6, 7, 7, 4, 4, 4, 8, 8, 6, 7, 9],
            borderColor: '#446DDF',
            backgroundColor: '#446DDF',
            tension: 0.2
          },
          {
            label: 'Hitos acumulados por el programa',
            data: [0, 2, 4, 6, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10],
            borderColor: '#D85A30',
            backgroundColor: '#D85A30',
            tension: 0.2
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'bottom' }
        },
        scales: {
          y: {
            min: 0,
            max: 10,
            ticks: { stepSize: 1 },
            title: {
              display: true,
              text: 'Hitos técnicos'
            }
          }
        }
      }
    });
  });
</script>

## El booster avanzó mientras la nave retrocedía

El estreno de V2 demuestra por qué una etiqueta simple de éxito o fracaso resulta insuficiente. Los vuelos 7 y 8 volvieron a capturar el booster, pero perdieron la nave durante el ascenso. El vuelo 9 completó ese ascenso, aunque ninguna de las dos etapas regresó de forma controlada.

**SpaceX conservaba las capacidades demostradas anteriormente, pero no conseguía repetirlas juntas**. Los tres vuelos completaron únicamente cuatro de los diez hitos analizados.

La recuperación llegó en agosto de 2025. Los vuelos 10 y 11 completaron ocho hitos cada uno y probaron por primera vez el despliegue de carga mediante ocho simuladores de satélites.

La cadencia tampoco explica por sí sola el progreso. El intervalo mediano entre lanzamientos fue de 82 días y V2 lo redujo a 58. Aun así, sus tres primeras misiones no añadieron ninguna capacidad nueva. Volar más permitió experimentar con mayor rapidez, pero no garantizó avances inmediatos.

## De los simuladores a una carga operativa

V3 debutó después de la pausa más larga de la campaña: 221 días. Su primer vuelo desplegó 20 simuladores y dos satélites modificados para fotografiar Starship. El siguiente liberó 20 Starlink V3 reales, pero en una trayectoria suborbital que los condujo de nuevo a la atmósfera.

El [vuelo 14](https://www.spacex.com/launches/starship-flight-14) convirtió finalmente esa prueba en una misión orbital. Desplegó 26 Starlink V3 operativos y añadió la última capacidad del análisis.

<div style="max-width: 560px; margin: 2rem auto;">
  <blockquote class="twitter-tweet" data-dnt="true">
    <a href="https://x.com/SpaceX/status/2104354931595423762">
      Ver la publicación de SpaceX sobre el vuelo 14 de Starship.
    </a>
  </blockquote>
</div>

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Solo siete de los catorce vuelos ampliaron la frontera técnica estudiada. Los demás repitieron capacidades, probaron configuraciones diferentes o terminaron antes de completar sus objetivos.

La llegada a órbita no elimina los problemas pendientes ni convierte a Starship en un sistema completamente reutilizable. Sí muestra algo más concreto: **el vehículo orbital surgió de acumular avances que rara vez aparecieron juntos y que, en varias ocasiones, parecieron desaparecer antes de regresar**.

**Puedes revisar los datos, reproducir los gráficos y consultar la clasificación de los hitos técnicos** en el [notebook de Jupyter del análisis de Starship](/nebula/analisis/analisis-evolucion-starship.ipynb).
