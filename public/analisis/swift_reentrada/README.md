# Predicción retrospectiva de la reentrada de Swift

Proyecto de machine learning de Nebula sobre la reentrada del observatorio Swift el 4 de noviembre de 2026 a las 12:39 UTC.

## Archivos

- `analisis_swift_reentrada.ipynb`: notebook reproducible y ejecutado.
- `datos/sat000028485.json`: historial orbital TLE original solicitado a CelesTrak para NORAD 28485.
- `explorar_modelo.py`: prueba técnica de modelos y cortes temporales.

## Método

El análisis conserva el orden temporal. Entrena hasta el 31 de agosto de 2026, valida entre el 1 de septiembre y el 15 de octubre y reserva las últimas 18 observaciones como prueba. Compara una regresión lineal de referencia con una relación de potencia entre altura aproximada y horas restantes.

## Fuentes

- CelesTrak Historical Archives: https://celestrak.org/norad/archives/
- NASA CCMC Swift Challenge: https://ccmc.gsfc.nasa.gov/challenges/swift-challenge/
- NASA Science: https://science.nasa.gov/blogs/swift/

Los TLE son aproximaciones orbitales redistribuidas por CelesTrak a partir de datos de USSPACECOM. El modelo es un ejercicio retrospectivo sobre un solo satélite y no debe utilizarse para decisiones de seguridad.
