---
titulo: '"Los móviles de ahora no aguantan nada": ¿seguro que antes duraban más?'
descripcion: 'El Nokia 3310 entra en el debate. Comparo doce smartphones de una década y separo autonomía, desgaste y reparación.'
tema: 'TECNOLOGÍA'
fecha: 2026-10-20
imagenPortada: '/nebula/imagenes/moviles_resistencia_portada.png'
cifraDestacada: '+128 %'
etiquetaCifra: 'autonomía del Galaxy S25 frente al S6 en la prueba Wi-Fi'
metodologia: 'EDA de doce modelos de tres familias (iPhone, Galaxy S y Moto G) en 2015, 2018, 2021 y 2025. Comparo los resultados exactos de navegación Wi-Fi v1.3 de Notebookcheck y compruebo once datos de vídeo. Es un panel intencional, no representativo del mercado; cambian tamaños, navegadores, software y equipo de ensayo. Para el Nokia 3310 de 2000 utilizo su comunicado y manual, sin mezclar máximos de espera o conversación con horas de navegación. Separo las especificaciones de ciclos de Apple de las mediciones independientes y comparo instrucciones de sustitución de batería. No estimo años de vida ni declaro un ganador histórico en caídas.'
---

Siempre hay alguien que lo dice antes del café: "Los móviles de ahora no aguantan nada". Después aparece el Nokia 3310, elevado a patrimonio de la humanidad. Se caía, salía la batería y volvía a funcionar. El suelo estaba peor que el teléfono.

La escena merece un aplauso. La conclusión necesita una comprobación. Porque "aguantar" puede significar llegar a la noche sin enchufe, conservar la batería durante años o sobrevivir a una caída. Y esas tres cosas no se miden con el mismo cronómetro.

<fieldset id="reto-nokia">
  <legend>Antes de sacar al Nokia del cajón…</legend>
  <p>
    Tú también recuerdas que la batería duraba una eternidad.
    Pero ¿cuánto anunciaba Nokia que aguantaba el 3310
    <strong>hablando sin parar</strong> con su batería estándar?
  </p>

  <div class="reto-nokia-opciones">
    <button type="button" data-acierto="true" aria-pressed="false">
      Cuatro horas y media
    </button>
    <button type="button" aria-pressed="false">
      Un día entero
    </button>
    <button type="button" aria-pressed="false">
      Casi once días
    </button>
  </div>

  <p class="reto-nokia-resultado" aria-live="polite">
    Haz tu apuesta. Aquí la nostalgia también pasa examen.
  </p>
</fieldset>

<style>
  #reto-nokia {
    margin: 2rem 0;
    padding: 1.25rem;
    min-width: 0;
    border: 1px solid #446ddf55;
    border-radius: 14px;
    background: #446ddf08;
  }

  #reto-nokia legend {
    padding: 0 .4rem;
    font-weight: 700;
  }

  .reto-nokia-opciones {
    display: flex;
    flex-wrap: wrap;
    gap: .6rem;
  }

  .reto-nokia-opciones button {
    padding: .7rem 1rem;
    border: 1px solid #446ddf;
    border-radius: 8px;
    background: white;
    color: #294da9;
    font: inherit;
    cursor: pointer;
  }

  .reto-nokia-opciones button[aria-pressed="true"] {
    background: #446ddf;
    color: white;
  }

  .reto-nokia-opciones button:focus-visible {
    outline: 3px solid #d85a30;
    outline-offset: 3px;
  }

  #reto-nokia .reto-nokia-resultado {
    margin-bottom: 0;
    line-height: 1.6;
  }
</style>

