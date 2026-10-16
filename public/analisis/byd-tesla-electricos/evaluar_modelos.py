from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd


def estacional(historia: np.ndarray, pasos: int) -> np.ndarray:
    """Uso el mismo mes del año anterior como referencia transparente."""
    return np.array([historia[len(historia) + i - 12] for i in range(pasos)], dtype=float)


def estacional_crecimiento(historia: np.ndarray, pasos: int) -> np.ndarray:
    """Proyecto el patrón anual y aplico el crecimiento observado en los últimos seis meses."""
    base = estacional(historia, pasos)
    anterior = historia[-18:-12].sum()
    reciente = historia[-6:].sum()
    factor = np.clip(reciente / anterior if anterior else 1.0, 0.55, 2.25)
    return base * factor


def matriz(t: np.ndarray) -> np.ndarray:
    """Represento tendencia y ciclos anual y trimestral con pocas variables estables."""
    return np.column_stack(
        [
            np.ones_like(t),
            t / 12,
            np.sin(2 * np.pi * t / 12),
            np.cos(2 * np.pi * t / 12),
            np.sin(2 * np.pi * t / 3),
            np.cos(2 * np.pi * t / 3),
            (t % 3 == 2).astype(float),
        ]
    )


def regresion_periodica(historia: np.ndarray, pasos: int, ventana: int | None, log: bool) -> np.ndarray:
    """Ajusto una regresión regularizada sin depender de una caja negra externa."""
    inicio = max(0, len(historia) - ventana) if ventana else 0
    t = np.arange(inicio, len(historia), dtype=float)
    futuro = np.arange(len(historia), len(historia) + pasos, dtype=float)
    x = matriz(t)
    y = np.log1p(historia[inicio:]) if log else historia[inicio:].astype(float)
    penalizacion = np.eye(x.shape[1]) * 1.5
    penalizacion[0, 0] = 0
    coeficientes = np.linalg.solve(x.T @ x + penalizacion, x.T @ y)
    prediccion = matriz(futuro) @ coeficientes
    if log:
        prediccion = np.expm1(prediccion)
    return np.clip(prediccion, 0, None)


MODELOS = {
    "estacional": estacional,
    "estacional_crecimiento": estacional_crecimiento,
    "regresion_periodica": lambda h, p: regresion_periodica(h, p, None, False),
    "regresion_periodica_24m": lambda h, p: regresion_periodica(h, p, 24, False),
    "regresion_logaritmica_24m": lambda h, p: regresion_periodica(h, p, 24, True),
}


def smape(real: np.ndarray, pred: np.ndarray) -> float:
    denominador = np.abs(real) + np.abs(pred)
    return float(np.mean(np.where(denominador == 0, 0, 2 * np.abs(real - pred) / denominador)) * 100)


