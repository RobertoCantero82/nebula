# Conexiones imposibles 01

**Categoría: EDA (análisis exploratorio de datos).**

## Pregunta

¿Qué semejanzas encuentran 32 millones de valoraciones, los géneros, las etiquetas y los créditos entre *Cazafantasmas 2* (1989) y *The Many Adventures of Winnie the Pooh* (1977), y qué detalle visible se les escapa?

## Datos

- MovieLens 32M: 32.000.204 valoraciones sobre 84.432 películas y etiquetas, con datos hasta el 12 de octubre de 2023.
- Wikidata: créditos de reparto, doblaje, dirección, guion, producción, montaje, fotografía y música. Los elementos de partida son `Q492214` y `Q498434`. Datos CC0 consultados el 2 de noviembre de 2026.
- Comprobación visual: Óscar lleva una prenda con Winnie the Pooh en la secuencia de su secuestro. La observación está documentada en Ghostbusters Wiki y debe verificarse en una copia legal de la película antes de publicar.
- Disney confirma que *The Many Adventures of Winnie the Pooh* se estrenó el 11 de marzo de 1977 y proporciona su reparto principal.

Cada fila de `valoraciones_compartidas.csv` representa un usuario de MovieLens que puntuó las dos películas. Cada fila de `rutas_wikidata.csv` representa una ruta única de cuatro relaciones de crédito: película inicial → profesional → película intermedia → profesional → película final.

## Método

Comparo volumen, media y distribución de valoraciones; cruzo los usuarios que puntuaron ambas películas; calculo la correlación entre sus notas; normalizo etiquetas; comparo géneros; y busco rutas con una sola película intermedia mediante ocho propiedades de Wikidata.

El EDA encuentra cero géneros compartidos, cero etiquetas coincidentes, 277 usuarios comunes y cinco rutas de créditos. Entre esos 277 usuarios, 179 prefieren Pooh, 46 prefieren *Cazafantasmas 2* y 52 las puntúan igual.

El resultado describe lo que Wikidata tiene registrado. No prueba que estas sean todas las conexiones posibles ni mide la intención de quienes hicieron las películas. La conexión visual del pijama queda fuera porque no está codificada como un crédito o una relación estructurada.

## Archivos

- `conexiones_imposibles_01_eda.ipynb`: notebook ejecutado.
- `rutas_wikidata.csv`: cinco rutas deduplicadas.
- `resumen_movielens.csv`: ficha estadística de las dos películas.
- `valoraciones_compartidas.csv`: notas de los 277 usuarios comunes.
- `resultados_movielens.json`: resultados agregados del análisis.
- `ficha_tecnica.csv`: datos técnicos y recuentos de créditos.
- `consulta_wikidata.sparql`: consulta reproducible.
- `fuentes.md`: enlaces y limitaciones.

