import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Carrega a base de dados
df = pd.read_csv("stack_overflow_developer_brazilian.csv", delimiter=';', encoding='utf-8', on_bad_lines='skip')

# Cria um DataFrame com as preferências de aprendizado de código
learn_code_df = df['LearnCode.1'].value_counts().rename_axis('Preferência').reset_index(name='Contagem')

# Cria o gráfico de cordas usando a biblioteca networkx
G = nx.Graph()

# Adiciona os nós (preferências) ao gráfico
G.add_nodes_from(learn_code_df['Preferência'])

# Calcula a força da conexão entre os nós,
# usando a contagem como um proxy para a força
for i in range(len(learn_code_df)):
    for j in range(i + 1, len(learn_code_df)):
        # A força da conexão é a contagem do nó com o menor valor
        connection_strength = min(learn_code_df['Contagem'][i], learn_code_df['Contagem'][j])
        G.add_edge(learn_code_df['Preferência'][i], learn_code_df['Preferência'][j], weight=connection_strength)

# Define o layout do gráfico
pos = nx.spring_layout(G, k=0.5, iterations=20)

# Plota o gráfico com as conexões como cordas
nx.draw(G, pos, with_labels=True, node_size=500, node_color='green', font_size=10, font_color='black', edge_color='skyblue')
max_width = 5  # Define o limite máximo de espessura
widths = [min(d['weight'], max_width) for (u, v, d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, width=widths,edge_color='skyblue')


# Adiciona um título ao gráfico
plt.title("Diagrama de Cordas: Preferências de Aprendizado de Código")

plt.show()
