---
imagenPortada: "/nebula/imagenes/planeta_fenix_portada.png"
titulo: "Una estrella murió. Sus restos pueden haber formado un planeta"
descripcion: "Niobio, ausencia de hierro y una señal que se repite cada 4,4 días sostienen una explicación nunca observada alrededor de una enana blanca."
tema: "CIENCIA"
fecha: 2026-10-09
cifraDestacada: "27 años"
etiquetaCifra: "estuvo archivada la pista química del posible planeta"
metodologia: "EDA de las abundancias de 24 elementos publicadas por Williams et al. para HS 0209+0832: nueve cantidades medidas y 15 límites superiores. Comparo las detecciones no sostenidas por levitación radiativa con las abundancias solares y contextualizo la búsqueda de niobio en otras 33 enanas blancas y la periodicidad medida por TESS. No reproceso los espectros ni la curva de luz, no reproduzco los modelos atmosféricos y no confirmo directamente la existencia del planeta."
---

*Nadie ha fotografiado el planeta que posiblemente gira alrededor de HS 0209+0832. Ni siquiera se ha observado un tránsito claro por delante de su estrella. La pista decisiva estaba en un espectro de 1999: decenas de marcas de niobio que no encajan con un planeta corriente.*

Una estrella parecida al Sol pasa la mayor parte de su vida transformando hidrógeno en helio. Cuando agota el combustible, se hincha, expulsa sus capas exteriores y deja al descubierto un núcleo pequeño y caliente. Ese resto recibe el nombre de **enana blanca**.

HS 0209+0832 es una de ellas. Tiene aproximadamente el 61 % de la masa del Sol, pero concentrada en un cuerpo apenas mayor que la Tierra. Se encuentra a unos 269 años luz y lleva alrededor de cinco millones de años enfriándose. En astronomía, eso la convierte en una enana blanca joven.

## La luz funciona como una huella dactilar

Un espectro separa la luz según su longitud de onda, como un arcoíris mucho más preciso. Cada elemento químico absorbe unas longitudes concretas y deja líneas oscuras en posiciones reconocibles. Si aparecen las líneas adecuadas, los astrónomos pueden saber que hay carbono, calcio o niobio sin recoger una muestra física.

El telescopio Hubble observó HS 0209+0832 en el año 1999. Su espectro contenía más de 200 líneas de metales y alrededor de un centenar seguía sin identificar. Veintisiete años después, mejores datos atómicos permitieron asignar buena parte de aquellas marcas al cobre y al niobio.

El [estudio publicado en *Nature Astronomy*](https://doi.org/10.1038/s41550-026-02983-7) identifica el niobio mediante **62 líneas espectrales**. No depende de una única raya dudosa: aparecen cinco líneas de Nb III y 57 de Nb IV. Los números romanos solo indican cuántos electrones ha perdido el átomo.

## El niobio rompe el patrón

En el EDA que da lugar a este artículo, analizo 24 elementos buscados en la atmósfera de la estrella. Nueve tienen una cantidad medida. En los otros 15 solo existe un **límite superior**: si están presentes, su abundancia debe quedar por debajo de ese máximo porque el instrumento no logró distinguirlos.

La comparación siguiente incluye seis elementos detectados que no pueden mantenerse suspendidos por el empuje de la radiación. Su presencia implica que está llegando material desde el exterior.

<div class="grafico-interactivo">
  <canvas id="grafico-planeta-fenix-abundancias" height="340" role="img" aria-label="El niobio presenta una diferencia de 4,25 unidades logarítmicas frente a la abundancia solar, muy por encima del cobre, el zinc, el calcio, el titanio y el níquel."></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    // localizo el lienzo y detengo el bloque si chart.js no está disponible
    const ctx = document.getElementById('grafico-planeta-fenix-abundancias');
    if (!ctx || !window.Chart) return;

    // traduzco las diferencias logarítmicas a factores para explicarlas en el tooltip
    const factores = [0.28, 7.24, 11.22, 14.13, 21.38, 17782.79];

    // represento una sola idea: la distancia excepcional del niobio frente al patrón solar
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Níquel', 'Titanio', 'Calcio', 'Zinc', 'Cobre', 'Niobio'],
        datasets: [{
          label: 'Diferencia frente al Sol',
          data: [-0.55, 0.86, 1.05, 1.15, 1.33, 4.25],
          backgroundColor: ['#7257D5', '#7257D5', '#7257D5', '#7257D5', '#7257D5', '#E45756'],
          borderRadius: 3,
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => {
                const factor = factores[context.dataIndex];
                const texto = factor < 1
                  ? `${factor.toLocaleString('es-ES')} veces la referencia solar`
                  : `${Math.round(factor).toLocaleString('es-ES')} veces la referencia solar`;
                return `${context.parsed.x.toLocaleString('es-ES')} unidades: ${texto}`;
              },
            },
          },
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Diferencia logarítmica (1 unidad equivale a multiplicar por 10)',
            },
          },
          y: { grid: { display: false } },
        },
      },
    });
  });
