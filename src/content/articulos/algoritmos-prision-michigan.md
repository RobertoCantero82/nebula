---
imagenPortada: "/nebula/imagenes/algoritmos_prision_portada.png"
titulo: "Michigan promete predecir mejor la violencia en prisión. El 30 % que anuncia es imposible de comprobar"
descripcion: "El nuevo sistema decidirá niveles de seguridad sin que se conozcan su métrica ni el reparto de sus errores."
tema: "INTELIGENCIA ARTIFICIAL"
fecha: 2026-11-02
cifraDestacada: "1.018"
etiquetaCifra: "personas señaladas como peligrosas que no reincidieron"
textoContinuo: "El algoritmo de Michigan señaló como peligrosas a 1.018 personas que no reincidieron"
metodologia: "EDA documental del anuncio y los documentos públicos de Michigan, acompañado de un análisis descriptivo de 6.172 evaluaciones COMPAS publicadas por ProPublica. La base de Florida se utiliza únicamente para explicar el efecto de los umbrales y el reparto de errores; no corresponde al nuevo sistema de Michigan y no permite auditarlo. Nebula no entrena ningún modelo ni genera predicciones propias."
---

*Una persona puede pasar más horas encerrada, moverse con menos libertad o tener menos opciones de estudiar por una puntuación que intenta anticipar lo que hará. Desde diciembre, Michigan probará un nuevo sistema para ayudar a decidir el nivel de seguridad de sus presos. El Gobierno promete que predecirá la violencia alrededor de un 30 % mejor. Suena preciso. El problema es que no ha publicado lo necesario para comprobarlo.*

La noticia circuló con una idea todavía más rotunda: **una inteligencia artificial iba a predecir qué presos cometerían futuros delitos**. No es exactamente eso. El [anuncio oficial de Michigan](https://www.michigan.gov/corrections/about/newsroom/press-releases/2026/10/29/new-prisoner-classification-system-announced-by-michigan-department-of-corrections) habla de riesgo de violencia dentro de prisión y de asignar uno de sus niveles de seguridad.

No es la primera vez que un titular convierte una herramienta concreta en algo casi autónomo. En Nebula ya ocurrió al investigar [la supuesta inteligencia artificial “rebelde” que atacó un sistema del Gobierno australiano](/nebula/articulos/ia-rebelde-agente-no-acepto-un-no/): la historia real era menos cinematográfica, pero explicaba mucho mejor dónde estaba el riesgo.

La diferencia importa. Esa clasificación determina cuánta vigilancia recibe una persona, cómo puede moverse y a qué actividades accede. El programa piloto empezará el próximo 1 de diciembre en varias cárceles masculinas y afectará a decisiones dentro de un sistema con unas 32.000 personas encarceladas.

Michigan todavía no ha estrenado su sistema. **En las prisiones catalanas, un algoritmo parecido lleva quince años influyendo en decisiones penitenciarias**. Este documental muestra qué puede significar una puntuación de riesgo para la persona que la recibe.

<div style="position: relative; width: 100%; aspect-ratio: 16 / 9; margin: 2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/ZlqiLOU3qlA"
    title="RisCanvi: la larga sombra del algoritmo que perfila a los presos en Catalunya"
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Un porcentaje al que le falta la letra pequeña

Para entender una mejora del 30 % hacen falta dos cifras: el resultado anterior y el nuevo. También hay que saber qué se está contando. Michigan no explica si habla de aciertos totales, de agresiones detectadas o de falsas alarmas evitadas.

**No se publica qué considera como violencia futura**, durante cuánto tiempo observa a cada persona ni cómo funciona el modelo en distintos grupos. La empresa sin ánimo de lucro Recidiviz [describe una herramienta](https://www.recidiviz.org/platform-modules/dynamic-classification) que actualiza clasificaciones cuando cambia la conducta y permite que el personal corrija resultados. Esas características no revelan el cálculo que sostiene el 30 %.

Por ahora, la cifra es una expectativa de la Administración, pero no un resultado que cualquiera pueda reproducir.

## Dos errores que no significan lo mismo

Para ver por qué falta información, **analicé** una base pública muy conocida: **6.172 evaluaciones del sistema COMPAS** recopiladas por [ProPublica](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm) en Florida. No es el algoritmo de Michigan ni estudia la misma situación. Este sirve como ejemplo real de lo que desaparece cuando todo se resume en un porcentaje.

COMPAS asignó notas de riesgo del 1 al 10. Si coloco el corte en 5, considero riesgo alto cualquier puntuación entre 5 y 10. Esa regla acierta en el 66,1 % de la muestra, pero comete 1.018 falsas alarmas: personas marcadas como riesgo alto que no reincidieron durante los dos años siguientes. También deja 1.076 casos al otro lado: personas marcadas como riesgo bajo que sí reincidieron.

Mueve el corte para comprobar cómo cambia la decisión:

<div class="grafico-interactivo" id="interactivo-umbral-prision" style="padding: 1.25rem; border: 1px solid #dce2f2; border-radius: 12px; margin: 1.5rem 0;">
  <label for="umbral-prision"><strong>Puntuación mínima considerada riesgo alto: <span id="valor-umbral-prision">5</span></strong></label>
  <input id="umbral-prision" type="range" min="1" max="10" value="5" step="1" style="width: 100%; accent-color: #446ddf; margin: 1rem 0;">
  <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .75rem; text-align: center;">
    <div><strong id="precision-prision">66,1 %</strong><br><small>aciertos totales</small></div>
    <div><strong id="fp-prision">1.018</strong><br><small>falsas alarmas</small></div>
    <div><strong id="fn-prision">1.076</strong><br><small>reincidencias no señaladas</small></div>
  </div>
  <p id="lectura-umbral-prision" style="margin: 1rem 0 0;">El corte habitual equilibra los dos errores, pero supera el millar en ambos.</p>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const datos = {
      1: [45.5, 3363, 0], 2: [57.4, 2354, 277], 3: [62.1, 1796, 541],
      4: [64.7, 1393, 785], 5: [66.1, 1018, 1076], 6: [66.4, 716, 1356],
      7: [65.0, 495, 1664], 8: [63.4, 297, 1962], 9: [60.4, 179, 2264],
      10: [57.5, 59, 2564]
    };
    const control = document.getElementById('umbral-prision');
    if (!control) return;
    const formato = new Intl.NumberFormat('es-ES');
    const actualizar = () => {
      const umbral = Number(control.value);
      const [precision, falsasAlarmas, noSenaladas] = datos[umbral];
      document.getElementById('valor-umbral-prision').textContent = umbral;
      document.getElementById('precision-prision').textContent = precision.toFixed(1).replace('.', ',') + ' %';
      document.getElementById('fp-prision').textContent = formato.format(falsasAlarmas);
      document.getElementById('fn-prision').textContent = formato.format(noSenaladas);
      document.getElementById('lectura-umbral-prision').textContent = umbral < 5
        ? 'Un corte bajo detecta más reincidencias, a cambio de multiplicar las falsas alarmas.'
        : umbral > 5
          ? 'Un corte alto reduce las falsas alarmas, pero deja más reincidencias sin señalar.'
          : 'El corte habitual equilibra los dos errores, pero supera el millar en ambos.';
    };
    control.addEventListener('input', actualizar);
    actualizar();
  });
