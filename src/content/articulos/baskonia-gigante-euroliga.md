---
titulo: "Baskonia ya ha vuelto de sitios peores: 26 temporadas de datos contra el pesimismo del mal inicio de la temporada 26/27 en Euroliga"
descripcion: "176 precedentes de la era moderna permiten medir la grandeza europea del Baskonia y cuánto significa realmente un mal comienzo."
tema: "BALONCESTO"
fecha: 2026-10-06T09:00:00+02:00
imagenPortada: "/nebula/imagenes/baskonia_historia_portada.png"
cifraDestacada: "368"
etiquetaCifra: "victorias del Baskonia en las 26 temporadas de la Euroliga moderna"
metodologia: "Análisis de los resultados oficiales de las 26 temporadas de la Euroliga moderna entre 2000-01 y 2025-26: 696 partidos del Baskonia y la trayectoria completa de los clubes participantes. Para medir el valor de un mal inicio se estudiaron 176 equipos-temporada desde 2016-17 hasta 2025-26, comparando su balance tras 1, 3, 5 y 10 encuentros con el porcentaje final de victorias. La referencia al Top 8 es una aproximación basada en victorias y diferencia de puntos y no reproduce todos los desempates oficiales. El R² describe asociación dentro de la muestra y no implica causalidad."
---

*Un par de derrotas puede mermar la moral de la afición en los primeros destellos del alba de la temporada. Enseguida hacemos diagnósticos del equipo: la plantilla no alcanza, el proyecto se ha equivocado y Europa vuelve a quedar demasiado lejos. El pesimismo siempre corre más que el calendario. Los datos, sin embargo, cuentan una historia bastante más larga.*

Desde el nacimiento de la Euroliga moderna, Baskonia ha participado en las **26 ediciones** disputadas entre 2000-01 y 2025-26. Ha jugado 696 partidos y ha ganado 368. Su porcentaje histórico de victorias es del **52,9%**.

No es una aparición esporádica ampliada por la nostalgia. Es más de un cuarto de siglo ganando más partidos de los que se pierden en la máxima competición continental.

Entre los clubes con al menos diez temporadas en el torneo, Baskonia ocupa el **octavo lugar por número de victorias**. Solo Barcelona, Real Madrid, Olympiacos, CSKA, Panathinaikos, Maccabi y Fenerbahçe aparecen por delante.

Detrás quedan Anadolu Efes, con 349 triunfos; Žalgiris, con 269; y Olimpia Milano, con 215. Equipos procedentes de mercados mayores, con presupuestos superiores o con una tradición europea indiscutible no han conseguido acumular tantas victorias como el club de Vitoria.

<div class="grafico-interactivo">
  <canvas id="grafico-victorias-historicas-baskonia" height="390"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-victorias-historicas-baskonia');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Barcelona', 'Real Madrid', 'Olympiacos', 'CSKA', 'Panathinaikos', 'Maccabi', 'Fenerbahçe', 'Baskonia', 'Anadolu Efes', 'Žalgiris'],
        datasets: [{
          label: 'Victorias desde 2000-01',
          data: [477, 450, 440, 420, 403, 376, 376, 368, 349, 269],
          backgroundColor: ['#446DDF', '#446DDF', '#446DDF', '#446DDF', '#446DDF', '#446DDF', '#446DDF', '#D85A30', '#AAB2C3', '#AAB2C3'],
          borderRadius: 3,
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => context.raw + ' victorias',
            },
          },
        },
        scales: {
          x: {
            beginAtZero: true,
            title: { display: true, text: 'Victorias en la Euroliga moderna' },
          },
        },
      },
    });
  });
</script>

Ese dato no convierte al Baskonia en campeón de Europa. Tampoco pretende esconder el gran vacío de su palmarés continental y sus últimas temporadas. Su grandeza es de otra naturaleza: **permanencia, resistencia y capacidad para regresar a lugares reservados casi siempre para estructuras mucho más poderosas**.

## Una final y cinco Final Four

La historia europea del Baskonia no se limita a estar presente.

En 2001, el entonces Tau Cerámica alcanzó la final de la primera Euroliga moderna. Aquella edición no terminó con una Final Four, sino con una serie al mejor de cinco partidos. Kinder Bolonia, dirigida por Ettore Messina y liderada por Manu Ginóbili, necesitó el quinto encuentro para impedir que el título viajara a Vitoria.

Después llegaron cinco Final Four: **2005, 2006, 2007, 2008 y 2016**.

En 2005, Baskonia eliminó a la Benetton y derrotó al CSKA en Moscú antes de caer en la final frente al Maccabi. Aquel resultado inició una secuencia extraordinaria: cuatro Final Four consecutivas.