</script>

*Comparación de las abundancias atmosféricas relativas al hidrógeno. No representa una medida directa de la composición del planeta.*

En la atmósfera de HS 0209+0832, el niobio aparece unas **17.800 veces por encima de la referencia solar**. La cifra necesita cautela: cada elemento se hunde a una velocidad diferente dentro de la estrella. Aun así, la separación es enorme.

Los autores revisaron además 33 enanas blancas calientes enriquecidas con metales. **No confirmaron niobio en ninguna**. Eso no significa que la probabilidad de encontrarlo sea una entre 34: la muestra no representa a todas las enanas blancas del universo. Sí demuestra que este sistema es único dentro de la comparación examinada.

## Lo que falta también aporta información

Los planetas rocosos conocidos contienen abundante hierro y silicio. Aquí ocurre algo extraño: apenas aparece silicio, no se detecta hierro y, sin embargo, sí hay níquel. El límite del hierro permite calcular que existen al menos **2,09 átomos de níquel por cada átomo de hierro**. En el Sol hay aproximadamente 0,06.

El niobio ofrece la pista sobre el origen. Es uno de los elementos que pueden producirse dentro de una estrella envejecida mediante capturas lentas de neutrones. Si parte del material expulsado al morir formó un disco, de ese disco pudo surgir un planeta nuevo. No sería un superviviente del sistema original, sino un **planeta de segunda generación construido con las cenizas de su propia estrella**.

## Una segunda pista que se repite cada 4,4 días

El satélite TESS aporta otra pieza. El brillo de HS 0209+0832 varía cada **4,399 ± 0,026 días**, con una amplitud de solo **0,120 ± 0,018%**. Si el brillo normal fueran 1.000 unidades, el cambio sería de aproximadamente 1,2.

La periodicidad encaja con un objeto cercano, posiblemente un planeta gigante cuya atmósfera se evapora y cae sobre la enana blanca. Sin embargo, también podría proceder de una cola de gas o de algún fenómeno de la propia estrella. TESS no observó un tránsito que cierre la discusión.

## Es un candidato, no un planeta confirmado

La explicación de segunda generación conecta la química inusual, el material que cae sobre la estrella y la variación periódica. Pero quedan piezas incómodas. El estroncio, que los modelos relacionan con el niobio, no fue detectado. Tampoco puede saberse si el planeta nació entero después de la muerte estelar o si un núcleo antiguo sobrevivió y adquirió una envoltura nueva.

Por eso el titular más preciso no es que una estrella muerta haya dado a luz un planeta. Los datos permiten afirmar algo más prudente: **HS 0209+0832 reúne una combinación excepcional de pistas compatible con el primer candidato a planeta de segunda generación alrededor de una enana blanca**.

Puedes revisar las abundancias, reproducir los gráficos y seguir cada decisión en el [notebook de Jupyter del planeta Fénix](/nebula/analisis/planeta-fenix/notebooks/01_planeta_fenix_eda.ipynb). Los [datos procesados](/nebula/analisis/planeta-fenix/data/processed/abundancias_hs0209.csv) también están disponibles.

Fuentes: [estudio en *Nature Astronomy*](https://doi.org/10.1038/s41550-026-02983-7), [prepublicación en arXiv](https://arxiv.org/abs/2610.07161), [comunicado de ESA/Hubble](https://esahubble.org/news/heic2613/) y [artículo de partida en Xataka](https://www.xataka.com/espacio/estrella-muerta-ha-dado-a-luz-planeta-puede-que-sol-haga-futuro).
