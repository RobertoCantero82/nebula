# Halloween: una película para cada noche

**Categoría: EDA.** Selección editorial de 120 títulos (1922–2022). Consulta: 26/10/2026. Votos de MovieLens 32M hasta 12/10/2023. No es un modelo predictivo ni una muestra representativa del cine de terror.

## Reproducir el análisis

1. Descomprimo `halloween_cine_reproducible.zip` en una carpeta.
2. Instalo Python 3.12 y las bibliotecas de `requirements.txt` (`python -m pip install -r requirements.txt`).
3. Abro `halloween_cine_eda.ipynb` en Jupyter o VS Code y ejecuto todas las celdas desde esa carpeta. No necesito red ni claves de API.
4. Obtengo `resultados.json`, `peliculas.json` y `peliculas_analizadas.csv`. Las huellas digitales de los datos de entrada están en `huellas.json`.

El notebook entregado contiene sus resultados y gráficos. El archivo de requisitos indica intervalos compatibles; `entorno_ejecucion.json` registra las versiones utilizadas para la ejecución de entrega.

## Archivos y unidad de observación

- `fichas_documentadas.csv`: una fila por película, con fuentes, etiquetas editoriales y metadatos. Los valores ausentes de texto se conservan vacíos.
- `votos_histograma.csv`: una fila por película y puntuación; `votos` cuenta cuántos usuarios dieron esa puntuación en el conjunto original. No contiene identificadores de personas.
- `duraciones_contrastadas.csv`: duración de referencia y enlace a la ficha de Wikipedia usada. Si la ficha enumera varias, uso la mayor; no abarca todos los montajes existentes.
- `peliculas_analizadas.csv`: fichas unidas a medias y recuentos calculados.
- `peliculas.json`: las mismas observaciones que lee el recomendador.
- `resultados.json`: cifras agregadas que sustentan el artículo.
- `recomendador_halloween.js`: filtro y ordenación deterministas utilizados en la web.
- `LICENCIA_MOVIELENS.txt`: condiciones originales que mantienen los datos y sus transformaciones.

## Diccionario abreviado

`movie_id`: identificador de MovieLens; `imdb` y `tmdb`: identificadores para cruces, no valoraciones de esas plataformas. `titulo`: título editorial para España; `titulo_fuente`: título original del catálogo. `anio`: año de referencia editorial; `anio_catalogo`: año que figura en MovieLens; `nota_anio`: diferencia documentada. `duracion`: minutos utilizados para filtrar; `duracion_min` y `duracion_max`: valores originales de Wikidata, conservados para contraste; `duraciones_ficha`: valores de la ficha de Wikipedia. `paises`: países de producción según Wikidata, separados por `|`, incluidas coproducciones; no equivale a idioma o ambientación. `generos`: géneros de MovieLens; `generos_wikidata`: géneros originales de Wikidata. `familias`, `tono`, `intensidad`, `sinopsis`: elaboración editorial. `nota`: media de estrellas, de 0,5 a 5; `votos`: número de valoraciones de la película en MovieLens 32M; `estrellas`: suma de puntuaciones. `epoca`: anterior a 2000 o desde 2000.

## Reglas de recomendación

Aplico todos los filtros elegidos a la vez. La intensidad funciona como un máximo; los demás filtros son coincidencias exactas o límites de tiempo. Si no queda nada, muestro cero resultados y propongo cambiar una preferencia. No relajo filtros automáticamente. Ordeno por nota media sin redondear, votos e identificador; si se elige participación, el orden es votos, nota e identificador. No hay modelo, personalización oculta ni predicción de gusto.

Etiqueto la intensidad como 1 (amenaza sugerida, poca explicitud relativa), 2 (tensión intermedia o violencia puntual) y 3 (violencia explícita, daño corporal o angustia especialmente dura). Es una codificación editorial orientativa basada en argumentos, sin experimento con espectadores ni evaluación independiente entre codificadores. No mide miedo, no es clasificación por edades y no garantiza ausencia de escenas sensibles. Cada fila conserva el criterio y la ficha de argumento que permite revisarlo. La comedia no rebaja automáticamente la intensidad.

## Selección, fuentes y limitaciones

He construido una selección nueva porque la conversación anterior no devolvió su lista completa. Incluyo clásicos, monstruos, fantasmas, ciencia ficción, asesinos, zombis, vampiros, cine español y asiático y comedia. No la selecciono por una nota mínima. Incluyo deliberadamente el mediometraje televisivo *La cabina*. Sustituyo Babadook por Onibaba al no localizar el primero por título en el catálogo descargado.

Distingo películas homónimas y remakes mediante identificadores: Drácula (1931) corresponde a la película en inglés, no a la versión en español; Verónica (2017) corresponde a la de Paco Plaza. *El ejército de las tinieblas* mantiene 1992 como estreno en festival, aunque MovieLens la registra en 1993. Las etiquetas de Wikidata no sustituyen los títulos editoriales; pueden contener errores.

Uso [MovieLens 32M, GroupLens](https://grouplens.org/datasets/movielens/32m/). Cito a F. Maxwell Harper y Joseph A. Konstan (2015), *The MovieLens Datasets: History and Context*, [DOI 10.1145/2827872](https://doi.org/10.1145/2827872). Conservo las condiciones de licencia originales, incluida la restricción de uso comercial sin autorización. GroupLens y la Universidad de Minnesota no respaldan este proyecto.

Los países y géneros de [Wikidata](https://www.wikidata.org/) son datos estructurados CC0. Los argumentos y duraciones se contrastan con las fichas de Wikipedia enlazadas por película. Las sinopsis son redacción propia, no reproducción de los argumentos. Los textos originales de Wikipedia están bajo sus condiciones de atribución y compartir igual; no los incluyo completos en el paquete público.

Conservo en `fuentes/` del análisis local el ZIP original (MD5 comprobado), los metadatos del catálogo y las respuestas de Wikidata y Wikipedia. La copia pública conserva las extracciones necesarias para repetir todos los cálculos sin redistribuir el ZIP de 239 MB. Las sumas se extraen de `ratings.csv` por película y puntuación. Para la cadena de extracción completa conservo los scripts locales y las huellas de las fuentes en `fuentes_manifest.json`.

Limitaciones: corte histórico en 2023, selección editorial, usuarios no representativos del público español, películas con participación desigual, diferencias entre montajes y metadatos, intensidad subjetiva y familias que se solapan. No comparo popularidad comercial ni disponibilidad en plataformas. No convierto correlaciones en explicaciones causales. No hay predicciones propias.
