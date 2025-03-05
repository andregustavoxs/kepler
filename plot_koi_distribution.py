import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Definir o estilo visual
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))

# Ler o arquivo CSV
print("Lendo o arquivo kepler.csv...")
df = pd.read_csv('kepler.csv', comment='#')

# Verificar o nome correto da coluna que contém a classificação (Exoplanet Archive Disposition)
print("Colunas disponíveis:", df.columns.tolist())

# Contar os registros por categoria
disposition_column = 'koi_disposition'  # Nome da coluna que contém a classificação
disposition_counts = df[disposition_column].value_counts()

print(f"\nDistribuição de KOIs por categoria:")
print(disposition_counts)

# Criar o gráfico de barras
plt.figure(figsize=(12, 7))
ax = sns.barplot(x=disposition_counts.index, y=disposition_counts.values, palette='viridis')

# Adicionar rótulos e título
plt.title('Distribuição de Kepler Objects of Interest (KOI) por Categoria', fontsize=16)
plt.xlabel('Categoria', fontsize=14)
plt.ylabel('Número de KOIs', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adicionar os valores em cima das barras
for i, count in enumerate(disposition_counts.values):
    ax.text(i, count + 50, f'{count}', ha='center', fontsize=12)

# Salvar o gráfico na pasta 'graphs'
os.makedirs('graphs', exist_ok=True)
plt.savefig('graphs/koi_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\nGráfico salvo em: graphs/koi_distribution.png")
