"""Mi preparación y validación reproducibles; Python 3.10+ y NumPy."""
from pathlib import Path
from datetime import date, timedelta
from statistics import mean, median
from urllib.parse import quote
import csv
import hashlib
import json
import math
import numpy as np

RAIZ = Path(__file__).resolve().parent
EXCLUSIONES = {'Dark_Souls_III': 'estreno japonés anterior al mundial', "Baldur's_Gate_3": 'cobertura incompleta del título en los primeros días'}

def preparar():
    # leo mis series conservadas y compruebo sus unidades
    series = json.loads((RAIZ/'series_consultadas.json').read_text(encoding='utf-8'))
    assert len(series) == len({s['t'] for s in series}) == 30
    filas, juegos = [], []
    for s in series:
        assert len(s['v']) == 43 and all(type(v) is int and v > 0 for v in s['v'])
        fecha = date.fromisoformat(s['d'])
        grupo = 'entrenamiento' if fecha.year <= 2019 else 'validacion' if fecha.year <= 2021 else 'prueba'
        for i, v in enumerate(s['v']):
            filas.append(dict(titulo=s['t'],fecha=(fecha+timedelta(days=i-7)).isoformat(),dia=i-7,consultas=v,grupo=grupo,exclusion=EXCLUSIONES.get(s['t'],'')))
        if s['t'] in EXCLUSIONES:
            continue
        v = s['v']
        juegos.append(dict(titulo=s['t'],fecha=s['d'],grupo=grupo,dia0=v[7],dia3=v[10],previa=mean(v[:7]),x=[math.log(v[10]/v[7]),math.log(mean(v[:7])/v[7])],y=[mean(v[21:28])/v[7],mean(v[35:42])/v[7]],v=v))
    with (RAIZ/'consultas_diarias.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(filas[0]));w.writeheader();w.writerows(filas)
    gta=json.loads((RAIZ/'gta_vi_consultado.json').read_text(encoding='utf-8'))
    assert len(gta['v'])==22
    gv=gta['v'];gta['x']=[math.log(gv[21]/gv[18]),math.log(mean(gv[11:18])/gv[18])]
    gta['dia0']=gv[18];gta['dia3']=gv[21]
    return juegos,gta

def ajustar(juegos,alpha):
    # aprendo la escala solo con mis juegos de entrenamiento
    x=np.asarray([s['x'] for s in juegos],dtype=float)
    y=np.log(np.asarray([s['y'] for s in juegos],dtype=float))
    mu=x.mean(axis=0); sd=x.std(axis=0);sd=np.where(sd==0,1,sd)
    z=np.column_stack([np.ones(len(x)),(x-mu)/sd])
    penal=np.diag([0.,alpha,alpha])
    coef=np.linalg.solve(z.T@z+penal,z.T@y)
    return mu,sd,coef

def predecir(modelo,juegos):
    mu,sd,coef=modelo
    x=np.asarray([s['x'] for s in juegos],dtype=float)
    return np.exp(np.column_stack([np.ones(len(x)),(x-mu)/sd])@coef)

def referencia(entrenamiento,juegos,tipo):
    if tipo=='mediana':
        m=np.median(np.asarray([s['y'] for s in entrenamiento]),axis=0)
        return np.tile(m,(len(juegos),1))
    return np.asarray([[s['dia3']/s['dia0']]*2 for s in juegos])

def medir(real,pred):
    real=np.asarray(real);pred=np.asarray(pred)
    e=np.abs(np.log(real)-np.log(pred))
    return dict(mae_log=float(e.mean()),mae_log_horizonte=e.mean(axis=0).tolist(),mae_puntos_retencion=(100*np.abs(real-pred).mean(axis=0)).tolist(),factor_error_geometrico=float(np.exp(e.mean())))

def ejecutar():
    juegos,gta=preparar()
    tr=[s for s in juegos if s['grupo']=='entrenamiento']; va=[s for s in juegos if s['grupo']=='validacion'];te=[s for s in juegos if s['grupo']=='prueba']
    assert (len(tr),len(va),len(te))==(14,7,7)
    assert max(s['fecha'] for s in tr)<min(s['fecha'] for s in va)<min(s['fecha'] for s in te)
    reales_va=[s['y'] for s in va];reales_te=[s['y'] for s in te]
    candidatos={str(a):medir(reales_va,predecir(ajustar(tr,a),va)) for a in (1.,10.)}
    alpha=float(min(candidatos,key=lambda a:candidatos[a]['mae_log']))
    modelo=ajustar(tr+va,alpha)
    pred=predecir(modelo,te)
    medidas={'ridge':medir(reales_te,pred),'mediana':medir(reales_te,referencia(tr+va,te,'mediana')),'persistencia':medir(reales_te,referencia(tr+va,te,'persistencia'))}
    pasa=medidas['ridge']['mae_log']<medidas['mediana']['mae_log']
    pred_gta=predecir(modelo,[gta])[0]
    residual_va=np.abs(np.log(np.asarray(reales_va))-np.log(predecir(ajustar(tr,alpha),va)))
    amplitud=residual_va.max(axis=0)
    intervalos=np.array([pred_gta*np.exp(-amplitud),pred_gta*np.exp(amplitud)]).T
    por_juego=[dict(titulo=s['titulo'],real=s['y'],ridge=pred[i].tolist(),mediana=referencia(tr+va,[s],'mediana')[0].tolist()) for i,s in enumerate(te)]
    origen=date.fromisoformat(gta['d'])
    resultados=dict(corte='2026-11-23',medida='consultas diarias de Wikipedia en inglés, all-access, user; días UTC',muestra=dict(recogidos=30,utilizados=len(juegos),entrenamiento=len(tr),validacion=len(va),prueba=len(te),exclusiones=EXCLUSIONES),seleccion_validacion=candidatos,alpha_elegido=alpha,metricas_prueba=medidas,mejora_relativa_mae_log=1-medidas['ridge']['mae_log']/medidas['mediana']['mae_log'],supera_referencia=pasa,prueba_por_juego=por_juego,modelo=dict(media=modelo[0].tolist(),desviacion=modelo[1].tolist(),coeficientes=modelo[2].tolist()),gta=dict(dia0=gta['dia0'],dia3=gta['dia3'],cambio_observado_pct=100*(gta['dia3']/gta['dia0']-1),prediccion_experimental_retencion=pred_gta.tolist(),prediccion_experimental_consultas=(pred_gta*gta['dia0']).tolist(),rango_orientativo_retencion=intervalos.tolist(),rango_orientativo_consultas=(intervalos*gta['dia0']).tolist(),rango_no_probabilistico=True,periodos=[dict(inicio=(origen+timedelta(days=d)).isoformat(),fin=(origen+timedelta(days=d+6)).isoformat()) for d in (14,28)],variables=gta['x'],rango_variables_entrenamiento=[np.min([s['x'] for s in tr+va],axis=0).tolist(),np.max([s['x'] for s in tr+va],axis=0).tolist()]),huellas={n:hashlib.sha256((RAIZ/n).read_bytes()).hexdigest() for n in ('series_consultadas.json','gta_vi_consultado.json','protocolo.md')})
    (RAIZ/'resultados.json').write_text(json.dumps(resultados,ensure_ascii=False,indent=2),encoding='utf-8')
    return resultados

if __name__=='__main__':
    r=ejecutar()
    print(json.dumps({k:r[k] for k in ('muestra','seleccion_validacion','alpha_elegido','metricas_prueba','supera_referencia','gta')},ensure_ascii=False,indent=2))
