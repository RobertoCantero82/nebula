---
imagenPortada: "/nebula/imagenes/bolanegra_portada.png"
titulo: "¿Llegará 'La bola negra a los Oscar? Mi modelo le da muchas opciones de entrar en la preselección"
tema: "CINE"
fecha: 2026-09-21
cifraDestacada: "74,7 %"
etiquetaCifra: "probabilidad estimada de alcanzar la preselección"
metodologia: "Modelo de machine learning basado en 1.264 candidaturas al Oscar internacional de las ediciones 84 a 98. Se utilizó una regresión logística con historial reciente del país y premios en Cannes, validación temporal y 500 remuestreos para estimar la incertidumbre."
---

*La película de Javier Calvo y Javier Ambrossi podría representar a España en los Oscar 2027 después de triunfar en Cannes y conquistar el premio del público de Toronto. Un modelo entrenado con 1.264 candidaturas internacionales estima que tiene un 74,7 % de probabilidades de superar el primer corte y un 62 % de conseguir la nominación.*

*La bola negra* ya ha superado la primera votación de su carrera hacia Hollywood. La Academia de Cine la ha elegido para representar a España en la categoría de mejor película internacional de los Oscar 2027. La decisión llega después de que Javier Calvo y Javier Ambrossi recibieran, *ex aequo*, el premio a mejor dirección en Cannes y de que la película ganara el premio del público en el Festival de Toronto. ([RTVE](https://www.rtve.es/noticias/20260916/oscar-2027-directo-anuncio-pelicula-espanola/17226149.shtml), [Festival de Cannes](https://www.festival-cannes.com/en/press/press-releases/the-79th-festival-de-cannes-winners-list/), [El País](https://elpais.com/cultura/2026-09-20/la-bola-negra-se-alza-con-el-premio-del-publico-en-el-festival-de-toronto.html))

Pero representar a un país no equivale a estar nominada. Antes deberá entrar en la preselección de la Academia estadounidense y, después, conseguir una de las cinco plazas finales. La pregunta es inevitable: **¿hasta dónde puede llegar?**

Para intentar responderla he construido un modelo de machine learning con las películas presentadas al Oscar internacional durante las últimas quince ediciones. El resultado sitúa a *La bola negra* como una candidata fuerte: **un 74,7 % de probabilidades de alcanzar la preselección y un 62 % de obtener la nominación**.

Son cifras llamativas, pero no certezas. Los intervalos de incertidumbre son amplios y el modelo depende mucho de una señal concreta: el premio de Cannes.

## Quince ediciones y 1.264 candidaturas

El conjunto de datos que he utilizado reúne 1.264 películas presentadas entre las ediciones 84 y 98 de los Oscar. La información sobre candidaturas, preselecciones, nominaciones y victorias procede de la [base de datos oficial de los Premios Oscar](https://awardsdatabase.oscars.org/).

De todas esas películas, 172 alcanzaron la preselección y solo 75 consiguieron una nominación. En términos porcentuales, una candidatura promedio tuvo un **13,6 %** de posibilidades de superar el primer corte y un **5,9 %** de llegar a la nominación.

Ese desequilibrio importa. Un modelo que afirme que ninguna película va a ser nominada acertaría el 94,1 % de las veces, pero no serviría para descubrir una sola candidata. Por eso **no basta con medir cuántos resultados acierta**, sino que también hay que comprobar si reconoce los pocos casos positivos.

El primer modelo ha utilizado tres datos disponibles antes de cada edición:

- El país que presenta la película.
- Las nominaciones obtenidas por ese país durante los diez años anteriores.
- Sus victorias durante el mismo periodo.

La trayectoria nacional sí contiene información. Las películas nominadas procedían de países que acumulaban una media de 1,40 nominaciones durante la década anterior, frente a las 0,51 de las no nominadas. Aun así, el historial del país por sí solo producía demasiadas falsas alarmas.

## Cannes cambia la predicción

El siguiente paso fue incorporar los premios de la competición principal de Cannes. Para hacerlo recopilé 141 registros del palmarés oficial entre 2011 y 2025 y corregí las diferencias entre títulos originales e internacionales. Así aparecieron 54 películas premiadas en Cannes que posteriormente representaron a sus países en los Oscar.

El patrón es muy fuerte: **38 de esas 54 películas alcanzaron la preselección y 26 fueron nominadas**. Es decir, el 70,4 % y el 48,1 %, respectivamente.

La relación no demuestra que Cannes cause el éxito posterior. Una película premiada en el festival francés puede contar también con mayor calidad, distribución internacional, atención mediática o capacidad para financiar una campaña. Sin embargo, el galardón funciona como una señal que resume parte de esas ventajas.

Al añadir esta variable, la capacidad del modelo para ordenar las candidaturas mejoró. En la predicción de la nominación, el área bajo la curva ROC pasó de 0,699 a 0,848. Esto significa, hablando de manera simple, que si el modelo recibe una película nominada y otra que no lo fue, asigna una puntuación superior a la primera, aproximadamente en el 85 % de las comparaciones.

En mi caso, el modelo utilizado es una regresión logística. No es una red neuronal ni una caja negra de cientos de capas, sino un algoritmo más sencillo e interpretable. En esta ocasión es una ventaja,ya que permite comprobar qué variables empujan cada resultado y detectar cuándo una predicción depende demasiado de una sola de ellas.

## Porcentajes para ilusionarse con las opciones de _La bola negra_

Para calcular la predicción final entrené el modelo con todo el historial disponible. El registro de *La bola negra* incluye el premio de Cannes y la trayectoria reciente de España: tres nominaciones y ninguna victoria durante las diez ediciones anteriores.

El resultado central es el siguiente:

- **Probabilidad de alcanzar la preselección: 74,7 %.**
- **Probabilidad de conseguir la nominación: 62 %.**

<div class="grafico-interactivo">
  <canvas id="grafico-prediccion-bola-negra" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-prediccion-bola-negra');
    if (!ctx || !window.Chart) return;
    const intervalos = ['44,6 % – 92,9 %', '31,8 % – 82,2 %'];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Preselección', 'Nominación'],
        datasets: [
          {
            label: 'Frecuencia histórica',
            data: [13.6, 5.9],
            backgroundColor: '#B8BEC9',
          },
          {
            label: 'Estimación para La bola negra',
            data: [74.7, 62.0],
            backgroundColor: '#446DDF',
          },
        ],
      },
      options: {
        responsive: true,
        interaction: { mode: 'index', intersect: false },
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            title: { display: true, text: 'Probabilidad estimada (%)' },
          },
        },
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              afterLabel: (context) => context.datasetIndex === 1
                ? `Intervalo del 95 %: ${intervalos[context.dataIndex]}`
                : '',
            },
          },
        },
      },
    });
  });
