---
imagenPortada: "/nebula/imagenes/conexiones_imposibles_01.png"
titulo: "Cazafantasmas 2 y Winnie the Pooh están conectadas: ¿encontrarán los datos el vínculo?"
descripcion: "32 millones de valoraciones, cinco rutas y un pequeño detalle frente a la cámara. Hagan sus apuestas."
tema: "CINE"
serie: "trama"
fecha: 2026-11-02
cifraDestacada: "277"
etiquetaCifra: "espectadores puntuaron las dos películas"
metodologia: "EDA de 32.000.204 valoraciones sobre 84.432 películas de MovieLens 32M, etiquetas, géneros y créditos estructurados de Wikidata. Comparo Cazafantasmas 2 (MovieLens 2717, Wikidata Q492214) con The Many Adventures of Winnie the Pooh (MovieLens 31193, Wikidata Q498434). No genero predicciones."
---

Nueva York está a punto de ahogarse en ectoplasma. En otro rincón del cine, un oso amarillo intenta sacar miel de un tarro. *Cazafantasmas 2* y *The Many Adventures of Winnie the Pooh* parecen elegidas al azar, pero están conectadas. La cuestión es dónde buscar.

Para inaugurar **Trama**, he enfrentado la intuición con 32 millones de valoraciones, 84.432 películas, géneros, etiquetas y créditos. Antes de ver qué encontraron, toca apostar.

<div class="conexion-apuesta" aria-labelledby="conexion-pregunta">
  <p class="conexion-kicker">TRAMA | ENTREGA 1</p>
  <h2 id="conexion-pregunta">¿Dónde crees que se esconde la conexión?</h2>
  <div class="conexion-opciones" role="group" aria-label="elige una respuesta">
    <button type="button" data-respuesta="publico">En los gustos del público</button>
    <button type="button" data-respuesta="creditos">En los créditos</button>
    <button type="button" data-respuesta="tema">En la historia</button>
    <button type="button" data-respuesta="pantalla">En un detalle de la pantalla</button>
  </div>
  <p class="conexion-resultado" aria-live="polite">Elige una opción y guarda tu apuesta hasta el final.</p>
</div>

## Los datos empiezan diciendo que no

Las dos películas están separadas por 12 años y 33 minutos. MovieLens clasifica *Cazafantasmas 2* como comedia, fantasía y ciencia ficción. Pooh aparece como animación, cine infantil y musical. **No comparten ninguno de sus seis géneros.**

Las palabras elegidas por los usuarios tampoco construyen un puente. *Fantasmas*, *comedia* y *paranormal* dominan las 140 etiquetas de una. *Disney*, *dibujos animados* y *animales parlantes* aparecen entre las 13 de la otra. Tras normalizar mayúsculas, acentos y espacios, el resultado vuelve a ser cero coincidencias.

No significa que las obras carezcan de temas comunes imaginables. Significa algo más preciso: **las categorías y etiquetas disponibles no los registran**.

## 277 personas entran en las dos salas

*Cazafantasmas 2* reúne 10.171 valoraciones en MovieLens y está en el percentil 99,1: solo el 0,9% de las películas tiene más. Pooh suma 788, suficientes para superar al 94,09% del catálogo. Las dos son conocidas, aunque juegan en escalas distintas.

El cruce deja **277 espectadores que puntuaron ambas**. Son apenas el 2,72% de quienes valoraron *Cazafantasmas 2*, pero representan el 35,15% del público de Pooh presente en estos datos.

<svg viewBox="0 0 680 290" role="img" aria-label="Entre los 277 usuarios compartidos, 179 prefirieron Winnie the Pooh, 52 puntuaron igual y 46 prefirieron Cazafantasmas 2" style="width:100%;height:auto;display:block;font-family:system-ui,sans-serif"><title>Pooh gana entre quienes puntuaron las dos</title><text x="20" y="30" font-size="20" fill="currentColor">Pooh gana la comparación compartida</text><text x="20" y="78" font-size="15" fill="currentColor">Winnie the Pooh</text><rect x="170" y="59" width="430" height="25" rx="4" fill="#446ddf"/><text x="612" y="78" font-size="15" fill="currentColor">179</text><text x="20" y="148" font-size="15" fill="currentColor">Empate</text><rect x="170" y="129" width="125" height="25" rx="4" fill="#aab8df"/><text x="307" y="148" font-size="15" fill="currentColor">52</text><text x="20" y="218" font-size="15" fill="currentColor">Cazafantasmas 2</text><rect x="170" y="199" width="111" height="25" rx="4" fill="#314ea4"/><text x="293" y="218" font-size="15" fill="currentColor">46</text><text x="20" y="270" font-size="13" fill="#555">Usuarios de MovieLens que dieron más nota a cada película</text></svg>

Pooh se impone en 179 casos. *Cazafantasmas 2*, en 46. Hay 52 empates. Las notas solo muestran una relación débil: una correlación de 0,257. Dicho sin jerga, saber cuánto le gustó una no permite adivinar bien la opinión sobre la otra.

Ya tenemos un pequeño público común, pero no la respuesta.

## Cinco caminos que dan un rodeo

Los créditos ofrecen más juego. He buscado reparto, voces, dirección, guion, producción, música, montaje y fotografía en Wikidata. Aparecen **cinco rutas** que conectan las películas mediante otro título y dos profesionales.

La más reconocible sale de *Cazafantasmas 2* con Rick Moranis, pasa por *Parenthood*, encuentra allí a Clint Howard y llega a Pooh, donde Howard puso voz a Roo.

