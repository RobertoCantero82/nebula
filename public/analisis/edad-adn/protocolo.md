# Edad a partir de marcas del ADN

**Categoría: machine learning. Protocolo fijado antes de ajustar modelos.**

Quiero predecir la edad cronológica de personas no utilizadas para entrenar a partir de metilación de sangre del conjunto GSE40279. No predigo su longevidad, su salud ni el resultado de un tratamiento de rejuvenecimiento. No utilizo los 71 marcadores del reloj original como si hubieran sido seleccionados sin conocer estas personas: aquel reloj se desarrolló con este conjunto.

## Particiones y comparación

Compruebo identificadores, edad y chip de laboratorio antes de fijar las particiones. Si dispongo del chip, lo mantengo entero en entrenamiento, calibración o prueba para evitar repartir un mismo lote entre grupos. Fijo semilla 20261023. Reservo aproximadamente un 20% para prueba y un 15% para calibrar un intervalo de error; el resto sirve para selección y entrenamiento. No modifico la partición para mejorar los resultados ni consulto las etiquetas de prueba para seleccionar marcas.

Comparo con predecir la mediana de edad del entrenamiento. Pruebo regresión ridge con 100 o 1.000 marcas seleccionadas por asociación con la edad y alpha de 10 o 100, en validación de cinco grupos dentro del entrenamiento, manteniendo los chips enteros. La imputación, selección y escala se calculan de nuevo con cada entrenamiento. Elijo por error absoluto medio de validación, antes de abrir la prueba final. No añado modelos tras conocerla.

Solo considero sitios CpG identificados como `cg`; filtro en cada entrenamiento los que tengan más de un 5% de valores ausentes o varianza nula. La imputación usa la media del entrenamiento. Si hay edades o duplicados ambiguos, los documento antes de modelar.

Antes de calcular asociaciones, limito el universo de candidatos a los identificadores cuyo número después de `cg` sea divisible entre 20. Esta regla depende solo del identificador, nunca de la edad. Permite publicar una matriz compacta con todos los candidatos y reproducir también la selección dentro de cada partición. No intento construir el mejor reloj posible usando todo el genoma.

## Evaluación

Mido error absoluto medio y mediano en años, raíz del error cuadrático medio, R² y error por grupos de edad con su tamaño. Estimo la incertidumbre del error medio mediante remuestreo por chip, sin presentarla como una probabilidad de salud. Calibro una banda de predicción del 90% con los errores del grupo de calibración y compruebo su cobertura en prueba. Su validez se limita a muestras comparables, no a cualquier persona o laboratorio.

Como sensibilidad fijada antes de entrenar, compruebo si el modelo tiende a sobreestimar a los más jóvenes e infravalorar a los mayores. No interpreto esos errores como edad biológica. No entreno un modelo por subgrupo a posteriori para corregir el titular.

## Entregables

Conservo la matriz original, las particiones, las métricas y las predicciones de prueba en el análisis. La copia pública incluirá los datos necesarios para reproducir el modelo y todos los pasos de selección. Si selecciono un subconjunto para facilitar la descarga, explico qué permite reproducir y qué requiere la matriz original. No publico datos identificativos privados: los identificadores son los códigos públicos del repositorio.

La aportación editorial es comprobar con un entrenamiento nuevo qué error comete el reloj y en qué edades falla, separando ese resultado de las afirmaciones sobre rejuvenecimiento. El artículo se redacta después de los resultados, sin prometer un error de antemano.
