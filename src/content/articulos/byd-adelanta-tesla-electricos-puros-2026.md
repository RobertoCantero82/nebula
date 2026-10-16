---
titulo: "Tesla ganó septiembre. BYD puede quedarse con todo el año"
descripcion: "BYD llega al último trimestre con 746 eléctricos de ventaja. Analizamos 6,8 millones de registros para calcular si Tesla todavía puede remontar."
tema: "TECNOLOGÍA"
fecha: 2026-10-15T09:00:00+02:00
imagenPortada: "/nebula/imagenes/byd_tesla_electricos_portada.png"
cifraDestacada: ">99%"
etiquetaCifra: "probabilidad estimada de que BYD termine 2026 por delante"
metodologia: "Predicción con los microdatos mensuales de matriculaciones de la DGT entre enero de 2023 y septiembre de 2026. Se filtran turismos nuevos con propulsión eléctrica y se comparan BYD y Tesla. La selección usa validación temporal en 2025 y una prueba separada en 2026. Como los modelos de regresión no superan la referencia estacional fuera de muestra, la previsión final repite el patrón de octubre a diciembre de 2025. La incertidumbre se estima con 50.000 remuestreos de los errores de prueba. No se anticipan cambios de precios, ayudas, oferta o logística."
---

*Septiembre pareció el mes de la remontada. Tesla matriculó 3.737 eléctricos puros en España, frente a 2.290 de BYD. El Model 3 fue incluso el turismo más vendido del país. Pero al levantar la vista del último mes aparece otra carrera: BYD llega a octubre con 14.227 unidades y Tesla con 13.481. La marca china conserva 746 coches de ventaja.*

La pregunta ya no es si BYD puede ponerse delante. Lo ha hecho. La pregunta es si resistirá los tres meses que faltan o si los habituales acelerones trimestrales de Tesla volverán a cambiar el orden.

He revisado 6,8 millones de registros mensuales de la [DGT](https://www.dgt.es/menusecundario/dgt-en-cifras/dgt-en-cifras-resultados/dgt-en-cifras-detalle/Microdatos-de-Matriculaciones-de-Vehiculos-mensual/), desde enero de 2023 hasta septiembre de 2026. Solo cuento turismos nuevos eléctricos de batería. Los híbridos enchufables quedan fuera, aunque compartan etiqueta cero.

La comprobación externa encaja casi al milímetro. [Ideauto situó a BYD en 14.233 eléctricos y a Tesla en 13.466](https://cincodias.elpais.com/companias/2026-10-07/china-se-come-el-mercado-espanol-de-coches-electrificados-concentra-el-38-de-las-ventas-hasta-septiembre.html). La pequeña diferencia procede de trabajar con cierres y fuentes distintas, pero no altera quién va primero.

## Una carrera a tirones

Tesla no vende siguiendo una línea tranquila. Acumula muchas entregas al final de cada trimestre. En 2026 pasó de 131 matriculaciones en julio y 304 en agosto a 3.737 en septiembre. [La propia información de mercado advierte de ese patrón](https://www.europapress.es/motor/sector-00644/noticia-tesla-model-domina-mercado-electrico-espana-septiembre-ser-lider-absoluto-mes-20261001143332.html).

BYD avanza de otra forma: superó las 1.500 unidades en seis de los nueve meses del año y reunió una gama más repartida. Tesla sigue teniendo los dos modelos eléctricos más vendidos, Model 3 y Model Y, pero BYD suma más como marca. Es la diferencia entre ganar varias etapas y encabezar la general.

<div class="grafico-interactivo">
  <canvas id="grafico-byd-tesla-mensual" height="310" role="img" aria-label="Matriculaciones mensuales de BYD y Tesla entre enero de 2025 y septiembre de 2026. Tesla muestra picos al cierre de trimestre y BYD una trayectoria más estable."></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-byd-tesla-mensual');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['ene 25','feb 25','mar 25','abr 25','may 25','jun 25','jul 25','ago 25','sep 25','oct 25','nov 25','dic 25','ene 26','feb 26','mar 26','abr 26','may 26','jun 26','jul 26','ago 26','sep 26'],
        datasets: [
          { label: 'BYD', data: [801,576,766,640,1019,1479,1419,1280,1760,1978,1991,2143,1039,1157,1673,1568,1648,1971,1524,1357,2290], borderColor: '#446ddf', backgroundColor: '#446ddf', tension: .25 },
          { label: 'Tesla', data: [269,919,1980,573,795,2635,702,1439,2995,393,1524,1797,458,1596,2479,301,1691,2784,131,304,3737], borderColor: '#d85a30', backgroundColor: '#d85a30', tension: .25 }
        ]
      },
      options: {
        responsive: true,
        plugins: { title: { display: true, text: 'Dos maneras muy distintas de vender eléctricos' } },
        scales: { y: { beginAtZero: true, title: { display: true, text: 'Turismos nuevos' } } }
      }
    });
  });
