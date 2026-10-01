---
imagenPortada: "/nebula/imagenes/records_nba_portada.png"
titulo: "Los 10 récords NBA que el machine learning ve más cerca de romperse esta temporada: Parte I"
descripcion: "Un modelo ha rastreado 90 récords de franquicia y señala cuáles pueden caer esta temporada: algunos parecen imposibles, pero los datos dicen lo contrario."
tema: "BALONCESTO"
fecha: 2026-10-05T10:00:00+02:00
cifraDestacada: "90"
etiquetaCifra: "récords de franquicia analizados entre jugadores y equipos"
metodologia: "Para este análisis revisé 90 posibles récords de la NBA 2026-27, tres por cada franquicia: algunos positivos y otros negativos. Después creé una puntuación que tiene en cuenta lo cerca que está cada marca, cuánto tendría que mejorar o empeorar el equipo o jugador, y lo raro que sería verla caer. Las cifras proceden principalmente de Basketball-Reference y del dataset preparado para este artículo. El modelo no adivina el futuro: solo ayuda a ordenar qué historias merece la pena seguir."
---

*Cada temporada NBA deja récords evidentes y otros que solo se ven cuando alguien abre la hoja de cálculo. Este año el radar encuentra de todo: un base que amenaza el territorio histórico de Michael Jordan en Chicago, un pívot de Portland que puede reescribir la tabla de rebotes, una versión estadísticamente monstruosa de Shai Gilgeous-Alexander y dos récords de triples que nacieron ayer y ya pueden caer mañana.*

Un récord de franquicia no siempre necesita una temporada legendaria. A veces basta con salud, volumen y un contexto táctico favorable. Otras veces exige algo cercano al absurdo: anotar como nunca, asistir como una dinastía o repetir cada noche una producción que apenas admite descanso.

Para separar ambas cosas he construido un radar con **90 posibles récords de franquicia** para la NBA 2026-27. Incluye registros de jugadores, marcas colectivas y alertas negativas. Después he usado un modelo de machine learning sencillo para ordenar los candidatos por una mezcla de rareza, cercanía y posibilidad real.

El resultado no es una lista de apuestas. Es algo más útil para escribir historias: **un mapa de los récords que pueden convertir una temporada normal en una rareza estadística**.

## El método: buscar rarezas que aún sean posibles

El dataset parte de tres pistas por franquicia: una marca individual positiva, una marca colectiva positiva y un récord negativo de derrotas. Para cada caso aparecen el registro vigente, el objetivo exacto para superarlo, lo conseguido en 2025-26, la distancia restante y el ritmo por partido necesario.

El modelo añade una señal de rareza. Para ello agrupa los 90 casos con K-Means y mide qué tan lejos queda cada candidato del centro de su grupo. Cuanto más lejos, más anómalo. Después combina esa rareza con la factibilidad inicial, la cercanía al umbral y la polaridad del récord.

La puntuación final se llama **índice de locura**. Va de 0 a 100 y sirve para responder una pregunta muy concreta: si solo pudiéramos vigilar diez historias durante el año, ¿cuáles prometen más?

## 1. Josh Giddey y la frontera de Michael Jordan

El caso más alto del ranking es Josh Giddey. El objetivo parece pequeño escrito así: **16 triple-dobles**. Pero la cifra pesa porque el récord de los Bulls está en 15 y pertenece a Michael Jordan.

Giddey cerró 2025-26 con **13 triple-dobles en 54 partidos**. No necesita duplicar su producción ni inventar una versión nueva de sí mismo. Necesita mantenerse en pista y añadir tres noches más de acumulación total. Por eso el modelo lo coloca en 100 sobre 100.

La historia tiene una tensión perfecta: Chicago no es una franquicia acostumbrada a que alguien toque registros asociados a Jordan sin que salten alarmas históricas. Si Giddey empieza fuerte, cada triple-doble dejará de ser una curiosidad para convertirse en cuenta atrás.

## 2. Sacramento vuelve a perseguir su techo ofensivo

Los Kings aparecen por una marca colectiva: **9.899 puntos**. El récord de la franquicia está en 9.898, conseguido en 2022-23. En 2025-26 anotaron 9.102, así que la distancia es grande: **797 puntos** más.

Traducido a ritmo de temporada completa, Sacramento tendría que vivir alrededor de **120,7 puntos por partido**. No es un paseo, pero tampoco suena imposible en una NBA inflada de posesiones, triples y noches de 130 puntos.

Esta pista funciona porque habla de identidad. Cuando Sacramento es divertido, suele ser por ataque. Si vuelve a rozar ese techo, el récord de puntos puede ser la forma estadística de contar que los Kings han recuperado su mejor versión.

