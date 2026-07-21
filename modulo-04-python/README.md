# Módulo 04 — Python (Aulas 4 e 5)

Material organizado por tópico, seguindo a ordem do conteúdo dado em aula
(Introdução ao Python — Lighthouse / Indicium).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `01_funcoes_e_pseudocodigo/` | Pseudocódigo, `*args` e `**kwargs`, ordem de argumentos |
| `02_modulos_e_pacotes/` | Módulos próprios (`utils.py` + `moduled_file.py`), uso de pacotes nativos (`os`, `json`) e arquivos de exemplo (`.json`) |
| `03_pandas/` | Exercício prático com Pandas (leitura de CSV/JSONL, merge, filtro, exportação) — os dados usados ficam em `data/` |
| `04_classes_e_oop/` | Classes, encapsulamento e polimorfismo |
| `05_loops/` | Exemplo de loop processando uma lista em batches |

## Como rodar

1. Ative o ambiente virtual (venv) na raiz do seu projeto.
2. Instale as dependências necessárias, por exemplo:
   ```
   pip install pandas
   ```
3. Para os scripts da pasta `03_pandas/`, rode a partir de **dentro** dessa
   pasta (os caminhos dos arquivos são relativos a `data/`):
   ```
   cd 03_pandas
   python pandas_practice.py
   ```

## Observação

O arquivo `moduled_file.py` importa funções de `utils.py` — os dois precisam
permanecer na mesma pasta para o `import` funcionar.