<div style="position:relative; width:100%; aspect-ratio:16/9; margin:2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/0vabeSxX_0U"
    title="Vídeo sobre la historia europea del Baskonia"
    style="position:absolute; inset:0; width:100%; height:100%; border:0;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

La quinta llegó en Berlín, en 2016. Habían transcurrido ocho años desde la anterior y habían cambiado entrenadores, patrocinadores y generaciones completas de jugadores. Baskonia volvió de todos modos.

| Temporada | Última ronda alcanzada | Resultado |
|---|---|---|
| 2000-01 | Final al mejor de cinco | Subcampeón |
| 2004-05 | Final Four | Subcampeón |
| 2005-06 | Final Four | Semifinalista |
| 2006-07 | Final Four | Semifinalista |
| 2007-08 | Final Four | Semifinalista |
| 2015-16 | Final Four | Semifinalista |

Una final y cinco Final Four. Seis temporadas entre los últimos aspirantes al título. No son suficientes para presumir de una Euroliga en la vitrina, pero sí para rechazar la idea de que el Baskonia sea un invitado menor en esta competición.

## Un par de jornadas explican muy poco

La historia ayuda a recuperar la perspectiva. Los datos permiten medirla.

Para comprobar cuánto debería preocuparnos un mal comienzo, he analizado **176 equipos-temporada** de la era de la liga regular, desde 2016-17 hasta 2025-26. El ejercicio compara el balance de cada equipo después de sus primeros 1, 2, 3, 5 y 10 partidos con el porcentaje de victorias conseguido al terminar el curso.

Después de dos encuentros, el balance inicial está asociado solamente con el **17,7%** de la variación observada en el resultado final. Es más información que tras la primera jornada, cuando el R² se queda en el 11,2%, pero sigue siendo una señal muy débil.

Dicho de otra manera: tras ochenta minutos de competición todavía conocemos muy poco sobre cómo acabará un equipo muchos meses después.

Utilizar directamente el balance de esas dos jornadas como pronóstico sería, además, una estrategia desastrosa. Su error medio es más del doble que el de asumir simplemente que el equipo terminará alrededor del 50% de victorias: **26,1 puntos porcentuales frente a 12,6**. Después de dos partidos solo existen clubes con un 100%, un 50% o un 0% de triunfos, una resolución demasiado pobre para describir una temporada completa.

Dos jornadas generan titulares. Todavía no generan certezas.

<div class="grafico-interactivo">
  <canvas id="grafico-senal-inicio-euroliga" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-senal-inicio-euroliga');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [{
          label: 'Parte del resultado final asociada al balance inicial',
          data: [11.2, 17.7, 29.4, 35.4, 40.1, 44.1, 51.8, 57.3, 63.7, 69.0],
          borderColor: '#446DDF',
          backgroundColor: 'rgba(68, 109, 223, 0.14)',
          pointBackgroundColor: ['#446DDF', '#D85A30', '#446DDF', '#446DDF', '#D85A30', '#446DDF', '#446DDF', '#446DDF', '#446DDF', '#D85A30'],
          pointRadius: [4, 6, 4, 4, 6, 4, 4, 4, 4, 6],
          borderWidth: 3,
          fill: true,
          tension: 0.25,
        }],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => 'R² descriptivo: ' + context.raw + '%',
            },
          },
        },
        scales: {
          x: {
            title: { display: true, text: 'Partidos disputados' },
          },
          y: {
            beginAtZero: true,
            max: 80,
            title: { display: true, text: 'R² descriptivo (%)' },
          },
        },
      },
    });
  });
</script>

La clasificación empieza a contar una historia más reconocible después de cinco partidos, cuando el balance inicial se asocia con alrededor del **40,1%** de la variación del resultado final. Después de diez, la relación alcanza el **69%**.

Ese es el verdadero calendario del pesimismo: preocuparse tras dos jornadas es humano; dictar sentencia es estadísticamente indefendible. A partir de diez encuentros ya existen tendencias mucho más sólidas. Antes abundan el ruido y las conclusiones precipitadas.

## Empezar 0-2 no significa quedarse fuera

La muestra contiene 44 equipos que comenzaron su temporada con dos derrotas. Su porcentaje final medio de victorias fue del **41,6%**. Y un **27,3%** terminó dentro de nuestra aproximación homogénea al Top 8.

| Balance inicial | Casos históricos | % medio final de victorias | Top 8 aproximado |
|---|---:|---:|---:|
| 0-2 | 44 | 41,6% | 27,3% |
| 1-1 | 88 | 49,4% | 42,0% |
| 2-0 | 44 | 59,7% | 70,5% |

