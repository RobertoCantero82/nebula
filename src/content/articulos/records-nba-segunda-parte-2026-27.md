---
titulo: "Los 10 récords NBA que el machine learning ve más cerca de romperse esta temporada: Parte II"
descripcion: "Un triple más puede traer otro récord. Unas derrotas más, también. Diez marcas muestran las dos caras de hacer historia en la NBA."
tema: "BALONCESTO"
fecha: 2026-10-19T08:00:00+02:00
imagenPortada: "/nebula/imagenes/records_nba_segunda_parte_portada.png"
cifraDestacada: "71 derrotas"
etiquetaCifra: "necesitarían los Nets para superar su peor total en la NBA"
metodologia: "EDA de cinco récords positivos de club y cinco negativos, comparados con los totales de 2025-26. Para los negativos selecciono los cinco equipos con menos victorias de ese curso. Utilizo fuentes de la NBA, sus clubes y guías estadísticas, con consulta del 19 de octubre de 2026. Calculo diferencias entre temporadas y el total necesario para superar cada marca; no estimo probabilidades. Distingo derrotas totales, consecutivas y porcentaje de victorias. El notebook incluye los datos, las correcciones al radar anterior y las fuentes."
---

*Hay dos maneras de aparecer en el libro de récords de la NBA. Una termina con el público de pie. La otra, con los aficionados deseando que llegue el verano. A veces, las dos están mucho más cerca de lo que parece.*

Luka Dončić necesita un triple más que la temporada pasada para mejorar su marca con los Lakers. Indiana necesitaría una derrota más para empeorar la suya. La distancia cabe en un dedo, pero nadie quiere estar en el segundo lado.

Después de la [primera entrega](/nebula/articulos/records-nba-predicciones-locas-2026-27/), reúno diez marcas para seguir en 2026-27: cinco positivas y cinco negativas. **¿Qué separa una temporada histórica de una que todos querrían olvidar?**

<div style="position: relative; aspect-ratio: 16 / 9; margin: 28px 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/hic-u8U-3cI"
    title="Vídeo sobre los récords de la NBA"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 8px;"
  ></iframe>
</div>

## Un triple más, pero desde cero

Dončić anotó 254 triples en 64 partidos. Collin Gillespie hizo 232 con Phoenix y Nickeil Alexander-Walker, 251 con Atlanta. Los tres establecieron el récord de su club. Ahora sus objetivos son 255, 233 y 252, respectivamente.
 
Suena sencillo: uno más. Pero octubre vacía el contador. Hay que repetir toda aquella producción antes de añadir la canasta que cambia la historia. La salud, los minutos y las oportunidades para lanzar vuelven a importar desde el primer día.

Golden State tiene una tarea colectiva: alcanzar **2.492 asistencias**, los pases que terminan en canasta de un compañero. Son 123 más que en 2025-26. El salto ronda el 5,2% y permitiría superar su registro de 2016-17.

Jay Huff afronta otra cuesta. El pívot de Indiana necesita 229 tapones, acciones que bloquean el lanzamiento del rival, para superar los 228 de Jermaine O’Neal en 2000-01. Viene de 153: tendría que sumar casi un 50% más. Y ya jugó los 82 partidos. Añadir noches al calendario no resuelve esa diferencia.

El gráfico muestra cuánto tendría que aumentar cada total respecto al curso pasado. Las estadísticas son distintas: ese porcentaje ayuda a comparar el salto, pero no mide la dificultad de conseguirlo.

