---
titulo: "El negocio norcoreano que se escondía detrás de un empleo remoto"
descripcion: "Nombres prestados, portátiles y empresas que no sabían a quién contrataban."
tema: "TECNOLOGÍA"
fecha: 2026-10-15T09:00:00+02:00
imagenPortada: "/nebula/imagenes/norcoreanos_portada.png"
cifraDestacada: "3"
etiquetaCifra: "casos para entender el engaño"
metodologia: "EDA documental de cuatro comunicados del Departamento de Justicia estadounidense sobre tres casos. Corte: 15 de octubre de 2026. Se conservan calificadores, unidades y estado judicial. Se elimina una actualización repetida para comparar referencias por caso. No se suman empresas únicas ni se estima la incidencia global. Los ingresos se distinguen de los daños y los equipos no se convierten en trabajadores."
---

*El candidato supera la entrevista. La empresa le manda un portátil. Empieza a trabajar, entrega tareas y cobra su sueldo. Todo parece normal. Solo hay un pequeño problema: la persona contratada, el dueño de su nombre y quien utiliza el ordenador pueden ser tres personas diferentes.*

<div class="reto-identidad" aria-labelledby="pregunta-identidad">
  <p id="pregunta-identidad">
    <strong>El portátil está en Estados Unidos. ¿Qué demuestra eso?</strong>
  </p>

  <div class="reto-opciones" role="group" aria-label="Elige una respuesta">
    <button type="button" data-identidad="persona" aria-pressed="false">
      Que el empleado trabaja allí
    </button>
    <button type="button" data-identidad="equipo" aria-pressed="false">
      Que el ordenador está allí
    </button>
    <button type="button" data-identidad="nombre" aria-pressed="false">
      Que su identidad es auténtica
    </button>
  </div>

  <p class="reto-resultado" aria-live="polite" aria-atomic="true">
    Haz tu apuesta antes de seguir leyendo.
  </p>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    // preparo una revelación distinta para cada respuesta
    const bloque = document.querySelector('.reto-identidad');
    if (!bloque) return;

    const botones = bloque.querySelectorAll('[data-identidad]');
    const resultado = bloque.querySelector('.reto-resultado');

    const respuestas = {
      persona:
        'No necesariamente. Alguien puede manejar ese portátil desde otro país. El ordenador tiene una dirección; quien lo utiliza puede tener otra.',
      equipo:
        'Exacto. Has localizado una máquina, no a una persona. Esa diferencia permite que una casa llena de portátiles aparente ser el lugar de trabajo de empleados que están lejos.',
      nombre:
        'No. Una dirección real puede acompañar a un nombre prestado. Saber dónde está el portátil no demuestra quién está detrás del teclado.'
    };

    // marco la elección y explico qué permite concluir realmente
    botones.forEach((boton) => {
      boton.addEventListener('click', () => {
        botones.forEach((opcion) => {
          const seleccionado = opcion === boton;
          opcion.classList.toggle('seleccionado', seleccionado);
          opcion.setAttribute('aria-pressed', String(seleccionado));
        });

        resultado.textContent = respuestas[boton.dataset.identidad];
      });
    });
  });
</script>

<style>
  .reto-identidad {
    margin: 1.75rem 0;
    padding: 1.25rem;
    border: 1px solid rgba(68, 109, 223, 0.25);
    border-radius: 14px;
    background: rgba(68, 109, 223, 0.055);
  }

  .reto-identidad > p:first-child {
    margin-top: 0;
  }

  .reto-opciones {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin: 1rem 0;
  }

  .reto-opciones button {
    max-width: 100%;
    padding: 0.65rem 1rem;
    border: 1px solid #446ddf;
    border-radius: 999px;
    background: #fff;
    color: #294792;
    font: inherit;
    line-height: 1.4;
    cursor: pointer;
    transition: background-color 150ms ease, color 150ms ease;
  }

  .reto-opciones button:hover,
  .reto-opciones button.seleccionado {
    background: #446ddf;
    color: #fff;
  }

  .reto-opciones button:focus-visible {
    outline: 3px solid #294792;
    outline-offset: 3px;
  }

  .reto-resultado {
    margin-bottom: 0;
    line-height: 1.6;
  }
</style>

## El ordenador está donde debe. Su dueño, no

Imagina que compras una entrada de cine y mandas a alguien a sentarse por ti. El asiento está ocupado, pero tú no has pisado la sala. Algo parecido ocurre con las llamadas **granjas de portátiles**, aunque aquí la entrada abre la puerta de una empresa.

Son **lugares que alojan ordenadores enviados por empleadores**. Los equipos están en Estados Unidos. Quien trabaja con ellos puede encontrarse en otro país y manejarlos a distancia. El domicilio ayuda a sostener la apariencia de una contratación local.

No hace falta imaginar una guarida de película. Parte del decorado puede ser una casa corriente, una conexión a internet y alguien dispuesto a recibir paquetes.

## Un compañero con varias capas

Las **autoridades estadounidenses llevan años persiguiendo redes que utilizan ese mecanismo** para colocar trabajadores tecnológicos norcoreanos en empresas extranjeras. Según sus investigaciones, las identidades falsas o prestadas permiten conseguir empleos y generar ingresos para el régimen.

La operación anunciada el 13 de octubre de 2026 vuelve a mostrar ese engranaje. El Departamento de Justicia comunicó dos detenciones y la intervención de unos 187 dispositivos en Texas. El expediente describe más de 70 empresas afectadas y aproximadamente tres millones de dólares de ingresos. Son acusaciones pendientes de probar, no condenas.

