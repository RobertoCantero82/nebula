---
imagenPortada: "/nebula/imagenes/conexiones_imposibles_02.png"
titulo: "'Big' y 'Men in Black' están conectadas: ¿a través de los datos o hay algo más?"
descripcion: "15.741 espectadores, un director, dos hermanos y una canción que llevaba nueve años esperando."
tema: "CINE"
serie: "trama"
fecha: 2026-11-12
cifraDestacada: "9 años"
etiquetaCifra: "separan dos películas mucho más próximas de lo que parecen"
textoContinuo: "Son 9 años los que separan 'Big' y 'Men in Black'. Los datos demuestran que entre ambas hay más de un camino y una sola conexión definitiva."
metodologia: "EDA de 32.000.204 valoraciones sobre 84.432 películas de MovieLens 32M, géneros, etiquetas y créditos comprobados en AFI, Amblin y Sony. Comparo Big (MovieLens 2797) con Men in Black (MovieLens 1580). No genero predicciones."
---

Un niño cierra los ojos ante una máquina de feria y desea ser mayor. Nueve años después, dos agentes vestidos de negro borran recuerdos mientras vigilan extraterrestres en Nueva York. ***Big* y *Men in Black* parecen vivir en universos distintos, pero están conectadas**. El problema es que esta vez hay demasiadas respuestas posibles.

He cruzado 32 millones de valoraciones, géneros, etiquetas y créditos. Los datos encuentran espectadores comunes, temas parecidos y dos puentes profesionales difíciles de superar. Sin embargo, la conexión más directa estaba sonando desde el principio. Antes de descubrirla, toca apostar.

<div class="conexion-apuesta" aria-labelledby="conexion-pregunta">
  <p class="conexion-kicker">TRAMA | ENTREGA 2</p>
  <h2 id="conexion-pregunta">¿Dónde crees que se esconde la conexión definitiva?</h2>
  <div class="conexion-opciones" role="group" aria-label="elige una respuesta">
    <button type="button" data-respuesta="publico">En los gustos del público</button>
    <button type="button" data-respuesta="creditos">En un cineasta</button>
    <button type="button" data-respuesta="familia">En una familia</button>
    <button type="button" data-respuesta="musica">En la música</button>
  </div>
  <p class="conexion-resultado" aria-live="polite">Elige una opción y guarda tu apuesta hasta el final.</p>
</div>

## Miles de personas entraron en las dos salas

**Las películas solo comparten uno de los seis géneros que les asigna MovieLens: comedia**. *Big* añade drama, fantasía y romance. *Men in Black*, acción y ciencia ficción. No empiezan tan lejos como Cazafantasmas y Winnie the Pooh, pero tampoco forman una pareja evidente.

Las etiquetas acercan algo más sus mundos. Entre cientos de palabras aparecen 14 coincidencias. Las dos hablan de identidad, tienen un protagonista masculino, pasan por Nueva York e incluyen béisbol. Son pistas sugerentes, aunque ninguna demuestra que las películas estén realmente unidas.

El público sí construye un puente enorme. *Big* acumula 24.016 valoraciones y *Men in Black*, 48.434. Hay **15.741 personas que puntuaron ambas**: casi dos de cada tres espectadores de *Big* presentes en MovieLens también valoraron la aventura de los agentes J y K.

<figure class="grafico-interactivo conexion-publico">
  <figcaption><strong>Big gana por poco la comparación compartida</strong><br>Usuarios de MovieLens que dieron más nota a cada película.</figcaption>
  <div class="conexion-publico__filas" role="img" aria-label="Entre los 15.741 usuarios compartidos, 5.772 prefirieron Big, 5.309 Men in Black y 4.660 las puntuaron igual">
    <div><span>Big</span><i><b style="width:100%"></b></i><strong>5.772</strong></div>
    <div><span>Men in Black</span><i><b style="width:92%"></b></i><strong>5.309</strong></div>
    <div><span>Empate</span><i><b style="width:81%"></b></i><strong>4.660</strong></div>
  </div>
</figure>

