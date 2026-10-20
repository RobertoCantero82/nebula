"""Preparo las tablas del EDA a partir de las filas originales conservadas."""
from pathlib import Path
import hashlib
import json
import re
import pandas as pd


def preparar(raiz):
    # leo el manifiesto para conservar el vínculo entre cada cifra y su fuente
    raiz = Path(raiz)
    fuentes = json.loads((raiz / 'fuentes.json').read_text(encoding='utf-8'))
    filas = []
    for fuente in fuentes:
        if not fuente.get('modelo'):
            continue
        texto = (raiz / fuente['archivo']).read_text(encoding='utf-8')
        assert 'WiFi v1.3' in texto, fuente['clave']
        wifi = re.search(r'WiFi Websurfing[^\n]*?\|\s*\|\s*(\d+)h\s*(\d+)min', texto)
        video = re.search(r'Big Buck Bunny H\.264 1080p[^\n]*?\|\s*\|\s*(\d+)h\s*(\d+)min', texto)
        assert wifi, f"no encuentro las horas y los minutos de {fuente['clave']}"
        fila = {clave: fuente[clave] for clave in ['clave', 'modelo', 'anio', 'familia', 'url']}
        fila.update(wifi_original=f'{wifi[1]}h {wifi[2]}min', wifi_minutos=int(wifi[1])*60+int(wifi[2]),
                    video_original=f'{video[1]}h {video[2]}min' if video else None,
                    video_minutos=int(video[1])*60+int(video[2]) if video else None,
                    protocolo='Notebookcheck WiFi v1.3; 150 cd/m²', consulta='2026-10-20')
        filas.append(fila)
    # compruebo las doce observaciones y convierto los minutos en horas decimales
    datos = pd.DataFrame(filas).sort_values(['familia', 'anio']).reset_index(drop=True)
    assert len(datos) == 12 and not datos.duplicated(['familia','anio']).any()
    assert datos['wifi_minutos'].between(60, 3000).all()
    assert set(datos['anio']) == {2015, 2018, 2021, 2025}
    datos['wifi_horas'] = datos['wifi_minutos'] / 60
    datos['video_horas'] = datos['video_minutos'] / 60
    procesados = raiz / 'data' / 'processed'
    procesados.mkdir(parents=True, exist_ok=True)
    datos.to_csv(procesados / 'autonomia.csv', index=False, encoding='utf-8')
    # guardo por separado declaraciones y documentos que no comparten prueba
    declaraciones = pd.DataFrame([
        dict(modelo='Nokia 3310 (2000)', magnitud='espera', valor=260, unidad='horas', tipo='máximo anunciado', fuente='nokia_comunicado.txt'),
        dict(modelo='Nokia 3310 (2000)', magnitud='conversación', valor=4.5, unidad='horas', tipo='máximo anunciado', fuente='nokia_comunicado.txt'),
        dict(modelo='iPhone 14 y anteriores', magnitud='ciclos hasta conservar el 80 %', valor=500, unidad='ciclos', tipo='objetivo de diseño en condiciones ideales', fuente='apple_ciclos.txt'),
        dict(modelo='iPhone 15 y posteriores', magnitud='ciclos hasta conservar el 80 %', valor=1000, unidad='ciclos', tipo='objetivo de diseño en condiciones ideales', fuente='apple_ciclos.txt'),
    ])
    declaraciones.to_csv(procesados / 'declaraciones.csv', index=False, encoding='utf-8')
    # calculo las huellas de los extractos para detectar cambios de la copia de trabajo
    huellas = {str(p.relative_to(raiz)).replace('\\','/'): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted((raiz / 'data' / 'raw').glob('*.txt'))}
    (procesados / 'huellas.json').write_text(json.dumps(huellas, indent=2), encoding='utf-8')
    return datos, declaraciones


if __name__ == '__main__':
    # preparo los datos desde la carpeta del proyecto y muestro el tamaño final
    datos, declaraciones = preparar(Path(__file__).resolve().parent)
    print(f'{len(datos)} móviles; {len(declaraciones)} declaraciones separadas')
