from pathlib import Path
import json, csv

# localizo mi carpeta al abrir el cuaderno desde ella
base = Path.cwd()
registros = json.loads((base / 'registro_manual.json').read_text(encoding='utf-8'))
fuentes = json.loads((base / 'fuentes.json').read_text(encoding='utf-8'))
ids_fuentes = {f['id'] for f in fuentes}
assert len({r['id'] for r in registros}) == len(registros)
assert len({r['titulo'].casefold() for r in registros}) == len(registros)
for registro in registros:
    assert set(registro['fuentes']) <= ids_fuentes
    assert registro['estado'] in {'declarada', 'reportada', 'pista'}
    assert registro['detalle'] and registro['limite']
with (base / 'referencias.csv').open('w', newline='', encoding='utf-8') as archivo:
    tabla = csv.DictWriter(archivo, fieldnames=list(registros[0]))
    tabla.writeheader()
    for registro in registros:
        tabla.writerow({**registro, 'fuentes': ';'.join(registro['fuentes'])})
(base / 'referencias.json').write_text(json.dumps(registros, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'He preparado {len(registros)} fichas y {len(fuentes)} fuentes.')
