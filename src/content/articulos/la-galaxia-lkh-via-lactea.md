---
imagenPortada: "/nebula/imagenes/galaxia_lkh_portada.png"
titulo: "La galaxia desaparecida que ayudó a construir la Vía Láctea"
descripcion: "Antiguos grupos de estrellas ayudan a reconstruir cómo la Vía Láctea creció al absorber otra galaxia."
tema: "CIENCIA"
fecha: 2026-09-30
cifraDestacada: "11.800 millones"
etiquetaCifra: "de años desde la fusión de la Vía Láctea con la galaxia LKH"
metodologia: "Análisis descriptivo de una cronología de seis acontecimientos construida con las cifras publicadas por Massari et al. en Nature Astronomy y por NASA. Se comparan la fusión con LKH, Gaia-Sausage-Enceladus, Sagitario y la formación del Sistema Solar. El notebook contextualiza el hallazgo, pero no reproduce el modelo astrofísico ni el catálogo individual de los 39 cúmulos globulares estudiados."
---

*Hace 11.800 millones de años, una galaxia enana chocó con la joven Vía Láctea y desapareció dentro de ella. Nadie observó aquel encuentro, solo faltaría, pero 39 cúmulos globulares han conservado suficientes pistas para reconstruirlo. El hallazgo desplaza 1.800 millones de años hacia atrás la historia conocida de las grandes fusiones de nuestra galaxia.*

La Vía Láctea parece estable, pero se formó poco a poco al unirse con otras galaxias. Creció formando estrellas y absorbiendo galaxias menores. Algunas todavía dejan corrientes visibles, mientras que de otras solo quedan poblaciones estelares mezcladas con las propias.

La más antigua identificada ha recibido el nombre de **Low-energy-Kraken-Heracles** o, de manera simplificada, **LKH**. Según el [estudio publicado en *Nature Astronomy*](https://doi.org/10.1038/s41550-026-02931-5), tenía aproximadamente **500 millones de masas solares en estrellas** cuando se incorporó a la Vía Láctea.

## Arqueología, no fotografía

En esta ocasión, el telescopio Hubble no captó la colisión. **El equipo analizó 39 cúmulos globulares situados en los 20.000 años luz más internos de nuestra galaxia**. Estas agrupaciones contienen estrellas muy antiguas nacidas en condiciones semejantes, por lo que conservan información sobre su lugar de origen.

Los investigadores compararon la edad, la composición y el movimiento de los cúmulos usando datos de Gaia, el telescopio espacial de la Agencia Espacial Europea y que es capaz de medir la posición, la distancia y el movimiento de casi 2.000 millones de estrellas para crear el mapa más preciso de la Vía Láctea. Al ordenarlos aparecieron tres secuencias: una formada en la propia Vía Láctea, otra asociada a Gaia-Sausage-Enceladus y una tercera población intermedia.

Esa tercera secuencia constituye la **principal evidencia de LKH**. Sin embargo, esta es una reconstrucción estadística y química, no la imagen directa de una galaxia intacta. La diferencia importa, igual que en [el análisis de la ameba de fuego](/nebula/articulos/ameba-fuego-limites-calor/), donde reproducirse, moverse y resistir unos minutos describían límites distintos aunque el titular pudiera mezclarlos.

La combinación resulta poderosa porque ninguna variable basta por separado. Dos cúmulos pueden tener edades parecidas y, aún así, una composición química distinta. También pueden compartir metales, pero seguir órbitas incompatibles. Cuando edad, metalicidad y dinámica apuntan en la misma dirección, es posible reconocer una familia estelar incluso después de que la gravedad haya deshecho y mezclado su galaxia original.

<div class="grafico-interactivo">
  <canvas id="grafico-cronologia-lkh" height="300"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-cronologia-lkh');
    if (!ctx || !window.Chart) return;

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          'Fusión con LKH',
          'Gaia-Sausage-Enceladus',
          'Inicio de la fusión con Sagitario',
          'Formación del Sistema Solar',
        ],
        datasets: [{
          label: 'Miles de millones de años antes del presente',
          data: [11.8, 10, 6, 4.6],
          backgroundColor: ['#D97745', '#6E86A6', '#9BB7B2', '#D5B07A'],
          borderColor: ['#B95E34', '#536E91', '#789C96', '#B38C55'],
          borderWidth: 1,
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: (context) => `Hace ${context.parsed.x.toLocaleString('es-ES')} mil millones de años`,
            },
          },
        },
        scales: {
          x: {
            beginAtZero: true,
            max: 13,
            title: { display: true, text: 'Miles de millones de años antes del presente' },
          },
          y: { grid: { display: false } },
        },
      },
    });
  });
</script>

## Cuando el universo tenía el 14,5 % de su edad

La cronología ayuda a medir la escala. **LKH se fusionó con la Vía Láctea** cuando el universo tenía alrededor de 2.000 millones de años, apenas el **14,5 % de su edad actual**. Gaia-Sausage-Enceladus, una galaxia enana que chocó y se fusionó con la Vía Láctea hace unos 10.000 millones de años, llegó unos 1.800 millones de años después. El Sistema Solar todavía tardaría aproximadamente 7.200 millones de años en aparecer.

Como ocurre al [analizar la aceleración de los lanzamientos espaciales de China](/nebula/articulos/articulo_lanzamientos_china_2026/), el dato llamativo adquiere significado al colocarlo dentro de una serie. LKH no añade simplemente otro choque a una lista: demuestra que la incorporación de estrellas nacidas fuera, comenzó durante la infancia de la Vía Láctea.

## Una casa construida con materiales ajenos

El hallazgo también cambia la imagen de la galaxia primitiva. Algunos modelos atribuían sus primeras poblaciones a estrellas formadas localmente. LKH indica que una parte relevante llegó desde fuera y terminó concentrada en las regiones internas.

Queda margen para la incertidumbre. La fecha y la masa dependen de modelos de evolución química y dinámica. El propio nombre LKH reúne varias hipótesis anteriores que el nuevo trabajo interpreta como rastros del mismo episodio. **Tampoco debemos imaginar un choque instantáneo**: una fusión galáctica transforma órbitas y distribuye material durante periodos enormes.

La galaxia enana desapareció, pero no borró su procedencia. Sus cúmulos funcionan como fósiles capaces de sobrevivir al objeto que los creó. **La Vía Láctea contiene su propia arqueología**: para conocer su origen no siempre hay que mirar más lejos, sino aprender a separar las poblaciones que ya viven dentro de ella.

Puedes **consultar la cronología, reproducir los gráficos y revisar los cálculos** en el [notebook de Jupyter del análisis de LKH](/nebula/analisis/analisis-fusion-galaxia-lkh.ipynb).

Fuentes: [artículo científico en *Nature Astronomy*](https://doi.org/10.1038/s41550-026-02931-5), [resumen de NASA Hubble](https://science.nasa.gov/missions/hubble/hubble-solves-merger-mystery-from-milky-ways-early-years/) y [artículo de partida en *Muy Interesante*](https://muyinteresante.okdiario.com/ciencia/fusion-galactica-via-lactea-lkh.html).