## 3. Donovan Clingan contra una marca de rebotes que parecía de otra época

Portland tiene una historia más física. Donovan Clingan necesita **968 rebotes** para superar el récord de franquicia, fijado en 967. En 2025-26 ya firmó **892 en 77 partidos**.

La diferencia son 76 rebotes. El ritmo exigido es de **11,8 por noche**, una cifra dura pero razonable para un interior con minutos estables. Aquí el modelo detecta una mezcla muy atractiva: marca antigua, jugador joven y distancia asumible.

No todos los récords modernos son de triples. Algunos todavía se rompen a base de cerrar posesiones, cargar el rebote ofensivo y sobrevivir a 82 partidos. Clingan tiene una de esas historias.

## 4. Shai Gilgeous-Alexander y el listón de los 2.594 puntos

Shai Gilgeous-Alexander necesita **2.594 puntos** para quedarse con el récord anotador de temporada en Oklahoma City y Seattle. En 2025-26 llegó a 2.117 en 68 partidos.

La exigencia es clara: **31,6 puntos por partido durante 82 encuentros**, o una media todavía mayor si descansa. No es una predicción cómoda. Es una puerta estrecha. Pero Shai pertenece al pequeño grupo de jugadores para quienes ese ritmo no suena ridículo.

La clave será la combinación entre uso, eficiencia y descanso. Si Oklahoma City domina demasiado pronto, el récord puede perderse en el calendario. Si la pelea competitiva se estira, cada noche de Shai tendrá valor histórico.

## 5. Jalen Brunson en territorio de Bernard King

Los Knicks tienen otro récord de puntos en el punto de mira. Jalen Brunson necesita **2.348 puntos**. En 2025-26 anotó 1.927 en 74 partidos. La distancia es de 421.

El ritmo objetivo, **28,6 puntos por partido**, parece exactamente el tipo de cifra que Brunson puede sostener cuando Nueva York vive alrededor de su bote. No necesita una explosión irrepetible, sino una versión plena de lo que ya es.

Este caso tiene algo muy neoyorquino: no sería solo un récord, sino una temporada de uso masivo, noches de playoff en enero y Madison Square Garden midiendo cada cuarto como si fuera una prueba de carácter.

## 6. Anthony Edwards y el techo anotador de Minnesota

Anthony Edwards aparece con una misión casi gemela: **2.178 puntos** para superar el récord de los Timberwolves. En 2025-26 se quedó en 1.757, pero lo hizo en solo 61 partidos.

Por eso el modelo lo trata como candidato real. La barrera exige **26,6 puntos por partido** si juega todos los encuentros. Edwards ya tiene el volumen, el protagonismo y el descaro. La pregunta es menos si puede anotar así y más si el cuerpo y el calendario le dejarán sumar suficiente.

En Minnesota, el récord tendría un significado generacional. Sería otra forma de decir que Edwards ya no persigue el futuro de la franquicia: lo está escribiendo.

## 7. Kevin Durant y el récord más difícil de la lista

Kevin Durant necesita **2.819 puntos** con Houston. El récord vigente está en 2.818. La cifra es brutal incluso para él: **34,4 puntos por partido durante 82 partidos**.

Aquí la locura pesa más que la factibilidad. Durant anotó 2.026 puntos en 2025-26, una barbaridad que todavía queda a 793 del umbral. Para romper esta marca tendría que combinar una salud casi perfecta con uno de los mayores cursos anotadores de su carrera.

Precisamente por eso merece estar en el radar. No es el récord más probable. Es el que, si empieza a asomar en diciembre, cambiaría el tono de toda la temporada.

## 8. Cleveland puede romper su récord de asistencias

Los Cavaliers son el primer caso colectivo no basado en puntos. Necesitan **2.350 asistencias**. El récord está en 2.349 desde 1992-93 y en 2025-26 ya llegaron a 2.321.

La distancia es mínima: 29 asistencias. El ritmo necesario, **28,7 por partido**, encaja con un equipo que reparte el balón y puede sostener creación desde varias posiciones.

Este récord no tiene el brillo de una media anotadora, pero cuenta algo más profundo: estructura ofensiva. Si Cleveland lo rompe, probablemente no será por una estrella aislada, sino por una forma colectiva de jugar.

## 9. Julian Champagnie puede mejorar un récord que ya es suyo

Julian Champagnie acaba de fijar el récord de triples de San Antonio con **195**. El objetivo ahora es casi cruel por su sencillez: **196**.

