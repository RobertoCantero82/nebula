# Voyager: una conversación de casi dos días

**Categoría: EDA. Corte: 22 de octubre de 2026, 00:00 UTC.**

Comparo seis destinos, una serie de Voyager 1 cada 30 días desde 1977 y series diarias de 2026 desde el centro de la Tierra y del Sol. Trabajo con efemérides calculadas por JPL, no registros observados de comunicaciones. El hito futuro del 18 de noviembre procede de NASA; no hago una predicción propia.

## Reproducir

Instalo `requirements.txt`, abro `analisis_voyager.ipynb` desde esta carpeta y ejecuto todas las celdas. Los CSV y `fuentes/` permiten repetir el análisis sin conexión. `fuentes.json` conserva consultas, fechas de descarga y SHA-256 de cada respuesta. `descargar.py` permite renovar la extracción en Windows con conexión; no reemplaza copias ya descargadas. Para obtener otra versión, uso una carpeta nueva y conservo la anterior. `ejecutar.py` automatiza la ejecución si dispongo de un kernel Python y las dependencias.

## Archivos

- `comparacion.csv`: seis destinos en un mismo corte.
- `historia.csv`: extracción histórica cada 30 días.
- `diario_2026.csv`, `diario_sol_2026.csv`: distancias diarias con dos centros distintos.
- `comparacion_limpia.csv`, `resultados.json`, `datos_web.json`: resultados reproducibles.
- `fuentes/`, `fuentes.json`: respuestas originales y trazabilidad.

## Limitaciones

Excluyo filas posteriores al corte aunque la API incluya el extremo solicitado del 23 de octubre. Uso vectores geométricos sin corrección por movimiento durante el vuelo de la señal. La ida y vuelta es el doble de distancia/c, una aproximación explicativa; no incluye ejecución de órdenes, planificación de antenas ni incidencias. No atribuyo las distancias de los centros planetarios a vehículos concretos. Los 93 intervalos de descenso son comparaciones entre medianoches, no una determinación subdiaria de los extremos. No presupongo comunicación disponible con todos los destinos. El muestreo de 30 días no resuelve oscilaciones diarias.
