---
titulo: "El Tesla Roadster ya ha volado. Estas son las cifras que explican la locura"
descripcion: "La versión más extrema recurre a diez propulsores, supera 4,6 g de aceleración y no está aprobada para circular por vías públicas."
tema: "TECNOLOGÍA"
fecha: 2026-10-16T09:00:00+02:00
imagenPortada: "/nebula/imagenes/tesla_roadster_datos_portada.png"
cifraDestacada: "7,9 metros"
etiquetaCifra: "es la distancia teórica para alcanzar 100 km/h"
metodologia: "EDA de las tres versiones anunciadas del Roadster, la prueba de 0 a 60 mph mostrada por Tesla y cuatro eléctricos de producción con tiempos publicados por sus fabricantes. Se distinguen demostraciones, objetivos futuros y prestaciones de producción. Las conversiones a fuerzas g y distancia suponen aceleración constante. También se comparan las especificaciones de 2017 y 2026, el calendario y el valor temporal de la reserva. No se predice la llegada del coche ni se equiparan protocolos de prueba diferentes."
---

*Veo un coche subir por una pared, quedarse boca abajo, salir despedido, dar una vuelta en el aire y aterrizar entre dos nubes blancas. Me parece el truco final de una película. Esta vez estoy viendo la presentación del nuevo Tesla Roadster.*

La demostración del 15 de octubre en las instalaciones de SpaceX, en Texas, me deja imágenes difíciles de olvidar. El prototipo alcanza 170 grados de inclinación a unos 21 metros de altura, se desprende de la rampa y utiliza propulsores de aire comprimido para controlar la caída.

Tesla también muestra una **aceleración hasta cerca de 100 kilómetros por hora en 0,81 segundos**. Sin embargo, creo que es posible contar tres historias distintas: lo que acabo de ver, lo que la compañía promete para 2028 y lo que todavía no sé. Para separarlas he reunido la telemetría del acto, las especificaciones publicadas y los datos de cuatro vehículos eléctricos de producción.

## Tres Roadster y una promesa extrema

La compañía de Elon Musk ha anunciado tres versiones de este Roadster. La Performance bajaría de 1,6 segundos en el 0 a 100 km/h. La Thrust añadiría propulsores traseros y lo haría en menos de 0,9 segundos. Por último, la Rocket, con una sola plaza y diez propulsores alrededor del vehículo, bajaría de **0,59 segundos** y podría desplazarse por el aire.

El Rocket también superaría los 370 km/h, pero [Tesla indica que no está aprobado para circular por vías públicas](https://x.com/Tesla/status/2110905588402295283). La autonomía anunciada para la gama supera los 480 kilómetros. Faltan el precio final, la masa del coche y las condiciones exactas de medición.

Son objetivos futuros. Por eso los comparo, por cercanía, con el [Rimac Nevera R](https://www.rimac-automobili.com/NeveraR/), que declara 1,66 segundos, el [Pininfarina Battista](https://www.automobili-pininfarina.com/media-hub/press-releases/automobili-pininfarina-confirms-record-breaking-battista-performance-uae), que registró 1,79 durante su homologación, y otros dos modelos documentados por sus fabricantes.

<div class="grafico-interactivo">
  <canvas id="grafico-aceleracion-roadster" height="330" role="img" aria-label="Comparación de tiempos de cero a sesenta millas por hora. El objetivo del Roadster Rocket es inferior a 0,59 segundos y la prueba mostrada por Tesla fue de 0,81 segundos."></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-aceleracion-roadster');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Roadster Rocket*', 'Prueba mostrada por Tesla', 'Roadster Thrust*', 'Roadster Performance*', 'Nevera R', 'Battista', 'Air Sapphire', 'Model S Plaid†'],
        datasets: [{
          data: [0.59, 0.81, 0.9, 1.6, 1.66, 1.79, 1.89, 1.99],
          backgroundColor: ['#d85a30', '#2a9d8f', '#d85a30', '#d85a30', '#446ddf', '#446ddf', '#446ddf', '#446ddf'],
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          legend: { display: false },
          title: { display: true, text: 'La demostración se acerca al objetivo, pero no lo alcanza' },
          tooltip: { callbacks: { label: c => `${c.raw} segundos` } }
        },
        scales: { x: { beginAtZero: true, title: { display: true, text: 'Segundos de 0 a 60 mph' } } }
      }
    });
  });