</script>

Los porcentajes están muy por encima de la frecuencia histórica, pero el margen de incertidumbre obliga a rebajar cualquier lectura triunfalista. Al repetir el entrenamiento 500 veces con distintas muestras de ediciones, el intervalo del 95 % para la preselección se situó entre el **44,6 % y el 92,9 %**. Para la nominación fue del **31,8 % al 82,2 %**.

La señal favorable se mantiene, pero su intensidad varía considerablemente. El modelo dice que la película tiene un perfil competitivo, pero no que su nominación esté asegurada.

## ¿Qué ocurriría sin Cannes?

La forma más directa de entender el resultado es repetir la predicción manteniendo España y su historial, pero retirando el premio de Cannes. En ese escenario, la probabilidad de entrar en la preselección cae del 74,7 % al **16,8 %**. La de conseguir la nominación baja del 62 % al **8,5 %**. El efecto asociado a Cannes es de 57,9 y 53,5 puntos porcentuales, respectivamente.

<div class="grafico-interactivo">
  <canvas id="grafico-impacto-cannes" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-impacto-cannes');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Preselección', 'Nominación'],
        datasets: [
          {
            label: 'Frecuencia histórica',
            data: [13.6, 5.9],
            backgroundColor: '#B8BEC9',
          },
          {
            label: 'La bola negra sin Cannes',
            data: [16.8, 8.5],
            backgroundColor: '#D8B98E',
          },
          {
            label: 'La bola negra con Cannes',
            data: [74.7, 62.0],
            backgroundColor: '#446DDF',
          },
        ],
      },
      options: {
        responsive: true,
        interaction: { mode: 'index', intersect: false },
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            title: { display: true, text: 'Probabilidad estimada (%)' },
          },
        },
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              label: (context) => `${context.dataset.label}: ${context.parsed.y.toFixed(1)} %`,
            },
          },
        },
      },
    });
  });
