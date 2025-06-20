import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df=pd.read_csv(url)


embarked=df['Embarked'].mode()[0]


df=df.dropna(subset=['Age'])

df['Embarked']=df['Embarked'].fillna(embarked)

test=df[df.duplicated(subset=['Age'])]


media_classe=df.groupby('Pclass')['Age'].mean()

df['Age']
print(media_classe)