</script>

Subir el corte parece prudente porque reduce las falsas alarmas. En 8 quedan 297. Pero las reincidencias no señaladas ascienden a 1.962. No existe un botón que borre el error. Solo decidimos cuál toleramos más y quién asume sus consecuencias.

Los promedios también pueden ocultar a quién perjudica más una predicción. En el análisis de Nebula sobre [el reloj de ADN que calcula la edad de una persona](/nebula/articulos/edad-adn-reloj-epigenetico/), el modelo sumaba años a los jóvenes y se los restaba a los mayores. Un error medio aceptable no garantizaba que fallase igual para todos.

## El promedio esconde a quién falla

La precisión global de COMPAS es parecida para las personas registradas como negras y blancas: 64,9 % frente a 67,2 %. Podríamos detenernos ahí y concluir que funciona casi igual. Al separar los fallos aparece otra historia.

**Entre quienes no reincidieron, el sistema marcó erróneamente como riesgo alto al 42,3 % de las personas negras y al 22,0 % de las blancas**. Entre quienes sí reincidieron sucedió lo contrario: clasificó como riesgo bajo al 28,5 % de las negras y al 49,6 % de las blancas.

<div class="grafico-interactivo">
  <canvas id="grafico-errores-compas" height="270"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-errores-compas');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Personas negras', 'Personas blancas'],
        datasets: [
          { label: 'Falsas alarmas', data: [42.3, 22.0], backgroundColor: '#d95f59' },
          { label: 'Reincidencias no señaladas', data: [28.5, 49.6], backgroundColor: '#e7a33e' }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          title: { display: true, text: 'Una precisión parecida puede repartir los errores de forma opuesta' }
        },
        scales: {
          y: { beginAtZero: true, max: 60, title: { display: true, text: 'Porcentaje dentro de cada resultado real' } }
        }
      }
    });
  });
</script>

Esto no demuestra cómo se comportará el nuevo sistema de Michigan. Demuestra qué debería publicar Michigan para que podamos juzgarlo: los dos tipos de error, sus denominadores y su reparto entre grupos, además del promedio general.

## La prueba empieza antes de que llegue la evidencia

Un algoritmo puede ordenar miles de expedientes con rapidez y detectar cambios que una revisión anual pasaría por alto. También puede dar apariencia científica a datos incompletos o desigualdades anteriores. La intervención humana tampoco resuelve el problema si quien revisa solo ve una puntuación y no puede entenderla ni corregir el historial que la alimenta.

**El titular decía que una inteligencia artificial predeciría futuros delitos**. La realidad comprobada es más estrecha: Michigan probará una herramienta para clasificar riesgo de violencia dentro de prisión. La promesa del 30 % podría acabar siendo cierta, pero hoy le **faltan las pruebas públicas que permitirían saberlo**.

Puedes consultar los cálculos, cambiar todos los umbrales y revisar las limitaciones en el **[notebook del análisis](/nebula/analisis/algoritmos-prision/analisis_algoritmos_prision.ipynb)**. Los datos utilizados están disponibles en la **[copia pública de la base COMPAS](/nebula/analisis/algoritmos-prision/datos/compas-scores-two-years.csv)**.

Fuentes: [Departamento de Prisiones de Michigan](https://www.michigan.gov/corrections/about/newsroom/press-releases/2026/10/29/new-prisoner-classification-system-announced-by-michigan-department-of-corrections), [Recidiviz](https://www.recidiviz.org/platform-modules/dynamic-classification), [metodología de ProPublica](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm), [datos y código originales](https://github.com/propublica/compas-analysis) y [noticia de partida de Futurism](https://futurism.com/artificial-intelligence/prisons-ai-prediction-incarceration-algorithm).
