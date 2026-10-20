# Los móviles de ahora no aguantan nada

**Categoría: EDA (análisis exploratorio de datos).** Consulta de fuentes: 20 de octubre de 2026. No genero predicciones.

## Pregunta y aportación

Compruebo qué parte de la frase puede contrastarse desde el Nokia 3310 de 2000 hasta los smartphones recientes. Separo cuatro sentidos de «aguantar»: autonomía de una carga, envejecimiento de la batería, facilidad de sustituirla y resistencia a golpes. No invento una puntuación general.

La aportación de Nebula consiste en comparar tres familias consigo mismas bajo una prueba de autonomía con una referencia común, comprobar dos cortes intermedios y distinguir mediciones independientes de máximos anunciados o especificaciones de diseño.

## Cómo reproduzco el análisis

1. Utilizo Python 3.12 y creo un entorno virtual.
2. Instalo las dependencias con `python -m pip install -r requirements.txt`.
3. Descomprimo el paquete conservando su estructura.
4. Ejecuto `python ejecutar.py`. Se ejecutan primero `01_preparacion_moviles.ipynb` y después `02_eda_moviles.ipynb`, desde esta carpeta.

También puedo abrir y ejecutar ambos cuadernos en Jupyter en ese orden, con esta carpeta como directorio de trabajo. No necesito una clave de EPREL ni conexión a las páginas originales para reproducir las cifras. Los extractos mínimos necesarios están incluidos. Instalar dependencias sí requiere conexión si no están instaladas.

`ejecutar.py` utiliza el intérprete desde el que se lanza y crea una especificación de núcleo dentro de `work/kernels`; no registra un núcleo en el perfil del usuario. En un entorno restringido, el proceso de Jupyter necesita permiso para iniciar su núcleo local.

## Datos y selección

Una fila de `data/processed/autonomia.csv` representa un modelo concreto probado cuando era nuevo. Selecciono doce modelos por familia y fecha: iPhone 6s, XR, 13 y 17; Galaxy S6, S9, S21 y S25; Moto G (2015), G6, G30 y G86. Los cortes son 2015, 2018, 2021 y 2025. Excluyo variantes Pro, Max, Plus, Ultra y Power para no escoger sistemáticamente los teléfonos con más batería.

2015 es el inicio de la versión wifi v1.3 de Notebookcheck; 2025 es el último año natural completo en la fecha de consulta. No afirmo estar comparando todos los modelos actuales de 2026. Los modelos no tienen idéntico tamaño, precio ni prestaciones; el XR tiene una pantalla mayor que el 6s y los Moto G no son sucesores de idéntica gama. No es una muestra aleatoria ni representativa de las ventas o del mercado. No hago una media mundial de duración.

Extraigo los minutos exactos de las filas de navegación, no las horas decimales redondeadas de las tablas comparativas. Conservo doce mediciones wifi y once de vídeo. No imputo el vídeo del Galaxy S6, ausente en la tabla conservada. El diccionario de columnas está en `diccionario_datos.csv`.

## Comparabilidad

- **Navegación wifi:** misma versión v1.3 y brillo de referencia de unos 150 nits. La fuente documenta un cambio de página cada 30 segundos. No garantiza un laboratorio idéntico a lo largo de diez años: cambian navegador, sistema operativo, equipo de red y entorno de prueba. Comparo el conjunto teléfono-software y no atribuyo causalidad a la batería o al procesador.
- **Vídeo:** contrasto las parejas con reproducción local H.264 1080p y brillo de referencia de 150 nits. No sumo esas horas a las de wifi.
- **Nokia 3310:** el comunicado original anuncia hasta 260 horas en espera y 4,5 horas de conversación con batería estándar. Son máximos anunciados; no resultados de navegación ni de uso mixto. No calculo un multiplicador frente a smartphones.
- **Ciclos:** Apple publica objetivos de diseño al 80 % de capacidad: 500 ciclos para iPhone 14 y anteriores y 1000 para iPhone 15 y posteriores, en condiciones ideales. Comparo lo declarado, no resultados longitudinales propios. No demuestro que los protocolos completos sean idénticos ni convierto ciclos en años.
- **Cambio de batería:** comparo instrucciones concretas del Nokia y del Fairphone y la descripción de batería no extraíble del S6; no cronometro reparaciones ni generalizo a todos los modelos de una época.
- **Caídas:** no encuentro una serie histórica homogénea que permita un ganador. Una advertencia del manual no mide resistencia. No trato vídeos de caídas aisladas como una prueba estadística.

