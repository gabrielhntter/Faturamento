import os
import pandas as pd
import plotly.express as px

#1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)

lista_arquivo = os.listdir("C:\\Users\Gabri\Downloads\Vendas")#Criando uma lista com os itens dentro da pasta de Vendas

tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    #Verificar se tem "Vendas" no nome do arquivo
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:\\Users\Gabri\Downloads\Vendas\{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela])
#2 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)

#3 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum(numeric_only=True)
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)

#4 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_lojas = tabela_total.groupby('Loja').sum(numeric_only=True)
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show() #Código para abrir o gráfico