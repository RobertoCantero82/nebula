"""Entreno y evalúo sin utilizar la prueba para elegir el modelo."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_regression, VarianceThreshold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GroupShuffleSplit, GroupKFold, GridSearchCV
from sklearn.metrics import mean_absolute_error, median_absolute_error, mean_squared_error, r2_score

class filtro_ausentes(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        self.columnas_ = np.mean(np.isnan(x), axis=0) <= .05
        return self
    def transform(self, x):
        return x[:, self.columnas_]

def ejecutar(raiz):
    raiz = Path(raiz)
    salida = raiz / 'resultados'
    salida.mkdir(exist_ok=True)
    datos = np.load(raiz / 'data/metilacion_candidatos.npz')
    x = datos['x']
    tabla = pd.read_csv(raiz / 'data/muestras.csv', dtype={'chip': str, 'muestra': str})
    y = tabla.edad.to_numpy()
    grupos = tabla.chip.to_numpy()
    desarrollo, prueba = next(GroupShuffleSplit(n_splits=1, test_size=.2, random_state=20261023).split(x, y, grupos))
    entreno_local, calibracion_local = next(GroupShuffleSplit(n_splits=1, test_size=.1875, random_state=20261023).split(x[desarrollo], y[desarrollo], grupos[desarrollo]))
    entreno, calibracion = desarrollo[entreno_local], desarrollo[calibracion_local]
    for a, b in [(entreno, prueba), (entreno, calibracion), (calibracion, prueba)]:
        assert not set(grupos[a]) & set(grupos[b])
    tabla['particion'] = ''
    for nombre, indices in [('entrenamiento', entreno), ('calibracion', calibracion), ('prueba', prueba)]:
        tabla.loc[indices, 'particion'] = nombre
    tabla.to_csv(salida / 'particiones.csv', index=False)
    cadena = Pipeline([('ausentes', filtro_ausentes()), ('imputacion', SimpleImputer(strategy='mean')),
                       ('varianza', VarianceThreshold()), ('seleccion', SelectKBest(f_regression)),
                       ('escala', StandardScaler()), ('ridge', Ridge())])
    busqueda = GridSearchCV(cadena, {'seleccion__k': [100, 1000], 'ridge__alpha': [10., 100.]},
                           scoring='neg_mean_absolute_error', cv=GroupKFold(5), n_jobs=1,
                           return_train_score=False, error_score='raise')
    busqueda.fit(x[entreno], y[entreno], groups=grupos[entreno])
    validacion = pd.DataFrame(busqueda.cv_results_).drop(columns=['params'])
    validacion.to_csv(salida / 'validacion.csv', index=False)
    print('Elección por validación:', busqueda.best_params_, 'MAE', -busqueda.best_score_, flush=True)
    modelo = busqueda.best_estimator_
    error_calibracion = np.sort(np.abs(y[calibracion] - modelo.predict(x[calibracion])))
    rango = min(int(np.ceil((len(calibracion) + 1) * .9)), len(calibracion))
    amplitud = float(error_calibracion[rango - 1])
    prediccion = modelo.predict(x[prueba])
    base = np.full(len(prueba), np.median(y[entreno]))
    resultado = tabla.iloc[prueba].copy()
    resultado['prediccion'] = prediccion
    resultado['error'] = prediccion - y[prueba]
    resultado['error_absoluto'] = np.abs(resultado.error)
    resultado['limite_inferior'] = prediccion - amplitud
    resultado['limite_superior'] = prediccion + amplitud
    resultado['cubierto'] = resultado.error_absoluto <= amplitud
    resultado.to_csv(salida / 'predicciones_prueba.csv', index=False)
    rng = np.random.default_rng(20261023)
    chips = resultado.chip.unique()
    errores = [resultado.loc[resultado.chip == chip, 'error_absoluto'].to_numpy() for chip in chips]
    remuestreos = [float(np.concatenate([errores[i] for i in rng.integers(0, len(chips), len(chips))]).mean()) for _ in range(2000)]
    resultado['grupo_edad'] = pd.cut(resultado.edad, [0, 40, 60, 80, np.inf], right=False,
                                    labels=['19–39', '40–59', '60–79', '80 o más'])
    por_edad = resultado.groupby('grupo_edad', observed=False).agg(n=('edad', 'size'), edad_media=('edad', 'mean'),
                error_medio=('error', 'mean'), mae=('error_absoluto', 'mean'), cobertura=('cubierto', 'mean'))
    por_edad.to_csv(salida / 'errores_por_edad.csv')
    metricas = {'mae': float(mean_absolute_error(y[prueba], prediccion)),
                'mediana_error_absoluto': float(median_absolute_error(y[prueba], prediccion)),
                'rmse': float(np.sqrt(mean_squared_error(y[prueba], prediccion))),
                'r2': float(r2_score(y[prueba], prediccion)), 'mae_base': float(mean_absolute_error(y[prueba], base)),
                'mediana_entrenamiento': float(np.median(y[entreno])),
                'mae_validacion': float(-busqueda.best_score_), 'mejores_parametros': busqueda.best_params_,
                'semianchura_intervalo_90': amplitud, 'cobertura_prueba': float(resultado.cubierto.mean()),
                'mae_ic95_por_chip': np.quantile(remuestreos, [.025, .975]).tolist(),
                'particiones': {k: {'n': len(v), 'chips': len(set(grupos[v]))} for k, v in [('entrenamiento', entreno), ('calibracion', calibracion), ('prueba', prueba)]}}
    (salida / 'metricas.json').write_text(json.dumps(metricas, ensure_ascii=False, indent=2), encoding='utf-8')
    marcadores = datos['marcadores'][modelo.named_steps['ausentes'].columnas_]
    marcadores = marcadores[modelo.named_steps['imputacion'].statistics_ == modelo.named_steps['imputacion'].statistics_]
    marcadores = marcadores[modelo.named_steps['varianza'].get_support()][modelo.named_steps['seleccion'].get_support()]
    pd.DataFrame({'marcador': marcadores, 'coeficiente_estandarizado': modelo.named_steps['ridge'].coef_}).to_csv(salida / 'marcadores_modelo.csv', index=False)
    print(json.dumps(metricas, indent=2, ensure_ascii=False))
    return tabla, resultado, por_edad, metricas, validacion

if __name__ == '__main__':
    ejecutar(Path(__file__).resolve().parent)
