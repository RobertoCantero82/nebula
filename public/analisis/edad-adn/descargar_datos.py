"""Descargo los datos públicos de metilación y conservo su procedencia."""
from pathlib import Path
import gzip
import hashlib
import json
import time
import requests

raiz=Path(__file__).resolve().parent
base='https://ftp.ncbi.nlm.nih.gov/geo/series/GSE40nnn/GSE40279/'

def descargar(nombre,url):
    # conservo archivos completos y una huella para comprobar las descargas
    carpeta=raiz/'data/raw'
    carpeta.mkdir(parents=True,exist_ok=True)
    ruta=carpeta/nombre
    parcial=ruta.with_suffix(ruta.suffix+'.part')
    if not ruta.exists():
        inicio=time.monotonic()
        with requests.get(url,stream=True,timeout=(30,180)) as respuesta:
            respuesta.raise_for_status()
            total=int(respuesta.headers.get('Content-Length',0))
            escritos=0
            ultimo=inicio
            with parcial.open('wb') as salida:
                for bloque in respuesta.iter_content(4*1024*1024):
                    salida.write(bloque)
                    escritos+=len(bloque)
                    if time.monotonic()-ultimo>15:
                        print(nombre,round(escritos/1024**2,1),'MB de',round(total/1024**2,1),flush=True)
                        ultimo=time.monotonic()
            if total:
                assert escritos==total,(escritos,total)
        parcial.replace(ruta)
    huella=hashlib.file_digest(ruta.open('rb'),'sha256').hexdigest()
    return {'archivo':nombre,'url':url,'bytes':ruta.stat().st_size,'sha256':huella}

if __name__=='__main__':
    # descargo metadatos y valores procesados originales, sin usar un reloj ya entrenado
    archivos=[
        ('GSE40279_sample_key.txt.gz',base+'suppl/GSE40279_sample_key.txt.gz'),
        ('GSE40279_series_matrix.txt.gz',base+'matrix/GSE40279_series_matrix.txt.gz')]
    registros=[]
    for nombre,url in archivos:
        registro=descargar(nombre,url)
        registros.append(registro)
        print('Completado:',nombre,registro['bytes'],flush=True)
        (raiz/'data/fuentes.json').write_text(json.dumps(registros,ensure_ascii=False,indent=2),encoding='utf-8')
