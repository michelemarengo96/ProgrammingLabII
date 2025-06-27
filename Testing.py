import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df=sb.load_dataset("penguins")

righecolonne=df.shape

mancanti=df.isna().sum()

moda_sex=df.sex.mode()[0]

df['sex']=df['sex'].fillna(moda_sex)

df=df.dropna(subset=['body_mass_g'])

duplicati=df.duplicated()

media_massa_species=df.groupby('species')['body_mass_g'].mean()

print(media_massa_species)

df['body_mass_g']=df.apply(lambda x: media_massa_species[x['species']] if pd.isna(x['body_mass_g']) else x['body_mass_g'],axis=1)

sb.violinplot(data=df, x='species', y='body_mass_g',hue='sex')
plt.show()