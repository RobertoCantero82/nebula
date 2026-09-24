---
imagenPortada: "/nebula/imagenes/iphone_duo_portada.png"
titulo: "¿Es el iPhone Duo un móvil o un iPad mini plegable?"
descripcion: "Una comparación de dimensiones, pantalla, peso y precio sitúa al iPhone Duo entre un teléfono plegable y la experiencia de un iPad mini."
tema: "TECNOLOGÍA"
fecha: 2026-09-19
cifraDestacada: "85,5%"
etiquetaCifra: "superficie de la pantalla del iPad mini que ofrece el iPhone Duo al abrirse"
metodologia: "Análisis de las especificaciones oficiales de Apple, Samsung y Google. La muestra incluye seis dispositivos y nueve pantallas. La superficie de cada panel se estimó a partir de su diagonal y la relación de aspecto derivada de la resolución. Los resultados describen los modelos seleccionados y no representan todo el mercado."
---

Un teléfono de 1.999 dólares que se abre hasta las 7,58 pulgadas invita a una comparación inevitable. ¿Es el **iPhone Duo** un móvil con una pantalla excepcionalmente grande o un intento de guardar un iPad mini en el bolsillo?

He comparado sus dimensiones, peso, pantalla y precio con los iPhone 18 Pro y Pro Max, el iPad mini y dos rivales plegables: el Samsung Galaxy Z Fold8 y el Google Pixel 11 Pro Fold. Los datos, a primera vista, ofrecen una respuesta curiosa. **Cerrado**, el Duo es un **teléfono extraño**. **Abierto**, no tiene el cuerpo de un iPad mini, pero sí gran parte de su **experiencia visual**.

## 1. Cerrado: menos móvil por delante, más móvil en el bolsillo

El iPhone Duo ocupa 99,1 cm² cuando está cerrado, un 15,8% menos que el promedio del iPhone 18 Pro y el Pro Max. Esa reducción, sin embargo, no consigue un teléfono más ligero ni más fino. La nueva creación de Apple pesa 254 gramos, un 10,4% más que los mencionados modelos de referencia, y sus 11,3 milímetros de grosor superan la media de los iPhone convencionales en un 29,1%.

Entonces, ¿cuál es la explicación? El iPhone Duo es un 24,8% más bajo que un iPhone Pro, pero un 12,2% más ancho. Su pantalla exterior también es un 18,2% menor. **No parece un móvil normal doblado por la mitad**: parece un objeto distinto, corto, ancho y grueso, pensado para cambiar de identidad al abrirse.

| Métrica | iPhone Duo | Media iPhone 18 Pro y Pro Max | Diferencia |
|---|---:|---:|---:|
| Peso | 254 g | 230 g | +10,4% |
| Altura | 117,8 mm | 156,7 mm | -24,8% |
| Anchura | 84,1 mm | 75,0 mm | +12,2% |
| Grosor | 11,3 mm | 8,8 mm | +29,1% |
| Superficie de pantalla | 86,5 cm² | 105,8 cm² | -18,2% |

La comparación con otros plegables tampoco le favorece. El Pixel 11 Pro Fold pesa 239 gramos y el Galaxy Z Fold8 baja hasta 201. Los dos son además más delgados cerrados. El Duo consigue ser compacto, pero no eficiente: es el plegable más pesado y grueso de los tres analizados.

## 2. Abierto: el 85,5% de un iPad mini

La pantalla interior cambia la comparación. Sus 174,4 cm² equivalen al **85,5% de la superficie del iPad mini**, pese a que el cuerpo abierto del Duo solo ocupa el 73,6% de la superficie física de la tableta. Apple consigue acercarse al área visual de un iPad mediante un mejor aprovechamiento del frontal: aproximadamente el 90% frente al 77,4% del mini.

La diagonal, por sí sola, oculta parte de la historia. El iPad mini mide 8,3 pulgadas y el Duo 7,58, pero la forma de la pantalla también importa. La relación entre el lado largo y el corto es de 1,52 en el iPad y de 1,42 en el Duo. Ambos se alejan mucho del formato alargado de los iPhone 18 Pro, cuya relación alcanza 2,17.