Dos derrotas iniciales reducen las probabilidades. No las destruyen. En algo más de uno de cada cuatro precedentes, un equipo que empezó 0-2 terminó igualmente entre los ocho mejores.

Esto tampoco significa que cualquier comienzo sea irrelevante. Ninguno de los nueve equipos que inició 0-5 en la muestra alcanzó después el Top 8 aproximado. La esperanza basada en datos no consiste en ignorar las señales negativas, sino en saber **cuándo una señal es lo bastante fuerte para creerla**.

## Baskonia ya ha regresado desde mucho más atrás

No hace falta buscar los mejores ejemplos lejos del Buesa Arena.

En la temporada 2017-18, Baskonia empezó la Euroliga con tres derrotas consecutivas. Después de cinco jornadas solo había ganado un partido. El equipo terminó la fase regular con un balance de **16-14** y ocupó la séptima posición.

Un año más tarde arrancó con tres victorias en sus primeros diez encuentros. También terminó séptimo y volvió a disputar los playoffs.

En 2023-24, el balance era de **una victoria y cuatro derrotas** después de cinco jornadas. Baskonia cerró la liga regular con 18 triunfos, alcanzó la octava plaza y regresó a las eliminatorias.

| Temporada | Inicio preocupante | Balance final | Posición |
|---|---:|---:|---:|
| 2017-18 | 0-3 y 1-4 | 16-14 | 7.ª |
| 2018-19 | 3-7 | 15-15 | 7.ª |
| 2023-24 | 1-4 | 18-16 | 8.ª |

Ninguno de esos precedentes garantiza que la historia vaya a repetirse. Los datos no prometen remontadas. También contienen campañas en las que el mal comienzo anunció problemas reales.

La temporada pasada es el recordatorio más cercano: Baskonia perdió sus cinco primeros encuentros y terminó con 13 victorias y 25 derrotas. Pero precisamente por eso importa distinguir entre un tropiezo y una tendencia. **Un 0-2 no contiene la misma información que un 0-5**.

## La historia no juega, pero establece el estándar

Los jugadores que disputan esta temporada no ganarán un solo partido gracias a Scola, Prigioni, Nocioni, Splitter, Calderón, Bennett, Hanga o Bourousis. Las victorias de otras generaciones no anotan puntos ni capturan rebotes.

Pero la historia sí establece qué puede exigir un club de sí mismo.

Baskonia pertenece a la Euroliga porque ha competido durante 26 temporadas, ha ganado 368 partidos, ha alcanzado seis veces la última gran frontera del torneo y ha sobrevivido a todas las transformaciones económicas y deportivas del baloncesto europeo.

Ha cambiado de nombre, de entrenador, de plantilla y de ciclo. Lo que no ha cambiado es su capacidad para reconstruirse cuando parecía haber quedado atrás. [El análisis anterior sobre sus plantillas](/nebula/articulos/baskonia-reconstruccion/) mostró hasta qué punto esa reconstrucción es constante: el club pierde de media más de la mitad de la anotación del curso anterior cada verano y, aun así, ha seguido encontrando formas de competir.

Por eso todavía es pronto para dejar de creer.

No porque todo vaya bien. No porque la plantilla esté libre de dudas. No porque el pasado garantice el futuro. Hay motivos para creer porque los datos demuestran que una jornada apenas sabe contar una temporada y porque este club ha convertido más de una vez un comienzo preocupante en una primavera europea.

El optimismo ciego no sirve de nada. El pesimismo prematuro tampoco.

Entre ambos queda la memoria. Quedan 26 temporadas, 696 partidos, 368 victorias, una final y cinco Final Four. Queda un club que, sin haberlo ganado todo, lleva un cuarto de siglo negándose a abandonar el lugar de los grandes.

Una mala noche puede explicar el enfado.

**No puede explicar al Baskonia.**

Puedes reproducir la clasificación histórica, modificar el corte de jornadas y revisar todos los precedentes en el [notebook de Jupyter del análisis histórico del Baskonia](/nebula/analisis/baskonia-historia-euroliga.ipynb).

Fuentes: resultados de la [API de EuroLeague Basketball](https://api-live.euroleague.net/), [perfil histórico de Baskonia en la Euroliga](https://admin.euroleague.net/competition/teams/showteam?clubcode=bas&lang=en&p=3&seasoncode=E2001&tabid=88) y registros del [EuroLeague Media Centre](https://mediacentre.euroleague.net/mediacentre/en/press_releases/5).
