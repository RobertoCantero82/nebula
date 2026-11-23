# Mis fuentes, unidades y límites

Autor: Roberto Cantero · Nebula. Corte: 23 de noviembre de 2026.

## Mi fuente numérica

Wikimedia Analytics API: https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/

Uso consultas de páginas en inglés, todos los accesos, agente user, días UTC. No cuento personas únicas ni búsquedas. Cada serie histórica guarda 43 números en orden, de -7 a +35 respecto a la fecha declarada. Los JSON son una transcripción estructurada de los números extraídos del JSON visible en el navegador; no son las respuestas HTTP originales completas. Conservo títulos, fechas, peticiones y huellas para auditar esta copia. Los redireccionamientos no se agregan automáticamente y son una limitación. He comprobado las fechas en las fichas visibles de cada artículo de Wikipedia, fuente secundaria para esas fechas; no afirmo que todas las fechas se hayan contrastado con la editora.

GTA VI: https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Grand_Theft_Auto_VI/daily/2026110100/2026112200

## Mi contexto original

- Tienda de Rockstar, lanzamiento el 19 de noviembre: https://store.rockstargames.com/game/buy-gta-vi?drm=playstation
- Comunicado de Take-Two del 20 de noviembre, también depositado en la SEC: https://www.sec.gov/Archives/edgar/data/946581/000162828026075217/exhibit9918k.htm . Los 3.790 millones de dólares son ventas al público estimadas por la empresa hasta el final del 19 de noviembre, no ingresos netos de Take-Two ni un dato usado para entrenar mi modelo.

## Mi muestra y sus fechas

Muestra de conveniencia de treinta grandes videojuegos de pago; no es un censo. El protocolo documenta mis dos exclusiones, las particiones temporales, las métricas y el tratamiento de incertidumbre. Los otros veintiocho juegos siguen incluidos, aun con controversias, pandemia o estrenos regionales próximos. No ajusto la selección a los resultados.

