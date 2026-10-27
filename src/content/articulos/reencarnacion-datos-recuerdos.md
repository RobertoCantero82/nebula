---
imagenPortada: "/nebula/imagenes/reencarnacion_portada.png"
titulo: "¿Qué revelan realmente 1.678 supuestos casos de reencarnación?"
descripcion: "Estos relatos sitúan los nuevos nacimientos más cerca de las muertes inesperadas. Los datos revelan el verdadero alcance del patrón."
tema: "CIENCIA"
fecha: 2026-10-27
cifraDestacada: "43%"
etiquetaCifra: "menos tiempo entre muerte y nacimiento en los relatos"
metodologia: "EDA del archivo anónimo de 2.254 casos de Sadeghi, Pehlivanova y Cozzolino. Selecciono 1.678 casos con fallecido identificado; 1.319 tienen intervalo y 1.075 incluyen también el grado de muerte inesperada. Reproduzco medianas, cuantiles y correlación con log10(intervalo + 4), y compruebo filtros de documentación y contacto familiar. No verifico relatos ni demuestro reencarnación. No genero predicciones."
---

Un niño cuenta que antes tenía otra familia. Recuerda una casa, un oficio o una muerte que nadie espera escuchar en boca de alguien tan pequeño. Historias así llevan décadas llegando a la Universidad de Virginia. Ahora, una investigación ha encontrado una relación entre dos fechas de esos expedientes. Y entenderla exige mirar algo más que el porcentaje más llamativo.

Los autores observaron **intervalos más cortos entre la muerte de la persona vinculada al relato y el nacimiento del niño cuando aquella muerte había sido inesperada**. ¿Hasta qué punto separa ese patrón unas historias de otras? En Nebula he revisado sus datos abiertos para comprobarlo.

<div style="position: relative; width: 100%; padding-top: 56.25%; margin: 2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/m1DFpkNdcv0"
    title="Vídeo de YouTube"
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 12px;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

## Nueve meses que llaman la atención

El archivo reúne **2.254 casos de supuestos recuerdos de vidas anteriores**. En 1.678, los investigadores identificaron a una persona fallecida que asociaron con lo contado por el niño. Esa identificación es un criterio del estudio. No equivale a haber demostrado una reencarnación.

El trabajo de Saeedeh Sadeghi, Marieta Pehlivanova y Philip Cozzolino compara cuánto tiempo separa la muerte registrada del nacimiento y hasta qué punto se esperaba el fallecimiento. Su escala va del cero, cuando se anticipaba más de un mes antes, al cuatro, cuando resultó completamente inesperado.

Al comparar esos extremos, aparecen 21 meses frente a 12. Son las medianas: si ordenamos los intervalos de menor a mayor, el valor que queda en medio. La diferencia es de nueve meses, un 43% respecto al primer grupo.

Es una cifra que invita a imaginar dos clases de historias muy distintas. Antes de aceptar esa imagen, conviene hacer una pequeña prueba: **¿cuánto crees que se parecen los intervalos de ambos grupos?**

<div class="apuesta-solapamiento" aria-labelledby="pregunta-solapamiento">
  <p id="pregunta-solapamiento">
    <strong>¿Cuánto crees que se solapa la mitad central de los dos grupos?</strong>
  </p>

  <div class="apuesta-opciones" role="group" aria-label="elige una respuesta">
    <button type="button" data-respuesta="poco">Menos de 5 meses</button>
    <button type="button" data-respuesta="correcta">Unos 27 meses</button>
    <button type="button" data-respuesta="mucho">Más de 50 meses</button>
  </div>

  <div class="apuesta-barras" hidden aria-hidden="true">
    <div class="barra-fila">
      <span>Muertes anticipadas</span>
      <div class="barra-escala">
        <span class="barra anticipada"></span>
      </div>
      <small>11,25–70,5 meses</small>
    </div>

    <div class="barra-fila">
      <span>Muertes inesperadas</span>
      <div class="barra-escala">
        <span class="barra inesperada"></span>
      </div>
      <small>5,75–38 meses</small>
    </div>
  </div>

  <p class="apuesta-resultado" aria-live="polite">
    Elige una opción antes de continuar.
  </p>
</div>

<script>
  document.querySelectorAll(".apuesta-solapamiento").forEach((apuesta) => {
    const botones = apuesta.querySelectorAll("button");
    const resultado = apuesta.querySelector(".apuesta-resultado");
    const barras = apuesta.querySelector(".apuesta-barras");

    botones.forEach((boton) => {
      boton.addEventListener("click", () => {
        botones.forEach((opcion) => {
          opcion.classList.remove("seleccionado");
          opcion.removeAttribute("aria-pressed");
        });

        boton.classList.add("seleccionado");
        boton.setAttribute("aria-pressed", "true");
        barras.hidden = false;
        barras.removeAttribute("aria-hidden");

        if (boton.dataset.respuesta === "correcta") {
          resultado.innerHTML =
            "<strong>Exacto.</strong> Las franjas coinciden durante unos 27 meses, desde 11,25 hasta 38. La diferencia entre las medianas no crea dos grupos separados.";
        } else {
          resultado.innerHTML =
            "<strong>El solapamiento es de unos 27 meses.</strong> Va desde 11,25 hasta 38 meses. Muchos relatos de ambos grupos ocupan, por tanto, el mismo intervalo.";
        }
      });
    });
  });
