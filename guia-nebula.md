# Guía rápida: publicar un artículo en Nebula

Esta es tu chuleta para crear artículos nuevos sin necesitar ayuda cada vez. Guárdala a mano.

---

## 1. Estructura básica de un artículo

Todo artículo vive en `src/content/articulos/` como un archivo `.md`. El nombre del archivo (sin `.md`) es la URL final.

Ejemplo: `src/content/articulos/mi-articulo-nuevo.md` → se publica en `/nebula/articulos/mi-articulo-nuevo`

Todo artículo empieza con este bloque de frontmatter (entre las dos líneas de `---`):

```markdown
---
titulo: "Tu titular aquí"
tema: "CINE"
fecha: 2026-09-20
cifraDestacada: "73%"
etiquetaCifra: "descripción corta de qué es esa cifra"
metodologia: "Explicación de tus fuentes y proceso, en una sola línea de texto entre comillas."
---
```

Campos:
- `titulo` — obligatorio
- `tema` — obligatorio, la etiqueta que aparece arriba (CINE, NBA, etc.)
- `fecha` — obligatorio, formato `AAAA-MM-DD` sin comillas
- `cifraDestacada` y `etiquetaCifra` — opcionales, la caja de cifra destacada. Si no quieres cifra destacada, simplemente no pongas estas dos líneas
- `metodologia` — opcional, todo en una línea entre comillas. Si no la pones, el desplegable de metodología no aparece

Después del segundo `---`, escribes el cuerpo en Markdown normal: `**negrita**`, párrafos separados por línea en blanco, etc.

---

## 2. Añadir una tabla

Markdown normal, se ve automáticamente con el estilo de Nebula (ya está en el CSS):

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|---|---|---|
| dato | dato | dato |
| dato | dato | dato |
```

---

## 3. Añadir un gráfico interactivo (Chart.js)

Copia y pega este bloque donde quieras que aparezca el gráfico, y cambia los datos:

```html
<div class="grafico-interactivo">
  <canvas id="grafico-NOMBRE-UNICO" height="280"></canvas>
</div>

<script>
  window.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('grafico-NOMBRE-UNICO');
    if (!ctx || !window.Chart) return;
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Etiqueta 1', 'Etiqueta 2', 'Etiqueta 3'],
        datasets: [
          {
            label: 'Serie 1',
            data: [10, 20, 30],
            backgroundColor: '#8B85C4',
          },
        ],
      },
      options: {
        responsive: true,
        plugins: { legend: { position: 'bottom' } },
      },
    });
  });
</script>
```

Importante: `NOMBRE-UNICO` tiene que ser distinto en cada gráfico que pongas dentro del mismo artículo (por ejemplo `grafico-presupuestos`, `grafico-vfx`), si no, solo se pintará el último.

Tipos de gráfico disponibles cambiando `type`: `'bar'` (barras), `'line'` (líneas), `'pie'` (tarta), `'scatter'` (dispersión). Para dos ejes Y (como hicimos en el artículo de Matrix), añade `yAxisID: 'y'` y `yAxisID: 'y1'` a cada dataset y define ambos ejes en `scales`.

---

## 4. Añadir una imagen propia

1. Guarda la imagen (jpg, png o svg) dentro de `public/imagenes/`. Créala si no existe:

```cmd
mkdir public\imagenes
```

2. Copia tu archivo ahí, por ejemplo `public/imagenes/grafico-presupuestos.png`.

3. En el Markdown del artículo, referencia la ruta empezando por `/nebula/`:

```markdown
![Descripción de la imagen](/nebula/imagenes/grafico-presupuestos.png)
```

El `/nebula/` es obligatorio porque el sitio vive bajo esa ruta base (recuérdalo también si algún día cambias el `base` en `astro.config.mjs`).

---

## 5. Publicar el artículo

Una vez guardado el `.md`:

```cmd
git add src/content/articulos/tu-articulo.md
git commit -m "Publico artículo: [título corto]"
git push
```

Si también añadiste imágenes nuevas en `public/imagenes/`, súbelas en el mismo commit:

```cmd
git add src/content/articulos/tu-articulo.md public/imagenes/
git commit -m "Publico artículo: [título corto]"
git push
```

Ve a la pestaña **Actions** de tu repositorio en GitHub y espera el check verde (1-3 minutos). El artículo aparecerá en `https://robertocantero82.github.io/nebula/articulos/tu-articulo`.

---

## 6. Verlo en local antes de publicar

Antes de subir nada, siempre puedes comprobarlo en tu máquina:

```cmd
npm run dev
```

Y visita `localhost:4321/nebula/articulos/tu-articulo` (no olvides el `/nebula/` en la ruta).

---

## 7. Errores típicos

- **La página sale en blanco o da error al abrirla**: revisa que el frontmatter tenga exactamente dos líneas `---` (una al principio, otra al final) y que `fecha` no lleve comillas.
- **El gráfico no aparece**: el `id` del `<canvas>` no coincide con el `id` que usas en `getElementById()`, o hay dos gráficos con el mismo `id` en el mismo artículo.
- **Cambié el CSS/código y no se ve el cambio**: para el servidor, borra la carpeta `.astro` (`rmdir /s /q .astro`), relanza `npm run dev`, y haz `Ctrl+Shift+R` en el navegador.
- **El artículo aparece en el listado pero al abrirlo da 404**: comprueba que el archivo está en `src/content/articulos/`, no en `src/pages/articulos/` (son carpetas distintas y fáciles de confundir).

---

## 8. Añadirlo a la portada

Para que aparezca en "Artículos recientes" de la home, edita `src/pages/index.astro` y añade una tarjeta más dentro de `<div class="grid-articulos">`, copiando el bloque `<a href="/articulos/...">...</a>` que ya existe y cambiando el enlace, la etiqueta de tema y el título.