<div class="grafico-interactivo">
  <canvas id="grafico-superficie-duo" height="360"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-superficie-duo');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [
          'Pixel 11 Pro Fold · interior',
          'iPad mini',
          'Galaxy Z Fold8 · interior',
          'iPhone Duo · interior',
          'iPhone 18 Pro Max',
          'Pixel 11 Pro Fold · exterior',
          'iPhone 18 Pro',
          'Galaxy Z Fold8 · exterior',
          'iPhone Duo · exterior',
        ],
        datasets: [{
          label: 'Superficie aproximada (cm²)',
          data: [206.32, 203.92, 179.19, 174.43, 115.31, 103.66, 96.29, 88.19, 86.52],
          backgroundColor: [
            '#B8BEC9', '#446DDF', '#B8BEC9', '#8B3FF1', '#B8BEC9',
            '#B8BEC9', '#B8BEC9', '#B8BEC9', '#8B3FF1',
          ],
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          x: { beginAtZero: true, title: { display: true, text: 'Superficie aproximada (cm²)' } },
        },
      },
    });
  });
</script>

La densidad de píxeles devuelve parte de la identidad de teléfono. La pantalla interior alcanza 430,7 píxeles por pulgada, un 31,9% más que el iPad mini y también por encima de los plegables de Samsung y Google. El iPhone Duo ofrece una pantalla con forma de tablet y una nitidez de móvil de gama alta.

Pero no es un iPad mini partido en dos. Abierto, el excepcional dispositivo es un 39,7% más bajo, un 22,1% más ancho y un 26,4% menor en superficie física. Su pantalla también sigue siendo un 14,5% más pequeña. **Se parece al iPad Mini en la forma de mostrar contenido, pero no en la forma de ocupar una mesa**.

## 3. La pantalla se acerca; el precio, no

El iPhone Duo cuesta 11,46 dólares por cada centímetro cuadrado de pantalla interior. Sí, hablamos de una medida de evaluación imperfecta, pero es que un dispositivo también se paga por sus cámaras, procesador, materiales y software. Sin embargo, resulta útil para poner el tamaño en contexto.

Dentro de los plegables, el Galaxy Z Fold8 baja a 10,60 dólares por cm² y el Pixel 11 Pro Fold a 9,20. El iPhone Duo es, por tanto, el que más cobra por cada unidad de superficie y, al mismo tiempo, el que ofrece la pantalla interior más pequeña de los tres.

<div class="grafico-interactivo">
  <canvas id="grafico-precio-superficie" height="280"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-precio-superficie');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['iPhone 18 Pro', 'iPhone Duo', 'iPhone 18 Pro Max', 'Galaxy Z Fold8', 'Pixel 11 Pro Fold', 'iPad mini'],
        datasets: [{
          label: 'Dólares por cm² de pantalla principal',
          data: [12.45, 11.46, 11.27, 10.60, 9.20, 2.94],
          backgroundColor: ['#B8BEC9', '#8B3FF1', '#B8BEC9', '#B8BEC9', '#B8BEC9', '#446DDF'],
        }],
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true, title: { display: true, text: 'USD por cm²' } },
        },
      },
    });
  });
</script>

El contraste con el iPad mini es extremo: 2,94 dólares por cm². La tableta parte de 128 GB, frente a los 256 GB del resto, y carece del mecanismo de plegado y de las mismas funciones telefónicas. Aun así, el iPhone Duo cuesta casi cuatro veces más por la superficie visual disponible. **Lo que se paga no es una pantalla grande, sino la posibilidad de doblarla y llevarla encima**.

## Conclusión

El iPhone Duo sigue siendo, ante todo, un teléfono móvil. Tiene su conectividad habitual, se cierra para transportarse y pesa prácticamente lo mismo que un iPhone 18 Pro Max. Eso sí, no se comporta como un teléfono convencional: cerrado es más corto, ancho y grueso, y su pantalla exterior es más pequeña.

Al abrirse aparece la razón de esa incomodidad. El Duo entrega el 85,5% de la pantalla de un iPad mini, una proporción casi idéntica y una densidad muy superior, en un cuerpo más compacto y ligero. No convierte iOS en iPadOS ni sustituye automáticamente la experiencia de una tableta, pero sí invade su territorio visual.

La mejor definición quizá no esté en ninguno de los dos extremos. **El iPhone Duo no es un iPad mini plegable: es un móvil que acepta dejar de parecerlo cada vez que se abre**.

Fuentes: [Apple, especificaciones del iPhone Duo](https://www.apple.com/iphone-duo/specs/), [Apple, iPhone 18 Pro](https://www.apple.com/iphone-18-pro/specs/), [Apple, iPad mini](https://www.apple.com/ipad-mini/specs/), [Samsung, Galaxy Z Fold8](https://news.samsung.com/global/samsung-galaxy-z-fold8-ultra-fold8-and-flip8foldables-perfected-for-every-way-of-living) y [Google, Pixel 11 Pro Fold](https://store.google.com/gb/product/pixel_11_pro_fold_specs?hl=en-GB).