</script>

## Lo que el porcentaje deja fuera

Una mediana no cuenta todo lo que ocurre alrededor. Dos clases pueden tener una edad central parecida y alumnos muy diferentes. Aquí sucede algo complementario: los valores centrales cambian, pero muchos intervalos ocupan la misma zona.

Para verlo, **el gráfico muestra el tramo que contiene aproximadamente la mitad central de cada grupo**. El punto marca la mediana. Las barras no representan todos los casos: quedan historias más cortas y más largas fuera de ellas.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" role="img" aria-label="Las medianas cambian, las historias se solapan. Mitad central: anticipada 11,25 a 70,5 meses; inesperada 5,75 a 38. Medianas 21 y 12." style="width:100%;height:auto;display:block;font-family:system-ui,sans-serif;color:inherit"><title>Las medianas cambian, las historias se solapan</title><text x="20" y="30" fill="currentColor" font-size="20">Dos cifras no cuentan toda la historia</text><text x="20" y="70" fill="currentColor" font-size="16">Anticipada (114 casos)</text><line x1="123.25" x2="561.7" y1="105" y2="105" stroke="#446ddf" stroke-width="22" stroke-opacity=".25" stroke-linecap="round"/><circle cx="195.4" cy="105" r="7" fill="#446ddf"/><text x="207.4" y="90" fill="currentColor" font-size="16">21 meses</text><text x="20" y="165" fill="currentColor" font-size="16">Inesperada (708 casos)</text><line x1="82.55000000000001" x2="321.2" y1="200" y2="200" stroke="#446ddf" stroke-width="22" stroke-opacity=".25" stroke-linecap="round"/><circle cx="128.8" cy="200" r="7" fill="#446ddf"/><text x="140.8" y="185" fill="currentColor" font-size="16">12 meses</text><text x="40.0" y="255" text-anchor="middle" fill="currentColor" font-size="14">0</text><text x="188.0" y="255" text-anchor="middle" fill="currentColor" font-size="14">20</text><text x="336.0" y="255" text-anchor="middle" fill="currentColor" font-size="14">40</text><text x="484.0" y="255" text-anchor="middle" fill="currentColor" font-size="14">60</text><text x="632.0" y="255" text-anchor="middle" fill="currentColor" font-size="14">80</text><text x="340" y="284" text-anchor="middle" fill="currentColor" font-size="14">Meses entre la muerte registrada y el nacimiento</text></svg>

En las muertes anticipadas, esa mitad central abarca desde unos 11 hasta unos 71 meses. En las completamente inesperadas, desde unos seis hasta 38. **Las dos franjas se solapan ampliamente.** La diferencia entre medianas existe, pero no permite asignar a cada historia un calendario reconocible.

Además, los grupos tienen tamaños distintos: 114 casos en el extremo de muertes anticipadas y 708 en el de inesperadas. No son dos muestras equilibradas ni una fotografía de cómo muere la población general. Son los expedientes disponibles de una colección particular.

## El archivo se hace más pequeño

Hay otra cifra menos vistosa que merece atención. Para comparar ambas variables necesito conocer tanto el intervalo como el grado de sorpresa de la muerte. No todos los expedientes tienen esa información.

De los 1.678 casos con una persona identificada, 1.319 incluyen el intervalo. Cuando exijo también la otra variable, quedan 1.075. El **gráfico** permite **seguir esa reducción sin confundir el archivo completo con la muestra** que sostiene esta comparación.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 350" role="img" aria-label="De 2.254 expedientes a 1.075 casos comparables. Archivo 2254, identificado 1678, intervalo 1319, ambas variables 1075." style="width:100%;height:auto;display:block;font-family:system-ui,sans-serif;color:inherit"><title>De 2.254 expedientes a 1.075 casos comparables</title><text x="20" y="30" fill="currentColor" font-size="20">Qué casos sostienen la comparación</text><text x="20" y="70" fill="currentColor" font-size="16">Archivo completo</text><rect x="20" y="80" width="550.0" height="22" rx="3" fill="#446ddf"/><text x="580.0" y="97" fill="currentColor" font-size="16">2.254</text><text x="20" y="140" fill="currentColor" font-size="16">Fallecido identificado</text><rect x="20" y="150" width="409.44986690328307" height="22" rx="3" fill="#446ddf"/><text x="439.44986690328307" y="167" fill="currentColor" font-size="16">1.678</text><text x="20" y="210" fill="currentColor" font-size="16">También consta el intervalo</text><rect x="20" y="220" width="321.8500443655723" height="22" rx="3" fill="#446ddf"/><text x="351.8500443655723" y="237" fill="currentColor" font-size="16">1.319</text><text x="20" y="280" fill="currentColor" font-size="16">También consta lo inesperado</text><rect x="20" y="290" width="262.3114463176575" height="22" rx="3" fill="#446ddf"/><text x="292.3114463176575" y="307" fill="currentColor" font-size="16">1.075</text></svg>

