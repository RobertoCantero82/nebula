# Reencarnación: EDA de relatos y sus intervalos

**Categoría: EDA. No genera predicciones.**

Pregunta: ¿qué oculta la diferencia entre medianas sobre el solapamiento de los intervalos y la disponibilidad de los datos?

Instalar `python -m pip install -r requirements.txt`. Abrir `reencarnacion_eda.ipynb` en Jupyter desde esta carpeta y ejecutar todas las celdas. Los datos son locales; no hace falta conexión. El cuaderno guarda `resultados.json`, `resumen_grados.csv` y `comprobaciones.csv`.

Fuente: https://zenodo.org/records/22677480 (v1, 9 septiembre 2026; descarga 27 octubre 2026). Estudio: https://doi.org/10.1037/cns0000493 . Conservo datos anónimos, diccionario, README original y código R de sus autores, con atribución. El archivo público no permite identificar personas ni comprobar sus relatos. No incorpora países ni fechas de recogida; no es una muestra representativa ni un experimento.

Resultados: 2254 filas; 1678 casos con fallecido identificado; 1319 con intervalo; 1075 con ambas variables. Medianas extremas: 21 y 12 meses, n=114 y n=708. La mitad central se solapa (11,25–70,5 frente a 5,75–38). No interpreto una identificación como reencarnación verificada. La revisión no reproduce todos los modelos del estudio ni evalúa su hipótesis metafísica.

No modifico los originales. El MD5 del CSV se verifica dentro del cuaderno contra el publicado en Zenodo. Los vacíos permanecen vacíos y los intervalos negativos se conservan, con una comprobación adicional que los excluye.
