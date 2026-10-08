## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)

## Criterio editorial de Nebula

- Todo artículo de datos de Nebula debe pertenecer a una de estas dos categorías: **EDA (análisis exploratorio de datos)** o **machine learning**. No existe una categoría intermedia.
- Un EDA describe, compara y contextualiza datos existentes. Puede analizar previsiones publicadas por terceros, pero no debe presentar una predicción propia.
- Un artículo de machine learning necesita un modelo reproducible, una referencia sencilla o *baseline*, separación entre entrenamiento y prueba y métricas de evaluación. Si los datos no permiten validar el modelo, el trabajo se convierte en EDA.
- El texto debe rondar las 700 palabras, salvo que el encargo indique otra extensión, y usar lenguaje sencillo: frases cortas, tecnicismos explicados y una idea principal fácil de identificar.
- Hay que separar con claridad hechos observados, previsiones de terceros y afirmaciones de empresas. Las limitaciones del análisis deben quedar visibles.
- Si el análisis parte de un cuaderno, el artículo debe enlazarlo desde `/nebula/analisis/`. El cuaderno y los datos locales necesarios para reproducirlo deben copiarse a `public/analisis/`.
- Cada artículo tendrá una portada original en `public/imagenes/`, coherente con las portadas habituales de Nebula y sin texto, logotipos ni marcas de agua. Se declarará mediante `imagenPortada`.
- Antes de entregar, ejecutar la compilación del sitio y comprobar que el artículo, la portada y los enlaces locales están incluidos.