<figure class="grafico-interactivo grafico-records-nba"><figcaption><strong>Huff necesita el mayor aumento del total</strong></figcaption><ol class="filas-records-nba"><li><span class="nombre-records-nba">Dončić</span><span class="pista-records-nba" aria-hidden="true"><span class="barra-records-nba" style="width:0.65616798%"></span></span><span class="valor-records-nba">0,4%</span></li><li><span class="nombre-records-nba">Gillespie</span><span class="pista-records-nba" aria-hidden="true"><span class="barra-records-nba" style="width:0.71839080%"></span></span><span class="valor-records-nba">0,4%</span></li><li><span class="nombre-records-nba">Alexander-Walker</span><span class="pista-records-nba" aria-hidden="true"><span class="barra-records-nba" style="width:0.66401062%"></span></span><span class="valor-records-nba">0,4%</span></li><li><span class="nombre-records-nba">Golden State</span><span class="pista-records-nba" aria-hidden="true"><span class="barra-records-nba" style="width:8.65344027%"></span></span><span class="valor-records-nba">5,2%</span></li><li><span class="nombre-records-nba">Huff</span><span class="pista-records-nba" aria-hidden="true"><span class="barra-records-nba" style="width:82.78867102%"></span></span><span class="valor-records-nba">49,7%</span></li></ol><div class="escala-records-nba" aria-hidden="true"><span>0%</span><span>30%</span><span>60%</span></div><figcaption>Aumento frente a 2025-26 para superar cada récord.</figcaption><details><summary>Ver las cifras completas</summary><div class="tabla-records-nba"><table><thead><tr><th scope="col">Jugador o equipo</th><th scope="col">Estadística</th><th scope="col">2025-26</th><th scope="col">Récord</th><th scope="col">Para superarlo</th></tr></thead><tbody><tr><td>Luka Dončić</td><td>Triples</td><td>254</td><td>254</td><td>255</td></tr><tr><td>Collin Gillespie</td><td>Triples</td><td>232</td><td>232</td><td>233</td></tr><tr><td>Nickeil Alexander-Walker</td><td>Triples</td><td>251</td><td>251</td><td>252</td></tr><tr><td>Golden State Warriors</td><td>Asistencias</td><td>2369</td><td>2491</td><td>2492</td></tr><tr><td>Jay Huff</td><td>Tapones</td><td>153</td><td>228</td><td>229</td></tr></tbody></table></div></details></figure>

## Perder también cuenta

**Indiana terminó con 63 derrotas**, su peor total desde que juega en la NBA. Una temporada con 64 dejaría otra marca indeseada. Sin embargo, la vuelta de Tyrese Haliburton, ausente durante todo 2025-26, cambia el punto de partida. Aquellas derrotas pertenecen al equipo que acabó aquel curso.

**Washington perdió 65 veces**, aunque su peor año sigue siendo el de las 67 derrotas de 2023-24. Para superarlo tendría que llegar a 68. Traducido a alegrías: ganar como máximo 14 de los 82 partidos.

**Utah y Sacramento vienen de 60 derrotas** y necesitarían 66 para superar sus respectivos récords. **Brooklyn** está más lejos: pasar de **62** a 71 derrotas dejaría atrás las 70 de los Nets de New Jersey en 2009-10. Sería perder casi nueve de cada diez noches.

Los puntos grises muestran las derrotas de 2025-26; los azules, cuántas harían falta para superar cada marca. Son diferencias entre temporadas, no derrotas acumuladas en la nueva.

<figure class="grafico-interactivo grafico-records-nba"><figcaption><strong>Cinco equipos y sus marcas más incómodas</strong></figcaption><ol class="filas-records-nba filas-derrotas-nba"><li><span class="nombre-records-nba">Indiana</span><span class="pista-records-nba pista-derrotas-nba" aria-hidden="true"><span class="tramo-records-nba" style="left:76.82926829%;width:1.21951220%"></span><span class="punto-records-nba punto-anterior-nba" style="left:76.82926829%"></span><span class="punto-records-nba punto-objetivo-nba" style="left:78.04878049%"></span></span><span class="valor-records-nba">63 → 64</span></li><li><span class="nombre-records-nba">Washington</span><span class="pista-records-nba pista-derrotas-nba" aria-hidden="true"><span class="tramo-records-nba" style="left:79.26829268%;width:3.65853659%"></span><span class="punto-records-nba punto-anterior-nba" style="left:79.26829268%"></span><span class="punto-records-nba punto-objetivo-nba" style="left:82.92682927%"></span></span><span class="valor-records-nba">65 → 68</span></li><li><span class="nombre-records-nba">Sacramento</span><span class="pista-records-nba pista-derrotas-nba" aria-hidden="true"><span class="tramo-records-nba" style="left:73.17073171%;width:7.31707317%"></span><span class="punto-records-nba punto-anterior-nba" style="left:73.17073171%"></span><span class="punto-records-nba punto-objetivo-nba" style="left:80.48780488%"></span></span><span class="valor-records-nba">60 → 66</span></li><li><span class="nombre-records-nba">Utah</span><span class="pista-records-nba pista-derrotas-nba" aria-hidden="true"><span class="tramo-records-nba" style="left:73.17073171%;width:7.31707317%"></span><span class="punto-records-nba punto-anterior-nba" style="left:73.17073171%"></span><span class="punto-records-nba punto-objetivo-nba" style="left:80.48780488%"></span></span><span class="valor-records-nba">60 → 66</span></li><li><span class="nombre-records-nba">Brooklyn</span><span class="pista-records-nba pista-derrotas-nba" aria-hidden="true"><span class="tramo-records-nba" style="left:75.60975610%;width:10.97560976%"></span><span class="punto-records-nba punto-anterior-nba" style="left:75.60975610%"></span><span class="punto-records-nba punto-objetivo-nba" style="left:86.58536585%"></span></span><span class="valor-records-nba">62 → 71</span></li></ol><div class="escala-records-nba escala-derrotas-nba" aria-hidden="true"><span>0</span><span>41</span><span>82</span></div><figcaption>Derrotas en 2025-26 (gris) y total para superar el récord (azul).</figcaption><details><summary>Ver las cifras completas</summary><div class="tabla-records-nba"><table><thead><tr><th scope="col">Jugador o equipo</th><th scope="col">Estadística</th><th scope="col">2025-26</th><th scope="col">Récord</th><th scope="col">Para superarlo</th></tr></thead><tbody><tr><td>Indiana Pacers</td><td>Derrotas</td><td>63</td><td>63</td><td>64</td></tr><tr><td>Washington Wizards</td><td>Derrotas</td><td>65</td><td>67</td><td>68</td></tr><tr><td>Sacramento Kings</td><td>Derrotas</td><td>60</td><td>65</td><td>66</td></tr><tr><td>Utah Jazz</td><td>Derrotas</td><td>60</td><td>65</td><td>66</td></tr><tr><td>Brooklyn Nets</td><td>Derrotas</td><td>62</td><td>70</td><td>71</td></tr></tbody></table></div></details></figure>