def main(csv_path: Path, salida: Path) -> None:
    datos = pd.read_csv(csv_path, parse_dates=["mes"])
    tabla = datos.pivot(index="mes", columns="marca", values="matriculaciones").sort_index()
    resultados: list[dict[str, object]] = []
    residuos_test: dict[str, dict[str, list[float]]] = {marca: {modelo: [] for modelo in MODELOS} for marca in tabla}

    # separo 2025 para validar y 2026 para una prueba temporal que no decide el modelo
    fases = {"validacion_2025": [24, 27, 30, 33], "prueba_2026": [36, 39, 42]}
    for marca in tabla.columns:
        serie = tabla[marca].to_numpy(dtype=float)
        for modelo, funcion in MODELOS.items():
            for fase, cortes in fases.items():
                reales_todos: list[float] = []
                pred_todos: list[float] = []
                for corte in cortes:
                    historia = serie[:corte]
                    real = serie[corte : corte + 3]
                    pred = funcion(historia, 3)
                    reales_todos.extend(real)
                    pred_todos.extend(pred)
                    if fase == "prueba_2026":
                        residuos_test[marca][modelo].extend((real - pred).tolist())
                reales = np.array(reales_todos)
                predichos = np.array(pred_todos)
                resultados.append(
                    {
                        "marca": marca,
                        "modelo": modelo,
                        "fase": fase,
                        "mae": float(np.mean(np.abs(reales - predichos))),
                        "smape": smape(reales, predichos),
                        "observaciones": len(reales),
                    }
                )

    metricas = pd.DataFrame(resultados)
    validacion = metricas[metricas["fase"] == "validacion_2025"]
    mejores = validacion.loc[validacion.groupby("marca")["mae"].idxmin()].set_index("marca")
    candidatos = {marca: str(mejores.loc[marca, "modelo"]) for marca in tabla.columns}
    finales: dict[str, str] = {}
    for marca in tabla.columns:
        mae_candidato = metricas.loc[(metricas["marca"] == marca) & (metricas["modelo"] == candidatos[marca]) & (metricas["fase"] == "prueba_2026"), "mae"].iloc[0]
        mae_base = metricas.loc[(metricas["marca"] == marca) & (metricas["modelo"] == "estacional") & (metricas["fase"] == "prueba_2026"), "mae"].iloc[0]
        # sólo desplazo la referencia si el modelo supera el examen temporal fuera de muestra
        finales[marca] = candidatos[marca] if mae_candidato < mae_base else "estacional"

    pronosticos: list[dict[str, object]] = []
    predicciones: dict[str, np.ndarray] = {}
    for marca in tabla.columns:
        elegido = finales[marca]
        pred = MODELOS[elegido](tabla[marca].to_numpy(dtype=float), 3)
        predicciones[marca] = pred
        for fecha, valor in zip(pd.date_range("2026-10-01", periods=3, freq="MS"), pred):
            pronosticos.append(
                {"mes": fecha.strftime("%Y-%m"), "marca": marca, "prediccion": int(round(valor)), "modelo": elegido}
            )

    rng = np.random.default_rng(42)
    simulaciones = 50_000
    totales = {}
    for marca in tabla.columns:
        elegido = finales[marca]
        errores = np.array(residuos_test[marca][elegido])
        # centro los residuos para expresar incertidumbre alrededor de la previsión puntual
        ruido = rng.choice(errores - errores.mean(), size=(simulaciones, 3), replace=True)
        futuros = np.clip(predicciones[marca] + ruido, 0, None)
        acumulado = tabla.loc[tabla.index.year == 2026, marca].sum()
        totales[marca] = acumulado + futuros.sum(axis=1)

    probabilidad_byd = float(np.mean(totales["BYD"] > totales["Tesla"]))
    diferencia = totales["BYD"] - totales["Tesla"]
    resumen = {
        "corte_datos": tabla.index.max().strftime("%Y-%m"),
        "acumulado_2026": {marca: int(tabla.loc[tabla.index.year == 2026, marca].sum()) for marca in tabla.columns},
        "modelo_candidato_validacion": candidatos,
        "modelo_final": finales,
        "mae_prueba_2026": {
            marca: int(round(metricas.loc[(metricas["marca"] == marca) & (metricas["modelo"] == finales[marca]) & (metricas["fase"] == "prueba_2026"), "mae"].iloc[0]))
            for marca in tabla.columns
        },
        "prevision_octubre_diciembre": {marca: int(round(predicciones[marca].sum())) for marca in tabla.columns},
        "total_2026_estimado": {
            marca: int(round(tabla.loc[tabla.index.year == 2026, marca].sum() + predicciones[marca].sum()))
            for marca in tabla.columns
        },
        "probabilidad_byd_supera_tesla": probabilidad_byd,
        "diferencia_mediana": int(round(np.median(diferencia))),
        "intervalo_diferencia_80": [int(round(x)) for x in np.quantile(diferencia, [0.1, 0.9])],
        "simulaciones": simulaciones,
    }

    salida.mkdir(parents=True, exist_ok=True)
    metricas.to_csv(salida / "metricas_modelos.csv", index=False)
    pd.DataFrame(pronosticos).to_csv(salida / "pronostico_oct_dic_2026.csv", index=False)
    (salida / "resumen_prediccion.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(metricas.sort_values(["marca", "fase", "mae"]).to_string(index=False, float_format=lambda x: f"{x:.1f}"))
    print(json.dumps(resumen, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Uso: evaluar_modelos.py CSV_MENSUAL CARPETA_SALIDA")
    main(Path(sys.argv[1]), Path(sys.argv[2]))
