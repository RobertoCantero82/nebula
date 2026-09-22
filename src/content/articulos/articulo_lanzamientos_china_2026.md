---
imagenPortada: "/nebula/imagenes/lanzamientoschina_portada.png"
titulo: "China lanza cuatro cohetes en 45 horas: analizo los datos para saber si el país va camino de un récord"
tema: "TECNOLOGÍA"
fecha: 2026-09-22
cifraDestacada: "110"
etiquetaCifra: "lanzamientos estimados para China en 2026"
metodologia: "Análisis de 802 lanzamientos orbitales realizados desde bases chinas entre 1970 y el 20 de septiembre de 2026. La predicción combina el ritmo observado durante el año, la distribución histórica de lanzamientos antes y después de esa fecha, validación retrospectiva y 10.000 simulaciones."
---

*China ha puesto en órbita cuatro cohetes diferentes en apenas 45 horas. El evento parece excepcional, pero los datos muestran que forma parte de una aceleración mucho mayor: el país podría terminar 2026 superando ampliamente su récord del año pasado.*

Cuatro cohetes, tres bases de lanzamiento y menos de dos días. Entre el 15 y el 17 de septiembre, China lanzó un Zhuque-2E, un Gravity-1, un Long March 12 y un Kuaizhou-11. Todos completaron sus misiones con éxito y dos de los vehículos pertenecían a compañías privadas.

La secuencia, recogida por [Space.com](https://www.space.com/space-exploration/launches-spacecraft/china-launches-4-different-rockets-to-orbit-in-45-hours-video), sirve como una fotografía bastante espectacular del momento que atraviesa el sector espacial chino. Sin embargo, una racha aislada no demuestra que un país esté acelerando realmente sus lanzamientos.

Para comprobarlo he analizado los registros históricos de [Launch Library 2](https://thespacedevs.com/llapi), una base de datos abierta especializada en misiones espaciales. El resultado confirma que **China** no solo lanza más cohetes: también **ha reducido drásticamente el tiempo que transcurre entre ellos**.

## Cuatro misiones completamente diferentes

La primera misión comenzó el 15 de septiembre a las 06:26 UTC. LandSpace lanzó desde Jiuquan un Zhuque-2E con diez satélites de la constelación Qianfan. Quince horas después, un Gravity-1 de Orienspace despegó desde una plataforma marítima. El 17 de septiembre llegaron las otras dos misiones: un Long March 12 salió desde Wenchang y un Kuaizhou-11 lo hizo desde Jiuquan apenas dos horas más tarde.

Desde el primer despegue hasta el último transcurrieron **44 horas y 14 minutos**. La cifra iguala el máximo histórico de cuatro lanzamientos chinos dentro de una ventana de 45 horas, pero esconde un detalle curioso: **no fue la secuencia más rápida**.

En **noviembre de 2025**, China completó cuatro misiones en **31 horas**. Un mes más tarde volvió a hacerlo en **menos de 30 horas**. La racha de septiembre de 2026 no es un hecho completamente nuevo, sino la tercera vez en menos de un año que el país alcanza semejante concentración de actividad.

## China ha multiplicado su ritmo de lanzamiento

El conjunto de datos reúne 802 lanzamientos realizados desde cinco bases chinas entre abril de 1970 y el 20 de septiembre de 2026. De ellos, 758 terminaron con éxito, 38 fracasaron y seis tuvieron un resultado parcialmente satisfactorio.

La transformación se aprecia especialmente durante la última década. China realizó 19 lanzamientos en 2015, superó los 60 en 2022 y alcanzó un récord de **93 misiones en 2025**.

<div class="grafico-interactivo">
  <canvas id="grafico-lanzamientos-china" height="320"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-lanzamientos-china');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          '2010', '2011', '2012', '2013', '2014', '2015',
          '2016', '2017', '2018', '2019', '2020', '2021',
          '2022', '2023', '2024', '2025', '2026'
        ],
        datasets: [
          {
            label: 'Operadores gubernamentales',
            data: [
              15, 19, 19, 15, 16, 19, 22, 17, 37,
              26, 34, 49, 55, 47, 49, 69, 45
            ],
            backgroundColor: '#C32B2B',
          },
          {
            label: 'Operadores comerciales',
            data: [
              0, 0, 0, 0, 0, 0, 0, 1, 2,
              8, 5, 6, 9, 20, 19, 24, 23
            ],
            backgroundColor: '#F2A541',
          },
        ],
      },
      options: {
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false
        },
        scales: {
          x: {
            stacked: true
          },
          y: {
            stacked: true,
            beginAtZero: true,
            title: {
              display: true,
              text: 'Lanzamientos'
            },
          },
        },
        plugins: {
          legend: {
            position: 'bottom'
          },
          tooltip: {
            callbacks: {
              afterBody: (items) => (
                items[0].dataIndex === 16
                  ? '2026: datos hasta el 20 de septiembre'
                  : ''
              ),
            },
          },
        },
      },
    });
  });
</script>

Los 68 lanzamientos de 2026 no representan un año completo. Son únicamente los registrados hasta el 20 de septiembre. A esa misma fecha, China acumulaba 56 misiones en 2025. Por tanto, **la actividad ha crecido un 21,4 %** frente al mismo periodo del año anterior.

La categoría “comercial” utilizada en los datos tampoco equivale siempre a una empresa completamente privada. Algunas compañías mantienen vínculos con corporaciones estatales. Aun así, su peso ha pasado de ser prácticamente inexistente a representar el **33,8 % de los lanzamientos de 2026**.

## Un lanzamiento cada 2,4 días