## ¿Qué temporada fue peor?

Hay una trampa al contar derrotas: no todos los años tuvieron la misma cantidad de partidos. Antes de seguir, propongo elegir entre dos temporadas que ningún aficionado querría repetir.

<div class="grafico-interactivo apuesta-records-nba" id="apuesta-records-nba" aria-labelledby="pregunta-records-nba">
  <p id="pregunta-records-nba"><strong>¿Qué equipo ganó una proporción menor de sus partidos?</strong></p>
  <div class="opciones-records-nba" role="group" aria-label="Elige un equipo">
    <button type="button" data-eleccion="philadelphia" aria-pressed="false">Philadelphia: 73 derrotas</button>
    <button type="button" data-eleccion="charlotte" aria-pressed="false">Charlotte: 59 derrotas</button>
  </div>
  <p id="eleccion-records-nba" aria-live="polite"></p>
  <details id="respuesta-records-nba">
    <summary>Ver la respuesta</summary>
    <p><strong>Charlotte.</strong> Los Bobcats ganaron 7 de 66 partidos en 2011-12: el 10,61%. Philadelphia ganó 9 de 82 en 1972-73: el 10,98%. Charlotte perdió menos veces porque jugó menos partidos, pero ganó una proporción todavía menor.</p>
  </details>
</div>

En una temporada de 82 partidos, acabar con ocho victorias y 74 derrotas bastaría para superar las 73 de Philadelphia y quedar por debajo del porcentaje de Charlotte. Un desastre capaz de batir dos marcas a la vez.

También existe el récord de perder sin descanso. **Detroit encadenó 28 derrotas en 2023-24**. Philadelphia llegó igualmente a 28, repartidas entre dos temporadas. Superarlas exigiría perder 29 partidos consecutivos: una sola victoria por el camino rompe la cadena.

<div style="position: relative; aspect-ratio: 16 / 9; margin: 28px 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/BkrdizJHKLA"
    title="Vídeo de baloncesto"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 8px;"
  ></iframe>
</div>

## Detroit encontró la salida

Precisamente Detroit recuerda que estas historias pueden cambiar. Pasó de 14 victorias en 2023-24 a 44 en el curso siguiente y 60 en 2025-26. En dos temporadas perdió 46 partidos menos.

Por eso miro los récords negativos con cuidado. Estar cerca el año anterior no condena a repetirlo. Tampoco haber metido 254 triples garantiza volver a hacerlo. El calendario, los compañeros y el papel de cada jugador pueden cambiar.

Los diez casos ofrecen motivos para seguir la temporada. Unos invitan a contar canastas y otros a respirar después de una victoria. **Hacer historia puede ser una fiesta o un alivio cuando, por fin, deja de ocurrir.**

Puedes consultar los cálculos y las fuentes en el [notebook de esta segunda parte](/nebula/analisis/records-nba-segunda-parte/records_nba_segunda_parte_eda.ipynb) y descargar los [datos de los diez récords](/nebula/analisis/records-nba-segunda-parte/records_segunda_parte.csv).

