---
imagenPortada: "/nebula/imagenes/apuestas_nba_beasley_portada.png"
titulo: "¿Se puede reconocer un partido amañado de la NBA mirando sus estadísticas?"
descripcion: "Cuatro encuentros de Malik Beasley están bajo sospecha. Los números cuentan una historia mucho menos evidente de lo esperado."
tema: "BALONCESTO"
fecha: 2026-10-28
cifraDestacada: "1 rebote"
etiquetaCifra: "separó una apuesta ganadora de una perdedora"
metodologia: "EDA de los 79 partidos de temporada regular disputados por Malik Beasley con Milwaukee Bucks en la temporada 2023-24, descargados de la API oficial de la NBA. Comparo los cuatro encuentros descritos en la acusación federal con la distribución completa de puntos y rebotes del jugador. El análisis no detecta amaños ni atribuye intenciones a partir de una estadística: un registro raro no demuestra una manipulación y uno habitual tampoco la descarta."
---

*Quedan 1,1 segundos. Milwaukee gana por siete puntos y el partido está decidido. Amir Coffey lanza un triple que no va a cambiar nada. Malik Beasley corre hacia el aro, aparta a un compañero y captura el rebote. Es el cuarto de su noche. Para el marcador, es una nota al pie. Para algunas apuestas, acaba de suceder lo único que importaba.*

La Fiscalía federal de Nueva York sostiene que esa jugada del 10 de marzo de 2024 permitió **superar una línea de 3,5 rebotes** pactada de antemano. Beasley, que inicialmente negó los cargos, tiene previsto declararse culpable el próximo 9 de diciembre. Todavía no se conocen los cargos concretos ni las condiciones del acuerdo.

La acusación describe cuatro partidos de su temporada con Milwaukee Bucks. La pregunta para los datos es más modesta que la del tribunal: **si borramos las fechas y miramos solo las estadísticas, ¿podemos reconocerlos?**

## Elige el partido que más te llama la atención

Los cuatro registros siguientes pertenecen a los encuentros señalados. Pulsa uno antes de continuar.

<div class="apuesta-beasley" aria-labelledby="pregunta-beasley">
  <p id="pregunta-beasley"><strong>¿Cuál parece más extraño?</strong></p>
  <div class="apuesta-beasley-opciones" role="group" aria-label="elige un registro">
    <button type="button" data-caso="a">3 puntos y 3 rebotes</button>
    <button type="button" data-caso="b">6 puntos y 4 rebotes</button>
    <button type="button" data-caso="c">17 puntos y 4 rebotes</button>
    <button type="button" data-caso="d">16 puntos y 6 rebotes</button>
  </div>
  <p class="apuesta-beasley-respuesta" aria-live="polite">Guarda tu intuición. Los datos de toda la temporada pondrán el registro en contexto.</p>
</div>

## Una frontera casi perfecta

Malik Beasley jugó **79 partidos** de temporada regular. En algunos de esos partidos se apostaba si el jugador conseguiría tres rebotes o menos o si llegaría a cuatro o más. Durante toda la temporada, ambos resultados estuvieron casi empatados: se quedó en tres o menos 39 veces y alcanzó al menos cuatro en 40.

No estamos ante una barrera que separase lo normal de lo extraordinario. Era prácticamente una moneda al aire construida alrededor de su rendimiento habitual. Quince partidos acabaron con tres rebotes y veinte con cuatro. **Una sola captura cambiaba el resultado de la apuesta**.

<div class="grafico-interactivo">
  <canvas id="grafico-rebotes-beasley" height="340"></canvas>
</div>

<p class="nota-grafico">La línea naranja marca los 3,5 rebotes. Las barras muestran cuántos partidos acabaron con cada total.</p>

La **primera fecha de la acusación**, el 26 de enero contra Cleveland, quedó en el lado inferior: **tres rebotes**. La Fiscalía afirma que Beasley había comunicado que rendiría por debajo de la línea. Sin el expediente, ese número no levantaría la voz: ocurrió otras catorce veces durante el curso.

## Dos aciertos y un rebote con suspense

El 27 de febrero frente a Charlotte terminó con **seis puntos y cuatro rebotes**. Según la acusación, el plan era quedarse por debajo de 12,5 puntos y superar los 3,5 rebotes. Cumplió ambas condiciones. Sin embargo, esa combinación tampoco era una rareza estadística: Beasley sumó doce puntos o menos y cuatro rebotes o más en **22 de sus 79 partidos**.

Después llegó la captura contra los Clippers. Fue su cuarto rebote, justo el necesario para cruzar la línea. La jugada resulta llamativa por el momento y por los mensajes recogidos por los investigadores, no porque cuatro rebotes fueran excepcionales. Fue su resultado más frecuente de la temporada.

**El cuarto partido rompió el guion**. Contra los Brooklyn Nets, el 21 de marzo, la acusación sostiene que la apuesta buscaba menos de 3,5 rebotes. Beasley consiguió **seis**. Los apostantes perdieron y uno de los implicados reclamó que le devolvieran el dinero o que se manipularan más encuentros. Seis rebotes parecen muchos junto a una línea de 3,5, pero Beasley llegó a esa cifra en 14 partidos.

## Los números no saben qué ocurrió

