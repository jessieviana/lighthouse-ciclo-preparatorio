# S30 - Operações e Inspeção com Pandas
# Objetivo: criar um DataFrame e fazer sua inspeção inicial.

import pandas as pd


dados = {
    "nome": ["João", "Maria", "Pedro", "Ana", "Lucas"],
    "idade": [28, 22, 35, 19, 42],
    "departamento": ["TI", "RH", "TI", "Financeiro", "Vendas"],
}

df = pd.DataFrame(dados)

print("--- Primeiras linhas ---")
print(df.head(3))

print("\n--- Dimensões ---")
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")

print("\n--- Nomes das colunas ---")
print(df.columns.tolist())

print("\n--- Tipos e valores não nulos ---")
df.info()

print("\n--- Resumo estatístico ---")
print(df.describe(include="all"))
