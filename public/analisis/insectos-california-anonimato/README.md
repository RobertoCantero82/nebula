# Insectos de California: índice de anonimato

**Categoría: EDA (análisis exploratorio de datos).**

Este proyecto presenta el **índice de anonimato de Nebula**, una medida creada para calcular qué porcentaje de los grupos genéticos detectados por la California Insect Barcoding Initiative no tiene una identificación de especie en la tabla publicada.

## Resultado principal

- 892.274 ejemplares con BIN.
- 42.305 BIN distintos.
- 39.488 BIN sin identificación de especie.
- Índice de anonimato: 93,3 sobre 100.

Un BIN sin nombre no equivale necesariamente a una especie nueva. El indicador mide un vacío de identificación dentro del conjunto de datos.

## Fuentes

- Estudio: https://doi.org/10.1002/ecog.08572
- Datos originales: https://doi.org/10.5061/dryad.qrfj6q5zs
- Código de los autores: https://github.com/Austin-Baker/CIBI-biodiversity

## Reproducción

1. Descargar `SupplementalTable3.csv` desde Dryad.
2. Guardarlo en `data/raw`.
3. Ejecutar `procesar_insectos_anonimato.py`.
4. Abrir y ejecutar `insectos_california_indice_anonimato_eda.ipynb`.

Los archivos de `data/raw` no se modifican. Los resultados agregados se guardan en `data/processed`.

