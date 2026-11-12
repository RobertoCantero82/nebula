# Conexiones imposibles 02: Big y Men in Black

## Categoría

**EDA (análisis exploratorio de datos).** Describo y comparo datos existentes. No genero predicciones.

## Pregunta

¿Qué caminos conectan *Big* (1988) y *Men in Black* (1997), y cuál permite construir la unión más directa entre lo que aparece y suena en ambas películas?

## Datos

- MovieLens 32M: 32.000.204 valoraciones sobre 84.432 películas, géneros y etiquetas, con datos hasta el 12 de octubre de 2023.
- Créditos comprobados en AFI Catalog, Amblin y Sony Pictures Museum.
- Canciones y autoría comprobadas mediante los créditos de *Big* y fuentes discográficas sobre *Men in Black* y *Forget Me Nots*.

Cada fila de `valoraciones_compartidas.csv` representa a una persona que puntuó las dos películas. Cada fila de `resumen_movielens.csv` resume una película. `conexiones_comprobadas.csv` separa los caminos de créditos, familia y música.

## Cómo reproducirlo

1. Descargo MovieLens 32M desde GroupLens y conservo el ZIP original.
2. Ajusto `archivo_zip` en `analizar_movielens.py` si cambia la ubicación local.
3. Ejecuto `python analizar_movielens.py`.
4. Ejecuto `python construir_notebook.py` para regenerar el notebook con sus resultados.

## Resultado principal

MovieLens encuentra 15.741 espectadores compartidos, una única categoría común y 14 etiquetas coincidentes. Los créditos ofrecen dos puentes especialmente fuertes: Barry Sonnenfeld y los hermanos Anne y Steven Spielberg. La conexión más literal aparece en la música: *Forget Me Nots*, presente en *Big*, es la composición que nueve años después sostiene la canción *Men in Black* de Will Smith.

## Limitaciones

MovieLens no representa a todo el público. Sus etiquetas son aportaciones de usuarios y pueden contener ruido, sinónimos u omisiones. Los créditos no capturan por sí solos elementos visuales o musicales. La comparación identifica conexiones documentadas; no demuestra que una película influyera creativamente en la otra.
