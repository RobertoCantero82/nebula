---
imagenPortada: "/nebula/imagenes/aves_ruidosas_portada.png"
titulo: "El concurso para encontrar el ave más ruidosa tenía una regla injusta"
descripcion: "Tres aves parecían disputarse el récord mundial. Al darles las mismas oportunidades, la campeona cambió."
tema: "CIENCIA"
fecha: 2026-10-13
cifraDestacada: "7.724"
etiquetaCifra: "intentos tuvo la primera ganadora"
metodologia: "EDA del suplemento DataS1 de Menezes y Podos, con 123 especies y medidas acústicas normalizadas a un metro. Comparo los máximos LAeq observados con LAeq_max30, la corrección publicada que iguala a 30 fragmentos por especie. El análisis describe asociaciones y no estima el límite anatómico de cada ave ni proclama una campeona mundial definitiva."
---

*Tres aves suben al escenario. No hay público, pero sí un sonómetro. Cada una canta tan fuerte como puede y el valor más alto gana. Parece una competición sencilla. Solo hay un problema: una concursante dispone de 7.724 intentos y otra, de 870.*

## Haz tu apuesta

La **seriema de patas rojas** parece una mezcla de ave y dinosaurio. El **campanero blanco** es famoso por proyectar una llamada potentísima. Su pariente, el **campanero de garganta desnuda**, también juega en la liga de los sonidos extremos.

Antes de conocer las cifras, elige una campeona:

<div class="apuesta-aves" aria-labelledby="pregunta-apuesta">
  <p id="pregunta-apuesta" class="apuesta-pregunta"><strong>¿Qué ave crees que produjo el sonido más intenso?</strong></p>
  <div class="apuesta-opciones" role="group" aria-label="elige un ave">
    <button type="button" data-apuesta="seriema">Seriema</button>
    <button type="button" data-apuesta="blanco">Campanero blanco</button>
    <button type="button" data-apuesta="desnuda">Campanero de garganta desnuda</button>
  </div>
  <p class="apuesta-respuesta" aria-live="polite">Guarda tu intuición. Volveremos a ella después del giro.</p>
</div>

## Primer acto: tenemos ganador

El estudio de João C. T. Menezes y Jeffrey Podos reunió mediciones de **123 especies** registradas en Brasil y Massachusetts. Para comparar sus voces, ajustó el sonido a una distancia común de un metro.

La medida utilizada, LAeq, resume la energía sonora de un fragmento de solo **20 milisegundos**. Es una cincuentava parte de segundo. Algo así como un fotograma acústico, no un canto completo.

Al ordenar el fragmento más intenso de cada especie, el resultado parece claro. El campanero de garganta desnuda alcanza **122,4 decibelios**. La seriema y el campanero blanco empatan a **121,2**. Caso cerrado. O eso parece.

<div class="video-youtube">
  <iframe
    src="https://www.youtube-nocookie.com/embed/wdQbqrPLV74"
    title="Vídeo sobre las aves más ruidosas"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

<style>
  .video-youtube {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    margin: 2rem 0;
    overflow: hidden;
  }

  .video-youtube iframe {
    width: 100%;
    height: 100%;
    border: 0;
  }
</style>

## La pista que no encaja

Un máximo no depende únicamente de lo que un ave puede hacer. También depende de cuántas veces la escuchamos.

Imagina que buscas el lanzamiento más alto de un dado. Si lo tiras 7.724 veces, tendrás muchas más oportunidades de encontrar un resultado excepcional que si lo tiras 870. El dado no mejora. Lo que aumenta es la posibilidad de observar uno de sus extremos.

Eso sucedía aquí. El campanero de garganta desnuda tenía **7.724 fragmentos** disponibles. El campanero blanco, 3.758. La seriema, 870. El primer podio mezclaba potencia vocal con oportunidades de encontrar un instante extraordinario.

<div class="video-youtube">
  <iframe
    src="https://www.youtube-nocookie.com/embed/wdQbqrPLV74"
    title="Vídeo sobre las aves más ruidosas"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

