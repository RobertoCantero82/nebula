---
titulo: "Microsoft quiere ejecutar la IA en tu ordenador. El problema es el ordenador"
descripcion: "Los AI PC se multiplican, pero muchos no alcanzan el nivel exigido por Copilot+. Analizamos las cifras detrás de la nueva estrategia de Windows."
tema: "INTELIGENCIA ARTIFICIAL"
fecha: 2026-10-08T09:00:00+02:00
imagenPortada: "/nebula/imagenes/microsoft_inteligencia_hibrida_portada.png"
cifraDestacada: "91%"
etiquetaCifra: "de los AI PC analizados en Europa no alcanzaba la categoría Copilot+"
metodologia: "Análisis exploratorio de cifras publicadas por Gartner, Omdia, CONTEXT, Microsoft y medios especializados. Se comparan cuotas, revisiones de previsiones y requisitos técnicos. No se entrena ningún modelo ni se crea una predicción propia. Algunas cifras describen mercados, fechas y definiciones diferentes, por lo que no deben leerse como una única serie temporal."
---

*Microsoft quiere que Windows reparta el trabajo de la inteligencia artificial entre el ordenador y la nube. La idea suena sencilla: hacer en local lo que conviene por rapidez o privacidad y pedir ayuda a internet cuando la tarea exige más potencia. Los datos muestran, sin embargo, que hoy existen varios significados distintos para “PC con IA”.*

Este artículo es un **análisis exploratorio de datos (EDA)**. No intenta adivinar cuántos ordenadores se venderán. Compara cifras ya publicadas para entender dónde está el mercado y qué significa realmente el nuevo hardware presentado por Microsoft.

## Un Windows con dos motores

En su reciente evento de octubre, Microsoft presentó la llamada **inteligencia híbrida**. Windows podrá combinar modelos que funcionan dentro del equipo con servicios alojados en la nube. También anunció acciones desde la búsqueda, agentes capaces de completar tareas y contenedores aislados para ejecutar esos procesos con más seguridad.

<div style="position:relative; width:100%; aspect-ratio:16/9; margin:2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/fm6VQgCkj20"
    title="Presentación de la inteligencia híbrida de Microsoft"
    style="position:absolute; inset:0; width:100%; height:100%; border:0;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

El ejemplo más llamativo es el **Surface Laptop Ultra**. Su configuración más potente incorpora hasta 128 GB de memoria unificada y Microsoft afirma que puede ejecutar en local modelos de más de 120.000 millones de parámetros. Su precio parte de 2.599,99 dólares. La empresa también enseñó el **RTX Spark Dev Box**, una estación de 5.999,99 dólares orientada a desarrolladores.

Son equipos importantes, pero no representan al ordenador medio. Ahí aparece el primer problema: “AI PC” es una etiqueta muy amplia.

## La etiqueta crece más deprisa que la capacidad

Las estimaciones recopiladas sitúan los AI PC en el **17% del mercado mundial en 2024** y en el **31% en 2025**. En Estados Unidos, Omdia calculó una cuota del **48,3% en el segundo trimestre de 2026**. Esta última cifra no se puede unir sin más a las anteriores, porque describe otro territorio y otro momento, pero sí confirma que la etiqueta se está extendiendo.

Eso no significa que todos esos equipos puedan ofrecer la misma experiencia. En la distribución profesional europea, CONTEXT contabilizó 1,2 millones de AI PC durante el segundo trimestre de 2025. Solo el **9%** cumplía el requisito de 40 TOPS usado para la categoría Copilot+ de Microsoft. TOPS mide cuántas operaciones sencillas puede hacer por segundo el procesador dedicado a IA.

En otras palabras: un ordenador puede venderse como preparado para IA y quedarse lejos tanto de Copilot+ como de una máquina capaz de mover un modelo enorme en local.

