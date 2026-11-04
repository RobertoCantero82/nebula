# Horario escolar y amanecer en España

## Categoría

EDA (análisis exploratorio de datos).

## Pregunta

¿Cuántas mañanas escolares empezarían antes del amanecer para la población española de 5 a 17 años si se mantuviera el horario de verano durante todo el año?

## Archivos

- `analisis_horario_escolar_oscuridad.ipynb`: notebook ejecutado.
- `municipios_poblacion_5_17.csv`: población municipal procesada, coordenadas y comunidad autónoma.
- `resultados_municipios.csv`: resultados para tres relojes y tres horas de salida.
- `resumen_escenarios.csv`: resumen nacional.
- `resumen_comunidades.csv`: resumen autonómico para la salida a las 8:30.

## Fuentes

- INE, Censo anual de población 2021-2025, tabla nacional 68542, descargada el 4 de noviembre de 2026: `https://www.ine.es/jaxiT3/files/t/es/csv_bd/68542.csv?nocab=1`.
- IGN, centroides municipales del servicio SIGNA, descargados el 4 de noviembre de 2026: `https://certiserviciosgis.ign.es/servicios/rest/services/signa/Unidades_Administrativas/MapServer/7`.

Los archivos brutos permanecen en la carpeta de trabajo. La descarga nacional del INE ocupa unos 454 MB y no se duplica en la carpeta pública; el CSV procesado conserva las variables necesarias para revisar los resultados.

## Método

Calculo el amanecer oficial con las ecuaciones solares de NOAA para cada centroide municipal y mañana del calendario común del curso 2026-2027. Comparo el sistema estacional vigente, el horario de invierno permanente y el horario de verano permanente. Una mañana se clasifica como oscura cuando la hora de salida elegida es anterior al amanecer local.

El calendario común va del 7 de septiembre de 2026 al 18 de junio de 2027 y excluye fines de semana, vacaciones comunes de Navidad y Semana Santa y festivos nacionales. Los calendarios autonómicos y locales pueden restar algunas mañanas.

## Limitaciones

La población de 5 a 17 años no equivale exactamente al alumnado matriculado. No existen datos nacionales homogéneos sobre hora de entrada, duración del trayecto o medio de transporte de cada menor. Por eso se publican tres salidas, a las 8:00, 8:30 y 9:00, y los resultados se presentan como escenarios. Usansolo, con 623 residentes de esas edades, queda fuera porque el código municipal nuevo todavía no aparece en la capa del IGN utilizada.
