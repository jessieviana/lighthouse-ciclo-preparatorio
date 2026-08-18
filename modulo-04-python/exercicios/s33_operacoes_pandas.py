# S33 - Operações com Pandas
# Objetivo: praticar operações como filtragem, seleção, agrupamento
# e outras manipulações de DataFrame.

import pandas as pd


dados = {
    "nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa"],
    "departamento": ["Engenharia", "Vendas", "Engenharia", "RH", "Vendas"],
    "salario": [6500, 4200, 7200, 3900, 4800],
}

df = pd.DataFrame(dados)

print("--- 1. Filtragem e seleção ---")
filtro = df["departamento"] == "Engenharia"
df_engenharia = df.loc[filtro, ["nome", "salario"]]
print(df_engenharia)

print("\n--- 2. Agrupamento e média ---")
media_salarial = df.groupby("departamento")["salario"].mean()
print(media_salarial)

print("\n--- 3. Ordenação por salário ---")
df_ordenado = df.sort_values("salario", ascending=False)
print(df_ordenado[["nome", "salario"]])

print("\n--- 4. Criação de uma nova coluna ---")
df["salario_com_bonus"] = df["salario"] * 1.10
print(df[["nome", "salario", "salario_com_bonus"]])
