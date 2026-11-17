# Libro de códigos · EDA documental

Autor: Roberto Cantero · Nebula · consulta: 17 de noviembre de 2026.

Unidad: una película de las 25 entregas oficiales estrenadas entre 1962 y 2021. Conservo al menos una prueba por película positiva; no cuento todos los episodios.

No he visto ni cronometrado las 25 películas para este trabajo. Codifico manualmente sinopsis documentales consultadas, principalmente Wikipedia en inglés, y corroboraciones de 007.com, MI6-HQ y Forbes. No presento las sinopsis como guiones ni las fuentes secundarias como originales. Los índices de 007.com recuperados en búsqueda no estuvieron siempre accesibles por apertura directa; lo indico en el CSV.

## Categorías

- `captura`: un antagonista reduce, traslada, encierra, inmoviliza o mantiene a Bond bajo custodia contra su libertad de movimiento. Incluyo la retención a punta de pistola cuando la fuente describe cautiverio, traslado o reducción; no un simple intercambio de disparos. Una captura cuenta una vez por película, aunque haya más. No cuento la custodia ordinaria de sus superiores o aliados.
- `encierro_trampa`: encierro deliberado para matarlo, sin custodia posterior. Distingo el barco de Sin tiempo para morir de una captura con vigilancia continuada.
- `no_documentada`: las fuentes consultadas no acreditan un caso conforme a la definición. Es un valor desconocido, no un cero y no prueba de ausencia.
- `acceso_voluntario`: identifico Skyfall como caso contextual porque Bond acepta viajar para conocer al enemigo. No deduzco que quisiera ser detenido. En Spectre utilizo el secuestro de Londres, independiente de su visita voluntaria al Sahara.

## Tres lecturas

1. Criterio principal: presencia documentada de `captura`.
2. Conservador: excluyo además Skyfall. Es una comprobación de sensibilidad, no una clasificación de intenciones de todas las escenas.
3. Ampliado: añado el `encierro_trampa` de Sin tiempo para morir.

Todos los porcentajes usan 25 películas como denominador y son mínimos documentados. No son probabilidades, tasas por misión ni porcentajes de incompetencia.

## Variables que no utilizo

No creo un índice de incompetencia. No cuento identidades expuestas, persecuciones, muertos o daños sin una revisión completa. Los rescates son seis ejemplos documentados y no una muestra representativa: no calculo su frecuencia. No evalúo el éxito global de cada misión. No ordeno a los actores por capacidad.

## Revisión y límites

Una sola codificación, sin segunda persona evaluadora ni acuerdo entre codificadores. Las sinopsis omiten escenas y pueden contener errores. Comparo los tres criterios para hacer visible una decisión discutible. La película es la fuente primaria que permitiría ampliar y auditar los registros con marcas de tiempo; esa revisión queda fuera del trabajo realizado. Los resultados no evalúan a agentes reales ni acreditan que Bond sea mal profesional.