El partido de tres puntos fue uno de los peores registros ofensivos de Beasley durante aquella temporada. El último, con 16 puntos y seis rebotes, fue precisamente el que hizo perder la apuesta descrita en la acusación. Aun así, ninguno de esos resultados permite saber por sí solo si hubo un amaño.

Las estadísticas solo cuentan qué ocurrió en la pista. Para explicar por qué ocurrió hacen falta otras pruebas, como los mensajes entre los implicados, las cantidades apostadas y el recorrido del dinero. Por eso, **un resultado habitual puede formar parte de un delito y una actuación extraña puede ser simplemente una mala noche**.

Una diferencia mínima puede cambiar por completo una historia en la NBA. [Un solo triple puede romper un récord de franquicia](/nebula/articulos/records-nba-predicciones-locas-2026-27/) y [una derrota puede convertir una temporada en la peor de un equipo](/nebula/articulos/records-nba-segunda-parte-2026-27/). En este caso, un rebote separaba una apuesta ganadora de una perdedora.

Las apuestas individuales viven precisamente de esa ambigüedad. No necesitan que un equipo pierda ni que una estrella falle veinte tiros. La diferencia puede caber en una posesión aparentemente banal para casi todos. A veces todo se decide en una acción que el público olvidaría al salir del pabellón: **un rebote cuando quedan 1,1 segundos**.

## Fuentes y datos

- [Acusación y comunicado de la Fiscalía del Distrito Este de Nueva York](https://www.justice.gov/usao-edny/pr/former-national-basketball-association-players-current-player-agent-and-three-other)
- [Registro de partidos obtenido mediante la API oficial de estadísticas de la NBA](https://www.nba.com/stats)
- [Notebook reproducible](/nebula/analisis/apuestas-nba/analisis_apuestas_nba.ipynb)
- [Datos de los 79 partidos](/nebula/analisis/apuestas-nba/datos_malik_beasley_2023_24.csv)

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const respuestas = {
      a: 'Es el registro más bajo en puntos, pero los tres rebotes ocurrieron 15 veces esa temporada.',
      b: 'Cumplió las dos condiciones descritas por la Fiscalía, aunque la combinación apareció en 22 partidos.',
      c: 'Los cuatro rebotes fueron el total más frecuente. El detalle decisivo es que el último llegó a 1,1 segundos del final.',
      d: 'Fue el partido que frustró la apuesta a la baja: seis rebotes, una cifra que alcanzó 14 veces en el curso.',
    };
    const contenedor = document.querySelector('.apuesta-beasley');
    const salida = contenedor?.querySelector('.apuesta-beasley-respuesta');
    contenedor?.querySelectorAll('button').forEach((boton) => {
      boton.addEventListener('click', () => {
        contenedor.querySelectorAll('button').forEach((otro) => otro.classList.remove('seleccionado'));
        boton.classList.add('seleccionado');
        if (salida) salida.textContent = respuestas[boton.dataset.caso];
      });
    });

    const lienzo = document.getElementById('grafico-rebotes-beasley');
    if (!lienzo || !window.Chart) return;
    new Chart(lienzo, {
      type: 'bar',
      data: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '10', '11'],
        datasets: [{
          data: [7, 17, 15, 20, 6, 11, 1, 1, 1],
          backgroundColor: '#446ddf',
          borderRadius: 4,
        }],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          annotation: undefined,
          tooltip: { callbacks: { label: (context) => `${context.raw} partidos` } },
        },
        scales: {
          x: { title: { display: true, text: 'Rebotes de Beasley' } },
          y: { beginAtZero: true, ticks: { precision: 0 }, title: { display: true, text: 'Partidos' } },
        },
      },
      plugins: [{
        id: 'lineaApuesta',
        afterDraw(chart) {
          const { ctx, chartArea, scales } = chart;
          const x3 = scales.x.getPixelForValue(2);
          const x4 = scales.x.getPixelForValue(3);
          const x = (x3 + x4) / 2;
          ctx.save();
          ctx.strokeStyle = '#d85a30';
          ctx.lineWidth = 2;
          ctx.setLineDash([6, 5]);
          ctx.beginPath();
          ctx.moveTo(x, chartArea.top);
          ctx.lineTo(x, chartArea.bottom);
          ctx.stroke();
          ctx.restore();
        },
      }],
    });
  });
</script>

<style>
  .apuesta-beasley {
    margin: 1.75rem 0;
    padding: 1.25rem;
    border: 1px solid rgba(68, 109, 223, 0.25);
    border-radius: 14px;
    background: rgba(68, 109, 223, 0.06);
  }
  .apuesta-beasley-opciones {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.65rem;
  }
  .apuesta-beasley button {
    padding: 0.8rem;
    border: 1px solid #446ddf;
    border-radius: 9px;
    color: inherit;
    background: transparent;
    cursor: pointer;
  }
  .apuesta-beasley button:hover,
  .apuesta-beasley button.seleccionado {
    color: white;
    background: #446ddf;
  }
  .apuesta-beasley-respuesta { min-height: 3rem; margin-bottom: 0; }
  .nota-grafico { margin-top: -0.75rem; color: #666; font-size: 0.9rem; }
  @media (max-width: 640px) {
    .apuesta-beasley-opciones { grid-template-columns: 1fr; }
  }
</style>