*Big* gana por poco: 5.772 personas le dieron más nota, frente a 5.309 que prefirieron *Men in Black*. Otras 4.660 las dejaron empatadas. La correlación entre las notas es débil, de 0,306. Dicho de otro modo, saber que a alguien le gustó una ayuda poco a adivinar qué pensará de la otra.

Comparten mucha gente, pero el público no resuelve el misterio.

## La respuesta parece estar detrás de la cámara

**Los créditos ofrecen una conexión mucho más limpia**. Barry Sonnenfeld fue el director de fotografía de *Big*. Él decidió, junto a Penny Marshall, cómo mirar a Josh mientras intentaba moverse por un mundo de adultos. Nueve años más tarde dirigió *Men in Black*.

<div style="margin:2rem 0;overflow:hidden;border-radius:12px;aspect-ratio:16/9">
  <iframe
    src="https://www.youtube-nocookie.com/embed/w7zmrSwm-vg"
    title="Men in Black - Will Smith"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="width:100%;height:100%;border:0"
  ></iframe>
</div>

El camino solo necesita un nombre:

<div class="grafico-interactivo conexion-ruta" role="img" aria-label="Big conecta con Men in Black mediante Barry Sonnenfeld"><span class="pelicula">Big</span><i>→</i><span>Barry Sonnenfeld</span><i>→</i><span class="pelicula">Men in Black</span></div>

Podríamos detenernos aquí. No es una asociación imaginada ni una cadena de conocidos: la misma persona ocupa un puesto principal en las dos películas. Pero todavía queda otra respuesta.

## Los Spielberg aparecen a ambos lados

Anne Spielberg escribió *Big* junto a Gary Ross. Su hermano Steven fue productor ejecutivo de *Men in Black*. Una película llega a la otra atravesando una sola familia.

<div style="margin:2rem 0;overflow:hidden;border-radius:12px;aspect-ratio:16/9">
  <iframe
    src="https://www.youtube-nocookie.com/embed/w7zmrSwm-vg"
    title="Vídeo relacionado con Big y Men in Black"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="width:100%;height:100%;border:0"
  ></iframe>
</div>

Esta ruta es menos directa que la de Sonnenfeld porque cambia de persona, pero tiene algo irresistible. El apellido Spielberg estaba en los créditos de las dos y no correspondía al mismo profesional. **Los datos vuelven a encontrar una conexión auténtica**. Tampoco es la que buscábamos.

## El vínculo estaba saltando en una cama elástica

En una de las escenas más recordadas de *Big*, Josh y Susan saltan en la cama elástica de su enorme piso. La canción que suena es **Forget Me Nots**, publicada por Patrice Rushen en 1982. Su línea de bajo resulta familiar incluso para quien no reconoce el título.

<div style="margin:2rem 0;overflow:hidden;border-radius:12px;aspect-ratio:16/9">
  <iframe
    src="https://www.youtube-nocookie.com/embed/jtMHsNhQBvI"
    title="Patrice Rushen - Forget Me Nots"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="width:100%;height:100%;border:0"
  ></iframe>
</div>

Hay una razón. La canción **Men in Black**, interpretada por Will Smith y escuchada en los créditos finales de la película, está construida sobre *Forget Me Nots*. Reutiliza su base y transforma el estribillo. Los créditos de composición de la canción de 1997 incluyen a Patrice Rushen y Freddie Washington, coautores del tema original.

La conexión no necesita interpretar etiquetas ni recorrer una filmografía. Una melodía pasa de una escena de *Big* a la canción más reconocible de *Men in Black*. Entre ambas hay nueve años, pero el oído puede cruzarlos en unos segundos.

Los datos no han fracasado. Han encontrado 15.741 espectadores, 14 etiquetas comunes, un cineasta y dos hermanos. Sirvieron para medir las alternativas y demostrar que el camino no estaba preparado de antemano. Pero **la respuesta definitiva no cabía en una tabla de créditos cinematográficos**. Había que escuchar.

## Fuentes y análisis

