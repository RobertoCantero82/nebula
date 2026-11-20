from pathlib import Path
import csv
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile

RAIZ = Path(__file__).resolve().parent
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def preparar():
    # leo mi copia original sin modificar las cifras publicadas
    registros, notas = [], {}
    with zipfile.ZipFile(RAIZ / 'netflix_2026_s1.xlsx') as libro:
        cadenas = [''.join(n.itertext()) for n in ET.fromstring(libro.read('xl/sharedStrings.xml')).findall('s:si', NS)]
        for numero, formato in [(1, 'series'), (2, 'peliculas')]:
            filas = ET.fromstring(libro.read(f'xl/worksheets/sheet{numero}.xml')).findall('s:sheetData/s:row', NS)
            notas[formato] = []
            for fila in filas:
                valores = {}
                for celda in fila:
                    v = celda.find('s:v', NS)
                    if v is None:
                        continue
                    valor = cadenas[int(v.text)] if celda.get('t') == 's' else v.text
                    columna = ''.join(c for c in celda.attrib['r'] if c.isalpha())
                    valores[chr(ord(columna)-1)] = valor
                if not valores:
                    continue
                if valores.get('D', '').isdigit() and valores.get('A') and valores.get('A') != 'Title':
                    registros.append(dict(formato=formato, titulo=valores['A'], disponible_global=valores.get('B', ''), estreno=valores.get('C', ''), horas=int(valores['D']), duracion=valores.get('E', ''), visualizaciones=int(valores['F']) if valores.get('F', '').isdigit() else None))
                elif int(fila.attrib['r']) > 6:
                    notas[formato].append(valores)
    assert registros and all(r['horas'] >= 0 for r in registros)
    # conservo filas con el mismo nombre: no presupongo que sean la misma obra
    assert len({tuple(r.values()) for r in registros}) == len(registros)
    with (RAIZ / 'netflix_2026_s1.csv').open('w', encoding='utf-8', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(registros[0]))
        escritor.writeheader()
        escritor.writerows(registros)
    (RAIZ / 'notas_originales.json').write_text(json.dumps(notas, ensure_ascii=False, indent=2), encoding='utf-8')
    return registros

def resumir(registros, metrica='horas'):
    orden = sorted([r for r in registros if r['titulo'] not in {'Other Movies', 'Other Shows'}], key=lambda r: (-r[metrica], r['titulo']))
    total = sum(r[metrica] for r in registros)
    acumulado, mitad = 0, None
    for posicion, registro in enumerate(orden, 1):
        acumulado += registro[metrica]
        if mitad is None and acumulado >= total / 2:
            mitad = posicion
    return dict(registros=len(orden), total=total, horas_otros=sum(r[metrica] for r in registros if r['titulo'] in {'Other Movies', 'Other Shows'}), mitad=mitad, porcentaje_titulos_mitad=mitad/len(orden)*100,
                cuotas={str(n):sum(r[metrica] for r in orden[:n])/total*100 for n in [10, 100, 1000]},
                top=[{k:r[k] for k in ['titulo','formato',metrica]} for r in orden[:10]])

if __name__ == '__main__':
    registros = preparar()
    resultados = {grupo:resumir([r for r in registros if grupo=='conjunto' or r['formato']==grupo]) for grupo in ['conjunto','series','peliculas']}
    resultados['sensibilidad_visualizaciones'] = {grupo:resumir([r for r in registros if r['formato']==grupo and r['visualizaciones'] is not None], 'visualizaciones') for grupo in ['series','peliculas']}
    resultados['sha256_original'] = hashlib.sha256((RAIZ/'netflix_2026_s1.xlsx').read_bytes()).hexdigest()
    (RAIZ/'resultados.json').write_text(json.dumps(resultados,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(resultados,ensure_ascii=True,indent=2))
