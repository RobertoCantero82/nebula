from pathlib import Path
import json

import numpy as np
import pandas as pd


RUTA_PROYECTO = Path(
    r"C:\Users\rober\OneDrive\Documentos\proyectos_datos\_repos_nebula\insectos_california_anonimato"
)
ARCHIVO_ORIGINAL = RUTA_PROYECTO / "data" / "raw" / "SupplementalTable3.csv"
RUTA_PROCESADOS = RUTA_PROYECTO / "data" / "processed"
RUTA_PROCESADOS.mkdir(parents=True, exist_ok=True)

COLUMNAS = [
    "BIN",
    "Order",
    "Family",
    "Genus",
    "Species",
    "US_L3NAME",
    "Sampling Protocol",
]


def limpiar_texto(serie: pd.Series) -> pd.Series:
    """Convierto los marcadores vacíos del archivo en valores ausentes."""
    return serie.replace({"NA": pd.NA, "N/A": pd.NA, "": pd.NA, "Unknown": pd.NA})


def primer_valido(serie: pd.Series):
    """Conservo la primera etiqueta informativa dentro de cada grupo genético."""
    valores = serie.dropna()
    return valores.iloc[0] if len(valores) else pd.NA


fragmentos_bin = []
fragmentos_bin_region = []

for numero, fragmento in enumerate(
    pd.read_csv(
        ARCHIVO_ORIGINAL,
        usecols=COLUMNAS,
        chunksize=100_000,
        dtype="string",
        keep_default_na=False,
    ),
    start=1,
):
    # limpio solo las columnas necesarias y descarto filas sin grupo genético
    for columna in COLUMNAS:
        fragmento[columna] = limpiar_texto(fragmento[columna])
    fragmento = fragmento.dropna(subset=["BIN"]).copy()

    # reduzco cada fragmento a una fila por bin para no cargar el csv completo
    resumen_fragmento = (
        fragmento.groupby("BIN", observed=True)
        .agg(
            ejemplares=("BIN", "size"),
            orden=("Order", primer_valido),
            familia=("Family", primer_valido),
            genero=("Genus", primer_valido),
            especie=("Species", primer_valido),
        )
        .reset_index()
    )
    fragmentos_bin.append(resumen_fragmento)

    # guardo las apariciones territoriales sin repetir ejemplares del mismo bin
    pares = fragmento[["BIN", "US_L3NAME"]].dropna().drop_duplicates()
    fragmentos_bin_region.append(pares)
    print(f"fragmento {numero}: {len(fragmento):,} registros con BIN")

# uno las reducciones parciales y resuelvo los bins que cruzan fragmentos
catalogo_parcial = pd.concat(fragmentos_bin, ignore_index=True)
catalogo = (
    catalogo_parcial.groupby("BIN", observed=True)
    .agg(
        ejemplares=("ejemplares", "sum"),
        orden=("orden", primer_valido),
        familia=("familia", primer_valido),
        genero=("genero", primer_valido),
        especie=("especie", primer_valido),
    )
    .reset_index()
)

# un bin es anónimo si ninguna fila del conjunto aporta un nombre de especie
catalogo["anonimo"] = catalogo["especie"].isna()
catalogo["nivel_maximo"] = np.select(
    [
        catalogo["especie"].notna(),
        catalogo["genero"].notna(),
        catalogo["familia"].notna(),
        catalogo["orden"].notna(),
    ],
    ["especie", "género", "familia", "orden"],
    default="sin orden",
)


def resumir(grupo: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Calculo el índice de anonimato para una clasificación determinada."""
    salida = (
        grupo.groupby(columna, dropna=False, observed=True)
        .agg(
            grupos_geneticos=("BIN", "nunique"),
            grupos_anonimos=("anonimo", "sum"),
            ejemplares=("ejemplares", "sum"),
        )
        .reset_index()
    )
    salida["indice_anonimato"] = (
        100 * salida["grupos_anonimos"] / salida["grupos_geneticos"]
    ).round(1)
    return salida.sort_values(
        ["indice_anonimato", "grupos_geneticos"], ascending=[False, False]
    )


resumen_orden = resumir(catalogo.dropna(subset=["orden"]), "orden")
resumen_familia = resumir(catalogo.dropna(subset=["familia"]), "familia")

# asigno a cada presencia regional la condición global del bin
bin_region = pd.concat(fragmentos_bin_region, ignore_index=True).drop_duplicates()
bin_region = bin_region.merge(
    catalogo[["BIN", "anonimo", "ejemplares"]], on="BIN", how="left", validate="many_to_one"
)
resumen_region = resumir(bin_region, "US_L3NAME")

# agrupo la rareza observada para comprobar si los bins menos vistos tienen menos nombre
catalogo["tramo_ejemplares"] = pd.cut(
    catalogo["ejemplares"],
    bins=[0, 1, 5, 20, np.inf],
    labels=["1 ejemplar", "2–5 ejemplares", "6–20 ejemplares", "más de 20"],
)
resumen_rareza = resumir(catalogo, "tramo_ejemplares")

distribucion_nivel = (
    catalogo.groupby("nivel_maximo", observed=True)
    .agg(grupos_geneticos=("BIN", "nunique"))
    .reset_index()
)
distribucion_nivel["porcentaje"] = (
    100 * distribucion_nivel["grupos_geneticos"] / len(catalogo)
).round(1)

resumen_general = {
    "registros_con_bin": int(catalogo["ejemplares"].sum()),
    "grupos_geneticos": int(len(catalogo)),
    "grupos_anonimos": int(catalogo["anonimo"].sum()),
    "indice_anonimato": round(100 * float(catalogo["anonimo"].mean()), 1),
    "grupos_con_nombre": int((~catalogo["anonimo"]).sum()),
}

catalogo.to_csv(RUTA_PROCESADOS / "catalogo_bins.csv", index=False)
resumen_orden.to_csv(RUTA_PROCESADOS / "anonimato_por_orden.csv", index=False)
resumen_familia.to_csv(RUTA_PROCESADOS / "anonimato_por_familia.csv", index=False)
resumen_region.to_csv(RUTA_PROCESADOS / "anonimato_por_ecorregion.csv", index=False)
resumen_rareza.to_csv(RUTA_PROCESADOS / "anonimato_por_rareza.csv", index=False)
distribucion_nivel.to_csv(RUTA_PROCESADOS / "nivel_identificacion.csv", index=False)
(RUTA_PROCESADOS / "resumen_general.json").write_text(
    json.dumps(resumen_general, ensure_ascii=False, indent=2), encoding="utf-8"
)

print(json.dumps(resumen_general, ensure_ascii=False, indent=2))
print("\nÓrdenes con al menos 100 grupos genéticos:")
print(resumen_orden.loc[resumen_orden["grupos_geneticos"] >= 100].head(20).to_string(index=False))
print("\nRareza:")
print(resumen_rareza.to_string(index=False))
