# Voyager 1: un viaje, dos distancias

Categoría: EDA (análisis exploratorio de datos). Corte: 16 de noviembre de 2026 a las 00:00 UTC.

## Resultado

En las efemérides geométricas de NASA/JPL Horizons, la separación Tierra–Voyager 1 disminuye durante unos 93,5 días de 2026 (20 de enero–24 de abril). Se reduce 40,7 millones de kilómetros mientras la distancia al Sol aumenta 136,4 millones. La explicación se comprueba separando las contribuciones de velocidad de la Tierra y la sonda sobre la línea que las une.

## Reproducción

Python 3.10 o posterior; ejecución comprobada con Python 3.12. Solo biblioteca estándar: sin instalaciones ni acceso a internet para reproducir los archivos conservados.

1. Abre una terminal en esta carpeta.
2. Ejecuta: python ejecutar_notebook.py
3. Consulta analisis_voyager_acercamiento.ipynb, su versión HTML y resultados/resumen.json.

También puedes abrir el notebook en Jupyter y ejecutar todas las celdas, con esta carpeta como directorio de trabajo. Para consultar de nuevo la fuente, usa python descargar_datos.py; al actualizar Horizons sus soluciones podrían cambiar. Los cuatro JSON originales permiten reproducir esta versión concreta. analisis.py contiene los mismos cálculos, separados de la descarga.

## Datos y calidad

- 17.969 instantes diarios para cada referencia, del 06-09-1977 al 16-11-2026.
- 7.657 instantes horarios de 2026.
- Consulta independiente de la Tierra respecto al Sol para comprobar posiciones y velocidades.
- Sin filas duplicadas, fechas desalineadas, huecos diarios ni valores no finitos.
- Reconstrucción del movimiento relativo comprobada; diferencia con la derivada numérica inferior a 0,002 km/s.
- Diferencia entre límites diarios y horarios: unos 3,1 y 1,0 minutos.
- 36 años completos 1990–2025 con acercamiento, entre 93 y 94 muestreos diarios negativos por año.

## Limitaciones

Son efemérides calculadas, no mediciones diarias independientes. Horizons describe 1977–1980 como una reconstrucción aproximada por tramos; desde 1981 emplea un ajuste de 2022 sobre seguimiento de 1981–1992 prolongado mediante cálculo orbital. No publico una incertidumbre de distancia que la fuente no ofrece. Las fechas interpoladas y los segundos que aparecen en el JSON son precisión de cálculo, no exactitud física demostrada. Redondeo los resultados editoriales.

Uso distancias geométricas simultáneas entre centros de cuerpos, sin correcciones por tiempo de viaje de la luz. Distancia/c sirve como equivalencia aproximada, no como medida real del retardo de una comunicación. 2026 no es un año completo y se presenta separado de la comparación histórica. No produzco predicciones propias ni una fecha de fin de misión.

## Entrega para la web

El paquete contiene una carpeta nebula con el artículo en src/content/articulos, la portada en public/imagenes y las copias públicas reproducibles en public/analisis/voyager-acercamiento. Copia su contenido sobre tu carpeta local de la web. La carpeta _repos_nebula/voyager-acercamiento contiene el proyecto analítico. Ningún archivo se ha colocado en las carpetas finales porque esta sesión no tiene permiso de escritura en ellas.

El artículo tiene 713 palabras editoriales, sin contar metadatos, código, controles y fuentes. Incluye gráfico SVG generado mediante código, selector de fechas, tabla alternativa, foco visible y funcionamiento sin JavaScript. La portada es una ilustración editorial generada con IA; no representa escalas o posiciones reales.

La URL del post de LinkedIn corresponde a la ruta prevista tras tu publicación; todavía no se ha publicado esta entrega. NASA y NASA Jet Propulsion Laboratory tienen páginas verificadas en LinkedIn; los enlaces no crean etiquetas automáticas.

## Validación web

Compilación correcta en una copia aislada del sitio (69 páginas). Interacción comprobada en Chromium sin errores JavaScript, cambio de fecha por teclado, foco visible y sin desbordamiento horizontal en 320 y 390 píxeles. Los resultados de la comprobación se conservan en resultados/verificacion_web.json. No se modifica ni publica la web original.