</script>

El ejercicio no significa que un premio produzca por sí mismo semejante aumento. Es una comparación dentro del modelo: muestra cómo cambia su respuesta cuando se modifica una única variable. También expone su principal debilidad. Una parte enorme de la predicción descansa sobre una señal que solo aparece en 54 de las 1.264 películas analizadas y que agrupa galardones de distinta naturaleza.

## El triunfo en Toronto queda fuera del modelo

El premio del público de Toronto refuerza el relato de una película que llega a la carrera con visibilidad internacional y apoyo de la audiencia. Sin embargo, decidí no introducirlo en el cálculo. Al cruzar los ganadores históricos del premio principal de TIFF con las candidaturas al Oscar internacional solo apareció un precedente comparable dentro del periodo analizado: *Where Do We Go Now?*, la representante de Líbano en la edición 84. No alcanzó la preselección.

Un único caso no permite aprender una relación fiable. Si se añadiera la variable, el algoritmo podría interpretar de forma absurda que ganar en Toronto es una señal negativa. El galardón de *La bola negra* es periodísticamente relevante, pero no existe una muestra histórica suficiente para convertirlo en evidencia estadística.

**Esta exclusión también evita contaminar la predicción** con la propia noticia que queremos analizar. El 74,7 % y el 62 % proceden del historial de España y de Cannes, no del reciente triunfo en Toronto.

## Qué puede decir el modelo y qué no

El análisis reproduce una situación real: utiliza el pasado para evaluar ediciones posteriores. Los modelos se entrenaron inicialmente con las ediciones 84 a 95 y se probaron con las ediciones 96 a 98, que permanecieron separadas durante la evaluación.

Para calcular porcentajes se emplearon versiones sin pesos artificiales entre las clases. Su calibración fue considerablemente mejor: en el modelo de nominación, la probabilidad media estimada fue del 6,5 %, muy próxima al 5,8 % observado realmente en el periodo de prueba.

Aun así, **faltan variables capaces de cambiar la carrera**:

- La campaña y la distribución en Estados Unidos.
- La recepción de la crítica durante los próximos meses.
- Las nominaciones en otros premios de la temporada.
- La competencia concreta de la edición 99.
- Las preferencias de los votantes y cualquier cambio en las reglas.

**El modelo tampoco puntúa la calidad artística ni pretende anticipar una decisión individual**. Busca patrones en resultados anteriores y calcula cuánto se parece la candidatura actual a otras que tuvieron éxito.

## Una favorita, no una nominada segura

Los datos colocan a *La bola negra* en una posición excepcional. España llega con tres nominaciones en la última década, Cannes ha premiado a sus directores y Toronto acaba de confirmar su conexión con el público. Pocas candidaturas comienzan la carrera con una combinación semejante.

El modelo traduce ese impulso en un 74,7 % de opciones de alcanzar la preselección y un 62 % de conseguir la nominación. Pero también ofrece la advertencia que debería acompañar a cualquier predicción: cuando el intervalo es ancho y una sola variable explica gran parte del resultado, el porcentaje central cuenta solo una parte de la historia.

***La bola negra* es una candidata fuerte**. La estadística permite explicar por qué. Decidir si llegará hasta la ceremonia sigue estando en manos de los votantes.

---

### Metodología

- **Muestra:** 1.264 películas presentadas al Oscar a mejor película internacional en las ediciones 84 a 98.
- **Objetivos:** entrada en la preselección y nominación final.
- **Variables finales:** país, nominaciones y victorias del país durante los diez años anteriores, y premio en la competición principal de Cannes.
- **Algoritmo:** regresión logística con codificación del país y estandarización de las variables numéricas.
- **Evaluación:** división temporal; ediciones 84-95 para entrenamiento y 96-98 para prueba.
- **Incertidumbre:** 500 remuestreos por ediciones completas.
- **Código y resultados:** elaborados en Python con pandas, scikit-learn y matplotlib.
