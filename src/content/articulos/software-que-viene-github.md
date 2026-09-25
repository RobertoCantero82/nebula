---
imagenPortada: "/nebula/imagenes/github_portada.png"
titulo: "El software que viene ya se está construyendo en GitHub"
descripcion: "Trece repositorios muestran el avance de los productos autoalojables, los agentes de IA y las alternativas abiertas al software de suscripción."
tema: "TECNOLOGÍA"
fecha: 2026-09-25
cifraDestacada: "9 de 13"
etiquetaCifra: "proyectos analizados que funcionan como productos autoalojables"
metodologia: "Análisis de los metadatos públicos de trece repositorios de GitHub consultados el 25 de septiembre de 2026. Las estrellas, forks, licencias y fechas proceden de la API de GitHub; las categorías de producto, autoalojamiento e inteligencia artificial son una clasificación editorial propia basada en la documentación de cada proyecto."
---

*GitHub ya no es solo el lugar donde los programadores guardan código. Una selección de trece repositorios revela algo más interesante: herramientas abiertas que quieren sustituir productos completos, devolver el control al usuario y convertir la inteligencia artificial en un sistema de trabajo. Todavía no sabemos cuáles sobrevivirán, pero juntos permiten observar hacia dónde se mueve el software.*

Una lista de repositorios puede convertirse fácilmente en una colección de enlaces sin conexión. Para evitarlo, he comparado trece proyectos que había ido guardando durante los últimos meses. Nueve ya funcionan como productos autoalojables y diez han recibido alguna actualización en los últimos 90 días.

La muestra no representa todo GitHub, pero comparte una ambición reconocible: **hacer que capacidades antes encerradas en plataformas comerciales puedan instalarse, modificarse o combinarse**.

## El repositorio se convierte en producto

[MapToPoster](https://github.com/dimartarmizi/map-to-poster) transforma cualquier lugar en un póster cartográfico listo para imprimir. [Podsync](https://github.com/mxpv/podsync) convierte canales de YouTube y Vimeo en feeds de podcast con descargas y reproducción sin conexión. [TREK](https://github.com/liketrek/TREK) reúne itinerarios, reservas, gastos y documentos en un planificador de viajes colaborativo.

No son bibliotecas que esperan a que otra persona construya algo encima. Tienen una interfaz, resuelven una necesidad comprensible y pueden utilizarse como productos. Esa diferencia importa porque acerca el código abierto a personas que no quieren inspeccionar el código: solo quieren una herramienta útil y cierto control sobre ella.

El cambio también se aprecia en la escala. [Instatic](https://github.com/corebunch/instatic) se presenta como alternativa autoalojable a Webflow, Framer y WordPress. [OpenCut](https://github.com/opencut-app/opencut) aspira a competir con los editores de vídeo comerciales mediante una aplicación para navegador, escritorio y móvil. Su nueva versión sigue en desarrollo, pero su arquitectura ya contempla plugins, automatización y un servidor para agentes de IA.

El código abierto no necesita superar inmediatamente a esos productos para resultar relevante. Basta con que se convierta en una alternativa creíble para cambiar la competencia: las plataformas cerradas ya no pueden defenderse solo con funciones, sino también con comodidad, alojamiento y soporte.

## Popularidad no significa madurez

Las estrellas ofrecen contexto, no una clasificación de calidad. Favorecen a los proyectos antiguos, a los que se dirigen a comunidades grandes y a los que han recibido atención en redes. OpenCut encabeza esta muestra, pero está reescribiendo su aplicación; proyectos menores pueden ser más estables o resolver mejor un problema específico.

El gráfico utiliza una escala logarítmica para que las diferencias sean legibles. El morado señala actividad durante los 90 días anteriores a la consulta y el gris indica que no se registró un *push* reciente.

<div class="grafico-interactivo">
  <canvas id="grafico-repos-github" height="500"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-repos-github');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          'OpenCut',
          'Multica',
          'Open Generative AI',
          'Open Source Games',
          'OpenWA',
          'TREK',
          'Hello SQL',
          'Instatic',
          'Anti-slop',
          'Podsync',
          'Sprite-gen',
          'MapToPoster',
          'Ciencia de datos',
        ],
        datasets: [{
          label: 'Estrellas en GitHub',
          data: [90636, 51313, 29174, 15409, 14569, 14346, 10299, 8785, 3690, 1963, 1843, 1090, 331],
          backgroundColor: [
            '#6957D5', '#6957D5', '#6957D5', '#B8B3C7', '#6957D5',
            '#6957D5', '#B8B3C7', '#6957D5', '#6957D5', '#6957D5',
            '#6957D5', '#B8B3C7', '#6957D5',
          ],
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => `${context.parsed.x.toLocaleString('es-ES')} estrellas`,
            },
          },
        },
        scales: {
          x: {
            type: 'logarithmic',
            title: { display: true, text: 'Estrellas en GitHub · escala logarítmica' },
          },
          y: { grid: { display: false } },
        },
      },
    });
  });
</script>

## La IA deja de ser un chat

Los proyectos más reveladores no intentan construir otro chatbot. [Multica](https://github.com/multica-ai/multica) organiza agentes de programación como si fueran compañeros de equipo: reciben tareas, informan de avances, plantean bloqueos y entregan el trabajo para revisión. Conviene llamarlo *source-available*, no estrictamente código abierto, porque su licencia añade condiciones propias.

[Anti-slop](https://github.com/miqdadbadjuber/anti-slop) ataca otro problema: las interfaces, textos y fragmentos de código genéricos producidos por agentes. Sus reglas no generan una dirección creativa, pero funcionan como filtro de calidad. [Sprite-gen](https://github.com/aldegad/sprite-gen), por su parte, transforma una ilustración en sprites, animaciones y archivos preparados para un videojuego. Su valor no está en crear una imagen llamativa, sino en convertirla en un recurso utilizable.

Los tres proyectos apuntan al mismo cambio: **el modelo importa menos cuando no existe un buen proceso alrededor**.

## Tres predicciones

**Las alternativas abiertas presionarán al software de suscripción.** No reemplazarán masivamente al SaaS mientras instalarlas siga requiriendo tiempo, pero obligarán a las plataformas comerciales a justificar el pago mediante comodidad y servicio.

**Los agentes se gestionarán como equipos.** Necesitarán permisos, tareas, estados, revisiones y criterios compartidos. La conversación será solo una parte de la interfaz.

**“Abierto” dejará de ser una etiqueta suficiente.** Tendremos que distinguir entre código visible, licencia abierta, aplicación autoalojable, modelos locales y servicios externos. [OpenWA](https://github.com/rmyndharis/OpenWA), por ejemplo, devuelve control sobre una integración con WhatsApp, pero utiliza clientes no oficiales y advierte del riesgo de bloqueo de cuentas.

## El futuro como colección de señales

Ninguna estrella garantiza que un proyecto vaya a convertirse en empresa, estándar o producto duradero. Sin embargo, GitHub permite observar experimentos antes de que sus ideas lleguen al mercado general.

La señal más clara de esta selección no es que todo vaya a ser gratuito o autoalojado. Es que el código abierto ya no se conforma con proporcionar piezas: **quiere diseñar la experiencia completa**. Y, en el terreno de la IA, empieza a preocuparse menos por generar algo y más por conseguir que ese resultado sirva para trabajar.

**Puedes consultar los datos, reproducir los gráficos y revisar la clasificación editorial** en el [notebook de Jupyter del análisis](/nebula/analisis/senales-desde-github.ipynb).
