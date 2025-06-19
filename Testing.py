import numpy as np
import pandas as pd


affitti=np.array([720,980,650,1200], dtype="float64")

somma_iniziale=np.sum(affitti)

indice_1200=np.where(affitti==1200)[0][0]


affitti[indice_1200]*=1.12
np.isclose(affitti[indice_1200], 1344.0)

somma_post_aumento=np.sum(affitti)

valore_1200=affitti[indice_1200]


indice_650=np.where(affitti==650)[0][0]

affitti[indice_650]=affitti[indice_650]-affitti[indice_650]/10

valore_650=affitti[indice_650]

affitti=np.where((~np.isclose(affitti, valore_1200)) & (~np.isclose(affitti,valore_650)), affitti*1.05, affitti)


differenza=somma_post_aumento-somma_iniziale


data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
data = {
    'job_title': ['Data Analyst', 'Data Scientist', 'Data Engineer'],
    'location': ['Italy', 'USA', 'Germany'],
    'salary': [40000, 80000, 70000],
    'date_posted': ['2024-12-01', '2024-11-15', '2024-12-10']  # formato YYYY-MM-DD
}

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")

print(df.sort_values(by="beer_servings",ascending=False))