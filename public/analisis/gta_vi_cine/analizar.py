from pathlib import Path
from collections import Counter
import json, csv

# leo mis datos preparados y separo las clases de relación
base = Path.cwd()
with (base / 'referencias.csv').open(encoding='utf-8', newline='') as archivo:
    filas = list(csv.DictReader(archivo))
estados = Counter(f['estado'] for f in filas)
formatos = Counter(f['formato'] for f in filas)
una_fuente = sum(len(f['fuentes'].split(';')) == 1 for f in filas)
referentes_generales = sum(f['relacion'] == 'Referente del estudio' for f in filas)
resultado = {'total_fichas': len(filas), 'por_estado': dict(estados), 'por_formato': dict(formatos), 'fichas_una_pagina': una_fuente, 'referentes_generales_del_estudio': referentes_generales, 'revision_visual_completa_nebula': 0}
assert sum(estados.values()) == len(filas)
assert sum(formatos.values()) == len(filas)
print(json.dumps(resultado, ensure_ascii=False, indent=2))
(base / 'resultados.json').write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding='utf-8')

# hago una comprobación de sensibilidad: retiro mis pistas más débiles
sin_pistas = [f for f in filas if f['estado'] != 'pista']
print(f'Al retirar las pistas pendientes quedan {len(sin_pistas)} fichas; tampoco son un total de secretos confirmados.')
print('Contar páginas no demuestra observaciones independientes: las guías pueden citar el mismo clip.')