Fuentes: [Lakers](https://www.nba.com/lakers/news/luka-doncic-earns-sixth-all-nba-first-team-honor), [Phoenix](https://cdn-uat.nba.com/news/2026-27-season-preview-phx), [NBA Communications](https://pr.nba.com/hawks-nickeil-alexander-walker-named-2025-26-kia-nba-most-improved-player/), [Pacers](/nebula/analisis/records-nba-segunda-parte/fuentes/pacers_guia_20261019.pdf), [Warriors](/nebula/analisis/records-nba-segunda-parte/fuentes/warriors_20261019.pdf) y [lista completa de referencias](/nebula/analisis/records-nba-segunda-parte/auditoria_fuentes.csv).

<style>
  .filas-records-nba { list-style: none; padding: 0; margin: 1.2rem 0 .4rem; }
  .filas-records-nba li { display: grid; grid-template-columns: 145px minmax(0,1fr) 52px; align-items: center; gap: 10px; margin: 1.25rem 0; font-size: 14px; line-height: 1.3; }
  .nombre-records-nba { overflow-wrap: anywhere; }
  .pista-records-nba { position: relative; display: block; height: 22px; border-left: 1px solid #c7cedd; border-right: 1px solid #c7cedd; background: linear-gradient(to right,transparent 49.8%,#e7eaf2 49.8%,#e7eaf2 50.2%,transparent 50.2%); }
  .barra-records-nba { display: block; min-width: 2px; height: 100%; background: #446ddf; border-radius: 2px; }
  .valor-records-nba { font-variant-numeric: tabular-nums; white-space: nowrap; text-align: right; }
  .escala-records-nba { display: flex; justify-content: space-between; margin: 0 62px 0 155px; font-size: 12px; color: #55576a; }
  .filas-derrotas-nba li { grid-template-columns: 110px minmax(0,1fr) 68px; }
  .escala-derrotas-nba { margin-left: 120px; margin-right: 78px; }
  .punto-records-nba { position: absolute; top: 50%; width: 10px; height: 10px; margin: -5px 0 0 -5px; border-radius: 50%; }
  .punto-anterior-nba { background: #777f8e; }
  .punto-objetivo-nba { background: #446ddf; }
  .tramo-records-nba { position: absolute; height: 3px; top: 9px; background: #b4c5f0; }
  @media (max-width: 520px) {
    .filas-records-nba li { grid-template-columns: 108px minmax(0,1fr) 46px; gap: 6px; font-size: 12px; }
    .escala-records-nba { margin-left: 114px; margin-right: 52px; }
    .filas-derrotas-nba li { grid-template-columns: 82px minmax(0,1fr) 56px; }
    .escala-derrotas-nba { margin-left: 88px; margin-right: 62px; }
  }

  .opciones-records-nba { display: flex; flex-wrap: wrap; gap: .75rem; margin: 1rem 0; }
  .opciones-records-nba button { flex: 1 1 180px; padding: .85rem 1rem; border: 1px solid #446ddf; border-radius: 5px; background: #fff; color: #25479e; font: inherit; cursor: pointer; }
  .opciones-records-nba button:hover, .opciones-records-nba button[aria-pressed="true"] { color: #fff; background: #446ddf; }
  .opciones-records-nba button:focus-visible { outline: 3px solid #1b1836; outline-offset: 3px; }
  .apuesta-records-nba summary { cursor: pointer; color: #25479e; text-decoration: underline; }
  .apuesta-records-nba details[open] { margin-top: 1rem; }
  .grafico-records-nba svg { width: 100%; height: auto; display: block; }
  .grafico-records-nba figcaption { font-size: .85rem; color: #55576a; margin-top: .7rem; line-height: 1.5; }
  .grafico-records-nba details { margin-top: .8rem; font-size: .85rem; }
  .grafico-records-nba .tabla-records-nba { overflow-x: auto; }
  .grafico-records-nba { margin-left: 0; margin-right: 0; }
  @media (max-width: 520px) { .grafico-records-nba { padding: 10px; } }
</style>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const caja = document.getElementById('apuesta-records-nba');
    if (!caja) return;
    const respuesta = caja.querySelector('#respuesta-records-nba');
    const estado = caja.querySelector('#eleccion-records-nba');
    caja.querySelectorAll('[data-eleccion]').forEach(boton => {
      boton.addEventListener('click', () => {
        caja.querySelectorAll('[data-eleccion]').forEach(opcion => {
          opcion.setAttribute('aria-pressed', String(opcion === boton));
        });
        estado.textContent = boton.dataset.eleccion === 'charlotte'
          ? 'Charlotte: sí, el calendario corto cambia la comparación.'
          : 'Philadelphia perdió más partidos, pero Charlotte ganó una proporción menor.';
        respuesta.open = true;
      });
    });
  });
</script>
