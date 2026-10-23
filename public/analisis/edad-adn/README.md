# Edad a partir de marcas del ADN

**Categoría: machine learning.**

Quiero predecir edad cronológica en personas reservadas y comprobar si los errores pueden confundirse con una señal de rejuvenecimiento. No predigo longevidad, salud ni respuesta a un tratamiento.

## Resultado comprobado

- 656 personas de 19–101 años, de GSE40279.
- 23.734 candidatos fijados por identificador, sin consultar edades; 1.000 marcas en el modelo elegido.
- 420 personas de entrenamiento, 109 de calibración y 127 de prueba; chips separados: 43, 10 y 14, respectivamente.
- Error absoluto medio de prueba: **5,317 años**; referencia de mediana del entrenamiento: **14,047 años**.
- Error absoluto mediano: 4,404 años; raíz del error cuadrático: 7,335 años; R²: 0,819.
- Validación interna: error medio de 4,721 años; ridge con penalización 100 y 1.000 marcas.
- Intervalo orientativo del 95 % del error medio, por remuestreo de chips: 4,275–6,521 años.
- Banda calibrada buscando un 90 %: ±9,639 años; cobertura observada de prueba: **110/127, 86,61 %**.
- En 19–39 años asigno 6,462 años de más de media (16 personas); en 80 o más, 7,018 de menos (17 personas). Son residuos del modelo, no rejuvenecimiento observado.

## Reproducción desde la copia pública

1. Descargo esta carpeta completa, conservando `data/` y `resultados/`.
2. Instalo Python 3.12 y las dependencias de `requirements.txt`: `python -m pip install -r requirements.txt`.
3. Abro `edad_adn.ipynb` en Jupyter y ejecuto todas las celdas desde esta carpeta.

El cuaderno llama a `modelo.py`, repite las particiones, la selección completa de marcas y el entrenamiento. No necesita conectarse a la red para modelar. Los tiempos de ajuste pueden variar; pequeñas diferencias numéricas entre sistemas son posibles.

La copia pública contiene todos los candidatos fijados antes del entrenamiento en `data/metilacion_candidatos.npz` (unos 56 MB), no solo las marcas ganadoras. Por eso permite repetir la selección dentro de cada vuelta de validación sin una preselección por edad hecha con toda la cohorte.

Para auditar la extracción desde los originales ejecuto, en orden:

```
python descargar_datos.py
python preparar_datos.py
```

Necesito espacio para una descarga de aproximadamente 1,24 GB, además de la matriz compacta. `data/fuentes.json` conserva las URL originales y sus huellas SHA-256. La matriz original es una descarga de datos ya procesados por los investigadores, no un reprocesamiento de las intensidades del laboratorio.

## Archivos

- `edad_adn.ipynb`: cuaderno ejecutado, explicaciones, gráficos y comprobaciones.
- `protocolo.md`: decisiones fijadas antes de ajustar modelos.
- `modelo.py`: particiones, pipeline, validación, calibración y evaluación.
- `descargar_datos.py`, `preparar_datos.py`: preparación separada del análisis.
- `data/muestras.csv`: edad, procedencia, chip y códigos públicos de muestra.
- `data/metilacion_candidatos.npz`: matriz de metilación y nombres de candidatos.
- `data/preparacion.json`: controles de extracción.
- `resultados/particiones.csv`: asignación de personas a cada grupo.
- `resultados/validacion.csv`: cuatro candidatos y cinco vueltas internas.
- `resultados/predicciones_prueba.csv`: edades reales, predicciones y bandas de prueba.
- `resultados/metricas.json`, `errores_por_edad.csv`, `marcadores_modelo.csv`: resultados auditables.

## Límites

Mantengo chips separados, pero comparto cohorte, procedimientos originales y algunas placas y procedencias. No hago validación externa. No garantizo cobertura del 90 % fuera de estas muestras: la calibración sencilla presupone comparabilidad y los lotes pueden comprometer la independencia. Los intervalos por edad son especialmente inestables por su pequeño tamaño.

La sangre mezcla tipos celulares y no separo causalmente sus efectos. Tampoco mido cambios antes y después de una intervención. No utilizo los 71 marcadores del reloj original, que se desarrolló con estas mismas personas. La regla de candidatos por identificador reduce el tamaño de publicación y no pretende producir el reloj más preciso posible.

## Fuentes

- [GEO, GSE40279](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE40279).
- [Hannum et al., Molecular Cell, 2013](https://pubmed.ncbi.nlm.nih.gov/23177740/), DOI: 10.1016/j.molcel.2012.10.016.
- [Sumario de National Geographic, noviembre de 2026](https://www.nationalgeographic.com.es/edicion-impresa/national-geographic-noviembre-2026_29672): punto de partida editorial, no fuente de las métricas propias.
