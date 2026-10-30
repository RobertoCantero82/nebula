"""Descargo la respuesta original del catálogo Fermi GBM de NASA."""

from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

consulta = "select trigger_name,name,ra,dec,lii,bii,trigger_time,t90,t90_error,error_radius from fermigbrst"
url = "https://heasarc.gsfc.nasa.gov/xamin/vo/tap/sync?" + urlencode({"REQUEST": "doQuery", "LANG": "ADQL", "QUERY": consulta})
destino = Path("fermi_gbm_catalogo_raw.xml")

# conservo la respuesta binaria original para que la preparación sea auditable
with urlopen(url, timeout=120) as respuesta:
    destino.write_bytes(respuesta.read())

print(destino.resolve())
