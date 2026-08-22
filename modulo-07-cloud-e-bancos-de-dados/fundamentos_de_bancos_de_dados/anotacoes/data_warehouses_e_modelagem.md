# Data Warehouses e modelagem

## OLTP e OLAP

| Característica | OLTP | OLAP |
| --- | --- | --- |
| Objetivo | operações do dia a dia | análises e relatórios |
| Prioridade | escrita rápida e integridade | leitura e agregação eficientes |
| Estrutura comum | mais normalizada | frequentemente dimensional |
| Armazenamento comum | orientado a linhas | frequentemente orientado a colunas |

Um Data Warehouse integra dados de diferentes fontes e preserva histórico para análises. Modelos dimensionais facilitam consultas analíticas sobre grandes volumes de dados.

## Armazenamento em linhas e colunas

- **Orientado a linhas:** mantém juntos os campos de cada registro e é apropriado para operações transacionais frequentes.
- **Orientado a colunas:** mantém juntos valores da mesma coluna e favorece leituras seletivas e agregações analíticas.

## Modelo entidade-relacionamento

O modelo entidade-relacionamento representa:

- entidades relevantes para o domínio;
- atributos que descrevem essas entidades;
- relacionamentos entre elas;
- cardinalidades, como um para um, um para muitos e muitos para muitos.

Antes da implementação, esse modelo ajuda a tornar regras e relações do domínio mais visíveis.

## Normalização

A normalização organiza tabelas para reduzir redundância e anomalias de inserção, atualização ou exclusão. Ela favorece consistência e integridade, embora uma estrutura muito normalizada possa exigir mais junções em consultas analíticas.

## Star Schema e Snowflake Schema

- **Star Schema:** concentra medidas em uma tabela fato ligada diretamente às dimensões; costuma ser mais simples para consultas.
- **Snowflake Schema:** normaliza parte das dimensões em tabelas adicionais; reduz redundância, mas aumenta o número de relações.

A escolha depende do objetivo, do volume, do desempenho esperado e da facilidade de uso para análise.
