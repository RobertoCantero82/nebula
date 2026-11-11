# Huelga del 11N y demanda eléctrica

EDA de la demanda eléctrica real y prevista durante la huelga general del 11 de noviembre de 2026.

## Pregunta

¿Cuánto se separa el consumo eléctrico real de la previsión de Red Eléctrica durante la jornada?

## Fuente principal

- Red Eléctrica, REData API, widget `demanda-tiempo-real`.
- Resolución de servicios mínimos: BOE-A-2026-23371.
- Los valores históricos se conservan en `datos/huelgas_historicas.csv` con su enlace y criterio de medición.

## Reproducción

1. Ejecutar `python descargar_datos.py` para actualizar la respuesta oficial.
2. Ejecutar `python analisis_huelga_11n.py`.
3. Ejecutar `python ejecutar_notebook.py` para regenerar las salidas del cuaderno.

## Limitaciones

- La diferencia entre demanda real y prevista mide actividad eléctrica, no porcentaje de huelguistas.
- La previsión ya intenta corregir calendario, actividad y meteorología, pero puede contener error.
- La borrasca Charles, el teletrabajo y el autoconsumo dificultan la comparación con 2010 y 2012.
- Red Eléctrica indica que la demanda publicada no incluye toda la energía autoconsumida.
- Los porcentajes históricos proceden de cortes horarios y medias diarias diferentes; se usan como contexto, no como una clasificación exacta.
