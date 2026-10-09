# Planeta Fénix

**Categoría Nebula: EDA (análisis exploratorio de datos).**

Este proyecto reconstruye, paso a paso y sin exigir conocimientos previos de
astronomía, por qué HS 0209+0832 se considera candidata a albergar un planeta
de segunda generación: un mundo formado con material expulsado durante la muerte
de su estrella.

## Pregunta

**¿Cómo pueden los astrónomos proponer la existencia de un planeta que nadie ha
visto directamente?**

El EDA estudia las tres capas de evidencia publicadas por Williams et al. (2026):

1. Una composición química extraordinaria, con una señal especialmente fuerte
   de niobio.
2. La ausencia de niobio en una muestra de comparación de 33 enanas blancas
   enriquecidas con metales.
3. Una variación periódica y muy pequeña en el brillo medido por TESS.

Este proyecto **no entrena un modelo ni produce una predicción propia**. Ordena,
compara y explica observaciones y resultados publicados por el equipo científico.

## Archivos

- `notebooks/01_planeta_fenix_eda.ipynb`: análisis guiado principal.
- `data/processed/abundancias_hs0209.csv`: tabla de abundancias de la estrella,
  transcrita de la tabla de datos extendidos del estudio.
- `data/processed/evidencias_clave.csv`: magnitudes publicadas necesarias para
  contextualizar el caso.
- `work/paper_source/`: fuente de arXiv empleada para verificar tablas y texto.

## Fuentes primarias

- Williams, J. T. et al. (2026), *Discovery of a second-generation planet
  candidate accreting onto a white dwarf*, Nature Astronomy.
  https://doi.org/10.1038/s41550-026-02983-7
- Prepublicación y materiales fuente:
  https://arxiv.org/abs/2610.07161

Los datos observacionales originales proceden de archivos públicos de Hubble,
FUSE, VLT, Gaia, Pan-STARRS, Spitzer y TESS. Esta primera versión trabaja con las
medidas ya publicadas en el artículo, no con una reducción nueva de los espectros.

## Reproducibilidad

1. Crear un entorno de Python.
2. Instalar `requirements.txt`.
3. Abrir y ejecutar el notebook de principio a fin.

El notebook guarda sus gráficos finales en `outputs/figures/`.

