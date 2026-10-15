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

## Publicaciones de Nebula en LinkedIn

- Los posts serán siempre cortos y dejarán al lector con ganas de abrir el artículo. No resumirán toda la historia ni revelarán por completo su giro principal.
- El gancho utilizará un *clickbait* moderado y honesto: debe crear tensión, sorpresa o una incógnita concreta, pero el artículo cumplirá exactamente la promesa sin engaños ni exageraciones.
- No basta con formular una pregunta neutra. El texto debe sugerir que existe un resultado inesperado, una contradicción o un detalle capaz de cambiar la interpretación.
- El inicio debe entenderse sin haber leído el artículo ni conocer previamente el tema. Cualquier récord, cifra o conflicto mencionado tendrá contexto suficiente desde la primera frase.
- Está prohibido utilizar emojis.
- La estructura preferida es: gancho claro, tensión o pregunta breve y enlace al artículo.
- Todos los posts incluirán hashtags relacionados con la búsqueda de empleo, el oficio periodístico, la redacción y la ciencia de datos. Como base: `#OpenToWork`, `#BuscandoTrabajo`, `#Periodista`, `#Redactor` y `#CienciaDeDatos`.
- Se añadirán también hashtags del asunto concreto tratado, como ciencia, tecnología, aves, inteligencia artificial o baloncesto, sin convertir el cierre en una lista excesiva.

## Lenguaje obligatorio de los artículos

- Todos los artículos de Nebula se escriben siempre en lenguaje coloquial, sencillo y fácil de entender, manteniendo el tono y el rigor periodísticos.
- El texto debe resultar entretenido y ágil. Cuenta una historia; no convierte las decisiones del análisis en un informe técnico.
- Los conceptos difíciles se explican dentro del relato con palabras cotidianas y ejemplos claros, sin presuponer conocimientos especializados.
- Se evitan tecnicismos, abstracciones y formulaciones enrevesadas cuando existe una forma corriente de decir lo mismo. Simplificar el lenguaje no significa perder precisión.
- Esta norma se aplica también al titular, la descripción, la cifra destacada, su etiqueta y los textos de gráficos e interacciones.
- La extensión habitual es de 700 a 800 palabras de texto editorial, salvo indicación expresa distinta.