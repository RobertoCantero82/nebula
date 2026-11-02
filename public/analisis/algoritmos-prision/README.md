# Algoritmos en prisión: el 30 % que no puede comprobarse

**Categoría: EDA (análisis exploratorio de datos).**

Este proyecto comprueba qué información respalda el anuncio de Michigan sobre un nuevo sistema de clasificación penitenciaria y utiliza la base pública de COMPAS como ejemplo didáctico para mostrar por qué la precisión global no describe por sí sola el coste de los errores.

## Pregunta

¿Basta una mejora global de precisión para saber si un sistema de clasificación penitenciaria tomará mejores decisiones?

## Alcance

- El anuncio de Michigan afirma que el nuevo sistema mejorará alrededor de un 30 % la predicción de violencia futura.
- No se han publicado la métrica, la referencia, la definición del resultado, el periodo de observación ni las tasas de error.
- Por ello, el proyecto no reproduce ni audita el sistema de Michigan.
- La base COMPAS corresponde al condado de Broward, Florida, y a reincidencia observada durante dos años. Solo se usa para explicar cómo cambian los falsos positivos y negativos al mover el umbral.
- No se entrena ningún modelo ni se genera una predicción propia de Nebula.

## Archivos

- `analisis_algoritmos_prision.ipynb`: notebook principal, ejecutado y documentado.
- `datos/compas-scores-two-years.csv`: copia del archivo publicado por ProPublica.
- `resultados/metricas_umbrales.csv`: métricas para los diez umbrales posibles.
- `resultados/metricas_grupos.csv`: comparación descriptiva con el corte en 5.
- `fuentes.md`: fuentes, fechas y función de cada documento.

## Reproducción

El notebook necesita Python 3 con `pandas`, `numpy`, `matplotlib`, `nbformat`, `nbclient` e IPython. Debe ejecutarse desde la carpeta del proyecto. Los dos CSV de `resultados/` se regeneran durante la ejecución.

## Hallazgos principales

- Con el umbral en 5, la precisión global en la muestra pública es del 66,1 %, con 1.018 falsos positivos y 1.076 falsos negativos.
- Subir el umbral a 8 reduce las falsas alarmas a 297, pero eleva los falsos negativos a 1.962.
- La precisión global es parecida entre personas registradas como negras y blancas, pero la tasa de falsos positivos es del 42,3 % y el 22,0 %, respectivamente.
- Estos porcentajes describen COMPAS en Broward. No son estimaciones del sistema de Michigan.

## Fuente de los datos

ProPublica, repositorio `compas-analysis`:

<https://github.com/propublica/compas-analysis>

La metodología y sus limitaciones están documentadas en:

<https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm>