<style>
  .video-youtube {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    margin: 2rem 0;
    overflow: hidden;
  }

  .video-youtube iframe {
    width: 100%;
    height: 100%;
    border: 0;
  }
</style>

## El giro: repetimos la competición

Los investigadores publicaron una segunda medida: el máximo esperado cuando todas las especies compiten con **30 fragmentos**. No inventa cantos nuevos. Repite muchas veces una selección igual de pequeña para reducir la ventaja de quien fue escuchada más.

Pulsa el botón y cambia las reglas del concurso:

<div class="duelo-aves">
  <div class="duelo-controles" role="group" aria-label="elige las reglas de la comparación">
    <button type="button" class="activo" data-modo="observado" aria-pressed="true">Todos los fragmentos</button>
    <button type="button" data-modo="justo" aria-pressed="false">30 por especie</button>
  </div>
  <p id="duelo-veredicto" class="duelo-veredicto" aria-live="polite"><strong>Primer final:</strong> gana el campanero de garganta desnuda con 122,4 dB.</p>
  <div class="grafico-interactivo">
    <canvas id="grafico-aves-podio" height="320" role="img" aria-label="comparación de los máximos sonoros de tres especies antes y después de igualar el número de fragmentos"></canvas>
  </div>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    // recojo la apuesta sin convertirla en una prueba de conocimientos
    const botonesApuesta = document.querySelectorAll('.apuesta-aves [data-apuesta]');
    const respuestaApuesta = document.querySelector('.apuesta-respuesta');

    botonesApuesta.forEach((boton) => {
      boton.addEventListener('click', () => {
        botonesApuesta.forEach((opcion) => opcion.classList.remove('seleccionado'));
        boton.classList.add('seleccionado');
        respuestaApuesta.textContent = `Has elegido: ${boton.textContent}. Ahora veamos qué significaba realmente ganar.`;
      });
    });

    // preparo el podio con la misma escala para que el cambio sea comparable
    const lienzo = document.getElementById('grafico-aves-podio');
    if (!lienzo || !window.Chart) return;

    const etiquetas = ['Seriema', 'Campanero blanco', 'Campanero de garganta desnuda'];
    const modos = {
      observado: {
        valores: [121.2, 121.2, 122.4],
        colores: ['#7257D5', '#7257D5', '#E45756'],
        texto: '<strong>Primer final:</strong> gana el campanero de garganta desnuda con 122,4 dB.',
      },
      justo: {
        valores: [118.5, 117.3, 112.3],
        colores: ['#E45756', '#7257D5', '#7257D5'],
        texto: '<strong>Final después del giro:</strong> gana la seriema con 118,5 dB.',
      },
    };

    const grafico = new Chart(lienzo, {
      type: 'bar',
      data: {
        labels: etiquetas,
        datasets: [{
          data: modos.observado.valores,
          backgroundColor: modos.observado.colores,
          borderRadius: 4,
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => `${context.parsed.x.toLocaleString('es-ES')} dB`,
            },
          },
        },
        scales: {
          x: {
            min: 108,
            max: 124,
            title: { display: true, text: 'máximo LAeq normalizado a un metro (dB)' },
          },
          y: { grid: { display: false } },
        },
      },
    });

    // cambio los datos y el desenlace cuando el lector modifica la regla
    const botonesModo = document.querySelectorAll('.duelo-controles [data-modo]');
    const veredicto = document.getElementById('duelo-veredicto');

    botonesModo.forEach((boton) => {
      boton.addEventListener('click', () => {
        const modo = boton.dataset.modo;
        botonesModo.forEach((opcion) => {
          const estaActivo = opcion === boton;
          opcion.classList.toggle('activo', estaActivo);
          opcion.setAttribute('aria-pressed', String(estaActivo));
        });
        grafico.data.datasets[0].data = modos[modo].valores;
        grafico.data.datasets[0].backgroundColor = modos[modo].colores;
        grafico.update();
        veredicto.innerHTML = modos[modo].texto;
      });
    });
  });
