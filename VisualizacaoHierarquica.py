import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas import read_csv

df = read_csv("stack_overflow_developer.csv", delimiter=';', encoding='utf-8', on_bad_lines='skip')
respostas_count = df['Age'].value_counts().rename_axis('idade').reset_index(name='countIdade')

idades = respostas_count['idade'].to_numpy()
contagens = respostas_count['countIdade'].to_numpy()

df = pd.DataFrame(dict(idade=idades,contagens=contagens))
df["all"] = "all" #garante um único nó raiz
fig = px.treemap(df,path=[idades],values=contagens)
fig.show()