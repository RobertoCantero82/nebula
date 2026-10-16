# BYD frente a Tesla en eléctricos puros

Predicción del líder de matriculaciones de turismos eléctricos de batería en España al cierre de 2026. El análisis usa los microdatos mensuales de la DGT desde enero de 2023 hasta septiembre de 2026.

## Reproducción

1. Crear un entorno e instalar `requirements.txt`.
2. Descargar los ZIP mensuales de la DGT en `data/raw`.
3. Ejecutar `python preparar_datos.py data/raw data/processed`.
4. Ejecutar el notebook `analisis_byd_tesla_electricos.ipynb`.

El repositorio público incluye la serie procesada para evitar una descarga de varios cientos de megabytes. Los registros individuales filtrados se conservan en el análisis privado para auditoría.

Fuentes: [microdatos mensuales DGT](https://www.dgt.es/menusecundario/dgt-en-cifras/dgt-en-cifras-resultados/dgt-en-cifras-detalle/Microdatos-de-Matriculaciones-de-Vehiculos-mensual/) y [diseño de registro](https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/dgt-en-cifras/matraba/MATRICULACIONES_MATRABA.pdf).