Son 603 casos identificados que no entran por faltar al menos uno de esos datos: casi el 36%. Eso no borra el resultado. Significa que describe a quienes sí tienen información suficiente. Si los expedientes incompletos fueran diferentes, la imagen del conjunto podría cambiar. Este análisis no permite saber cuánto.

El problema no es exclusivo de estos relatos. Cuando [un reloj epigenético intenta calcular la edad del cuerpo](/nebula/articulos/edad-adn-reloj-epigenetico/), el resultado también depende de qué se mide y de los datos usados para compararlo. Algo parecido ocurre con [el registro fósil de los antiguos gaviales](/nebula/articulos/cocodrilo-esfinge-maquina-tiempo/): los periodos más estudiados pueden parecer más diversos simplemente porque conservamos más información sobre ellos. En los tres casos, una cifra solo se entiende bien cuando sabemos qué datos la sostienen y cuáles han quedado fuera.

Tampoco aparecen países ni fechas de recogida en el archivo público. Por tanto, **no puedo comprobar si el patrón cambia entre lugares o épocas, ni separar su posible influencia**. Reunir muchos relatos no elimina automáticamente las diferencias en cómo se comunicaron, investigaron y registraron.

## Una relación no resuelve el misterio

Los autores examinaron posibles sesgos, entre ellos la relación entre las familias y sus creencias. En mi revisión reproduzco también una asociación débil entre lo inesperado de la muerte y el intervalo, usando la transformación del estudio para reducir el peso de las distancias más largas.

**La aportación de Nebula está en poner al lado del hallazgo sus dimensiones**: nueve meses entre medianas, mucho solapamiento y cientos de expedientes sin información completa. No he vuelto a investigar a los niños ni puedo verificar sus relatos con una tabla.

Los datos permiten estudiar cómo se relacionan las características registradas. No identifican por sí solos la causa de esa relación. La pregunta sobre la reencarnación sigue sin respuesta aquí. La pregunta sobre el porcentaje sí la tiene: **una diferencia del 43% puede ser cierta y, aun así, contar solo una parte de la historia**.

<div style="position: relative; width: 100%; padding-top: 56.25%; margin: 2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/l_AhxNjpWGY"
    title="Vídeo de YouTube"
    style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 12px;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
</div>

## Fuentes y análisis

- [Estudio original: Sadeghi, Pehlivanova y Cozzolino](https://doi.org/10.1037/cns0000493).
- [Datos, diccionario y código de los autores, versión 1](https://zenodo.org/records/22677480).
- [Notebook ejecutado de Nebula](/nebula/analisis/reencarnacion/reencarnacion_eda.ipynb).
- [Datos originales](/nebula/analisis/reencarnacion/CORT_IT_open_data.csv), [diccionario](/nebula/analisis/reencarnacion/CORT_IT_codebook.txt) e [instrucciones para reproducir](/nebula/analisis/reencarnacion/README.md).

<style>
.apuesta-solapamiento {
  margin: 2rem 0;
  padding: 1.3rem;
  border: 1px solid #446ddf;
  border-radius: 14px;
  background: rgba(68, 109, 223, 0.05);
}

.apuesta-opciones {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  margin: 1rem 0;
}

.apuesta-opciones button {
  padding: 0.7rem 1rem;
  border: 1px solid #446ddf;
  border-radius: 999px;
  color: #294da8;
  background: #fff;
  cursor: pointer;
}

.apuesta-opciones button:hover,
.apuesta-opciones button:focus-visible,
.apuesta-opciones button.seleccionado {
  color: #fff;
  background: #446ddf;
}

.apuesta-barras {
  margin: 1.5rem 0;
}

.barra-fila {
  margin-bottom: 1rem;
}

.barra-fila > span,
.barra-fila small {
  display: block;
}

.barra-fila small {
  margin-top: 0.3rem;
  color: #555;
}

.barra-escala {
  position: relative;
  height: 18px;
  margin-top: 0.35rem;
  border-radius: 999px;
  background: #e8ebf3;
}

.barra {
  position: absolute;
  top: 0;
  height: 18px;
  border-radius: 999px;
  background: #446ddf;
}

.barra.anticipada {
  left: 14.1%;
  width: 74.1%;
  opacity: 0.55;
}

.barra.inesperada {
  left: 7.2%;
  width: 40.3%;
}

.apuesta-resultado {
  margin-bottom: 0;
}
</style>