Aquí aparece la **primera trampa** para quien lee deprisa: 187 dispositivos no significan 187 infiltrados.

Entre los aparatos había portátiles y dispositivos para controlar teclado, pantalla y ratón desde otro lugar. Contarlos como personas sería como calcular cuántos cocineros tiene un restaurante sumando sus sartenes. Sabemos qué se intervino; no podemos convertirlo automáticamente en una plantilla.

## La casa que conectaba con cientos de empresas

La historia ya tenía un capítulo llamativo en mayo de 2024. El caso alrededor de Christina Marie Chapman describía una granja de portátiles y una trama vinculada con más de 300 empresas estadounidenses. También recogía más de 60 identidades comprometidas y al menos 6,8 millones de dólares de ingresos para los trabajadores en el extranjero.

El detalle inquietante es que el ordenador podía estar exactamente donde la empresa esperaba encontrarlo. Comprobar su ubicación no resolvía quién estaba detrás del teclado. Una dirección auténtica podía sostener una identidad que no lo era.

He comparado ese expediente con el caso Wang y el anuncio de Texas. El gráfico muestra que hubo más de 300, 100 y 70 empresas afectadas en cada caso, pero no sabemos cuántas exactamente.

<div class="grafico-interactivo">
  <canvas id="grafico-empresas-norcoreanos" height="300" role="img" aria-label="Umbrales publicados de empresas afectadas: más de 300 en Chapman, más de 100 en Wang y más de 70 en Texas. No son recuentos exactos ni una serie temporal."></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const elemento = document.getElementById('grafico-empresas-norcoreanos');
    if (!elemento || !window.Chart) return;
    new Chart(elemento, {
      type: 'bar',
      data: {
        labels: ['Chapman · anuncio 2024', 'Wang · actualización 2026', 'Texas · anuncio 2026'],
        datasets: [{
          label: 'Umbral publicado de empresas afectadas',
          data: [300, 100, 70],
          backgroundColor: '#446ddf',
          borderRadius: 3
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (contexto) => `Más de ${contexto.raw} empresas; no es un recuento exacto`
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            title: { display: true, text: 'Umbral publicado: en todos los casos, «más de»' },
            ticks: { precision: 0 }
          }
        }
      }
    });
  });
</script>

No son tres fotografías anuales del mismo fenómeno. **Cada investigación abarca personas y periodos diferentes**. Que Texas tenga una barra menor no demuestra que el negocio esté menguando, igual que una redada pequeña no demuestra que haya menos delincuencia en todo un país.

## La noticia que parecía una red nueva

Al revisar las noticias apareció otra trampa: contar dos veces el mismo caso.

En junio de 2025 se anunciaron acusaciones en una red donde figuraban Kejia Wang y Zhenxing Wang. En abril de 2026 llegaron las sentencias de ambos facilitadores. Las dos noticias hablaban de más de cien empresas. Era el mismo caso, no otras cien empresas afectadas.

Una noticia anunciaba las acusaciones y otra, las condenas del mismo caso. Si sumamos las empresas mencionadas en ambas, las contamos dos veces.

Al sumar las cifras de las cuatro noticias salen 570. Al quitar la repetida, quedan 470. Pero tampoco podemos afirmar que sean 470 empresas distintas: algunas podrían aparecer en varios casos. Con estos datos no sabemos cuántas fueron afectadas en total.

## El sueldo también abre una puerta

Conviene mirar con cuidado el dinero. Los tres millones de daños recogidos en el anuncio de Wang de 2025 no eran sus ingresos. Incluían costes y pérdidas para los empleadores. La comunicación de 2026 mencionaba más de cinco millones de ingresos. No es una hucha que haya crecido de tres a cinco millones: estamos mirando dos cuentas distintas.

**Lo más inquietante de estas historias es su normalidad aparente**. Una entrevista, un envío, unas tareas y una nómina pueden formar parte del engaño. La puerta de entrada tiene el aspecto de un empleo corriente.

Estos expedientes no permiten sospechar de cualquier compañero remoto, pero sí muestran una **grieta** concreta: **saber dónde está un ordenador no equivale a saber quién lo utiliza**. A veces, el portátil llega a la dirección correcta. Sin embargo, la confianza se entrega a la persona equivocada.

Puedes revisar y reproducir el [notebook de Jupyter](/nebula/analisis/norcoreanos_eda.ipynb), con la [tabla de cifras](/nebula/analisis/cifras_documentales.csv) y el [registro de fuentes](/nebula/analisis/fuentes.csv). Para ejecutarlo, descarga los tres archivos en la misma carpeta.

Fuentes: Departamento de Justicia de Estados Unidos, [caso Chapman, mayo de 2024](https://www.justice.gov/archives/opa/pr/charges-and-seizures-brought-fraud-scheme-aimed-denying-revenue-workers-associated-north), [acusaciones de junio de 2025](https://www.justice.gov/opa/pr/justice-department-announces-coordinated-nationwide-actions-combat-north-korean-remote), [sentencias del caso Wang, abril de 2026](https://www.justice.gov/opa/pr/two-us-nationals-sentenced-facilitating-fraudulent-remote-information-technology-worker) y [operación anunciada en octubre de 2026](https://www.justice.gov/opa/pr/justice-department-announces-coordinated-actions-combat-north-korean-remote-it-worker).