</script>

*Los tres Roadster son objetivos para un producto futuro. La prueba de 0,81 segundos fue mostrada por Tesla. El Model S Plaid descuenta el rollout y los protocolos pueden diferir.*

## ¿Hasta dónde llegaría antes de alcanzar 100 km/h?

Antes de hacer la cuenta, propongo una apuesta:

<div id="experimento-roadster" class="experimento-roadster" aria-labelledby="pregunta-distancia">
  <p id="pregunta-distancia"><strong>¿Qué distancia recorrería el Rocket en 0,59 segundos si acelerase de manera constante?</strong></p>
  <div class="opciones-roadster" role="group" aria-label="elige una distancia">
    <button type="button" data-apuesta="8">Unos 8 metros</button>
    <button type="button" data-apuesta="11">Unos 11 metros</button>
    <button type="button" data-apuesta="22">Unos 22 metros</button>
  </div>
  <p class="respuesta-roadster" aria-live="polite">Elige una distancia antes de continuar.</p>

  <div class="comparador-roadster" hidden>
    <p><strong>Cambia de coche y observa dónde termina la aceleración:</strong></p>
    <div class="modelos-roadster" role="group" aria-label="compara vehículos">
      <button type="button" class="activo" data-modelo="rocket">Rocket</button>
      <button type="button" data-modelo="demo">Prueba de Tesla</button>
      <button type="button" data-modelo="nevera">Nevera R</button>
      <button type="button" data-modelo="battista">Battista</button>
    </div>
    <div class="pista-roadster" aria-hidden="true">
      <span class="marca-roadster"></span>
      <span class="pista-inicio">0 m</span>
      <span class="pista-final">25 m</span>
    </div>
    <p class="dato-roadster" aria-live="polite"></p>
  </div>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const caja = document.getElementById('experimento-roadster');
    if (!caja) return;
    const respuesta = caja.querySelector('.respuesta-roadster');
    const comparador = caja.querySelector('.comparador-roadster');
    const marca = caja.querySelector('.marca-roadster');
    const dato = caja.querySelector('.dato-roadster');
    const modelos = {
      rocket: { nombre: 'Roadster Rocket', tiempo: 0.59, distancia: 7.91, g: 4.64, estado: 'objetivo anunciado' },
      demo: { nombre: 'Prueba mostrada por Tesla', tiempo: 0.81, distancia: 10.86, g: 3.38, estado: 'demostración del fabricante' },
      nevera: { nombre: 'Rimac Nevera R', tiempo: 1.66, distancia: 22.26, g: 1.65, estado: 'dato del fabricante' },
      battista: { nombre: 'Pininfarina Battista', tiempo: 1.79, distancia: 24.01, g: 1.53, estado: 'prueba de homologación' }
    };

    const mostrarModelo = (clave) => {
      const modelo = modelos[clave];
      marca.style.left = `${modelo.distancia / 25 * 100}%`;
      dato.innerHTML = `<strong>${modelo.nombre}:</strong> ${modelo.distancia.toLocaleString('es-ES')} metros, ${modelo.g.toLocaleString('es-ES')} g de media y ${modelo.tiempo.toLocaleString('es-ES')} segundos. <span>${modelo.estado}.</span>`;
    };

    caja.querySelectorAll('[data-apuesta]').forEach((boton) => {
      boton.addEventListener('click', () => {
        caja.querySelectorAll('[data-apuesta]').forEach(opcion => opcion.classList.toggle('seleccionado', opcion === boton));
        respuesta.innerHTML = boton.dataset.apuesta === '8'
          ? '<strong>Exacto.</strong> El cálculo da 7,9 metros: menos que la longitud de dos coches grandes.'
          : '<strong>El resultado es aún más extremo.</strong> El cálculo da solo 7,9 metros.';
        comparador.hidden = false;
        mostrarModelo('rocket');
      });
    });

    caja.querySelectorAll('[data-modelo]').forEach((boton) => {
      boton.addEventListener('click', () => {
        caja.querySelectorAll('[data-modelo]').forEach(opcion => opcion.classList.toggle('activo', opcion === boton));
        mostrarModelo(boton.dataset.modelo);
      });
    });
  });