<script>
(() => {
  const iniciar = () => {
    const reto = document.getElementById('reto-nokia');
    if (!reto || reto.dataset.iniciado) return;
    reto.dataset.iniciado = 'si';

    const botones = reto.querySelectorAll('button');
    const resultado = reto.querySelector('.reto-nokia-resultado');

    botones.forEach(boton => {
      boton.addEventListener('click', () => {
        botones.forEach(opcion => {
          opcion.setAttribute('aria-pressed', String(opcion === boton));
        });

        const entrada = boton.dataset.acierto === 'true'
          ? 'Has acertado. Buena memoria, además de cariño al ladrillo.'
          : 'La nostalgia acaba de pedir el comodín del público.';

        resultado.textContent = entrada +
          ' Nokia anunciaba hasta cuatro horas y media de conversación.' +
          ' Los casi once días eran en espera: conectado a la red,' +
          ' sin mantener una conversación continua.' +
          ' Las dos cifras eran máximos anunciados, no una prueba de uso cotidiano.';
      });
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', iniciar, { once: true });
  } else {
    iniciar();
  }
})();
</script>

## El Nokia no estuvo diez días viendo vídeos

El [comunicado con el que Nokia presentó el 3310](https://www.globenewswire.com/news-release/2000/09/01/1845525/0/en/Nokia-introduces-mobile-chat-with-the-Nokia-3310.html) en septiembre de 2000 anunciaba hasta **260 horas en espera** y **cuatro horas y media de conversación** con su batería estándar. Las primeras equivalen a casi once días. Las segundas, a una sobremesa especialmente peligrosa.

Ambas cifras podían convivir porque describían tareas distintas. Esperar una llamada no consume lo mismo que mantener una conversación. Mucho menos que llevar una pantalla encendida navegando, reproduciendo vídeos o enseñándonos cómo llegar a una dirección.

Por eso no enfrento los once días anunciados del Nokia con las horas de navegación de un smartphone. Sería comparar cuánto aguanta un coche aparcado con cuánto recorre en carretera. El ladrillo conserva su leyenda, pero no gana por incomparecencia del rival.

<div style="position:relative;width:100%;aspect-ratio:16/9;margin:2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/BtfIz74gCD8"
    title="Vídeo de YouTube sobre teléfonos móviles"
    style="position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:12px;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>  

## La prueba que sí podemos compartir

He reunido doce resultados de [Notebookcheck](https://www.notebookcheck.net/How-does-Notebookcheck-test-laptops-and-smartphones-A-behind-the-scenes-look-into-our-review-process.15394.0.html): cuatro generaciones de **iPhone, Galaxy S y Moto G**, entre 2015 y 2025. Es una selección de tres familias, no todo el mercado. Elijo 2025 como último año completo y añado 2018 y 2021 para no quedarme solo con los extremos.

Comparten una prueba de navegación por Wi-Fi y un brillo de referencia parecido. Cambian los navegadores y el software, así que no es un laboratorio congelado durante una década. Aun así, ofrece una comparación bastante más razonable que enfrentar recuerdos con anuncios.

Antes de mirar, haz tu apuesta: ¿qué generación crees que aguanta más en las tres parejas, la de 2015 o la de 2025?

<fieldset class="moviles-apuesta" id="moviles-apuesta">
  <legend>Tu apuesta antes de ver las cifras</legend>
  <p>¿Qué año gana en las tres parejas de navegación por Wi-Fi?</p>
  <div class="moviles-opciones">
    <button type="button" data-voto="2015" aria-pressed="false">2015: los veteranos</button>
    <button type="button" data-voto="2025" aria-pressed="false">2025: los recientes</button>
    <button type="button" data-voto="empate" aria-pressed="false">Quedan empatados</button>
  </div>
  <p id="moviles-veredicto" aria-live="polite">Elige un año y comprueba tu intuición.</p>
</fieldset>

El gráfico muestra **horas de navegación**: cuanto más larga sea la barra, más tardó en agotarse la carga. Puedes cambiar de familia para seguir sus cuatro modelos.

<section class="moviles-grafico" aria-labelledby="moviles-titulo-grafico">
<h3 id="moviles-titulo-grafico">Los tres modelos de 2025 superan a sus referencias de 2015</h3>
<div class="moviles-filtro" hidden><label for="moviles-familia">Familia de móviles</label><select id="moviles-familia"><option value="Galaxy S">Galaxy S</option><option value="iPhone">iPhone</option><option value="Moto G">Moto G</option><option value="todas">Ver las tres</option></select></div>
<p class="moviles-nota">Horas de navegación por Wi-Fi. Todas las barras usan la misma escala, de 0 a 24 horas.</p>
<div class="moviles-panel" data-familia="Galaxy S"><h4>Galaxy S</h4><ul><li><div class="moviles-fila"><span>2015 · Samsung Galaxy S6</span><strong>7 h 55 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:32.98611%"></span></div></li><li><div class="moviles-fila"><span>2018 · Samsung Galaxy S9</span><strong>7 h 54 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:32.91667%"></span></div></li><li><div class="moviles-fila"><span>2021 · Samsung Galaxy S21</span><strong>9 h 04 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:37.77778%"></span></div></li><li><div class="moviles-fila"><span>2025 · Samsung Galaxy S25</span><strong>18 h 02 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:75.13889%"></span></div></li></ul></div>
<div class="moviles-panel" data-familia="iPhone"><h4>iPhone</h4><ul><li><div class="moviles-fila"><span>2015 · Apple iPhone 6s</span><strong>8 h 12 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:34.16667%"></span></div></li><li><div class="moviles-fila"><span>2018 · Apple iPhone XR</span><strong>15 h 10 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:63.19444%"></span></div></li><li><div class="moviles-fila"><span>2021 · Apple iPhone 13</span><strong>16 h 59 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:70.76389%"></span></div></li><li><div class="moviles-fila"><span>2025 · Apple iPhone 17</span><strong>20 h 03 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:83.54167%"></span></div></li></ul></div>
<div class="moviles-panel" data-familia="Moto G"><h4>Moto G</h4><ul><li><div class="moviles-fila"><span>2015 · Motorola Moto G (2015)</span><strong>8 h 46 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:36.52778%"></span></div></li><li><div class="moviles-fila"><span>2018 · Motorola Moto G6</span><strong>9 h 13 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:38.40278%"></span></div></li><li><div class="moviles-fila"><span>2021 · Motorola Moto G30</span><strong>17 h 49 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:74.23611%"></span></div></li><li><div class="moviles-fila"><span>2025 · Motorola Moto G86</span><strong>17 h 18 min</strong></div><div class="moviles-pista" aria-hidden="true"><span style="width:72.08333%"></span></div></li></ul></div>
<p id="moviles-lectura" class="moviles-nota" aria-live="polite">Fuente: pruebas Wi-Fi v1.3 de Notebookcheck. Doce modelos de 2015, 2018, 2021 y 2025; brillo de referencia de 150 nits. Los navegadores y el software cambian entre pruebas. No mide años de vida útil.</p>
<details><summary>Consulta los doce resultados y sus fuentes</summary><div class="moviles-tabla"><table><caption>Resultados publicados cuando cada modelo era nuevo</caption><thead><tr><th scope="col">Modelo</th><th scope="col">Año</th><th scope="col">Navegación Wi-Fi</th><th scope="col">Fuente</th></tr></thead><tbody><tr><td>Samsung Galaxy S6</td><td>2015</td><td>7 h 55 min</td><td><a href="https://www.notebookcheck.net/Samsung-Galaxy-S6-Smartphone-Review.140249.0.html">Prueba original de Samsung Galaxy S6</a></td></tr><tr><td>Samsung Galaxy S9</td><td>2018</td><td>7 h 54 min</td><td><a href="https://www.notebookcheck.net/Samsung-Galaxy-S9-Smartphone-Review.293936.0.html">Prueba original de Samsung Galaxy S9</a></td></tr><tr><td>Samsung Galaxy S21</td><td>2021</td><td>9 h 04 min</td><td><a href="https://www.notebookcheck.net/Samsung-Galaxy-S21-smartphone-review-The-most-affordable-high-end-Galaxy.522690.0.html">Prueba original de Samsung Galaxy S21</a></td></tr><tr><td>Samsung Galaxy S25</td><td>2025</td><td>18 h 02 min</td><td><a href="https://www.notebookcheck.net/Samsung-Galaxy-S25-review-The-star-among-compact-smartphones-is-losing-ground.989246.0.html">Prueba original de Samsung Galaxy S25</a></td></tr><tr><td>Motorola Moto G (2015)</td><td>2015</td><td>8 h 46 min</td><td><a href="https://www.notebookcheck.net/Motorola-Moto-G-3rd-Generation-Smartphone-Review.147931.0.html">Prueba original de Motorola Moto G (2015)</a></td></tr><tr><td>Motorola Moto G6</td><td>2018</td><td>9 h 13 min</td><td><a href="https://www.notebookcheck.net/Motorola-Moto-G6-Smartphone-Review.303202.0.html">Prueba original de Motorola Moto G6</a></td></tr><tr><td>Motorola Moto G30</td><td>2021</td><td>17 h 49 min</td><td><a href="https://www.notebookcheck.net/Motorola-Moto-G30-Review-90-Hz-smartphone-with-an-IP-certification-and-NFC-for-less-than-180-Euros.530863.0.html">Prueba original de Motorola Moto G30</a></td></tr><tr><td>Motorola Moto G86</td><td>2025</td><td>17 h 18 min</td><td><a href="https://www.notebookcheck.net/The-brightest-star-in-the-midrange-Motorola-Moto-G86-smartphone-review.1069107.0.html">Prueba original de Motorola Moto G86</a></td></tr><tr><td>Apple iPhone 6s</td><td>2015</td><td>8 h 12 min</td><td><a href="https://www.notebookcheck.net/Apple-iPhone-6S-Smartphone-Review.151403.0.html">Prueba original de Apple iPhone 6s</a></td></tr><tr><td>Apple iPhone XR</td><td>2018</td><td>15 h 10 min</td><td><a href="https://www.notebookcheck.net/Apple-iPhone-XR-Smartphone-Review.346971.0.html">Prueba original de Apple iPhone XR</a></td></tr><tr><td>Apple iPhone 13</td><td>2021</td><td>16 h 59 min</td><td><a href="https://www.notebookcheck.net/Apple-iPhone-13-Smartphone-Review-High-quality-Apple-phone-with-an-even-brighter-display.572153.0.html">Prueba original de Apple iPhone 13</a></td></tr><tr><td>Apple iPhone 17</td><td>2025</td><td>20 h 03 min</td><td><a href="https://www.notebookcheck.net/Apple-iPhone-17-smartphone-review-The-best-iPhone-of-the-year-is-unbelievably-close-to-an-iPhone-Pro.1129296.0.html">Prueba original de Apple iPhone 17</a></td></tr></tbody></table></div></details>
</section>

El Galaxy S6 registró **7 horas y 55 minutos**. El S25 llegó a **18 horas y 2 minutos**: un **128 % más**. El iPhone pasó de 8 horas y 12 minutos a 20 horas y 3 minutos. El Moto G, de 8 horas y 46 minutos a 17 horas y 18 minutos. Los tres modelos recientes ganan sus respectivas parejas.

Eso no significa que cada generación mejore siempre. El Moto G30 de 2021 duró 31 minutos más que el G86 de 2025. El progreso también tiene días de pedir el cargador.

## Una carga no es toda una vida

Estas pruebas utilizan teléfonos nuevos. No dicen cómo estarán después de tres veranos, cientos de cargas y una vida al fondo del bolso.

Para el desgaste, [Apple declara](https://support.apple.com/es-es/106348) que las baterías del iPhone 14 y anteriores están diseñadas para conservar el 80 % de capacidad tras 500 ciclos completos en condiciones ideales. Para el iPhone 15 y posteriores, eleva la cifra a 1.000.

Un ciclo no es cada vez que enchufas: varias cargas parciales pueden sumar uno. Y conservar el 80 % tampoco significa que el teléfono muera al siguiente mensaje. Son especificaciones de la empresa, no años de supervivencia comprobados por mí ni una conclusión sobre todas las marcas.

El propio [manual del Nokia](https://www.manuallib.com/download/NOKIA-3310-USER-GUIDE.PDF) ya avisaba de que la batería acabaría desgastándose. La inmortalidad no venía incluida en la caja.

<div style="aspect-ratio:16/9;margin:2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/QqwqEUgLPk0"
    title="Vídeo de YouTube"
    style="width:100%;height:100%;border:0;border-radius:12px;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

## Donde el ladrillo sí tenía una ventaja

En el 3310 podías retirar la tapa y sacar la batería mediante pestañas. Cambiar una pieza gastada no exigía despegar el teléfono. Esa comodidad sí está documentada y ya faltaba en el Galaxy S6 de 2015.

Tampoco desapareció de todos los móviles modernos: el [Fairphone Gen. 6 permite sustituirla siguiendo una guía](https://support.fairphone.com/hc/en-us/articles/37412807551634-How-to-replace-the-battery-in-The-Fairphone-Gen-6), aunque requiere destornillador y siete tornillos. Reparar sigue siendo una decisión de diseño.

Sobre los golpes, no he encontrado una serie que enfrente al Nokia y a los actuales con igual altura, suelo y criterio de rotura. Su manual pedía evitarlos; eso no demuestra que fuese frágil. Dejo ese duelo sin ganador.

Decir que los móviles de ahora duran menos es quedarse a medias. En los modelos comparados, la batería aguanta más con una carga, aunque cambiarla no siempre sea tan fácil como en el Nokia. Y sobre los golpes, faltan pruebas para dar un ganador. El viejo ladrillo tenía sus ventajas, pero la nostalgia también le ha echado una mano.


## Fuentes y cuadernos

Puedes revisar la [preparación de los datos](/nebula/analisis/moviles-resistencia/01_preparacion_moviles.ipynb), el [EDA ejecutado](/nebula/analisis/moviles-resistencia/02_eda_moviles.ipynb), la [tabla de autonomía](/nebula/analisis/moviles-resistencia/data/processed/autonomia.csv) y las [fuentes y limitaciones](/nebula/analisis/moviles-resistencia/README.md). La [carpeta completa comprimida](/nebula/analisis/moviles-resistencia/moviles_resistencia.zip) contiene los cuadernos y los datos necesarios para reproducirlos sin conexión a las fuentes originales, una vez instaladas las dependencias.

<style>
  .moviles-apuesta,.moviles-grafico{margin:2rem 0;padding:1.4rem;border:1px solid #446ddf40;border-radius:14px;background:#446ddf06;min-width:0}
  .moviles-apuesta legend{padding:0 .4rem;font-weight:700;color:#1b1836}
  .moviles-opciones{display:flex;gap:.6rem;flex-wrap:wrap}
  .moviles-opciones button{font:inherit;padding:.65rem .9rem;border:1px solid #446ddf;border-radius:8px;background:white;color:#294da9;cursor:pointer}
  .moviles-opciones button[aria-pressed="true"]{background:#446ddf;color:white}
  .moviles-opciones button:focus-visible,.moviles-filtro select:focus-visible,.moviles-grafico summary:focus-visible{outline:3px solid #d85a30;outline-offset:4px}
  #moviles-veredicto{min-height:3.4em;margin-bottom:0}
  .moviles-grafico h3{font-size:1.2rem;line-height:1.4;margin-top:0}
  .moviles-filtro:not([hidden]){display:flex;align-items:center;gap:.8rem;flex-wrap:wrap;margin:1rem 0}
  .moviles-filtro label{font-weight:700}
  .moviles-filtro select{font:inherit;padding:.5rem .75rem;border:1px solid #446ddf;border-radius:6px;background:white;color:#1b1836;max-width:100%}
  .moviles-panel[hidden]{display:none}
  .moviles-panel h4{margin:1rem 0 .8rem}
  .moviles-panel ul{list-style:none;padding:0!important;margin:0}
  .moviles-panel li{margin:1rem 0}
  .moviles-fila{display:flex;justify-content:space-between;gap:.8rem;line-height:1.45;font-size:.94rem}
  .moviles-fila strong{white-space:nowrap;font-variant-numeric:tabular-nums}
  .moviles-pista{height:16px;background:#446ddf13;border-radius:3px;margin-top:.35rem}
  .moviles-pista span{display:block;height:100%;background:#446ddf;border-radius:3px}
  .moviles-nota{font-size:.86rem;line-height:1.6;color:#55516a}
  .moviles-grafico summary{cursor:pointer;font-weight:600;padding:.4rem 0;color:#294da9}
  .moviles-tabla{overflow-x:auto;max-width:100%}
  .moviles-tabla table{font-size:.85rem;width:100%;border-collapse:collapse}
  .moviles-tabla th,.moviles-tabla td{text-align:left;padding:.55rem;border-bottom:1px solid #446ddf26}
  .moviles-tabla caption{text-align:left;margin:.7rem 0}
  @media(max-width:480px){.moviles-apuesta,.moviles-grafico{padding:1rem}.moviles-fila{font-size:.85rem}.moviles-fila span{max-width:65%}}
</style>
<script>
(() => {
  const iniciar = () => {
    const apuesta = document.getElementById('moviles-apuesta');
    if (!apuesta || apuesta.dataset.lista) return;
    apuesta.dataset.lista = 'si';
    const salida = document.getElementById('moviles-veredicto');
    apuesta.querySelectorAll('[data-voto]').forEach(boton => boton.addEventListener('click', () => {
      apuesta.querySelectorAll('[data-voto]').forEach(b => b.setAttribute('aria-pressed', String(b === boton)));
      const entrada = boton.dataset.voto === '2025' ? 'Has acertado.' : 'Esta vez ganan los recientes.';
      salida.textContent = entrada + ' Los tres modelos de 2025 superan a sus parejas de 2015 en navegación por Wi-Fi. Eso no dice cuántos años durarán ni cuántas caídas resistirán.';
    }));
    const selector = document.getElementById('moviles-familia');
    const filtro = document.querySelector('.moviles-filtro');
    const lecturas = {
      'Galaxy S':'El Galaxy S6 registró 7 h 55 min; el S25, 18 h 02 min: un 128 % más en esta prueba. El S9 quedó un minuto por debajo del S6, una diferencia que no interpreto como significativa.',
      'iPhone':'El iPhone 6s registró 8 h 12 min; el iPhone 17, 20 h 03 min: un 145 % más en esta prueba. Los tamaños, los navegadores y el software no son idénticos.',
      'Moto G':'El Moto G de 2015 registró 8 h 46 min; el G86, 17 h 18 min: un 97 % más. Sin embargo, el G30 de 2021 aguantó 31 minutos más que el G86.',
      'todas':'Los tres modelos de 2025 superan a sus referencias de 2015. Las mejoras van del 97 % al 145 %. Son tres familias seleccionadas, no todo el mercado.'
    };
    const actualizar = () => {
      document.querySelectorAll('.moviles-panel').forEach(panel => { panel.hidden = selector.value !== 'todas' && panel.dataset.familia !== selector.value; });
      document.getElementById('moviles-lectura').textContent = lecturas[selector.value] + ' Fuente: Notebookcheck, prueba Wi-Fi v1.3 con brillo de referencia de 150 nits. No mide años de vida útil.';
    };
    filtro.hidden = false;
    selector.addEventListener('change', actualizar);
    actualizar();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar, {once:true});
  else iniciar();
})();
</script>
