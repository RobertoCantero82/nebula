# Microsoft y la inteligencia híbrida · EDA Nebula

Este proyecto realiza un análisis exploratorio de datos sobre el crecimiento de los PC con hardware dedicado para IA y la distancia que existe entre esa categoría amplia, los Copilot+ PC y los nuevos equipos premium presentados por Microsoft.

Abre `eda_inteligencia_hibrida.ipynb` y ejecuta todas las celdas. El cuaderno trabaja con CSV locales y no necesita descargar datos.

## Pregunta editorial

Cuando la industria afirma que los “PC con IA” están cerca de ser mayoría, ¿habla realmente de ordenadores capaces de ejecutar la inteligencia híbrida que Microsoft acaba de presentar?

## Clasificación

**EDA.** No contiene machine learning ni una predicción propia de Nebula.

Los datos públicos disponibles combinan pocas estimaciones globales, previsiones de consultoras con definiciones diferentes y observaciones regionales. Esa estructura no permite entrenar y validar de forma responsable un modelo de machine learning.

## Estructura

- `datos_prevision_ai_pc.csv`: estimaciones, revisiones y previsiones publicadas.
- `senales_mercado.csv`: señales observadas y especificaciones de Microsoft.
- `fuentes.csv`: registro documental con cautelas.
- `eda_inteligencia_hibrida.ipynb`: análisis ejecutado.
- `graficos/`: cinco gráficos del EDA.
- `resultados/resumen_editorial_eda.csv`: hallazgos para construir el artículo.
- `resultados/especificaciones_microsoft.csv`: tabla de producto.
- `requirements.txt`: dependencias reproducibles.

## Hallazgo central

El hardware dedicado a IA avanza con rapidez, pero “AI PC” no equivale a Copilot+ PC ni a una estación capaz de ejecutar modelos locales de 120.000 millones de parámetros. El crecimiento de la categoría mide disponibilidad de componentes; no demuestra uso habitual, productividad ni confianza en los agentes.

Consulta documental: 8 de octubre de 2026. Antes de publicar, conviene comprobar si las consultoras han revisado sus cifras.