El modelo premia la cercanía absoluta. Un triple más basta para reescribir el registro. Claro que eso también revela una fragilidad: no todos los récords cercanos tienen el mismo peso histórico. Este es un récord de continuidad, no de explosión.

Aun así, San Antonio vive una etapa en la que cada pieza alrededor de Victor Wembanyama importa. Si Champagnie sostiene volumen y puntería, el récord de triples será una señal lateral de cómo respira el ataque.

## 10. Kon Knueppel y el récord recién nacido de Charlotte

El cierre del top 10 es Kon Knueppel. Su marca a batir: **274 triples**. En 2025-26 hizo 273, que ya era récord de la franquicia.

La lectura es parecida a la de Champagnie, pero con una escala más agresiva. Knueppel no necesita demostrar que puede ser un tirador de alto volumen. Ya lo hizo. Necesita repetirlo y añadir un triple.

Charlotte rara vez entra en las conversaciones grandes de la NBA. Un récord así no cambia la historia de la liga, pero sí ofrece una forma concreta de mirar al equipo: volumen exterior, juventud y una marca que puede caer casi por inercia si el rol se mantiene.

<div class="grafico-interactivo">
  <canvas id="grafico-records-nba-top10" height="420"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-records-nba-top10');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          'Giddey',
          'Kings',
          'Clingan',
          'Shai',
          'Brunson',
          'Edwards',
          'Durant',
          'Cavaliers',
          'Champagnie',
          'Knueppel',
        ],
        datasets: [{
          label: 'Índice de locura',
          data: [100.0, 90.8, 89.1, 81.2, 79.7, 79.7, 75.5, 75.4, 75.3, 75.2],
          backgroundColor: [
            '#D85A30',
            '#446DDF',
            '#446DDF',
            '#446DDF',
            '#446DDF',
            '#446DDF',
            '#446DDF',
            '#446DDF',
            '#446DDF',
            '#446DDF',
          ],
        }],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => `Índice de locura: ${context.raw}`,
            },
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 105,
            title: { display: true, text: 'Índice de locura ML' },
          },
        },
      },
    });
  });
</script>

## Lo que queda guardado para una segunda parte

**El modelo también deja una lista de reserva con candidatos muy aprovechables**. Ahí aparecen récords con menos puntuación, pero con mejor variedad editorial: alertas negativas, marcas colectivas y casos que pueden crecer si cambia el contexto de la temporada.

Ese segundo grupo es importante porque el top 10 salió casi completamente positivo. Tiene sentido: los récords positivos suelen estar más cerca cuando un jugador o equipo viene de una buena temporada. Los negativos, en cambio, necesitan una caída larga, fea y sostenida.

<div class="grafico-interactivo">
  <canvas id="grafico-records-nba-reserva" height="320"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-records-nba-reserva');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Jugador positivo', 'Equipo positivo', 'Equipo negativo'],
        datasets: [{
          data: [6, 6, 3],
          backgroundColor: ['#446DDF', '#7C9AEE', '#D85A30'],
          borderWidth: 0,
        }],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              label: (context) => `${context.label}: ${context.raw} candidatos guardados`,
            },
          },
        },
      },
    });
  });
</script>

## Cómo leer estas predicciones

**La tentación sería convertir el ranking en una profecía**. No lo es. Un modelo con datos de récords no sabe si un jugador va a lesionarse, si un entrenador cambiará la rotación o si una franquicia decidirá bajar el ritmo en marzo.

Lo que sí hace es ordenar el ruido. Detecta qué récords están cerca, cuáles requieren una anomalía enorme y cuáles combinan ambas cosas de forma lo bastante atractiva como para seguirlos durante el curso.

Por eso el caso de Giddey es tan fuerte: la cifra histórica es reconocible, la distancia no es absurda y el protagonista ya mostró el patrón estadístico necesario. Por eso Durant aparece aunque sea difícil: si alguien se acerca a 2.819 puntos con 38 años, el artículo se escribe solo. Y por eso Cleveland tiene valor aunque no sea un titular viral: una marca de asistencias puede ser la huella más limpia de un equipo que juega bien.

La NBA siempre vende estrellas, pero las franquicias también se cuentan por sus tablas históricas. A veces basta una línea nueva en esa tabla para saber que algo raro ha pasado.

**Puedes revisar el ranking completo, reproducir el índice de locura y consultar las candidatas guardadas para una segunda parte** en el [notebook de Jupyter del análisis de récords NBA](/nebula/analisis/records-nba-predicciones-locas-ml.ipynb).

Fuentes: [Basketball-Reference](https://www.basketball-reference.com/), radar propio de récords de franquicia NBA 2026-27 y notebook de análisis enlazado en este artículo.