| Juego | Día 0 utilizado | Procedencia |
|---|---|---|
| Red Dead Redemption 2 | 2018-10-26 | [Fecha consultada](https://en.wikipedia.org/wiki/Red_Dead_Redemption_2) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Red_Dead_Redemption_2/daily/2018101900/2018113000) |
| Fallout 4 | 2015-11-10 | [Fecha consultada](https://en.wikipedia.org/wiki/Fallout_4) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Fallout_4/daily/2015110300/2015121500) |
| Dark Souls III | 2016-04-12 | [Fecha consultada](https://en.wikipedia.org/wiki/Dark_Souls_III) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Dark_Souls_III/daily/2016040500/2016051700) |
| Uncharted 4: A Thief's End | 2016-05-10 | [Fecha consultada](https://en.wikipedia.org/wiki/Uncharted_4%3A_A_Thief%27s_End) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Uncharted_4%3A_A_Thief%27s_End/daily/2016050300/2016061400) |
| No Man's Sky | 2016-08-09 | [Fecha consultada](https://en.wikipedia.org/wiki/No_Man%27s_Sky) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/No_Man%27s_Sky/daily/2016080200/2016091300) |
| Final Fantasy XV | 2016-11-29 | [Fecha consultada](https://en.wikipedia.org/wiki/Final_Fantasy_XV) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Final_Fantasy_XV/daily/2016112200/2017010300) |
| Horizon Zero Dawn | 2017-02-28 | [Fecha consultada](https://en.wikipedia.org/wiki/Horizon_Zero_Dawn) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Horizon_Zero_Dawn/daily/2017022100/2017040400) |
| The Legend of Zelda: Breath of the Wild | 2017-03-03 | [Fecha consultada](https://en.wikipedia.org/wiki/The_Legend_of_Zelda%3A_Breath_of_the_Wild) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/The_Legend_of_Zelda%3A_Breath_of_the_Wild/daily/2017022400/2017040700) |
| Super Mario Odyssey | 2017-10-27 | [Fecha consultada](https://en.wikipedia.org/wiki/Super_Mario_Odyssey) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Super_Mario_Odyssey/daily/2017102000/2017120100) |
| Assassin's Creed Origins | 2017-10-27 | [Fecha consultada](https://en.wikipedia.org/wiki/Assassin%27s_Creed_Origins) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Assassin%27s_Creed_Origins/daily/2017102000/2017120100) |
| God of War (2018 video game) | 2018-04-20 | [Fecha consultada](https://en.wikipedia.org/wiki/God_of_War_%282018_video_game%29) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/God_of_War_%282018_video_game%29/daily/2018041300/2018052500) |
| Spider-Man (2018 video game) | 2018-09-07 | [Fecha consultada](https://en.wikipedia.org/wiki/Spider-Man_%282018_video_game%29) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Spider-Man_%282018_video_game%29/daily/2018083100/2018101200) |
| Resident Evil 2 (2019 video game) | 2019-01-25 | [Fecha consultada](https://en.wikipedia.org/wiki/Resident_Evil_2_%282019_video_game%29) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Resident_Evil_2_%282019_video_game%29/daily/2019011800/2019030100) |
| Sekiro: Shadows Die Twice | 2019-03-22 | [Fecha consultada](https://en.wikipedia.org/wiki/Sekiro%3A_Shadows_Die_Twice) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Sekiro%3A_Shadows_Die_Twice/daily/2019031500/2019042600) |
| Death Stranding | 2019-11-08 | [Fecha consultada](https://en.wikipedia.org/wiki/Death_Stranding) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Death_Stranding/daily/2019110100/2019121300) |
| Doom Eternal | 2020-03-20 | [Fecha consultada](https://en.wikipedia.org/wiki/Doom_Eternal) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Doom_Eternal/daily/2020031300/2020042400) |
| Animal Crossing: New Horizons | 2020-03-20 | [Fecha consultada](https://en.wikipedia.org/wiki/Animal_Crossing%3A_New_Horizons) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Animal_Crossing%3A_New_Horizons/daily/2020031300/2020042400) |
| The Last of Us Part II | 2020-06-19 | [Fecha consultada](https://en.wikipedia.org/wiki/The_Last_of_Us_Part_II) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/The_Last_of_Us_Part_II/daily/2020061200/2020072400) |
| Ghost of Tsushima | 2020-07-17 | [Fecha consultada](https://en.wikipedia.org/wiki/Ghost_of_Tsushima) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Ghost_of_Tsushima/daily/2020071000/2020082100) |
| Cyberpunk 2077 | 2020-12-10 | [Fecha consultada](https://en.wikipedia.org/wiki/Cyberpunk_2077) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Cyberpunk_2077/daily/2020120300/2021011400) |
| Resident Evil Village | 2021-05-07 | [Fecha consultada](https://en.wikipedia.org/wiki/Resident_Evil_Village) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Resident_Evil_Village/daily/2021043000/2021061100) |
| Ratchet & Clank: Rift Apart | 2021-06-11 | [Fecha consultada](https://en.wikipedia.org/wiki/Ratchet_%26_Clank%3A_Rift_Apart) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Ratchet_%26_Clank%3A_Rift_Apart/daily/2021060400/2021071600) |
| Horizon Forbidden West | 2022-02-18 | [Fecha consultada](https://en.wikipedia.org/wiki/Horizon_Forbidden_West) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Horizon_Forbidden_West/daily/2022021100/2022032500) |
| Elden Ring | 2022-02-25 | [Fecha consultada](https://en.wikipedia.org/wiki/Elden_Ring) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Elden_Ring/daily/2022021800/2022040100) |
| God of War Ragnarök | 2022-11-09 | [Fecha consultada](https://en.wikipedia.org/wiki/God_of_War_Ragnar%C3%B6k) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/God_of_War_Ragnar%C3%B6k/daily/2022110200/2022121400) |
| Resident Evil 4 (2023 video game) | 2023-03-24 | [Fecha consultada](https://en.wikipedia.org/wiki/Resident_Evil_4_%282023_video_game%29) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Resident_Evil_4_%282023_video_game%29/daily/2023031700/2023042800) |
| The Legend of Zelda: Tears of the Kingdom | 2023-05-12 | [Fecha consultada](https://en.wikipedia.org/wiki/The_Legend_of_Zelda%3A_Tears_of_the_Kingdom) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/The_Legend_of_Zelda%3A_Tears_of_the_Kingdom/daily/2023050500/2023061600) |
| Final Fantasy XVI | 2023-06-22 | [Fecha consultada](https://en.wikipedia.org/wiki/Final_Fantasy_XVI) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Final_Fantasy_XVI/daily/2023061500/2023072700) |
| Baldur's Gate 3 | 2023-08-03 | [Fecha consultada](https://en.wikipedia.org/wiki/Baldur%27s_Gate_3) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Baldur%27s_Gate_3/daily/2023072700/2023090700) |
| Spider-Man 2 (2023 video game) | 2023-10-20 | [Fecha consultada](https://en.wikipedia.org/wiki/Spider-Man_2_%282023_video_game%29) · [Serie](https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/Spider-Man_2_%282023_video_game%29/daily/2023101300/2023112400) |

## Cómo reproduzco mi trabajo

1. Uso Python 3.10 o posterior e instalo NumPy. El entorno de ejecución y la versión efectiva aparecen en el primer notebook.
2. Mantengo modelo.py, protocolo.md, series_consultadas.json y gta_vi_consultado.json juntos.
3. Ejecuto `python modelo.py`. Regenero consultas_diarias.csv y resultados.json sin conexión.
4. Ejecuto los dos notebooks en orden en esa carpeta. Alternativamente, `python crear_entrega.py` ejecuta secuencialmente sus celdas mediante Python y guarda sus salidas; no utiliza un servidor de Jupyter.

La expresión de ridge es B=(ZᵀZ+diag(0,α,α))⁻¹Zᵀlog(Y), con intercepto sin penalizar y entradas estandarizadas solo con el conjunto de ajuste. Pruebo α=1 y α=10 en validación. Cada juego aporta una fila y dos objetivos. La prueba final permanece fuera del ajuste. Conservo el modelo ajustado con veintiún juegos para aplicarlo a GTA VI.

Mi banda orientativa usa el máximo error absoluto logarítmico por horizonte en los siete juegos de validación: predicción × exp(±error). No es un intervalo de confianza ni de predicción con cobertura probabilística garantizada. No uso los errores de prueba para ajustar la banda. La extrapolación de GTA VI y la pequeña muestra limitan su interpretación.

## Cómo contrastaré la previsión

Para el primer horizonte consultaré 2026120300–2026120900 y para el segundo 2026121700–2026122300, siempre con los mismos proyecto, título, accesos y agente. Compararé su media con las previsiones congeladas, 92.162,90 y 51.382,60 consultas diarias. Estas cifras sin redondear son para reproducir el cálculo; el artículo las redondea. No he creado una automatización ni programado una revisión.

## Huellas de los archivos

- series_consultadas.json: `2987953f6c49fe831613f92af8e3bbcb2f4d5815d959fea7482e9317983a1cfc`
- gta_vi_consultado.json: `cdbd07d5e8dce7b652d835e1ebe9cb7b56582428e617daa98501778b12381105`
- protocolo.md: `d2788ddcc0e09f8d911e9b6e8816f3dbdd3941ba708503b5355b2478681b6af9`
