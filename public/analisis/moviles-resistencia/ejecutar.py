"""Ejecuto la preparación y el EDA con el intérprete del entorno activo."""
from pathlib import Path
import json
import os
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

# preparo un núcleo dentro del proyecto sin modificar el registro del usuario
raiz = Path(__file__).resolve().parent
carpeta_nucleos = raiz / 'work' / 'kernels'
carpeta_nucleo = carpeta_nucleos / 'nebula'
carpeta_nucleo.mkdir(parents=True, exist_ok=True)
entorno = os.environ.copy()
entorno['MPLCONFIGDIR'] = str(raiz / 'work' / 'matplotlib')
especificacion = {'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
                 'display_name':'Nebula local','language':'python','env':entorno}
(carpeta_nucleo / 'kernel.json').write_text(json.dumps(especificacion),encoding='utf-8')
for nombre in ['01_preparacion_moviles.ipynb','02_eda_moviles.ipynb']:
    # ejecuto cada cuaderno en orden y solo guardo una ejecución sin errores
    gestor = KernelManager(kernel_name='nebula', kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(carpeta_nucleos)]))
    cuaderno = nbformat.read(raiz / nombre,as_version=4)
    NotebookClient(cuaderno,km=gestor,timeout=180,resources={'metadata':{'path':str(raiz)}}).execute()
    nbformat.write(cuaderno,raiz / nombre)
    print(nombre,'ejecutado')
