---
imagenPortada: "/nebula/imagenes/edad_adn_portada_v3.png"
titulo: "¿Puede el ADN decir cuántos años tienes? Entrené un modelo para comprobarlo"
descripcion: "Lo puse a prueba con muestras de sangre de 127 personas que no había utilizado para entrenarlo. Sus errores cuentan algo que la precisión media esconde."
tema: "CIENCIA"
fecha: 2026-10-23
cifraDestacada: "127 personas"
etiquetaCifra: "en la prueba final de predicción de edad"
metodologia: "Machine learning con GSE40279: 656 personas y 23.734 marcas candidatas fijadas por identificador, sin consultar edades. Separación por chip: 420 personas de entrenamiento, 109 de calibración y 127 de prueba. Regresión ridge elegida entre cuatro combinaciones mediante validación interna de cinco grupos. Selección de marcas, imputación y escala dentro de cada entrenamiento. Comparación con la mediana del entrenamiento. Validación interna de una cohorte histórica; no mide salud, longevidad ni rejuvenecimiento."
---

*¿Y si un análisis de sangre te quitara diez años? Antes de celebrarlo, convendría mirar cómo se hace la cuenta. He entrenado un modelo para adivinar edades a partir de marcas del ADN. Aprende bastante. También comete un error que puede llevar a engaño cuando hablamos de rejuvenecer.*

<div
  id="pregunta-edad-adn"
  class="grafico-interactivo"
  style="text-align:center;padding:1.5rem"
>
  <p style="font-size:1.25rem">
    <strong>Tu ADN dice que tienes diez años menos.</strong>
  </p>

  <p>
    Un modelo ha calculado una edad inferior a la que tienes.
    ¿Qué puedes concluir con ese dato?
  </p>

  <div
    role="group"
    aria-label="Elige qué permite concluir la predicción"
    style="display:flex;flex-wrap:wrap;justify-content:center;gap:.6rem"
  >
    <button type="button" data-respuesta="rejuvenecer" aria-pressed="false">
      He rejuvenecido
    </button>

    <button type="button" data-respuesta="vivir" aria-pressed="false">
      Voy a vivir más
    </button>

    <button type="button" data-respuesta="estimacion" aria-pressed="false">
      Todavía no puedo saberlo
    </button>
  </div>

  <p
    id="respuesta-edad-adn"
    aria-live="polite"
    aria-atomic="true"
    style="margin:1.25rem 0 0;min-height:3rem"
  >
    Elige una respuesta antes de seguir leyendo.
  </p>
</div>

<style>
  #pregunta-edad-adn button {
    padding: .7rem 1rem;
    border: 1px solid #446ddf;
    border-radius: 5px;
    background: transparent;
    color: #304fa5;
    font: inherit;
    cursor: pointer;
  }

  #pregunta-edad-adn button[aria-pressed="true"] {
    background: #446ddf;
    color: white;
  }

  #pregunta-edad-adn button:focus-visible {
    outline: 3px solid #1b1836;
    outline-offset: 3px;
  }
</style>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const modulo = document.getElementById('pregunta-edad-adn');
    const salida = document.getElementById('respuesta-edad-adn');

    if (!modulo || !salida) return;

    const mensajes = {
      rejuvenecer:
        'Ese dato no demuestra rejuvenecimiento. Sabemos que el modelo ha calculado una edad menor, pero la diferencia también puede deberse a sus errores.',

      vivir:
        'Este modelo intenta calcular la edad, no los años que te quedan de vida. Una predicción más joven no permite concluir que vivirás más.',

      estimacion:
        'Exacto. Primero habría que comprobar cuánto se equivoca el modelo y qué otras pruebas existen. Una edad calculada menor no basta para demostrar rejuvenecimiento.'
    };

    const botones = modulo.querySelectorAll('button[data-respuesta]');

    botones.forEach(boton => {
      boton.addEventListener('click', () => {
        botones.forEach(opcion => {
          opcion.setAttribute(
            'aria-pressed',
            String(opcion === boton)
          );
        });

        salida.textContent = mensajes[boton.dataset.respuesta];
      });
    });
  });
</script>