<div class="grafico-interactivo">
  <canvas id="grafico-revision-ai-pc" height="300" role="img" aria-label="Gartner redujo su previsión mundial de cuota de AI PC para 2025 del 43 al 31 por ciento y para 2026 del 55 al 49 por ciento."></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-revision-ai-pc');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['2025', '2026'],
        datasets: [
          { label: 'Previsión inicial', data: [43, 55], backgroundColor: '#8B85C4', borderRadius: 3 },
          { label: 'Previsión revisada', data: [31, 49], backgroundColor: '#D85A30', borderRadius: 3 }
        ]
      },
      options: {
        responsive: true,
        plugins: { legend: { position: 'bottom' } },
        scales: { y: { beginAtZero: true, max: 60, title: { display: true, text: 'Cuota mundial prevista (%)' } } }
      }
    });
  });
</script>

*Revisión de Gartner de sus previsiones mundiales: doce puntos menos para 2025 y seis menos para 2026.*

## Las previsiones también cambian

[Gartner esperaba inicialmente](https://www.gartner.com/en/newsroom/press-releases/2024-09-25-gartner-forecasts-worldwide-shipments-of-artificial-intelligence-pcs-to-account-for-43-percent-of-all-pcs-in-2025) que los AI PC alcanzaran el 43% del mercado mundial en 2025. [Después redujo la cifra al 31%](https://www.gartner.com/en/newsroom/press-releases/2025-08-28-gartner-says-artificial-intelligence-pcs-will-represent-31-percent-of-worldwide-pc-market-by-the-end-of-2025). Para 2026 bajó su cálculo del 55% al 49%. No es un detalle pequeño: demuestra que incluso una tendencia clara puede avanzar más despacio de lo esperado.

Las diferencias crecen cuando miramos a 2028. Una [estimación de Morgan Stanley](https://advisor.morganstanley.com/the-wbs-group/documents/field/w/wb/wbs-group/Q2_2024_Commentary.pdf) sitúa la cuota en el 64%, mientras que [una cifra de IDC citada por ITPro](https://www.itpro.com/hardware/global-pc-shipments-surge-in-q3-2025-fueled-by-ai-and-windows-10-refresh-cycles) llega al 93%. Hay **29 puntos de distancia** entre ambas. No conviene escoger la cifra más alta y presentarla como destino inevitable. Son escenarios construidos con supuestos distintos.

## Qué cambia para el consumidor normal

La propuesta híbrida tiene sentido. Una tarea local puede responder rápido, funcionar sin conexión y mantener datos sensibles dentro del ordenador. La nube permite usar modelos mayores sin comprar una estación de miles de dólares. Windows intentará elegir entre ambos caminos.

Pero el comprador debe mirar algo más que la pegatina. La NPU, la memoria y el consumo importan; también importa saber qué aplicaciones aprovechan de verdad ese hardware. Comprar hoy un AI PC no garantiza ejecutar los modelos mostrados en el Surface Laptop Ultra.

La conclusión del EDA es sencilla: **el nombre “AI PC” se normalizará antes que una capacidad común para todos esos equipos**. Microsoft está enseñando hacia dónde quiere llevar Windows. El mercado todavía reúne bajo la misma etiqueta máquinas muy distintas.

Puedes revisar las cifras, las fuentes y todos los pasos en el [notebook de Jupyter del análisis](/nebula/analisis/microsoft-inteligencia-hibrida/eda_inteligencia_hibrida.ipynb). También está disponible el [paquete reproducible con el cuaderno y los datos](/nebula/analisis/microsoft-inteligencia-hibrida/microsoft-inteligencia-hibrida-eda.zip).

Fuentes principales: [Microsoft](https://news.microsoft.com/source/latam/noticias-de-microsoft/windows-inteligencia-hibrida/), [Omdia](https://omdia.tech.informa.com/pr/2026/sep/us-pc-shipments-grew-1point0percent-in-2q26-while-full-year-market-forecast-to-decline-10point7-percent), [Ars Technica](https://arstechnica.com/gadgets/2026/10/microsoft-event-debuts-new-ai-friendly-hardware-and-windows-changes/) y [TechRadar, con datos de CONTEXT](https://www.techradar.com/pro/ai-pcs-are-here-but-businesses-arent-exactly-rushing-to-buy-them-just-yet).