## Resultados calculados

En los pares wifi de 2015 frente a 2025 encuentro +144,512 % para iPhone, +127,789 % para Galaxy S y +97,338 % para Moto G. Es correcto redondear a +145 %, +128 % y +97 %. No digo que los tres dupliquen. El Moto G86 queda 31 minutos por debajo del G30; el S9 registra un minuto menos que el S6, sin que pueda interpretar ese minuto como una diferencia significativa.

La comprobación de vídeo da mejoras en las dos familias con ambos extremos disponibles. Son observaciones adicionales de la misma selección, no una muestra independiente del mercado. No calculo intervalos ni pruebas de significación: no tengo repeticiones de cada ensayo.

No conozco años de supervivencia real, tasas de avería, costes históricos homogéneos de reparación ni experiencias representativas de usuarios. Tampoco equiparo una promesa de actualizaciones con años observados de vida útil.

## Fuentes y archivo

- [Notebookcheck: procedimiento de prueba](https://www.notebookcheck.net/How-does-Notebookcheck-test-laptops-and-smartphones-A-behind-the-scenes-look-into-our-review-process.15394.0.html). Las doce reseñas están enlazadas individualmente en `fuentes.json` y en `autonomia.csv`.
- [Nokia Oyj: comunicado del 1 de septiembre de 2000](https://www.globenewswire.com/news-release/2000/09/01/1845525/0/en/Nokia-introduces-mobile-chat-with-the-Nokia-3310.html).
- [Nokia: manual original, copia conservada por Manuallib](https://www.manuallib.com/download/NOKIA-3310-USER-GUIDE.PDF). Páginas impresas 23-24 (batería extraíble), 99 (desgaste) y 101 (golpes); equivalen a páginas PDF 23-24, 99 y 101, contando la primera como 1.
- [Apple: batería y rendimiento](https://support.apple.com/es-es/106348).
- [Fairphone: sustitución de batería Gen. 6](https://support.fairphone.com/hc/en-us/articles/37412807551634-How-to-replace-the-battery-in-The-Fairphone-Gen-6).

También reviso y descarto como escalas históricas únicas el [cambio de test de GSMArena en 2023](https://www.gsmarena.com/introducing_gsmarena_battery_test_v2-news-60397.php), los [criterios cambiantes de iFixit](https://www.ifixit.com/repairability/smartphone-repairability-scores) y las [etiquetas actuales de EPREL](https://energy-efficient-products.ec.europa.eu/product-list/smartphones-and-tablets_en). No afirmo haber descargado todo EPREL: su consulta directa de catálogo devolvió 403 y no es necesaria para este análisis histórico.

La descarga HTTP directa de Notebookcheck, del comunicado de Nokia y de la copia del manual devolvió 403. Accedí a su contenido mediante el buscador web y conservé los extractos numéricos o documentales mínimos, las URLs y la fecha de consulta. Los archivos `.txt` son extractos, no copias HTML completas. Las huellas en `data/processed/huellas.json` identifican esta copia; no autentican por sí solas el contenido externo.

## Estructura

- `01_preparacion_moviles.ipynb`: procedencia, extracción, limpieza y calidad, con salidas ejecutadas.
- `02_eda_moviles.ipynb`: comparaciones, comprobaciones y límites, con salidas ejecutadas.
- `preparar_datos.py`: extracción repetible sin conexión a fuentes.
- `data/raw/*.txt`: evidencia mínima utilizada.
- `data/processed/`: tablas limpias y huellas.
- `resultados/`: cifras calculadas, tablas auxiliares y gráfico vectorial.
- `fuentes.json`, `diccionario_datos.csv`, `requirements.txt`, `ejecutar.py`: reproducción y trazabilidad.

Los gráficos de la web se generan mediante código HTML/CSS y los doce resultados, no mediante imágenes del notebook. La portada es una acuarela generada, no una fotografía ni evidencia de una prueba física.
