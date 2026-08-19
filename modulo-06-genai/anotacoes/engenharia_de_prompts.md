# Engenharia de prompts

Engenharia de prompts é a prática de fornecer instruções claras, contextualizadas e específicas. Não se trata de uma fórmula mágica: quanto melhor a descrição do problema, maiores são as chances de a resposta ser útil.

## Quatro elementos de um bom prompt

1. **Persona:** indica a perspectiva ou especialidade esperada.
2. **Contexto:** apresenta o ambiente, os dados e as restrições do problema.
3. **Tarefa:** descreve claramente o que deve ser feito.
4. **Formato:** define como a resposta deve ser entregue.

## Exemplo aplicado a dados

### Prompt pouco específico

> Crie uma consulta sobre vendas.

Esse pedido permite muitas interpretações e provavelmente produzirá uma resposta genérica.

### Prompt mais completo

> Atue como analista de dados. Estou usando PostgreSQL e possuo as tabelas `pedidos(id_pedido, id_cliente, data_pedido, valor)` e `clientes(id_cliente, nome, estado)`. Escreva uma consulta que calcule o valor total de vendas por estado em outubro de 2024. Ordene o resultado do maior para o menor e explique resumidamente os relacionamentos utilizados.

Nesse segundo caso, a tecnologia, as tabelas, o período, o cálculo e o formato estão definidos. Ainda assim, a consulta gerada precisa ser revisada e executada com dados de teste.

## Processo de uso

Um fluxo mais seguro é:

1. descrever o problema e fornecer apenas o contexto necessário;
2. solicitar uma resposta que possa ser compreendida e verificada;
3. revisar cada parte da solução;
4. executar o código em um ambiente controlado;
5. comparar o resultado com o objetivo e ajustar o prompt quando necessário;
6. registrar o que foi alterado e aprendido.

O prompt pode acelerar o início da tarefa, mas testar e entender a saída é parte indispensável do trabalho.