El crecimiento anual cuenta solo una parte de la historia. **Otra manera de medir la aceleración** consiste en calcular cuánto **tiempo** suele pasar **entre dos misiones consecutivas**.

En 2010, la mediana era de 15,9 días. En 2025 descendió hasta 2,6 y, durante **2026**, se ha situado en **2,4 días**. Además, este año ya se han registrado 30 ocasiones en las que dos lanzamientos estuvieron separados por un máximo de 48 horas.

<div class="grafico-interactivo">
  <canvas id="grafico-cadencia-china" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-cadencia-china');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          '2010', '2011', '2012', '2013', '2014', '2015',
          '2016', '2017', '2018', '2019', '2020', '2021',
          '2022', '2023', '2024', '2025', '2026'
        ],
        datasets: [
          {
            label: 'Mediana de días entre lanzamientos',
            data: [
              15.89, 10.32, 15.67, 9.48, 9.90, 8.94,
              13.51, 9.29, 8.84, 8.94, 7.28, 3.90,
              3.55, 4.12, 4.83, 2.58, 2.41
            ],
            borderColor: '#C32B2B',
            backgroundColor: '#F2A541',
            pointBackgroundColor: '#F2A541',
            pointRadius: 4,
            pointHoverRadius: 7,
            tension: 0.2,
          },
        ],
      },
      options: {
        responsive: true,
        interaction: {
          mode: 'nearest',
          intersect: false
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Días entre lanzamientos'
            },
          },
        },
        plugins: {
          legend: {
            position: 'bottom'
          },
          tooltip: {
            callbacks: {
              label: (context) => (
                `${context.parsed.y.toFixed(2)} días`
              ),
            },
          },
        },
      },
    });
  });
</script>

La **conclusión** es clara: **la sucesión de cuatro cohetes no fue una casualidad estadística**. Es una manifestación especialmente visible de una cadencia que lleva años aumentando.

## ¿Cuántos cohetes lanzará China en 2026?

Para estimar el cierre del año comparé qué porcentaje de los lanzamientos anuales se había completado ya el 20 de septiembre durante las cinco ediciones anteriores. Después probé el procedimiento como si todavía no conociera el resultado final de cada año.

En esa validación, el modelo se desvió una media de **2,4 lanzamientos**. Aplicado a las 68 misiones observadas en 2026, ofrece una estimación central de **110 lanzamientos**, con un intervalo del 90 % situado entre 105 y 115.

<div class="grafico-interactivo">
  <canvas id="grafico-prediccion-china" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-prediccion-china');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          '2025 completo',
          '2026 hasta el 20 de septiembre',
          'Predicción para 2026'
        ],
        datasets: [
          {
            label: 'Lanzamientos',
            data: [93, 68, 110],
            backgroundColor: [
              '#9AA3AD',
              '#F2A541',
              '#C32B2B'
            ],
          },
          {
            type: 'line',
            label: 'Récord de 2025',
            data: [93, 93, 93],
            borderColor: '#64748B',
            borderDash: [6, 5],
            pointRadius: 0,
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        interaction: {
          mode: 'index',
          intersect: false
        },
        scales: {
          y: {
            beginAtZero: true,
            suggestedMax: 120,
            title: {
              display: true,
              text: 'Lanzamientos orbitales'
            },
          },
        },
        plugins: {
          legend: {
            position: 'bottom'
          },
          tooltip: {
            callbacks: {
              afterLabel: (context) => (
                context.datasetIndex === 0 &&
                context.dataIndex === 2
                  ? 'Intervalo del 90 %: 105–115'
                  : ''
              ),
            },
          },
        },
      },
    });
  });
</script>

También utilicé un modelo mensual de series temporales como comprobación. Su predicción fue más conservadora, con 100 lanzamientos, pero cometió el doble de error al reconstruir los últimos cinco años.

En las **10.000 simulaciones realizadas**, todas superaron el récord de 93 lanzamientos y **alcanzaron al menos 100**. Esto no significa que ambos resultados estén garantizados: expresa que, bajo las condiciones históricas utilizadas por el modelo, no apareció ningún escenario que quedara por debajo.

## China ya no lanza cohetes de forma excepcional

Los datos confirman la impresión que deja la noticia. China está lanzando más cohetes y dejando cada vez menos tiempo entre misiones. Lo extraordinario ya no es completar cuatro despegues en 45 horas, sino haber convertido estas concentraciones en un fenómeno repetido.

Si mantiene el ritmo, **el país podría terminar 2026** alrededor de los **110 lanzamientos**, 17 más que su récord anterior. La cifra exacta dependerá de retrasos, fallos técnicos y cambios de calendario. Sin embargo, incluso el extremo inferior del intervalo supondría un nuevo máximo histórico.

La **carrera espacial china** ya no se explica únicamente por grandes misiones aisladas. También **se mide en frecuencia, capacidad industrial y en una infraestructura capaz de volver a lanzar apenas unas horas después**.

---

### Metodología

- **Fuente:** Launch Library 2, de The Space Devs.
- **Muestra:** 802 lanzamientos orbitales desde bases chinas entre 1970 y el 20 de septiembre de 2026.
- **Análisis:** evolución anual, resultado de las misiones, tipo de operador y tiempo entre lanzamientos.
- **Predicción principal:** proporción histórica del año completada el 20 de septiembre, utilizando como referencia 2021-2025.
- **Validación:** reconstrucción retrospectiva de los cierres anuales.
- **Incertidumbre:** 10.000 simulaciones; intervalo central del 90 %.
- **Modelo alternativo:** serie temporal mensual utilizada como contraste.
- **Código y resultados:** elaborados en Python con pandas, statsmodels, NumPy y Plotly.