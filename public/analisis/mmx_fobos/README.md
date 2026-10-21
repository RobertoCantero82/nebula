# Marte y sus lunas: EDA de campañas de exploración

**Categoría: EDA. Corte: 21 de octubre de 2026.**

Analizo cómo cambia la lectura de la exploración marciana al separar órbita, superficie de Marte y superficie de Fobos. Parto del lanzamiento de MMX y construyo un inventario manual trazable. No entreno un modelo ni genero predicciones.

## Archivos y reproducción

- `analisis_misiones_marte.ipynb`: notebook guiado, ejecutado con sus salidas.
- `misiones_manual.csv`: transcripción de 49 campañas; referencia de entrada.
- `misiones_limpias.csv`: salida de preparación, con enteros anulables y periodo.
- `fuentes.json` y `fuentes/`: enlaces, copias consultadas y huellas SHA-256.
- `resultados.json`, `resumen_periodos.csv`, `sensibilidad.csv` y `misiones_web.json`: salidas reproducibles del notebook.
- `mmx-fobos-misiones-marte.md`: artículo integrado con gráficos en código e interacción.
- `mmx_fobos_portada.png`, `portada_prompt.txt`: portada original y especificación utilizada.
- `linkedin.md`: borrador para copiar, sin publicación autorizada.
- `requirements.txt`: entorno del análisis.

Instalo los requisitos, abro Jupyter en esta carpeta y ejecuto todas las celdas de arriba abajo. Los cálculos solo leen archivos locales y no necesitan acceso a internet. La descarga de fuentes se conserva en `preparar_fuentes.py` para documentar el origen; no es necesaria para repetir el análisis y las páginas pueden cambiar después del corte.

## Unidad, selección y clasificación

Cuento campañas por lanzamiento. Agrupo Mars Polar Lander y Deep Space 2; Phobos-Grunt y Yinghuo-1; el orbitador y Beagle 2; TGO y Schiaparelli; el vehículo y sus auxiliares de superficie. Spirit y Opportunity tienen lanzamientos distintos y son campañas distintas. ESCAPADE (dos naves en un lanzamiento) y MMX son las dos campañas pendientes.

Incluyo 47 campañas de destino principal Marte o sus lunas de 1960 a 2020 más dos lanzamientos de 2025–2026. Excluyo cancelaciones, Zond 3, sobrevuelos con otro destino principal y auxiliares sin campaña propia. No es un recuento universal de objetos enviados al espacio.

Columnas:

| Campo | Significado |
| --- | --- |
| `mision` | Nombre de la campaña agrupada |
| `anio` | Año de lanzamiento |
| `agencia` | Responsable principal; no empleo el campo para clasificar países |
| `salida_tierra` | Abandono físico del entorno terrestre; no implica lanzamiento sin fallos |
| `orbita_prevista` | Al menos un orbitador de Marte previsto |
| `orbita_lograda` | Entrada conseguida; no exige completar la ciencia ni seguir activo |
| `superficie_destino` | Marte, Fobos o ninguna |
| `superficie_operativa` | Trabajo comunicado desde el suelo durante más de un día terrestre |
| `nota` | Evidencia resumida, agrupaciones y resultados parciales |
| `fuentes` | Identificadores separados por `\|`, resueltos en el manifiesto |

Uso 1 y 0 solo cuando el objetivo tiene resultado; un vacío puede indicar que no se pretendía o que sigue pendiente. Mantengo los fallos de lanzamiento en los denominadores. Los conjuntos de órbita y superficie se solapan y no forman un embudo.

## Resultados comprobados

| Objetivo | Lanzamientos 1960–1999 | Lanzamientos 2000–2020 |
| --- | --- | --- |
| Entrar en órbita de Marte | 8 de 18 | 8 de 9 |
| Trabajar en el suelo de Marte | 3 de 10 | 7 de 9 |

Cuatro campañas tienen órbita conseguida y superficie de Marte sin trabajo prolongado: Mars 2, Mars 3, Mars Express y ExoMars 2016. Las tres campañas anteriores destinadas a la superficie de Fobos no llegaron a trabajar allí. Dos no llegaron a orbitar Marte; la tercera se perdió antes de soltar sus módulos.

## Decisiones y límites

La clasificación es editorial, no oficial. El contacto breve de Mars 3 no cumple mi criterio principal; al admitirlo paso a 4/10 en el periodo antiguo. Beagle 2 se trata como llegada física sin comunicación ni trabajo: al admitir la llegada física paso a 8/9 en el periodo reciente. Sputnik 24 figura como aterrizador en NSSDCA y como sobrevuelo en JPL: al excluirlo paso a 3/9 en el periodo antiguo. Kosmos 419 se clasifica como orbitador siguiendo NASA SP-4524. Uso el año y no el día de lanzamiento por diferencias de husos y erratas de las tablas antiguas.

Los fallos de las campañas de Fobos ocurrieron antes de trabajar allí; no los describo como tres impactos sobre la luna. No utilizo los tres antecedentes como muestra para calcular el riesgo de MMX. No establezco causalidad entre época y mejora: cambian agencias, objetivos y recursos. No cuantifico presupuesto, toda la ciencia ni cada subsistema. Una campaña con dos objetivos puede conseguir uno y perder otro. Las copias de las páginas son documentación, no datos nuevos: el CSV exige revisión humana.

## Portada y publicación

Portada generada con la herramienta integrada de ImageGen, consultando visualmente las referencias de Nebula. Es una ilustración editorial, no una imagen científica ni una fotografía de la misión. El prompt completo figura en `portada_prompt.txt`.

Preparar estos archivos no implica publicar el sitio ni enviar el post. El enlace de LinkedIn será público cuando se publique el cambio de la web.
