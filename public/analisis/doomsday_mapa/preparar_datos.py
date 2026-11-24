from pathlib import Path
import json, collections, hashlib
BASE = Path.cwd()
if not (BASE / 'pistas.json').exists():
    BASE = Path(__file__).resolve().parent if '__file__' in globals() else BASE
pistas = json.loads((BASE/'pistas.json').read_text(encoding='utf-8'))
fuentes = json.loads((BASE/'fuentes.json').read_text(encoding='utf-8'))
# compruebo las unidades y las referencias antes de contar
ids = {f['id'] for f in fuentes}
assert len({p['id'] for p in pistas}) == len(pistas)
assert all(set(p['fuentes'].split(';')) <= ids for p in pistas)
assert all(p['estado'] in {'detalle_reportado','hipotesis','contexto_oficial'} for p in pistas)
assert all(p['segundo'] is None for p in pistas)
assert all(set(p['depende_de']) <= {q['id'] for q in pistas} for p in pistas)
print(f'Cargo {len(pistas)} afirmaciones y {len(fuentes)} páginas. No tengo un inventario de planos.')

# cuento afirmaciones y compruebo cuánto depende la selección de una sola página
estados = dict(collections.Counter(p['estado'] for p in pistas))
por_fuente = {f['nombre']:sum(f['id'] in p['fuentes'].split(';') for p in pistas) for f in fuentes}
una_fuente = [p['id'] for p in pistas if len(p['fuentes'].split(';')) == 1]
hipotesis = [p for p in pistas if p['estado']=='hipotesis']
grupos = {f['id']:f['grupo_editorial'] for f in fuentes}
grupos_por_pista = {p['id']:len({grupos[f] for f in p['fuentes'].split(';')}) for p in pistas}
solapamientos = []
for i,a in enumerate(fuentes):
    for b in fuentes[i+1:]:
        sa={p['id'] for p in pistas if a['id'] in p['fuentes'].split(';')}
        sb={p['id'] for p in pistas if b['id'] in p['fuentes'].split(';')}
        solapamientos.append({'a':a['nombre'],'b':b['nombre'],'comunes':len(sa & sb),'union':len(sa | sb)})
resultado = {'fecha_corte':'2026-11-24','categoria':'EDA','unidad':'afirmación seleccionada',
    'total_fichas':len(pistas),'estados':estados,'fichas_por_fuente':por_fuente,
    'fichas_con_una_sola_pagina':una_fuente,'hipotesis_con_una_sola_pagina':sum(len(p['fuentes'].split(';'))==1 for p in hipotesis),
    'grupos_editoriales':len(set(grupos.values())),'grupos_por_pista':grupos_por_pista,
    'solapamientos':solapamientos,'revision_visual_completa':0,
    'pistas_con_tiempo_de_subtitulo':sum(p['segundo_transcripcion'] is not None for p in pistas),
    'sha256_pistas':hashlib.sha256((BASE/'pistas.json').read_bytes()).hexdigest()}
(BASE/'resultados.json').write_text(json.dumps(resultado,ensure_ascii=False,indent=2),encoding='utf-8')
print('Recuento por tipo:', estados)
print('Fichas con una sola página:',len(una_fuente), 'de',len(pistas))
print('Hipótesis con una sola página:',resultado['hipotesis_con_una_sola_pagina'],'de',len(hipotesis))
print('Páginas por grupo editorial:',len(fuentes),'páginas /',resultado['grupos_editoriales'],'grupos')
for f in fuentes:
    quedan=[p for p in pistas if set(p['fuentes'].split(';'))-{f['id']}]
    print('Al retirar',f['nombre'],'conservo',len(quedan),'fichas con al menos otra página.')