</script>

<style>
  .experimento-roadster { margin: 1.75rem 0; padding: 1.25rem; border: 1px solid rgba(68,109,223,.24); border-radius: 14px; background: rgba(68,109,223,.055); }
  .opciones-roadster, .modelos-roadster { display: flex; flex-wrap: wrap; gap: .65rem; margin: 1rem 0; }
  .opciones-roadster button, .modelos-roadster button { border: 1px solid #446ddf; border-radius: 999px; padding: .6rem .9rem; color: #294792; background: #fff; font: inherit; cursor: pointer; }
  .opciones-roadster button:hover, .opciones-roadster button:focus-visible, .opciones-roadster button.seleccionado, .modelos-roadster button:hover, .modelos-roadster button:focus-visible, .modelos-roadster button.activo { color: #fff; background: #446ddf; }
  .pista-roadster { position: relative; height: 58px; margin: 1.5rem .25rem .5rem; border-bottom: 4px solid #b9c7ef; }
  .marca-roadster { position: absolute; bottom: -8px; width: 13px; height: 13px; border-radius: 50%; background: #d85a30; transform: translateX(-50%); transition: left 450ms ease; }
  .pista-inicio, .pista-final { position: absolute; bottom: -2rem; font-size: .82rem; color: #555; }
  .pista-inicio { left: 0; } .pista-final { right: 0; }
  .dato-roadster { margin: 2.5rem 0 0; }
  .dato-roadster span { color: #666; }
</style>

La cifra de 0,59 segundos implica más de **4,6 g horizontales de media**. La prueba de 0,81 equivale a unos 3,4 g y 10,9 metros. Para alcanzar el objetivo, Tesla todavía tendría que recortar un 27% el tiempo mostrado.

No sumo esas fuerzas a los 2 g de succión: una empuja el coche hacia delante y la otra lo pega a la superficie. Los depósitos almacenan, según lo explicado durante el acto, unos 250 kilos de aire comprimido en 600 litros. Sin la masa total del coche no puedo convertir los más de 80 kN anunciados en una aceleración real.

En la rampa encuentro otra medida del espectáculo. La pantalla muestra una carga vertical equivalente a 4.700 kilos cerca de la posición invertida y un pico de 3,3 g durante la caída. No interpreto esas lecturas como una certificación: son telemetría ofrecida por Tesla en una demostración controlada. Sí muestran que el salto combina ventiladores, aerodinámica activa y propulsores cuando las ruedas dejan de tocar la superficie.

## Nueve años y un coche distinto

La propuesta también ha cambiado. En 2017 ofrecía cuatro plazas, 620 millas de autonomía y más de 400 km/h. En 2026 quedan dos plazas como máximo, una en el Rocket, unos 480 kilómetros y más de 370 km/h para la versión extrema. No puedo calcular una pérdida exacta de autonomía porque «más de 300» no es un valor cerrado.

Tesla anunció entonces producción para 2020. Entre aquella presentación y esta han transcurrido **3.255 días**. Ahora, el nuevo objetivo, 2028, queda ocho años por detrás del primero.

La espera también tiene precio. La **reserva del Performance** exige 50.000 dólares, unos **44.000 euros**. Las [condiciones de Tesla](https://www.tesla.com/configurator/api/v4/terms?locale=en_US&model=mt&saleType=PreSale) permiten cancelarla, pero el dinero no genera intereses. Según el IPC estadounidense, hoy harían falta unos 68.000 dólares, alrededor de **60.000 euros**, para conservar el poder de compra de 50.000 en noviembre de 2017. Una reinversión teórica en letras del Tesoro habría alcanzado unos 56.000 euros.

El Roadster que he visto es real como prototipo. Su vuelo también. Sus cifras más extremas, su homologación y su calendario continúan en el futuro. **Puedo alucinar con la demostración y exigir pruebas para las promesas al mismo tiempo.**

Puedes revisar los cálculos, las fuentes y las limitaciones en el [notebook ejecutado](/nebula/analisis/tesla-roadster-datos/tesla_roadster_datos.ipynb) y descargar la [tabla de aceleraciones](/nebula/analisis/tesla-roadster-datos/data/aceleracion_fabricantes.csv).
