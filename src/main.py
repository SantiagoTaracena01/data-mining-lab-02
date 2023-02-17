"""
Universidad del Valle de Guatemala
Minería de Datos
Laboratorio 02
Marco Orozco (20857) y Santiago Taracena (20017)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./data/breast-cancer-wisconsin.csv")

data["bare_nuclei"] = data["bare_nuclei"].apply(lambda x: 0 if (x == "?") else int(x))

# 1.3 gráficos chetos

sns.catplot(x="class", y="uniformity_cell_size", data=data, kind="boxen", height=4, aspect=2)
plt.show()
