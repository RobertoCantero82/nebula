# Predicción de taquilla de *La bola negra*

Este proyecto estima la recaudación final en España de *La bola negra* con los datos disponibles después del fin de semana del 6 al 8 de noviembre de 2026.

## Fuentes

- [Histórico de taquilla de Cinerama](https://cinerama.es/taquilla/historico/).
- Fichas individuales de las películas en Cinerama.
- Cinerama atribuye las cifras de taquilla a Comscore Movies.
- [Serie semanal del ICAA](https://www.cultura.gob.es/cultura/areas/cine/datos/taquilla-espectadores.html), utilizada como contraste institucional.

La descarga reunió 1.137 observaciones semanales de 108 películas. La muestra final contiene 13 títulos que seguían en el top 10 en su séptima semana y cuya trayectoria posterior ya había terminado.

## Reproducción

1. Instalar Node.js 22 o posterior y ejecutar `npm install cheerio`.
2. Descargar los datos con `node descargar_datos.mjs`.
3. Instalar Python 3.12 y las dependencias de `requirements.txt`.
4. Ejecutar `python analizar_prediccion_acumulada.py`.
5. Abrir y ejecutar `prediccion_taquilla_la_bola_negra.ipynb`.

El notebook público ya contiene las ocho celdas de código ejecutadas, sin errores, y dos gráficos incrustados.

## Límites

- Solo 13 películas de 2026 cumplen todos los criterios de comparación.
- La prueba temporal contiene cuatro películas; sus métricas son orientativas.
- El modelo no conoce futuros reestrenos, cambios de salas ni el efecto de nuevos premios.
- Los datos de Comscore son reproducidos por Cinerama; no existe una API pública documentada para esta serie.

