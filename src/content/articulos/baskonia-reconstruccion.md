---
titulo: "Baskonia cambia medio equipo cada verano, pero los datos señalan otro problema"
tema: "BALONCESTO"
fecha: 2026-09-18
cifraDestacada: "51,3%"
etiquetaCifra: "porcentaje medio de la anotación anterior que Baskonia pierde cada verano"
metodologia: "Análisis de las estadísticas oficiales de la Euroliga entre las temporadas 2016-17 y 2025-26. Se estudiaron 153 registros de jugadores, nueve transiciones de plantilla y los resultados finales de diez fases regulares. La continuidad se midió como el porcentaje de puntos de una temporada producido por jugadores que no aparecieron en la plantilla del curso siguiente. Las correlaciones describen asociaciones y no demuestran causalidad."
---

El Baskonia lleva años conviviendo con una certeza incómoda: cuando encuentra talento, conservarlo resulta difícil. Shane Larkin, Vincent Poirier, Tornike Shengelia o Wade Baldwin son algunos de los nombres que abandonaron Vitoria después de liderar al equipo. La sensación es conocida por cualquier aficionado: cada verano toca empezar otra vez. Pero ¿esa reconstrucción permanente explica realmente la pérdida de competitividad del club en la Euroliga?

He analizado las diez temporadas disputadas desde el cambio de formato de 2016-17 hasta 2025-26. El resultado confirma la magnitud de la rotación, pero también desmonta su explicación más evidente. **Baskonia pierde de media el 51,3% de los puntos producidos por la plantilla anterior cada verano**, aunque esa fuga no presenta una relación clara con el porcentaje de victorias de la temporada siguiente.

## 1. La reconstrucción permanente sí existe

En cuatro de las nueve transiciones analizadas desapareció más de la mitad de la producción anotadora. El caso más extremo llegó en el verano de 2020: los jugadores que salieron habían generado el 66,3% de los puntos del curso anterior. Un año después volvió a ocurrir casi lo mismo, con una pérdida del 65,7%.

Solo la plantilla de 2018-19 conservó más de dos tercios de la anotación previa. En el resto de los casos, Baskonia tuvo que reemplazar entre el 44% y el 66% de los puntos. La rotación tampoco afecta únicamente a jugadores secundarios. El máximo anotador dejó el club en cinco de las nueve transiciones, el 55,6% del total.

<div class="grafico-interactivo">
  <canvas id="grafico-produccion-perdida" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-produccion-perdida');
    if (!ctx || !window.Chart) return;
    const perdidos = [60.78, 27.06, 49.84, 66.25, 65.69, 52.86, 44.52, 45.32, 49.20];
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26'],
        datasets: [
          { label: 'Puntos retenidos', data: perdidos.map(v => 100 - v), backgroundColor: '#446ddf' },
          { label: 'Puntos perdidos', data: perdidos, backgroundColor: '#D85A30' },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: { stacked: true },
          y: { stacked: true, min: 0, max: 100, title: { display: true, text: '% de los puntos del curso anterior' } },
        },
        plugins: { legend: { position: 'bottom' } },
      },
    });
  });
</script>

El ejemplo más reconocible es el de Shengelia. En 2019-20 concentró el 21,6% de la anotación y se marchó al terminar el curso. Sin embargo, Baskonia pasó de ganar el 42,9% de sus partidos a alcanzar el 52,9% en 2020-21. La pérdida de la estrella no impidió que el equipo mejorara.

## 2. Perder al líder no cambia las victorias

Las temporadas en las que continuó el máximo anotador anterior terminaron con un 46,7% de victorias de media. Cuando se marchó, el promedio fue del 47,3%. La diferencia, apenas medio punto porcentual, es demasiado pequeña para sostener que conservar al referente garantice mejores resultados.

La comparación de toda la producción ofrece la misma respuesta. La correlación entre el porcentaje de puntos perdidos y el porcentaje de victorias es de 0,078, prácticamente cero. Baskonia ha ganado y perdido con niveles de renovación muy parecidos. En 2020-21 reemplazó dos tercios de la anotación y consiguió 18 victorias. En 2021-22 afrontó una reconstrucción casi idéntica y solo logró 12.

Esto no convierte la rotación en algo irrelevante. Reconstruir cada verano obliga a acertar repetidamente en los fichajes, dificulta consolidar automatismos y aumenta el riesgo. Los datos indican, sin embargo, que el club ha sido capaz de reemplazar suficiente producción como para que la fuga de talento no determine por sí sola su balance final.

## 3. El verdadero límite aparece al otro lado de la pista

La anotación tampoco explica las victorias. Su correlación con el porcentaje de triunfos vuelve a ser de 0,078. La temporada 2025-26 es el mejor ejemplo: Baskonia firmó su mayor media ofensiva del periodo, 87,4 puntos, pero terminó con 13 victorias, 25 derrotas y la 18.ª posición.

El problema estaba en los 91,7 puntos recibidos por partido. La diferencia entre anotación y puntos encajados cayó hasta -4,3, el peor registro de las diez temporadas. Esa diferencia presenta una correlación de 0,863 con el porcentaje de victorias, muy superior a la continuidad, la anotación o la permanencia del líder.

<div class="grafico-interactivo">
  <canvas id="grafico-diferencia" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-diferencia');
    if (!ctx || !window.Chart) return;
    const diferencias = [2.30, 3.80, 2.37, -3.43, 3.62, -2.50, 2.44, -0.53, -1.03, -4.26];
    new Chart(ctx, {
      data: {
        labels: ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25', '2025-26'],
        datasets: [
          {
            type: 'bar',
            label: 'Diferencia de puntos por partido',
            data: diferencias,
            backgroundColor: diferencias.map(v => v >= 0 ? '#446ddf' : '#D85A30'),
            yAxisID: 'y',
          },
          {
            type: 'line',
            label: 'Victorias (%)',
            data: [56.67, 53.33, 50.00, 42.86, 52.94, 42.86, 52.94, 52.94, 41.18, 34.21],
            borderColor: '#1B1836',
            backgroundColor: '#1B1836',
            tension: 0.2,
            yAxisID: 'y1',
          },
        ],
      },
      options: {
        responsive: true,
        interaction: { mode: 'index', intersect: false },
        scales: {
          y: { position: 'left', title: { display: true, text: 'Diferencia de puntos' } },
          y1: { position: 'right', min: 0, max: 70, title: { display: true, text: 'Victorias (%)' }, grid: { drawOnChartArea: false } },
        },
        plugins: { legend: { position: 'bottom' } },
      },
    });
  });
</script>

Las cinco temporadas con diferencia positiva acabaron con al menos un 50% de victorias. Las cuatro que bajaron de -1 punto quedaron por debajo del 43%. El patrón no demuestra por sí solo qué decisiones deportivas causaron el deterioro, pero sí sitúa el problema: **Baskonia no dejó de competir porque anotara poco ni porque cambiara demasiados jugadores, sino porque perdió el equilibrio entre lo que producía y lo que concedía**.

## Conclusión

Los datos confirman la intuición del aficionado y corrigen su diagnóstico. Baskonia vive en una reconstrucción permanente, pierde a su máximo anotador más de la mitad de los veranos y reemplaza, de media, uno de cada dos puntos. Aun así, esa inestabilidad no explica sus victorias.

La capacidad histórica del club para detectar y desarrollar talento ha compensado muchas salidas. El límite aparece cuando esa reinvención produce equipos capaces de anotar, pero no de contener al rival. El reto no consiste únicamente en conservar estrellas. Consiste en reconstruir sin perder el equilibrio.
