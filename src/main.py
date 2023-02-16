"""
Universidad del Valle de Guatemala
Minería de Datos
Laboratorio 02
Marco Orozco (20857) y Santiago Taracena (20017)
"""

import pandas as pd

data = pd.read_csv("./data/breast-cancer-wisconsin.csv")

data["bare_nuclei"] = data["bare_nuclei"].apply(lambda x: 0 if (x == "?") else int(x))

print(data.head())
print(data.isnull().mean())
print(data.dtypes)
print(data.describe())
