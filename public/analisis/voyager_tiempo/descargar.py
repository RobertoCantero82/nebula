from pathlib import Path
import urllib.request
import urllib.parse
import json
import hashlib
import datetime
import csv
import io
import subprocess

base = Path(__file__).resolve().parent
raw = base / 'fuentes'
raw.mkdir(exist_ok=True)
manifest = []

def guardar(nombre, url):
    path = raw / nombre
    if not path.exists():
        comando = "Invoke-WebRequest -Uri '" + url.replace("'", "''") + "' -OutFile '" + str(path).replace("'", "''") + "' -TimeoutSec 90"
        subprocess.run(['powershell.exe','-NoProfile','-Command',comando],check=True)
    manifest.append({'archivo': 'fuentes/' + nombre, 'url': url, 'consulta_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    return path.read_text(encoding='utf-8')

def consulta(nombre, codigo, inicio, fin, paso='1 d', centro='500@399'):
    params = {'format':'json','COMMAND':"'"+codigo+"'", 'EPHEM_TYPE':"'VECTORS'",'CENTER':"'"+centro+"'",'START_TIME':"'"+inicio+"'",'STOP_TIME':"'"+fin+"'",'STEP_SIZE':"'"+paso+"'",'OUT_UNITS':"'KM-S'",'VEC_TABLE':"'3'",'VEC_CORR':"'NONE'",'CSV_FORMAT':"'YES'",'TIME_TYPE':"'UT'"}
    url = 'https://ssd.jpl.nasa.gov/api/horizons.api?' + urllib.parse.urlencode(params)
    data = json.loads(guardar(nombre+'.json',url))
    result = data.get('result','')
    if '$$SOE' not in result:
        raise RuntimeError(result[:2000])
    text = result.split('$$SOE')[1].split('$$EOE')[0].strip()
    rows = []
    for row in csv.reader(io.StringIO(text)):
        if not row: continue
        rows.append({'fecha_utc': row[1].strip().replace('A.D. ',''), 'distancia_km': float(row[9]), 'segundos_ida':float(row[8]), 'velocidad_radial_km_s':float(row[10])})
    print(nombre, len(rows), rows[-1], flush=True)
    return rows

targets = [('Luna','301'),('Marte','499'),('Júpiter','599'),('New Horizons','-98'),('Voyager 2','-32'),('Voyager 1','-31')]
filas = []
for nombre,codigo in targets:
    row = consulta('actual_'+codigo.replace('-','m'),codigo,'2026-10-22','2026-10-23')[0]
    filas.append({'destino':nombre,'codigo':codigo,**row})
for name, rows in [('comparacion',filas),('historia',consulta('historia','-31','1977-09-06','2026-10-23','30 d')),('diario_2026',consulta('diario_2026','-31','2026-01-01','2026-10-23')),('diario_sol_2026',consulta('diario_sol_2026','-31','2026-01-01','2026-10-23',centro='500@10'))]:
    with (base/(name+'.csv')).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for name,url in [('hito.html','https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/'),('faq.html','https://science.nasa.gov/mission/voyager/frequently-asked-questions/'),('horizons_api.html','https://ssd-api.jpl.nasa.gov/doc/horizons.html'),('horizons_manual.html','https://ssd.jpl.nasa.gov/horizons/manual.html')]:
    guardar(name,url)
(base/'fuentes.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
