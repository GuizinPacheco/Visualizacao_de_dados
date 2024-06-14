import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas import read_csv

df = read_csv("stack_overflow_developer.csv", delimiter=';', encoding='utf-8', on_bad_lines='skip')
respostas_count = df['RemotoWork'].value_counts().rename_axis('modelos').reset_index(name='contagem')

modelos = respostas_count['modelos'].to_numpy()
contagens = respostas_count['contagem'].to_numpy()

plt.bar(modelos, contagens)  # Definir as posições das barras por "resposta" e as alturas por "contagens"
plt.title('Modelos de trabalho')  # Título do gráfico
plt.show()

