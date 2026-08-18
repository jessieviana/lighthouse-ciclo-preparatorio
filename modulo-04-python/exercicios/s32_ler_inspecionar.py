# S32 - Ler e Inspecionar Dados
# Objetivo: praticar a leitura de arquivos (csv, json, etc.) e
# a inspeção inicial dos dados carregados.

from pathlib import Path

import pandas as pd


PASTA_DADOS = (
    Path(__file__).parents[1]
    / "exemplos_da_aula"
    / "03_pandas"
    / "data"
)

detalhes_pedidos = pd.read_csv(PASTA_DADOS / "order_details.csv")
pedidos = pd.read_json(PASTA_DADOS / "public-orders.jsonl", lines=True)

print("--- Arquivo CSV ---")
print(detalhes_pedidos.head())
print(f"Dimensões: {detalhes_pedidos.shape}")
print(f"Colunas: {detalhes_pedidos.columns.tolist()}")
print(f"Valores nulos por coluna:\n{detalhes_pedidos.isna().sum()}")

print("\n--- Arquivo JSONL ---")
print(pedidos.head())
print(f"Dimensões: {pedidos.shape}")
print(f"Colunas: {pedidos.columns.tolist()}")
print(f"Valores nulos por coluna:\n{pedidos.isna().sum()}")
