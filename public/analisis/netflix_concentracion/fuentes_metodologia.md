# Fuentes y método

Autor: Roberto Cantero · Nebula. Consulta y análisis: 20 de noviembre de 2026.

Pregunta: tenemos miles de títulos para elegir, pero ¿cuánto de lo que vemos se concentra en unos pocos?

Fuente numérica: Netflix, What We Watched, enero-junio de 2026, hojas Shows y Movies. [Página oficial](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026). El archivo original se conserva como netflix_2026_s1.xlsx; su SHA-256 figura en resultados.json. Sus notas al pie están en notas_originales.json. La fecha del anuncio no es la fecha del periodo analizado.

## Decisiones

- La unidad es una entrada del informe: película, temporada u otro programa. No agrupo temporadas ni fusiono obras con nombres iguales.
- Ordeno por horas en sentido descendente. Resuelvo empates alfabéticamente. Localizo la primera posición que alcanza al menos el 50 % del total.
- Sumo 97.664.500.000 horas. Incluyo 859.900.000 horas de Other Movies y Other Shows en el denominador, pero excluyo ambas bolsas del ranking y de las 17.370 entradas identificadas.
- Según la nota del archivo, las bolsas contienen títulos con menos de 50.000 visualizaciones y Other Shows incluye todos los videopódcast.
- Conservo los valores originales redondeados. No trato las visualizaciones ausentes de las bolsas como cero.
- La sensibilidad por visualizaciones solo usa entradas identificadas; tiene un denominador diferente. Las visualizaciones equivalentes no son espectadores únicos.
- No interpreto el informe mundial como un catálogo disponible simultáneamente en una cuenta. Fechas de estreno, duración y disponibilidad territorial son distintas.
- Los resultados son descriptivos; no miden algoritmos, satisfacción, calidad, beneficios o diversidad individual. Son datos publicados por Netflix, sin auditoría independiente de Nebula.

## Reproducción

Requiero Python 3.10 o posterior y solo su biblioteca estándar. Coloco el Excel y preparar_datos.py junto a los cuadernos. Ejecuto `python preparar_datos.py` y después los cuadernos 01 y 02 en orden desde esa carpeta. Los dos cuadernos se han ejecutado celda a celda y contienen sus salidas reales. No requieren acceso a internet.

## Resultados

| Grupo | Entradas identificadas | Entradas para el 50 % | Horas de los 100 primeros |
| --- | ---: | ---: | ---: |
| Todo el informe | 17.370 | 775 | 18,9 % |
| Películas | 9.177 | 468 | 24,5 % |
| Series y otros programas | 8.193 | 473 | 23,6 % |

## Contexto y menciones

- [Noticia de Digital Trends, 19 de noviembre de 2026](https://www.digitaltrends.com/movies/netflix-has-325-million-subscribers-but-its-ceo-thinks-the-real-battle-is-just-beginning/).
- [Página de Netflix en LinkedIn](https://www.linkedin.com/company/netflix/). Al publicar, selecciono su página real en el editor para activar la mención; escribir un nombre por sí solo no crea una etiqueta.

## Ubicaciones finales

Artículo: `nebula/src/content/articulos/netflix_miles_titulos.md`.

Portada: `nebula/public/imagenes/netflix_miles_titulos_portada.png`.

Cuadernos, Excel, CSV, preparar_datos.py, resultados.json, notas_originales.json y este documento: `nebula/public/analisis/netflix_concentracion/`.

Copia de trabajo y post: `_repos_nebula/netflix_concentracion/`.

Los directorios anteriores dependen de `C:\Users\rober\OneDrive\Documentos\proyectos_datos`. No he escrito en esas ubicaciones ni he publicado cambios.
