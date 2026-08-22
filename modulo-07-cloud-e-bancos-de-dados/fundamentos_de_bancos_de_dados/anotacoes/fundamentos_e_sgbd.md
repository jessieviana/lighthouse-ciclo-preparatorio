# Fundamentos de bancos de dados e SGBDs

## Banco de dados

Um banco de dados é uma coleção organizada de informações armazenadas de modo que possam ser consultadas, atualizadas e relacionadas com eficiência.

## Tipos de dados

- **Estruturados:** seguem um esquema definido, como linhas e colunas de uma tabela relacional.
- **Semiestruturados:** possuem alguma organização, mas não dependem de um esquema tabular rígido, como documentos JSON.
- **Não estruturados:** não possuem um modelo de dados predefinido, como imagens, vídeos, PDFs e textos livres.

## Sistema Gerenciador de Banco de Dados

Um SGBD é o conjunto de programas que permite criar, armazenar, consultar, alterar, proteger e recuperar dados. Entre seus componentes estão:

- motor do banco de dados;
- processador e otimizador de consultas;
- gestor de transações;
- gestor de armazenamento.

Exemplos de SGBDs relacionais incluem PostgreSQL, MySQL, Oracle, SQL Server e IBM Db2. MongoDB, Cassandra, Redis e CouchDB são exemplos associados a modelos NoSQL.

## Arquitetura em camadas

Os dados podem ser observados em três níveis:

1. **Físico ou interno:** trata de arquivos, índices e armazenamento em disco.
2. **Lógico ou conceitual:** descreve tabelas, regras e relacionamentos.
3. **Externo ou de visão:** oferece recortes específicos para usuários e aplicações.

Essa separação favorece abstração e independência: mudanças na forma de armazenamento não precisam alterar a maneira como cada usuário enxerga os dados.

## Transações e propriedades ACID

- **Atomicidade:** uma transação é concluída por inteiro ou desfeita por inteiro.
- **Consistência:** as regras de integridade devem ser respeitadas antes e depois da transação.
- **Isolamento:** transações simultâneas não devem produzir interferências indevidas.
- **Durabilidade:** depois do `COMMIT`, as alterações confirmadas devem permanecer mesmo após falhas.

Os comandos `COMMIT` e `ROLLBACK` ajudam a confirmar ou desfazer operações de uma transação.

## Formas de interação

É possível interagir com um SGBD pelo terminal, por ferramentas nativas do fornecedor ou por aplicações independentes, como o DBeaver.
