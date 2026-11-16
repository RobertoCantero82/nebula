# ejecuto cada celda en orden y conservo sus salidas sin dependencias externas
from pathlib import Path
import contextlib
import io
import json
import re
from html import escape

raiz = Path.cwd()
secciones = json.loads((raiz / "secciones_notebook.json").read_text(encoding="utf-8"))
celdas = []
espacio = {"__name__": "__main__"}
contador = 0
for seccion in secciones:
    texto = "# " + seccion["title"] + "\n\n" + seccion["text"]
    celdas.append({"cell_type": "markdown", "metadata": {}, "source": texto.splitlines(True)})
    if "code" in seccion:
        codigo = seccion["code"].replace("# expreso los límites aproximados en UTC", "# expreso los límites aproximados en utc")
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            exec(compile(codigo, "celda_" + str(contador + 1), "exec"), espacio)
        contador += 1
        celdas.append({"cell_type": "code", "metadata": {}, "source": codigo.splitlines(True), "execution_count": contador, "outputs": [{"output_type": "stream", "name": "stdout", "text": salida.getvalue().splitlines(True)}]})
        print("Celda", contador, "correcta")
notebook = {"cells": celdas, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.12"}, "nebula": {"categoria": "EDA", "ejecucion": "celdas ejecutadas secuencialmente con Python; salidas capturadas", "fecha_corte_utc": "2026-11-16T00:00:00Z"}}, "nbformat": 4, "nbformat_minor": 4}
(raiz / "analisis_voyager_acercamiento.ipynb").write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")

def formato(texto):
    # convierto el relato a html y mantengo el código dentro de desplegables
    texto = escape(texto)
    texto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(chr(96) + r"([^" + chr(96) + r"]+)" + chr(96), r"<code>\1</code>", texto)
    texto = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', texto)
    bloques = []
    for parrafo in texto.split("\n\n"):
        if parrafo.startswith("!["):
            bloques.append((raiz / "resultados" / "variacion_distancia.svg").read_text(encoding="utf-8"))
        elif parrafo.startswith("### "):
            bloques.append("<h3>" + parrafo[4:] + "</h3>")
        elif parrafo.startswith("## "):
            bloques.append("<h2>" + parrafo[3:] + "</h2>")
        elif parrafo.startswith("# "):
            bloques.append("<h1>" + parrafo[2:] + "</h1>")
        else:
            bloques.append("<p>" + parrafo.replace("\n", "<br>") + "</p>")
    return "\n".join(bloques)

cuerpo = []
for celda in celdas:
    if celda["cell_type"] == "markdown":
        cuerpo.append(formato("".join(celda["source"])))
    else:
        cuerpo.append('<details><summary>Ver código ejecutado</summary><pre>' + escape("".join(celda["source"])) + '</pre></details>')
        cuerpo.append('<pre class="salida">' + escape("".join(celda["outputs"][0]["text"])) + '</pre>')
estilo = 'body{max-width:960px;margin:auto;padding:30px 22px;background:#faf8f2;color:#172342;font:17px/1.65 system-ui}h1{font-size:clamp(28px,5vw,46px);line-height:1.15}h2{margin-top:40px}a{color:#355bc6}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.6 monospace;background:#edf0f6;padding:16px;border-radius:8px}svg{width:100%;height:auto}summary{cursor:pointer}code{font-size:.9em}'
(raiz / "analisis_voyager_acercamiento.html").write_text('<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Voyager 1 · EDA de Nebula</title><style>'+estilo+'</style><body>'+''.join(cuerpo)+'</body></html>', encoding="utf-8")
print("Notebook ejecutado y versión HTML generada.")
