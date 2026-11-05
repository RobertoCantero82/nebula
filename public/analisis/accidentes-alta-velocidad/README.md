# ¿Más de la mitad? Accidentes mortales de alta velocidad

**Categoría: EDA (análisis exploratorio de datos).**

Este proyecto comprueba cuánto cambia el peso de España en las muertes asociadas a accidentes de alta velocidad cuando cambia la definición del universo analizado.

## Pregunta

¿España concentra más de la mitad de los fallecidos en accidentes de alta velocidad del mundo?

## Datos y alcance

La tabla de partida reúne los 15 accidentes mortales publicados por Verificat en su visualización del 4 de noviembre de 2026. Cada fila representa un accidente y conserva el enlace empleado para su balance de fallecidos.

No existe un registro mundial único de accidentes de alta velocidad. Por eso el notebook no presenta la tabla como un censo definitivo: reproduce cuatro criterios publicados o reconocibles y muestra cuánto cambia la respuesta.

- **Criterio amplio:** tren de alta velocidad implicado, incluso en vía convencional o durante pruebas.
- **Desde 2000:** el criterio amplio limitado a accidentes fechados desde el año 2000.
- **Principales siniestros:** selección de nueve accidentes utilizada por *El País*.
- **Línea de alta velocidad en servicio comercial:** excluye Angrois, pruebas y sucesos en líneas convencionales.

La palabra «víctimas» puede incluir personas heridas. Este análisis cuenta exclusivamente fallecidos porque es la magnitud comparable publicada para todos los casos.

## Archivos

- `accidentes_alta_velocidad.csv`: tabla documentada y etiquetas de inclusión.
- `analisis_accidentes_alta_velocidad.ipynb`: notebook ejecutado.
- `resumen_escenarios.csv`: resultados reproducibles de los cuatro criterios.

## Reproducción

1. Instalar Python 3, pandas, matplotlib y Jupyter.
2. Abrir el notebook en esta misma carpeta.
3. Ejecutar todas las celdas en orden.

Comprobado el 5 de noviembre de 2026. Los balances de Adamuz y Urda pueden revisarse cuando concluyan las investigaciones oficiales.