<div class="conexion-ruta" role="img" aria-label="Cazafantasmas 2 conecta con Winnie the Pooh mediante Rick Moranis, Parenthood y Clint Howard"><span class="pelicula">Cazafantasmas 2</span><i>→</i><span>Rick Moranis</span><i>→</i><span class="pelicula">Parenthood</span><i>→</i><span>Clint Howard</span><i>→</i><span class="pelicula">Winnie the Pooh</span></div>

Las demás atraviesan *Oliver y su pandilla*, *EDtv*, *The Cannonball Run* y *The Brave Little Toaster Goes to Mars*. Son conexiones reales, pero todas necesitan cuatro créditos. El camino más corto seguía escondido.

Aquí aparece una pequeña paradoja. Cuanta más información estructurada añado, más caminos puedo dibujar, pero ninguno entra realmente en una escena. Las relaciones siguen carreras profesionales desde fuera: alguien actuó, compuso o montó dos obras distintas. Es como demostrar que dos casas están comunicadas porque sus propietarios conocen al mismo fontanero. La ruta existe y puede medirse, aunque no explica qué objeto comparten las habitaciones. Para encontrar eso hay que abandonar por un momento los créditos y mirar lo que ocurre delante de la cámara.

## La base de datos no mira el pijama

La respuesta aparece durante una de las escenas más inquietantes de *Cazafantasmas 2*. Janosz llega flotando ante la ventana para llevarse al bebé Óscar y entregárselo a Vigo. El niño viste una prenda en la que aparece **Winnie the Pooh**.

No hacen falta espectadores compartidos, otra película ni dos carreras profesionales. Pooh ya estaba dentro de *Cazafantasmas 2*, delante de la cámara.

La transcripción describe la acción, pero no el estampado. Wikidata sabe quién actuó y MovieLens conserva lo que votó su comunidad. Ninguna registra todo lo que cabe en un plano: un juguete, un cartel, un libro o el dibujo de un pijama.

Los datos han servido para medir lo improbable de la pareja: cero géneros, cero etiquetas, 277 espectadores comunes y cinco rodeos por los créditos. Pero la conexión ganadora pertenecía a quien decidió mirar. Primera apuesta resuelta.

## Fuentes y análisis

EDA con [MovieLens 32M, GroupLens](https://grouplens.org/datasets/movielens/32m/), con valoraciones hasta el 12 de octubre de 2023, y datos estructurados CC0 de [Wikidata](https://www.wikidata.org/). Fichas de [Disney](https://movies.disney.com/the-many-adventures-of-winnie-the-pooh) y [Sony Pictures](https://www.sonypictures.com/movies/ghostbustersii). La prenda está documentada en la [ficha especializada de la secuencia](https://ghostbusters.fandom.com/wiki/Ghostbusters_II_%28Chapter_20%29%3A_Kidnapping_Oscar). MovieLens no representa a todo el público y Wikidata puede contener omisiones.

[Notebook ejecutado](/nebula/analisis/conexiones_imposibles_01/conexiones_imposibles_01_eda.ipynb) | [Resumen de películas](/nebula/analisis/conexiones_imposibles_01/resumen_movielens.csv) | [Valoraciones compartidas](/nebula/analisis/conexiones_imposibles_01/valoraciones_compartidas.csv) | [Rutas de créditos](/nebula/analisis/conexiones_imposibles_01/rutas_wikidata.csv) | [Metodología](/nebula/analisis/conexiones_imposibles_01/README.md).

<script>
  document.querySelectorAll(".conexion-apuesta").forEach((apuesta) => {
    const botones = apuesta.querySelectorAll("button");
    const resultado = apuesta.querySelector(".conexion-resultado");
    botones.forEach((boton) => boton.addEventListener("click", () => {
      botones.forEach((opcion) => opcion.classList.remove("seleccionado"));
      boton.classList.add("seleccionado");
      const mensajes = { publico: "Hay espectadores compartidos. ¿Será suficiente?", creditos: "Los créditos encuentran varios caminos. Falta saber si son la respuesta.", tema: "Las historias admiten parecidos, pero necesitamos una prueba concreta.", pantalla: "Has apostado por mirar con atención. Guarda esa intuición." };
      resultado.textContent = mensajes[boton.dataset.respuesta];
    }));
  });
</script>

<style>
.conexion-apuesta{margin:2rem 0;padding:1.4rem;border:1px solid #446ddf;border-radius:14px;background:rgba(68,109,223,.05)}.conexion-kicker{margin:0;color:#446ddf;font-size:.75rem;font-weight:800;letter-spacing:.1em}.conexion-opciones{display:flex;flex-wrap:wrap;gap:.7rem;margin:1rem 0}.conexion-opciones button{padding:.7rem 1rem;border:1px solid #446ddf;border-radius:999px;background:#fff;color:#294da8;cursor:pointer}.conexion-opciones button:hover,.conexion-opciones button:focus-visible,.conexion-opciones button.seleccionado{background:#446ddf;color:#fff}.conexion-resultado{margin-bottom:0;color:#505569}.conexion-ruta{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:.55rem;margin:2rem 0;padding:1.2rem;background:#f5f6fb;border-radius:12px;font-size:.9rem}.conexion-ruta span{padding:.45rem .65rem;border:1px solid #cbd4ed;border-radius:6px;background:#fff}.conexion-ruta .pelicula{border-color:#446ddf;color:#294da8;font-weight:700}.conexion-ruta i{color:#446ddf;font-style:normal;font-weight:800}
</style>
