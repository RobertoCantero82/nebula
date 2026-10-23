"""Preparo una matriz pública sin consultar asociaciones con la edad."""
from pathlib import Path
import csv
import gzip
import json
import re
import numpy as np
import pandas as pd

raiz = Path(__file__).resolve().parent

def preparar():
    destino = raiz / 'data'
    metadatos = {}
    caracteristicas = {}
    marcadores, valores = [], []
    with gzip.open(destino / 'raw/GSE40279_series_matrix.txt.gz', 'rt') as entrada:
        for fila in csv.reader(entrada, delimiter='\t'):
            if not fila:
                continue
            if fila[0] == '!series_matrix_table_begin':
                columnas = next(csv.reader([next(entrada)], delimiter='\t'))[1:]
                break
            if fila[0] == '!Sample_characteristics_ch1':
                nombre = fila[1].split(': ', 1)[0]
                caracteristicas[nombre] = [v.split(': ', 1)[1] for v in fila[1:]]
            elif fila[0].startswith('!Sample_'):
                metadatos[fila[0]] = fila[1:]
        for numero, linea in enumerate(entrada):
            if linea.startswith('!series_matrix_table_end'):
                break
            identificador, datos = linea.rstrip().split('\t', 1)
            identificador = identificador.strip('"')
            if re.fullmatch(r'cg\d+', identificador) and int(identificador[2:]) % 20 == 0:
                vector = np.fromstring(datos.replace('NA', 'nan'), sep='\t', dtype=np.float32)
                assert len(vector) == len(columnas)
                marcadores.append(identificador)
                valores.append(vector)
            if numero % 100000 == 0:
                print('Filas leídas:', numero, 'candidatos:', len(marcadores), flush=True)
    claves = pd.read_csv(destino / 'raw/GSE40279_sample_key.txt.gz', sep='\t', header=None,
                        names=['orden', 'persona', 'posicion'], dtype={'persona': str})
    tabla = pd.DataFrame({'muestra': metadatos['!Sample_geo_accession'],
                          'persona': [re.search(r'(\d+)$', v).group(1) for v in metadatos['!Sample_title']],
                          'edad': np.array(caracteristicas['age (y)'], dtype=int),
                          'procedencia': caracteristicas['source'],
                          'placa': caracteristicas['plate'],
                          'sexo': caracteristicas['gender']})
    tabla = tabla.merge(claves[['persona', 'posicion']], on='persona', validate='one_to_one', sort=False)
    tabla['chip'] = tabla['posicion'].str.split('_').str[0]
    assert tabla['muestra'].tolist() == columnas
    assert len(tabla) == 656 and tabla['persona'].is_unique
    assert tabla.notna().all().all() and len(set(marcadores)) == len(marcadores)
    matriz = np.stack(valores, axis=1)
    assert ((matriz >= 0) | np.isnan(matriz)).all() and ((matriz <= 1) | np.isnan(matriz)).all()
    np.savez_compressed(destino / 'metilacion_candidatos.npz', x=matriz, marcadores=np.array(marcadores))
    tabla.to_csv(destino / 'muestras.csv', index=False)
    resumen = {'personas': len(tabla), 'candidatos': len(marcadores), 'chips': tabla['chip'].nunique(),
               'edad_minima': int(tabla.edad.min()), 'edad_maxima': int(tabla.edad.max()),
               'ausentes': int(np.isnan(matriz).sum()), 'regla': 'identificador cg divisible entre 20'}
    (destino / 'preparacion.json').write_text(json.dumps(resumen, indent=2, ensure_ascii=False), encoding='utf-8')
    print(resumen)

if __name__ == '__main__':
    preparar()
