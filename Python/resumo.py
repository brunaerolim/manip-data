import pandas as pd

# Criando um DataFrame com dados de vendas

df = pd.DataFrame({
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Vendas': [100, 200, 150, 50, 300, 250],
    'Região': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul']

})

# Agrupando os dados por Produto e Região e calcular média de Vendas
grouped_df = df.groupby(['Produto', 'Região'])['Vendas'].mean()

print(grouped_df)