La [portada de noviembre de National Geographic](https://www.nationalgeographic.com.es/edicion-impresa/national-geographic-noviembre-2026_29672) dedica su tema principal a la reprogramación celular y la búsqueda de la eterna juventud. Esa promesa me hace plantearme una pregunta: **¿cómo sabemos que hemos conseguido dar marcha atrás al reloj?**

Mi experimento aborda algo más pequeño. Intento predecir cuántos años tiene una persona leyendo unas señales de su sangre. No hay tratamientos ni seguimiento de su salud. Hay cumpleaños conocidos y un modelo que debe intentar acertarlos.

## Las marcas del ADN que dan pistas sobre tu edad

El ADN conserva instrucciones, pero además tiene pequeñas marcas químicas. Algunas cambian con la edad. Se llaman marcas de metilación: podemos imaginarlas como anotaciones sobre un libro, aunque esa comparación no explica todo su funcionamiento.

Entrené un modelo para relacionar las marcas del ADN con la edad de cada persona. Después lo puse a prueba con muestras de otras personas que había reservado. Su tarea era calcular cuántos años tenían sin conocer la respuesta.

Utilizo datos públicos de sangre de **656 personas de entre 19 y 101 años**, del [estudio de Hannum y sus colaboradores](https://pubmed.ncbi.nlm.nih.gov/23177740/). La relación entre esas marcas y la edad ya estaba publicada. Mi aportación consiste en entrenar otro modelo y examinar sus equivocaciones, sin atribuirme aquel hallazgo.

<div style="margin:2rem 0">
  <iframe
    src="https://www.youtube-nocookie.com/embed/tA3llUK-nqo"
    title="Vídeo de YouTube"
    width="560"
    height="315"
    style="display:block;width:100%;height:auto;aspect-ratio:16/9;border:0"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>
</div>

## Un examen con las respuestas escondidas

Reservo 127 personas para la prueba final. Otras 109 sirven para calcular un margen de error. Las 420 restantes, para aprender y elegir el modelo. Las muestras procesadas en un mismo chip de laboratorio permanecen juntas, para reducir el riesgo de confundir una peculiaridad de medición con una pista sobre la edad.

También preparo un rival muy sencillo: responder siempre **64 años**, la edad central del entrenamiento. Ese rival falla 14 años de media. El modelo que lee la metilación reduce el error a **5,3 años**.

El gráfico compara edad real y predicha. Cada punto es una persona reservada; sobre la diagonal estaría el acierto perfecto. Cuanto más se aleja, mayor es la equivocación.

<figure class="grafico-interactivo" style="margin:1.75rem 0">
<svg viewBox="0 0 640 470" role="img" aria-labelledby="edad-titulo edad-descripcion" style="width:100%;height:auto;font-family:inherit">
<title id="edad-titulo">El reloj aproxima la edad, pero se equivoca en personas concretas</title>
<desc id="edad-descripcion">127 personas de prueba. La diagonal indica acierto perfecto. El error absoluto medio es de 5,3 años. Las edades reales van de 19 a 101 años.</desc>
<path d="M94.7 40V405M65 384.7H600" stroke="#ddd9d0" stroke-width="1"/>
<text x="94.7" y="428" text-anchor="middle" font-size="14">20</text><text x="53" y="389.7" text-anchor="end" font-size="14">20</text>
<path d="M213.6 40V405M65 303.6H600" stroke="#ddd9d0" stroke-width="1"/>
<text x="213.6" y="428" text-anchor="middle" font-size="14">40</text><text x="53" y="308.6" text-anchor="end" font-size="14">40</text>
<path d="M332.5 40V405M65 222.5H600" stroke="#ddd9d0" stroke-width="1"/>
<text x="332.5" y="428" text-anchor="middle" font-size="14">60</text><text x="53" y="227.5" text-anchor="end" font-size="14">60</text>
<path d="M451.4 40V405M65 141.4H600" stroke="#ddd9d0" stroke-width="1"/>
<text x="451.4" y="428" text-anchor="middle" font-size="14">80</text><text x="53" y="146.4" text-anchor="end" font-size="14">80</text>
<path d="M570.3 40V405M65 60.3H600" stroke="#ddd9d0" stroke-width="1"/>
<text x="570.3" y="428" text-anchor="middle" font-size="14">100</text><text x="53" y="65.3" text-anchor="end" font-size="14">100</text>
<path d="M65 405L600 40" stroke="#777" stroke-dasharray="5 5" fill="none"/>
<circle cx="296.83" cy="213.88" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 54; predicha: 62,1 años</title></circle>
<circle cx="576.22" cy="124.69" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 101; predicha: 84,1 años</title></circle>
<circle cx="445.44" cy="141.15" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 79; predicha: 80,1 años</title></circle>
<circle cx="475.17" cy="145.69" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 84; predicha: 78,9 años</title></circle>
<circle cx="481.11" cy="168.49" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 85; predicha: 73,3 años</title></circle>
<circle cx="493.00" cy="136.58" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 87; predicha: 81,2 años</title></circle>
<circle cx="415.72" cy="145.57" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 74; predicha: 79,0 años</title></circle>
<circle cx="433.56" cy="178.66" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 77; predicha: 70,8 años</title></circle>
<circle cx="409.78" cy="186.58" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 73; predicha: 68,9 años</title></circle>
<circle cx="493.00" cy="123.64" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 87; predicha: 84,4 años</title></circle>
<circle cx="481.11" cy="165.49" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 85; predicha: 74,1 años</title></circle>
<circle cx="439.50" cy="143.93" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 78; predicha: 79,4 años</title></circle>
<circle cx="362.22" cy="196.78" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 65; predicha: 66,3 años</title></circle>
<circle cx="362.22" cy="183.87" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 65; predicha: 69,5 años</title></circle>
<circle cx="504.89" cy="121.70" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 89; predicha: 84,9 años</title></circle>
<circle cx="481.11" cy="128.89" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 85; predicha: 83,1 años</title></circle>
<circle cx="368.17" cy="224.34" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 66; predicha: 59,5 años</title></circle>
<circle cx="427.61" cy="176.77" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 76; predicha: 71,3 años</title></circle>
<circle cx="415.72" cy="153.94" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 74; predicha: 76,9 años</title></circle>
<circle cx="475.17" cy="146.48" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 84; predicha: 78,7 años</title></circle>
<circle cx="397.89" cy="178.57" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 71; predicha: 70,8 años</title></circle>
<circle cx="261.17" cy="258.26" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 48; predicha: 51,2 años</title></circle>
<circle cx="397.89" cy="190.17" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 71; predicha: 68,0 años</title></circle>
<circle cx="284.94" cy="251.82" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 52; predicha: 52,8 años</title></circle>
<circle cx="356.28" cy="234.54" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 64; predicha: 57,0 años</title></circle>
<circle cx="261.17" cy="271.12" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 48; predicha: 48,0 años</title></circle>
<circle cx="302.78" cy="248.51" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 55; predicha: 53,6 años</title></circle>
<circle cx="380.06" cy="188.21" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 68; predicha: 68,5 años</title></circle>
<circle cx="249.28" cy="289.38" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 46; predicha: 43,5 años</title></circle>
<circle cx="356.28" cy="219.46" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 64; predicha: 60,8 años</title></circle>
<circle cx="314.67" cy="241.41" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 57; predicha: 55,3 años</title></circle>
<circle cx="243.33" cy="278.29" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 45; predicha: 46,2 años</title></circle>
<circle cx="279.00" cy="249.82" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 51; predicha: 53,3 años</title></circle>
<circle cx="320.61" cy="247.16" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 58; predicha: 53,9 años</title></circle>
<circle cx="350.33" cy="228.43" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 63; predicha: 58,5 años</title></circle>
<circle cx="302.78" cy="233.38" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 55; predicha: 57,3 años</title></circle>
<circle cx="273.06" cy="237.73" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 50; predicha: 56,2 años</title></circle>
<circle cx="314.67" cy="221.33" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 57; predicha: 60,3 años</title></circle>
<circle cx="172.00" cy="300.10" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 33; predicha: 40,9 años</title></circle>
<circle cx="249.28" cy="261.71" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 46; predicha: 50,3 años</title></circle>
<circle cx="249.28" cy="254.66" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 46; predicha: 52,1 años</title></circle>
<circle cx="368.17" cy="229.73" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 66; predicha: 58,2 años</title></circle>
<circle cx="302.78" cy="231.92" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 55; predicha: 57,7 años</title></circle>
<circle cx="356.28" cy="232.46" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 64; predicha: 57,5 años</title></circle>
<circle cx="481.11" cy="177.88" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 85; predicha: 71,0 años</title></circle>
<circle cx="368.17" cy="196.92" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 66; predicha: 66,3 años</title></circle>
<circle cx="386.00" cy="173.20" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 72,2 años</title></circle>
<circle cx="475.17" cy="169.51" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 84; predicha: 73,1 años</title></circle>
<circle cx="445.44" cy="181.51" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 79; predicha: 70,1 años</title></circle>
<circle cx="356.28" cy="225.95" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 64; predicha: 59,1 años</title></circle>
<circle cx="439.50" cy="142.93" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 78; predicha: 79,6 años</title></circle>
<circle cx="290.89" cy="203.79" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 53; predicha: 64,6 años</title></circle>
<circle cx="326.56" cy="224.67" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 59; predicha: 59,5 años</title></circle>
<circle cx="362.22" cy="208.40" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 65; predicha: 63,5 años</title></circle>
<circle cx="338.44" cy="199.71" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 61; predicha: 65,6 años</title></circle>
<circle cx="320.61" cy="260.42" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 58; predicha: 50,7 años</title></circle>
<circle cx="284.94" cy="242.00" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 52; predicha: 55,2 años</title></circle>
<circle cx="362.22" cy="198.42" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 65; predicha: 65,9 años</title></circle>
<circle cx="409.78" cy="182.42" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 73; predicha: 69,9 años</title></circle>
<circle cx="362.22" cy="204.64" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 65; predicha: 64,4 años</title></circle>
<circle cx="475.17" cy="138.26" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 84; predicha: 80,8 años</title></circle>
<circle cx="279.00" cy="243.94" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 51; predicha: 54,7 años</title></circle>
<circle cx="439.50" cy="163.96" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 78; predicha: 74,4 años</title></circle>
<circle cx="290.89" cy="234.41" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 53; predicha: 57,1 años</title></circle>
<circle cx="380.06" cy="144.74" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 68; predicha: 79,2 años</title></circle>
<circle cx="284.94" cy="247.13" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 52; predicha: 53,9 años</title></circle>
<circle cx="403.83" cy="201.66" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 72; predicha: 65,1 años</title></circle>
<circle cx="261.17" cy="262.09" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 48; predicha: 50,2 años</title></circle>
<circle cx="332.50" cy="244.84" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 60; predicha: 54,5 años</title></circle>
<circle cx="338.44" cy="28.15" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 61; predicha: 107,9 años</title></circle>
<circle cx="386.00" cy="168.55" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 73,3 años</title></circle>
<circle cx="457.33" cy="187.84" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 81; predicha: 68,5 años</title></circle>
<circle cx="308.72" cy="225.11" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 56; predicha: 59,4 años</title></circle>
<circle cx="445.44" cy="180.21" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 79; predicha: 70,4 años</title></circle>
<circle cx="463.28" cy="149.04" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 82; predicha: 78,1 años</title></circle>
<circle cx="320.61" cy="271.41" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 58; predicha: 47,9 años</title></circle>
<circle cx="421.67" cy="198.46" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 75; predicha: 65,9 años</title></circle>
<circle cx="439.50" cy="157.97" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 78; predicha: 75,9 años</title></circle>
<circle cx="314.67" cy="210.60" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 57; predicha: 62,9 años</title></circle>
<circle cx="391.94" cy="157.14" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 70; predicha: 76,1 años</title></circle>
<circle cx="433.56" cy="175.54" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 77; predicha: 71,6 años</title></circle>
<circle cx="308.72" cy="241.80" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 56; predicha: 55,2 años</title></circle>
<circle cx="374.11" cy="192.41" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 67; predicha: 67,4 años</title></circle>
<circle cx="427.61" cy="177.25" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 76; predicha: 71,2 años</title></circle>
<circle cx="504.89" cy="150.55" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 89; predicha: 77,7 años</title></circle>
<circle cx="386.00" cy="202.82" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 64,9 años</title></circle>
<circle cx="356.28" cy="249.04" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 64; predicha: 53,5 años</title></circle>
<circle cx="136.33" cy="314.98" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 27; predicha: 37,2 años</title></circle>
<circle cx="148.22" cy="344.80" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 29; predicha: 29,8 años</title></circle>
<circle cx="237.39" cy="269.38" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 44; predicha: 48,4 años</title></circle>
<circle cx="219.56" cy="277.65" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 41; predicha: 46,4 años</title></circle>
<circle cx="243.33" cy="275.77" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 45; predicha: 46,9 años</title></circle>
<circle cx="136.33" cy="339.85" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 27; predicha: 31,1 años</title></circle>
<circle cx="261.17" cy="255.90" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 48; predicha: 51,8 años</title></circle>
<circle cx="308.72" cy="249.59" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 56; predicha: 53,3 años</title></circle>
<circle cx="177.94" cy="306.55" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 34; predicha: 39,3 años</title></circle>
<circle cx="386.00" cy="232.17" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 57,6 años</title></circle>
<circle cx="255.22" cy="260.38" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 47; predicha: 50,7 años</title></circle>
<circle cx="237.39" cy="260.69" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 44; predicha: 50,6 años</title></circle>
<circle cx="195.78" cy="304.95" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 37; predicha: 39,7 años</title></circle>
<circle cx="136.33" cy="337.89" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 27; predicha: 31,5 años</title></circle>
<circle cx="386.00" cy="212.14" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 62,6 años</title></circle>
<circle cx="142.28" cy="320.42" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 28; predicha: 35,9 años</title></circle>
<circle cx="267.11" cy="258.64" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 49; predicha: 51,1 años</title></circle>
<circle cx="177.94" cy="297.74" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 34; predicha: 41,4 años</title></circle>
<circle cx="237.39" cy="256.59" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 44; predicha: 51,6 años</title></circle>
<circle cx="344.39" cy="179.89" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 62; predicha: 70,5 años</title></circle>
<circle cx="154.17" cy="291.95" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 30; predicha: 42,9 años</title></circle>
<circle cx="267.11" cy="248.68" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 49; predicha: 53,5 años</title></circle>
<circle cx="189.83" cy="302.24" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 36; predicha: 40,3 años</title></circle>
<circle cx="124.44" cy="337.81" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 25; predicha: 31,6 años</title></circle>
<circle cx="189.83" cy="297.70" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 36; predicha: 41,5 años</title></circle>
<circle cx="100.67" cy="347.93" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 21; predicha: 29,1 años</title></circle>
<circle cx="213.61" cy="278.93" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 40; predicha: 46,1 años</title></circle>
<circle cx="106.61" cy="358.29" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 22; predicha: 26,5 años</title></circle>
<circle cx="189.83" cy="276.07" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 36; predicha: 46,8 años</title></circle>
<circle cx="391.94" cy="160.71" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 70; predicha: 75,2 años</title></circle>
<circle cx="356.28" cy="196.12" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 64; predicha: 66,5 años</title></circle>
<circle cx="273.06" cy="245.19" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 50; predicha: 54,4 años</title></circle>
<circle cx="415.72" cy="111.78" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 74; predicha: 87,3 años</title></circle>
<circle cx="386.00" cy="189.23" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 68,2 años</title></circle>
<circle cx="487.06" cy="119.17" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 86; predicha: 85,5 años</title></circle>
<circle cx="368.17" cy="214.33" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 66; predicha: 62,0 años</title></circle>
<circle cx="391.94" cy="160.04" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 70; predicha: 75,4 años</title></circle>
<circle cx="504.89" cy="99.61" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 89; predicha: 90,3 años</title></circle>
<circle cx="439.50" cy="146.34" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 78; predicha: 78,8 años</title></circle>
<circle cx="386.00" cy="168.79" r="4" fill="#446ddf" fill-opacity=".65"><title>Edad real: 69; predicha: 73,2 años</title></circle>
<text x="330" y="457" text-anchor="middle" font-size="16">Edad real (años)</text><text transform="translate(18 225) rotate(-90)" text-anchor="middle" font-size="16">Edad predicha (años)</text></svg><figcaption>Cada punto es una persona. La línea discontinua representa el acierto perfecto. Fuente: predicciones propias sobre GSE40279.</figcaption></figure>

La mejora es clara, pero cinco años de error medio no significan que todo el mundo quede a cinco años de su cumpleaños. Hay aciertos cercanos y fallos bastante mayores. La media los mete en la misma bolsa.

## El regalo de cumpleaños que hace el modelo

Al separar edades aparece el detalle que cambia la lectura. En las 16 personas menores de 40 años, el reloj añade **6,5 años de media**. En las 17 de 80 o más, resta **7 años**. En estas últimas, el error absoluto medio asciende a 7,2 años.

El siguiente gráfico muestra la dirección del error. Las barras positivas añaden años; las negativas los quitan. Los tamaños de cada grupo importan: son pocos casos para convertir este patrón en una regla universal.

<figure class="grafico-interactivo" style="margin:1.75rem 0"><svg viewBox="0 0 640 345" role="img" aria-labelledby="sesgo-titulo sesgo-descripcion" style="width:100%;height:auto;font-family:inherit">
<title id="sesgo-titulo">El modelo suma años a los jóvenes y se los resta a los mayores</title>
<desc id="sesgo-descripcion">Error medio con signo: de 19 a 39 años, más 6,5; de 40 a 59, más 2,4; de 60 a 79, menos 0,4; desde 80, menos 7,0 años. Grupos de 16, 40, 54 y 17 personas.</desc>
<path d="M55 256H620" stroke="#ddd9d0"/><text x="45" y="261" text-anchor="end" font-size="14">-8</text>
<path d="M55 204H620" stroke="#ddd9d0"/><text x="45" y="209" text-anchor="end" font-size="14">-4</text>
<path d="M55 152H620" stroke="#777"/><text x="45" y="157" text-anchor="end" font-size="14">+0</text>
<path d="M55 100H620" stroke="#ddd9d0"/><text x="45" y="105" text-anchor="end" font-size="14">+4</text>
<path d="M55 48H620" stroke="#ddd9d0"/><text x="45" y="53" text-anchor="end" font-size="14">+8</text>
<rect x="85" y="68.0" width="70" height="84.0" fill="#446ddf"/><text x="120" y="59.0" text-anchor="middle" font-size="17">6,5</text>
<text x="120" y="292" text-anchor="middle" font-size="15">19–39</text><text x="120" y="314" text-anchor="middle" font-size="13">16 personas</text>
<rect x="225" y="120.5" width="70" height="31.5" fill="#446ddf"/><text x="260" y="111.5" text-anchor="middle" font-size="17">2,4</text>
<text x="260" y="292" text-anchor="middle" font-size="15">40–59</text><text x="260" y="314" text-anchor="middle" font-size="13">40 personas</text>
<rect x="365" y="152.0" width="70" height="4.7" fill="#446ddf"/><text x="400" y="176.7" text-anchor="middle" font-size="17">-0,4</text>
<text x="400" y="292" text-anchor="middle" font-size="15">60–79</text><text x="400" y="314" text-anchor="middle" font-size="13">54 personas</text>
<rect x="505" y="152.0" width="70" height="91.2" fill="#446ddf"/><text x="540" y="263.2" text-anchor="middle" font-size="17">-7,0</text>
<text x="540" y="292" text-anchor="middle" font-size="15">80 o más</text><text x="540" y="314" text-anchor="middle" font-size="13">17 personas</text>
<text x="320" y="20" text-anchor="middle" font-size="15">Años que añade (+) o quita (−), de media</text></svg><figcaption>Grupos de edad real. Son errores del modelo, no cambios observados en el cuerpo. Fuente: prueba reservada.</figcaption></figure>

El resultado es compatible con una **tendencia a acercar las predicciones al centro de las edades**. Un modelo puede hacer parecer mayores a los jóvenes y más jóvenes a los mayores sin que sus cuerpos hayan cambiado durante el experimento.

Puedes **comprobarlo caso por caso**. Primero verás la edad calculada y su margen; después, al pulsar, el cumpleaños real. Todos los casos pertenecen a la prueba, sin escoger únicamente los más llamativos.

<div id="reloj-adn" class="grafico-interactivo" style="text-align:center">
  <label for="persona-adn">Elige una persona de la prueba</label><br>
  <select id="persona-adn" style="margin:.75rem;padding:.5rem;max-width:100%"><option value="0">Persona 1 de 127</option><option value="1">Persona 2 de 127</option><option value="2">Persona 3 de 127</option><option value="3">Persona 4 de 127</option><option value="4">Persona 5 de 127</option><option value="5">Persona 6 de 127</option><option value="6">Persona 7 de 127</option><option value="7">Persona 8 de 127</option><option value="8">Persona 9 de 127</option><option value="9">Persona 10 de 127</option><option value="10">Persona 11 de 127</option><option value="11">Persona 12 de 127</option><option value="12">Persona 13 de 127</option><option value="13">Persona 14 de 127</option><option value="14">Persona 15 de 127</option><option value="15">Persona 16 de 127</option><option value="16">Persona 17 de 127</option><option value="17">Persona 18 de 127</option><option value="18">Persona 19 de 127</option><option value="19">Persona 20 de 127</option><option value="20">Persona 21 de 127</option><option value="21">Persona 22 de 127</option><option value="22">Persona 23 de 127</option><option value="23">Persona 24 de 127</option><option value="24">Persona 25 de 127</option><option value="25">Persona 26 de 127</option><option value="26">Persona 27 de 127</option><option value="27">Persona 28 de 127</option><option value="28">Persona 29 de 127</option><option value="29">Persona 30 de 127</option><option value="30">Persona 31 de 127</option><option value="31">Persona 32 de 127</option><option value="32">Persona 33 de 127</option><option value="33">Persona 34 de 127</option><option value="34">Persona 35 de 127</option><option value="35">Persona 36 de 127</option><option value="36">Persona 37 de 127</option><option value="37">Persona 38 de 127</option><option value="38">Persona 39 de 127</option><option value="39">Persona 40 de 127</option><option value="40">Persona 41 de 127</option><option value="41">Persona 42 de 127</option><option value="42">Persona 43 de 127</option><option value="43">Persona 44 de 127</option><option value="44">Persona 45 de 127</option><option value="45">Persona 46 de 127</option><option value="46">Persona 47 de 127</option><option value="47">Persona 48 de 127</option><option value="48">Persona 49 de 127</option><option value="49">Persona 50 de 127</option><option value="50">Persona 51 de 127</option><option value="51">Persona 52 de 127</option><option value="52">Persona 53 de 127</option><option value="53">Persona 54 de 127</option><option value="54">Persona 55 de 127</option><option value="55">Persona 56 de 127</option><option value="56">Persona 57 de 127</option><option value="57">Persona 58 de 127</option><option value="58">Persona 59 de 127</option><option value="59">Persona 60 de 127</option><option value="60">Persona 61 de 127</option><option value="61">Persona 62 de 127</option><option value="62">Persona 63 de 127</option><option value="63">Persona 64 de 127</option><option value="64">Persona 65 de 127</option><option value="65">Persona 66 de 127</option><option value="66">Persona 67 de 127</option><option value="67">Persona 68 de 127</option><option value="68">Persona 69 de 127</option><option value="69">Persona 70 de 127</option><option value="70">Persona 71 de 127</option><option value="71">Persona 72 de 127</option><option value="72">Persona 73 de 127</option><option value="73">Persona 74 de 127</option><option value="74">Persona 75 de 127</option><option value="75">Persona 76 de 127</option><option value="76">Persona 77 de 127</option><option value="77">Persona 78 de 127</option><option value="78">Persona 79 de 127</option><option value="79">Persona 80 de 127</option><option value="80">Persona 81 de 127</option><option value="81">Persona 82 de 127</option><option value="82">Persona 83 de 127</option><option value="83">Persona 84 de 127</option><option value="84">Persona 85 de 127</option><option value="85">Persona 86 de 127</option><option value="86">Persona 87 de 127</option><option value="87">Persona 88 de 127</option><option value="88">Persona 89 de 127</option><option value="89">Persona 90 de 127</option><option value="90">Persona 91 de 127</option><option value="91">Persona 92 de 127</option><option value="92">Persona 93 de 127</option><option value="93">Persona 94 de 127</option><option value="94">Persona 95 de 127</option><option value="95">Persona 96 de 127</option><option value="96">Persona 97 de 127</option><option value="97">Persona 98 de 127</option><option value="98">Persona 99 de 127</option><option value="99">Persona 100 de 127</option><option value="100">Persona 101 de 127</option><option value="101">Persona 102 de 127</option><option value="102">Persona 103 de 127</option><option value="103">Persona 104 de 127</option><option value="104">Persona 105 de 127</option><option value="105">Persona 106 de 127</option><option value="106">Persona 107 de 127</option><option value="107">Persona 108 de 127</option><option value="108">Persona 109 de 127</option><option value="109">Persona 110 de 127</option><option value="110">Persona 111 de 127</option><option value="111">Persona 112 de 127</option><option value="112">Persona 113 de 127</option><option value="113">Persona 114 de 127</option><option value="114">Persona 115 de 127</option><option value="115">Persona 116 de 127</option><option value="116">Persona 117 de 127</option><option value="117">Persona 118 de 127</option><option value="118">Persona 119 de 127</option><option value="119">Persona 120 de 127</option><option value="120">Persona 121 de 127</option><option value="121">Persona 122 de 127</option><option value="122">Persona 123 de 127</option><option value="123">Persona 124 de 127</option><option value="124">Persona 125 de 127</option><option value="125">Persona 126 de 127</option><option value="126">Persona 127 de 127</option></select>
  <p id="prediccion-adn" aria-live="polite"></p>
  <button id="revelar-adn" type="button" style="padding:.65rem 1rem;background:#446ddf;color:white;border:0;border-radius:4px;font:inherit;cursor:pointer">Revelar la edad real</button>
  <p id="resultado-adn" aria-live="polite"></p>
  <noscript>Para probar la revelación, activa JavaScript. También puedes consultar todas las edades y predicciones en el archivo descargable al final.</noscript>
</div>
<script>
window.addEventListener('DOMContentLoaded', () => {
  const casos = [{"edad": 54, "prediccion": 62.126, "inferior": 52.487, "superior": 71.765}, {"edad": 101, "prediccion": 84.118, "inferior": 74.479, "superior": 93.756}, {"edad": 79, "prediccion": 80.059, "inferior": 70.42, "superior": 89.697}, {"edad": 84, "prediccion": 78.939, "inferior": 69.3, "superior": 88.577}, {"edad": 85, "prediccion": 73.316, "inferior": 63.678, "superior": 82.955}, {"edad": 87, "prediccion": 81.186, "inferior": 71.548, "superior": 90.825}, {"edad": 74, "prediccion": 78.969, "inferior": 69.33, "superior": 88.607}, {"edad": 77, "prediccion": 70.809, "inferior": 61.171, "superior": 80.448}, {"edad": 73, "prediccion": 68.858, "inferior": 59.219, "superior": 78.496}, {"edad": 87, "prediccion": 84.376, "inferior": 74.738, "superior": 94.015}, {"edad": 85, "prediccion": 74.056, "inferior": 64.418, "superior": 83.695}, {"edad": 78, "prediccion": 79.374, "inferior": 69.735, "superior": 89.013}, {"edad": 65, "prediccion": 66.343, "inferior": 56.704, "superior": 75.982}, {"edad": 65, "prediccion": 69.524, "inferior": 59.886, "superior": 79.163}, {"edad": 89, "prediccion": 84.856, "inferior": 75.217, "superior": 94.494}, {"edad": 85, "prediccion": 83.082, "inferior": 73.443, "superior": 92.72}, {"edad": 66, "prediccion": 59.546, "inferior": 49.907, "superior": 69.184}, {"edad": 76, "prediccion": 71.277, "inferior": 61.638, "superior": 80.916}, {"edad": 74, "prediccion": 76.906, "inferior": 67.267, "superior": 86.545}, {"edad": 84, "prediccion": 78.744, "inferior": 69.106, "superior": 88.383}, {"edad": 71, "prediccion": 70.832, "inferior": 61.193, "superior": 80.47}, {"edad": 48, "prediccion": 51.182, "inferior": 41.543, "superior": 60.82}, {"edad": 71, "prediccion": 67.972, "inferior": 58.333, "superior": 77.611}, {"edad": 52, "prediccion": 52.771, "inferior": 43.132, "superior": 62.41}, {"edad": 64, "prediccion": 57.032, "inferior": 47.393, "superior": 66.671}, {"edad": 48, "prediccion": 48.013, "inferior": 38.374, "superior": 57.651}, {"edad": 55, "prediccion": 53.586, "inferior": 43.948, "superior": 63.225}, {"edad": 68, "prediccion": 68.454, "inferior": 58.816, "superior": 78.093}, {"edad": 46, "prediccion": 43.508, "inferior": 33.869, "superior": 53.147}, {"edad": 64, "prediccion": 60.75, "inferior": 51.112, "superior": 70.389}, {"edad": 57, "prediccion": 55.337, "inferior": 45.698, "superior": 64.976}, {"edad": 45, "prediccion": 46.243, "inferior": 36.604, "superior": 55.882}, {"edad": 51, "prediccion": 53.263, "inferior": 43.625, "superior": 62.902}, {"edad": 58, "prediccion": 53.919, "inferior": 44.28, "superior": 63.557}, {"edad": 63, "prediccion": 58.538, "inferior": 48.899, "superior": 68.177}, {"edad": 55, "prediccion": 57.316, "inferior": 47.678, "superior": 66.955}, {"edad": 50, "prediccion": 56.245, "inferior": 46.606, "superior": 65.884}, {"edad": 57, "prediccion": 60.29, "inferior": 50.651, "superior": 69.928}, {"edad": 33, "prediccion": 40.866, "inferior": 31.228, "superior": 50.505}, {"edad": 46, "prediccion": 50.333, "inferior": 40.694, "superior": 59.971}, {"edad": 46, "prediccion": 52.069, "inferior": 42.431, "superior": 61.708}, {"edad": 66, "prediccion": 58.217, "inferior": 48.578, "superior": 67.856}, {"edad": 55, "prediccion": 57.676, "inferior": 48.038, "superior": 67.315}, {"edad": 64, "prediccion": 57.545, "inferior": 47.906, "superior": 67.183}, {"edad": 85, "prediccion": 71.001, "inferior": 61.362, "superior": 80.64}, {"edad": 66, "prediccion": 66.307, "inferior": 56.668, "superior": 75.946}, {"edad": 69, "prediccion": 72.155, "inferior": 62.516, "superior": 81.794}, {"edad": 84, "prediccion": 73.065, "inferior": 63.427, "superior": 82.704}, {"edad": 79, "prediccion": 70.108, "inferior": 60.469, "superior": 79.746}, {"edad": 64, "prediccion": 59.149, "inferior": 49.511, "superior": 68.788}, {"edad": 78, "prediccion": 79.619, "inferior": 69.981, "superior": 89.258}, {"edad": 53, "prediccion": 64.613, "inferior": 54.974, "superior": 74.252}, {"edad": 59, "prediccion": 59.465, "inferior": 49.826, "superior": 69.104}, {"edad": 65, "prediccion": 63.477, "inferior": 53.838, "superior": 73.115}, {"edad": 61, "prediccion": 65.618, "inferior": 55.98, "superior": 75.257}, {"edad": 58, "prediccion": 50.651, "inferior": 41.012, "superior": 60.289}, {"edad": 52, "prediccion": 55.192, "inferior": 45.554, "superior": 64.831}, {"edad": 65, "prediccion": 65.938, "inferior": 56.3, "superior": 75.577}, {"edad": 73, "prediccion": 69.882, "inferior": 60.243, "superior": 79.521}, {"edad": 65, "prediccion": 64.404, "inferior": 54.765, "superior": 74.043}, {"edad": 84, "prediccion": 80.771, "inferior": 71.133, "superior": 90.41}, {"edad": 51, "prediccion": 54.712, "inferior": 45.074, "superior": 64.351}, {"edad": 78, "prediccion": 74.433, "inferior": 64.795, "superior": 84.072}, {"edad": 53, "prediccion": 57.063, "inferior": 47.425, "superior": 66.702}, {"edad": 68, "prediccion": 79.174, "inferior": 69.536, "superior": 88.813}, {"edad": 52, "prediccion": 53.926, "inferior": 44.287, "superior": 63.565}, {"edad": 72, "prediccion": 65.138, "inferior": 55.5, "superior": 74.777}, {"edad": 48, "prediccion": 50.238, "inferior": 40.6, "superior": 59.877}, {"edad": 60, "prediccion": 54.491, "inferior": 44.852, "superior": 64.13}, {"edad": 61, "prediccion": 107.921, "inferior": 98.282, "superior": 117.56}, {"edad": 69, "prediccion": 73.304, "inferior": 63.665, "superior": 82.942}, {"edad": 81, "prediccion": 68.546, "inferior": 58.907, "superior": 78.185}, {"edad": 56, "prediccion": 59.357, "inferior": 49.719, "superior": 68.996}, {"edad": 79, "prediccion": 70.428, "inferior": 60.79, "superior": 80.067}, {"edad": 82, "prediccion": 78.113, "inferior": 68.474, "superior": 87.752}, {"edad": 58, "prediccion": 47.939, "inferior": 38.3, "superior": 57.578}, {"edad": 75, "prediccion": 65.928, "inferior": 56.29, "superior": 75.567}, {"edad": 78, "prediccion": 75.911, "inferior": 66.272, "superior": 85.549}, {"edad": 57, "prediccion": 62.933, "inferior": 53.295, "superior": 72.572}, {"edad": 70, "prediccion": 76.116, "inferior": 66.477, "superior": 85.755}, {"edad": 77, "prediccion": 71.58, "inferior": 61.941, "superior": 81.218}, {"edad": 56, "prediccion": 55.242, "inferior": 45.603, "superior": 64.88}, {"edad": 67, "prediccion": 67.42, "inferior": 57.781, "superior": 77.058}, {"edad": 76, "prediccion": 71.159, "inferior": 61.52, "superior": 80.797}, {"edad": 89, "prediccion": 77.74, "inferior": 68.102, "superior": 87.379}, {"edad": 69, "prediccion": 64.852, "inferior": 55.214, "superior": 74.491}, {"edad": 64, "prediccion": 53.456, "inferior": 43.818, "superior": 63.095}, {"edad": 27, "prediccion": 37.197, "inferior": 27.559, "superior": 46.836}, {"edad": 29, "prediccion": 29.843, "inferior": 20.204, "superior": 39.481}, {"edad": 44, "prediccion": 48.441, "inferior": 38.802, "superior": 58.079}, {"edad": 41, "prediccion": 46.4, "inferior": 36.761, "superior": 56.039}, {"edad": 45, "prediccion": 46.865, "inferior": 37.226, "superior": 56.504}, {"edad": 27, "prediccion": 31.064, "inferior": 21.425, "superior": 40.703}, {"edad": 48, "prediccion": 51.764, "inferior": 42.125, "superior": 61.402}, {"edad": 56, "prediccion": 53.321, "inferior": 43.683, "superior": 62.96}, {"edad": 34, "prediccion": 39.277, "inferior": 29.638, "superior": 48.915}, {"edad": 69, "prediccion": 57.617, "inferior": 47.978, "superior": 67.255}, {"edad": 47, "prediccion": 50.661, "inferior": 41.022, "superior": 60.299}, {"edad": 44, "prediccion": 50.582, "inferior": 40.943, "superior": 60.221}, {"edad": 37, "prediccion": 39.669, "inferior": 30.03, "superior": 49.308}, {"edad": 27, "prediccion": 31.547, "inferior": 21.908, "superior": 41.186}, {"edad": 69, "prediccion": 62.555, "inferior": 52.916, "superior": 72.194}, {"edad": 28, "prediccion": 35.856, "inferior": 26.218, "superior": 45.495}, {"edad": 49, "prediccion": 51.09, "inferior": 41.451, "superior": 60.728}, {"edad": 34, "prediccion": 41.447, "inferior": 31.809, "superior": 51.086}, {"edad": 44, "prediccion": 51.594, "inferior": 41.956, "superior": 61.233}, {"edad": 62, "prediccion": 70.508, "inferior": 60.869, "superior": 80.146}, {"edad": 30, "prediccion": 42.874, "inferior": 33.236, "superior": 52.513}, {"edad": 49, "prediccion": 53.544, "inferior": 43.906, "superior": 63.183}, {"edad": 36, "prediccion": 40.338, "inferior": 30.7, "superior": 49.977}, {"edad": 25, "prediccion": 31.567, "inferior": 21.928, "superior": 41.206}, {"edad": 36, "prediccion": 41.458, "inferior": 31.819, "superior": 51.096}, {"edad": 21, "prediccion": 29.072, "inferior": 19.433, "superior": 38.711}, {"edad": 40, "prediccion": 46.086, "inferior": 36.447, "superior": 55.725}, {"edad": 22, "prediccion": 26.518, "inferior": 16.879, "superior": 36.157}, {"edad": 36, "prediccion": 46.792, "inferior": 37.153, "superior": 56.431}, {"edad": 70, "prediccion": 75.236, "inferior": 65.597, "superior": 84.874}, {"edad": 64, "prediccion": 66.504, "inferior": 56.865, "superior": 76.143}, {"edad": 50, "prediccion": 54.404, "inferior": 44.765, "superior": 64.043}, {"edad": 74, "prediccion": 87.3, "inferior": 77.662, "superior": 96.939}, {"edad": 69, "prediccion": 68.204, "inferior": 58.565, "superior": 77.843}, {"edad": 86, "prediccion": 85.479, "inferior": 75.84, "superior": 95.118}, {"edad": 66, "prediccion": 62.014, "inferior": 52.375, "superior": 71.653}, {"edad": 70, "prediccion": 75.401, "inferior": 65.762, "superior": 85.039}, {"edad": 89, "prediccion": 90.301, "inferior": 80.662, "superior": 99.94}, {"edad": 78, "prediccion": 78.779, "inferior": 69.141, "superior": 88.418}, {"edad": 69, "prediccion": 73.242, "inferior": 63.604, "superior": 82.881}];
  const selector = document.getElementById('persona-adn');
  const prediccion = document.getElementById('prediccion-adn');
  const resultado = document.getElementById('resultado-adn');
  const boton = document.getElementById('revelar-adn');
  if (!selector || !prediccion || !resultado || !boton) return;
  const numero = valor => valor.toLocaleString('es-ES', {minimumFractionDigits:1, maximumFractionDigits:1});
  const actualizar = () => {
    const caso = casos[Number(selector.value)];
    prediccion.textContent = `Edad calculada: ${numero(caso.prediccion)} años. Banda calibrada: de ${numero(caso.inferior)} a ${numero(caso.superior)} años.`;
    resultado.textContent = '';
    boton.disabled = false;
  };
  selector.addEventListener('change', actualizar);
  boton.addEventListener('click', () => {
    const caso = casos[Number(selector.value)];
    const diferencia = caso.prediccion - caso.edad;
    const dentro = caso.edad >= caso.inferior && caso.edad <= caso.superior;
    resultado.textContent = `Edad real: ${caso.edad} años. El modelo le asignó ${numero(Math.abs(diferencia))} años de ${diferencia >= 0 ? 'más' : 'menos'}. Su edad real ${dentro ? 'queda dentro' : 'queda fuera'} de la banda. Esto describe un error, no un cambio en su salud.`;
    boton.disabled = true;
  });
  actualizar();
});
</script>

## Que el modelo te quite años no significa que hayas rejuvenecido

Para acompañar cada edad calculada, añadí un margen de unos 9,6 años por encima y por debajo. Ese margen incluyó la edad real de 110 de las 127 personas de prueba. Las otras 17 quedaron fuera. Además, todas las muestras proceden del mismo estudio: todavía **faltaría comprobar cómo funciona el modelo con personas de otra población o en otro laboratorio**.

La búsqueda del rejuvenecimiento que protagoniza National Geographic en su número de noviembre exige distinguir dos cosas: que un modelo calcule una edad menor y que el cuerpo haya rejuvenecido. Mi prueba solo permite hablar de la primera. A los mayores de 80 años les asignó siete años menos de media, sin haber ensayado ningún tratamiento. Una edad predicha más joven, por sí sola, no demuestra rejuvenecimiento.

Comprobar qué significa realmente una cifra también cambió otras historias de Nebula: la de [una ameba que soporta temperaturas extremas, pero no conserva todas sus capacidades](/nebula/articulos/ameba-fuego-limites-calor/), y la de [un fósil que cuenta una historia mucho más antigua que la Esfinge](/nebula/articulos/cocodrilo-esfinge-maquina-tiempo/). En ciencia, **el dato que llama la atención es el principio de la historia**. Después hay que averiguar qué permite concluir.

Puedes revisar el [notebook ejecutado](/nebula/analisis/edad-adn/edad_adn.ipynb), las [predicciones de prueba](/nebula/analisis/edad-adn/resultados/predicciones_prueba.csv) y la [guía con los datos y el código](/nebula/analisis/edad-adn/README.md). La fuente original es el [repositorio público GSE40279](/nebula/analisis/edad-adn/data/fuentes.json), disponible en [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE40279).

También puedes descargar el [paquete reproducible completo (56 MB)](/nebula/analisis/edad-adn/edad-adn-reproducible.zip).
