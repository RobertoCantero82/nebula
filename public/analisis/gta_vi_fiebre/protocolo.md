# Mi protocolo previo a los cálculos

Fecha de corte: 23 de noviembre de 2026. Autor: Roberto Cantero · Nebula.

Mi pregunta: ¿puedo anticipar las consultas de la página inglesa de GTA VI durante sus semanas tercera y quinta usando solo los primeros cuatro días desde el estreno?

Mido consultas de Wikipedia en inglés, all-access, agent=user, días UTC. No mido jugadores, ventas, búsquedas en Google ni personas distintas. Uso una muestra de conveniencia de grandes videojuegos de pago con lanzamiento entre 2015 y 2023. No es una muestra representativa de toda la industria. No trato los días como juegos independientes.

Recojo 43 días por juego: -7 a +35, ambos incluidos. Día 0 es la fecha de lanzamiento indicada. Las variables del modelo solo usan -7 a +3. Mi objetivo es la media diaria de +14 a +20 y de +28 a +34, dividida entre las consultas del día 0. Comparo semanas completas para suavizar el efecto del día de la semana. Para GTA VI, estrenado el 19 de noviembre, corresponden al 3–9 y al 17–23 de diciembre de 2026. No equivale a predecir el día en que se acaba el interés.

Separo por fecha: entrenamiento hasta 2019; validación en 2020–2021; prueba final en 2022–2023. No selecciono juegos por su curva posterior. Excluyo Dark Souls III por su lanzamiento japonés anterior al internacional y Baldur's Gate 3 por un problema observable de cobertura del título: las primeras visitas son casi nulas y saltan después. Conservo ambas series y sus exclusiones.

Mis referencias sencillas son mantener las visitas del día +3 y aplicar la mediana de retención de los juegos de entrenamiento. Pruebo regresión ridge sobre el logaritmo de retención con dos variables: log(visitas +3 / visitas 0) y log(media -7 a -1 / visitas 0). Comparo penalizaciones 1 y 10 solo en validación, con estandarización aprendida en entrenamiento. Elijo según error absoluto medio de los logaritmos, promediando los dos horizontes. Después reajusto con entrenamiento + validación y evalúo una vez en prueba. Informo también error absoluto en puntos de retención y resultados por juego. No reutilizo la prueba para cambiar el modelo.

Si no mejora la referencia de la mediana en la prueba, no presento su salida como una predicción fiable: documento el intento y el límite. Si mejora, la presento como experimental, dado el tamaño pequeño de la prueba. Un intervalo empírico basado en errores históricos solo puede describirse como orientativo: no prometo cobertura garantizada en un fenómeno fuera de muestra como GTA VI.

Conservo datos, fechas, procedencia, código, notebooks y resultados. Compruebo duplicados, integridad de días, fechas, positividad y que no se usa información posterior al día +3 como entrada. Limitaciones: títulos/redirecciones, cambios en Wikipedia, muestra pequeña elegida a mano, diferencias de plataformas, lanzamientos regionales, pandemia, noticias y premios. GTA V de 2013 queda fuera porque la serie diaria de este servicio comienza en 2015.
