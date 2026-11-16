# descargo las cuatro consultas originales con parámetros fijos y sin modificar su contenido
from pathlib import Path
import json
import urllib.request

raiz = Path(__file__).resolve().parent
consultas = json.loads((raiz / "fuentes" / "consultas.json").read_text(encoding="utf-8"))
for nombre, url in consultas["archivos"].items():
    with urllib.request.urlopen(url, timeout=120) as respuesta:
        datos = respuesta.read()
    objeto = json.loads(datos)
    if "result" not in objeto or "$$SOE" not in objeto["result"]:
        raise RuntimeError(f"respuesta de horizons no válida para {nombre}")
    (raiz / "fuentes" / nombre).write_bytes(datos)
    print(nombre, len(datos), "bytes")