</script>

<style>
  .apuesta-aves,
  .duelo-aves {
    margin: 1.75rem 0;
    padding: 1.25rem;
    border: 1px solid rgba(114, 87, 213, 0.22);
    border-radius: 14px;
    background: rgba(114, 87, 213, 0.055);
  }

  .apuesta-pregunta,
  .duelo-veredicto {
    margin-top: 0;
  }

  .apuesta-opciones,
  .duelo-controles {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin: 1rem 0;
  }

  .apuesta-opciones button,
  .duelo-controles button {
    border: 1px solid #7257d5;
    border-radius: 999px;
    padding: 0.6rem 0.9rem;
    color: #3e326f;
    background: #fff;
    font: inherit;
    cursor: pointer;
  }

  .apuesta-opciones button:hover,
  .apuesta-opciones button:focus-visible,
  .apuesta-opciones button.seleccionado,
  .duelo-controles button:hover,
  .duelo-controles button:focus-visible,
  .duelo-controles button.activo {
    color: #fff;
    background: #7257d5;
  }

  .apuesta-respuesta {
    margin-bottom: 0;
  }
</style>

La campeona cambia. La **seriema** queda primera con **118,5 dB** y el campanero blanco, segundo con 117,3. El campanero de garganta desnuda baja a 112,3.

No se ha vuelto menos ruidoso. Ha perdido una ventaja estadística.

## Lo que revelan diez decibelios

La caída del campanero es de unos **10,2 dB**. Los decibelios usan una escala logarítmica: sumar 10 dB equivale aproximadamente a multiplicar por diez la intensidad física. No significa que nuestro oído perciba el sonido exactamente diez veces más fuerte, pero sí que el cambio está lejos de ser pequeño.

En el conjunto completo, el número de fragmentos y el tamaño de la corrección presentan una asociación por rangos de **0,86**. Las especies observadas más veces son, en general, las que más bajan cuando igualamos las oportunidades.

## La moraleja no es que los récords sean falsos

El máximo de 122,4 dB ocurrió. El campanero de garganta desnuda produjo además un pico instantáneo de 130,9 dB. Los datos no borran esos registros.

Lo que cambia es la pregunta. Si preguntamos “¿cuál fue el fragmento más intenso encontrado?”, gana el campanero. Si preguntamos “¿qué especie obtiene el máximo más alto con las mismas oportunidades?”, gana la seriema.

<div class="video-youtube">
  <iframe
    src="https://www.youtube-nocookie.com/embed/Rs8ovSxMgFQ"
    title="Vídeo sobre las aves más ruidosas"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

Todavía queda otra cautela: 30 fragmentos equivalen a solo **0,6 segundos** acumulados, y el estudio no midió el mismo número de individuos de cada especie. Las 123 especies tampoco representan a las más de 10.000 conocidas. No existe una campeona absoluta; existe una ganadora dentro de cada protocolo.

Los récords parecen cifras puras, pero siempre tienen reglas. A veces, el dato más sorprendente no es quién ganó. Es descubrir que la competición ya estaba inclinada antes de empezar.

Puedes revisar las 123 especies, reproducir los gráficos y seguir cada decisión en el [notebook de Jupyter de las aves ruidosas](/nebula/analisis/aves-ruidosas/analisis_aves_ruidosas.ipynb). El [archivo suplementario utilizado](/nebula/analisis/aves-ruidosas/datos/DataS1.xlsx) también está disponible.

Fuentes: [estudio en *Evolution*](https://doi.org/10.1093/evolut/qpag153), [comunicado de UMass Amherst](https://www.umass.edu/news/article/umass-amherst-biologists-may-have-discovered-two-worlds-loudest-birds) y [artículo de partida en SciTechDaily](https://scitechdaily.com/biologists-may-have-discovered-two-of-the-worlds-loudest-birds/).
