# Mapas de inundación de Valencia

EDA sobre las viviendas situadas dentro de la huella observada de la DANA del 29 de octubre de 2024 y su presencia en las zonas oficiales de riesgo.

## Reproducción

1. Sitúa `municipios.csv` y `resumen_fuente.json` dentro de `datos/`.
2. Ejecuta `python crear_notebook.py` desde esta carpeta.
3. El script crea `analisis_mapas_inundacion_valencia.ipynb` y ejecuta sus celdas en orden.

El notebook utiliza únicamente la biblioteca estándar de Python.

## Procedencia

Los agregados proceden del estudio S19 de EasyxLab, publicado bajo CC BY 4.0. Ese estudio construyó las cifras a partir de Copernicus EMSR773, Catastro INSPIRE, SNCZI, PATRICOVA y límites municipales del IGN. Este proyecto conserva los datos agregados, no geometrías de edificios ni referencias catastrales.

La aportación de este EDA es analizar la desigualdad municipal y la concentración del desfase. No vuelve a atribuirse el cálculo geoespacial original.

## Limitación principal

La cartografía estatal leída por la fuente figura actualizada el 20 de diciembre de 2024. La versión vigente el día de la DANA no pudo recuperarse. La revisión del PATRICOVA anunciada en octubre de 2026 tampoco estaba disponible como capa descargable durante este trabajo.
