from pathlib import Path
import sys
import os
base=Path(__file__).resolve().parent
deps=base.parent/'voyager_deps'
if deps.exists():
    sys.path.insert(0,str(deps))
    os.environ['PYTHONPATH']=str(deps)
os.environ['MPLBACKEND']='module://matplotlib_inline.backend_inline'
os.environ['MPLCONFIGDIR']=str(base/'.matplotlib')
os.environ['IPYTHONDIR']=str(base/'.ipython')
os.environ['JUPYTER_RUNTIME_DIR']=str(base/'.runtime')
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpec
print('Dependencias cargadas',flush=True)
n=nbformat.read(base/'analisis_voyager.ipynb',as_version=4)
print('Notebook leído',flush=True)
km=KernelManager(kernel_name='python3')
print('Gestor creado',flush=True)
km._kernel_spec=KernelSpec(argv=[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],display_name='Python 3',language='python')
print('Kernel configurado',flush=True)
NotebookClient(n,km=km,timeout=120,resources={'metadata':{'path':str(base)}},on_cell_start=lambda cell,cell_index:print('Celda',cell_index,flush=True)).execute()
nbformat.validate(n)
nbformat.write(n,base/'analisis_voyager.ipynb')
for c in n.cells:
    for o in c.get('outputs',[]):
        if o.output_type=='stream':print(o.text)
print('Notebook ejecutado y validado')