</script>

*Matriculaciones de turismos nuevos con propulsión eléctrica. Fuente: microdatos mensuales de la DGT.*

## Un modelo sencillo gana por ser menos malo

Probé cinco métodos. El más básico repite para cada marca lo ocurrido en el mismo mes del año anterior. Los demás intentan aprender la tendencia, el crecimiento reciente y los ciclos anual y trimestral.

Separé el tiempo como se debe: 2025 sirvió para elegir candidato y los nueve primeros meses de 2026 quedaron como examen. Los modelos más elaborados parecían mejores durante la validación, pero fallaron al llegar a datos nuevos. En BYD, el error medio mensual del candidato fue de 696 coches; la referencia se quedó en 499. En Tesla, fueron 589 frente a 570.

Así que no premio la complejidad. La predicción final conserva la referencia estacional. Es como pronosticar el tiempo diciendo que mañana se parecerá a hoy: modesto, pero difícil de superar cuando hay poco historial y muchos saltos.

También hice una prueba de sensibilidad: ¿cambiaría el ganador si, pese al examen, utilizase cualquiera de las otras fórmulas? No. Los cinco métodos colocan a BYD por delante al terminar diciembre. Lo que cambia es el tamaño de la ventaja, desde unos 1.400 hasta 5.400 coches. Eso refuerza el orden previsto, pero también recuerda que dar una cifra con apariencia exacta sería vender más precisión de la que permiten los datos.

## Haz tu apuesta antes de ver el resultado

<div id="apuesta-byd-tesla" class="grafico-interactivo" style="text-align:center;padding:1.25rem">
  <p><strong>¿Quién terminará 2026 con más eléctricos puros matriculados?</strong></p>
  <button type="button" data-eleccion="BYD" style="margin:.3rem;padding:.65rem 1rem">BYD</button>
  <button type="button" data-eleccion="Tesla" style="margin:.3rem;padding:.65rem 1rem">Tesla</button>
  <p id="resultado-apuesta" aria-live="polite"></p>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const caja = document.getElementById('apuesta-byd-tesla');
    const salida = document.getElementById('resultado-apuesta');
    if (!caja || !salida) return;
    caja.querySelectorAll('button').forEach(boton => boton.addEventListener('click', () => {
      salida.innerHTML = `<strong>El modelo apuesta por BYD.</strong><br>Estima 20.339 matriculaciones frente a 17.195 de Tesla. Elegiste ${boton.dataset.eleccion}.`;
      caja.querySelectorAll('button').forEach(b => b.disabled = true);
    }));
  });
</script>

Octubre, noviembre y diciembre añadirían unas 6.112 unidades a BYD y 3.714 a Tesla. El cierre central queda en **20.339 frente a 17.195**, una ventaja de 3.144 coches para la marca china.

No me quedo con una única cuenta. He simulado 50.000 finales de año reutilizando los errores cometidos durante la prueba. En 49.988, BYD termina delante: **más del 99% de probabilidad**. En el 80% central de los escenarios, su ventaja se mueve entre unos 1.600 y 4.500 coches.

## La marca puede estar clara; la cifra, no

Una probabilidad alta no convierte diciembre en un trámite. El modelo no conoce futuras rebajas, problemas logísticos, cambios en las ayudas ni campañas de matriculación. Además, 45 meses son poco historial y BYD apenas empezaba a vender en España en 2023.

La conclusión razonable es más estrecha: con la ventaja ya acumulada y un último trimestre parecido al anterior, **BYD debería cerrar 2026 como la marca con más turismos eléctricos puros matriculados en España**. Tesla puede volver a ganar un mes. Para ganar el año necesitaría algo bastante mayor que uno de sus acelerones habituales.

Puedes revisar cada paso en el [notebook ejecutado](/nebula/analisis/byd-tesla-electricos/analisis_byd_tesla_electricos.ipynb), descargar la [serie mensual](/nebula/analisis/byd-tesla-electricos/matriculaciones_mensuales.csv) y consultar el [código de extracción](/nebula/analisis/byd-tesla-electricos/preparar_datos.py).