EDA con [MovieLens 32M, GroupLens](https://grouplens.org/datasets/movielens/32m/), con valoraciones hasta el 12 de octubre de 2023. Créditos y canciones de [AFI Catalog](https://catalog.afi.com/Film/58497-BIG), [Amblin](https://amblin.com/movie/men-in-black/) y [Sony Pictures Museum](https://www.sonypicturesmuseum.com/collection/film/692/men-in-black.html). La presencia de *Forget Me Nots* en la escena de la cama elástica también aparece recogida en la [entrevista de Interlochen Public Radio a Patrice Rushen](https://www.interlochenpublicradio.org/2022-09-22/patrice-rushen-takes-the-stage-with-interlochen-students). MovieLens no representa a todo el público y sus etiquetas pueden contener omisiones.

[Notebook ejecutado](/nebula/analisis/conexiones_imposibles_02/conexiones_imposibles_02_eda.ipynb) | [Resumen de películas](/nebula/analisis/conexiones_imposibles_02/resumen_movielens.csv) | [Valoraciones compartidas](/nebula/analisis/conexiones_imposibles_02/valoraciones_compartidas.csv) | [Conexiones comprobadas](/nebula/analisis/conexiones_imposibles_02/conexiones_comprobadas.csv) | [Metodología](/nebula/analisis/conexiones_imposibles_02/README.md).

<script>
  document.querySelectorAll(".conexion-apuesta").forEach((apuesta) => {
    const botones = apuesta.querySelectorAll("button");
    const resultado = apuesta.querySelector(".conexion-resultado");
    botones.forEach((boton) => boton.addEventListener("click", () => {
      botones.forEach((opcion) => opcion.classList.remove("seleccionado"));
      boton.classList.add("seleccionado");
      const mensajes = { publico: "Hay miles de espectadores comunes. Falta saber si miran hacia el mismo sitio.", creditos: "Un nombre une los créditos de las dos. ¿Será el último camino?", familia: "El mismo apellido aparece a ambos lados, aunque no pertenece a la misma persona.", musica: "Has decidido escuchar. Guarda esa intuición hasta el final." };
      resultado.textContent = mensajes[boton.dataset.respuesta];
    }));
  });
</script>

<style>
.conexion-apuesta{margin:28px 0;padding:clamp(18px,4vw,27px);border:1px solid #c7d3f4;border-radius:18px;background:#f5f7fd;box-shadow:0 8px 24px rgba(40,66,125,.06)}.conexion-kicker{margin:0;color:#446ddf;font-size:.75rem;font-weight:800;letter-spacing:.1em}.conexion-opciones{display:flex;flex-wrap:wrap;gap:.7rem;margin:1rem 0}.conexion-opciones button{padding:.7rem 1rem;border:1px solid #446ddf;border-radius:999px;background:#fff;color:#294da8;cursor:pointer}.conexion-opciones button:hover,.conexion-opciones button:focus-visible,.conexion-opciones button.seleccionado{background:#446ddf;color:#fff}.conexion-resultado{margin-bottom:0;color:#505569}.conexion-publico figcaption{color:#596477;line-height:1.45;margin-bottom:1.5rem}.conexion-publico figcaption strong{color:#1b1836;font:600 clamp(1.45rem,3vw,2.1rem) var(--font-heading)}.conexion-publico__filas{display:grid;gap:1.2rem}.conexion-publico__filas>div{align-items:center;display:grid;gap:.8rem;grid-template-columns:120px 1fr 58px}.conexion-publico__filas span{font-size:.9rem}.conexion-publico__filas i{background:#dfe5f5;border-radius:999px;display:block;height:22px;overflow:hidden}.conexion-publico__filas b{background:#446ddf;border-radius:inherit;display:block;height:100%}.conexion-publico__filas strong{color:#3157bd;font:600 1rem var(--font-mono);white-space:nowrap}.conexion-ruta{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:.55rem;font-size:.9rem}.conexion-ruta span{padding:.45rem .65rem;border:1px solid #cbd4ed;border-radius:6px;background:#fff}.conexion-ruta .pelicula{border-color:#446ddf;color:#294da8;font-weight:700}.conexion-ruta i{color:#446ddf;font-style:normal;font-weight:800}@media(max-width:620px){.conexion-apuesta{border-radius:14px}.conexion-publico__filas>div{grid-template-columns:1fr auto;gap:.35rem .8rem}.conexion-publico__filas i{grid-column:1/-1;grid-row:2}}
</style>
