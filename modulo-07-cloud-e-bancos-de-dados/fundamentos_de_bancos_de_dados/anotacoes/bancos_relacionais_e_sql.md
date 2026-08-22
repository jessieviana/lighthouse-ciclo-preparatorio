# Bancos relacionais e SQL

## Estrutura relacional

Em um banco relacional, os dados são organizados em tabelas:

- **coluna ou campo:** representa um atributo e possui um tipo de dado;
- **linha ou registro:** representa uma ocorrência;
- **chave primária:** identifica cada registro de forma única;
- **chave estrangeira:** conecta registros de tabelas diferentes;
- **constraint:** aplica uma regra de integridade aos dados.

As relações entre tabelas reduzem repetição, aumentam a consistência e permitem combinar informações por meio de consultas.

## Índices

Um índice mantém uma estrutura auxiliar para localizar valores mais rapidamente. Sem um índice adequado, o SGBD pode precisar percorrer grande parte ou toda a tabela.

Índices podem melhorar consultas, mas também ocupam espaço e adicionam custo às operações de escrita. Por isso, devem ser definidos de acordo com os padrões reais de acesso.

## Categorias de comandos SQL

| Categoria | Finalidade | Exemplos |
| --- | --- | --- |
| DDL | definir estruturas do banco | `CREATE`, `ALTER`, `DROP` |
| DML | inserir, alterar e remover dados | `INSERT`, `UPDATE`, `DELETE` |
| DQL | consultar dados | `SELECT` |
| DCL | controlar permissões | `GRANT`, `REVOKE` |
| TCL | controlar transações | `BEGIN`, `COMMIT`, `ROLLBACK` |

Algumas referências usam a sigla DTL para a linguagem de controle de transações. Neste registro adoto TCL, nomenclatura bastante comum na documentação técnica.

## Banco de dados e planilha

Planilhas são úteis para análises menores e flexíveis. Bancos de dados tornam-se mais adequados quando há maior volume, múltiplos usuários, necessidade de regras de integridade, consultas reproduzíveis e controle de acesso.
