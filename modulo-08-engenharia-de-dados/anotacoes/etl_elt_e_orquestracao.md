# ETL, ELT e orquestração

## ETL

No processo ETL, a ordem é:

1. **Extract:** extrair os dados das fontes.
2. **Transform:** limpar, combinar e adaptar os dados antes do destino.
3. **Load:** carregar o resultado no ambiente de armazenamento.

Essa abordagem é útil quando os dados precisam chegar ao destino já tratados ou quando o ambiente de destino não deve realizar o processamento principal.

## ELT

No processo ELT, a ordem é:

1. **Extract:** extrair os dados.
2. **Load:** carregá-los no ambiente de destino.
3. **Transform:** executar as transformações usando a capacidade do próprio ambiente.

O ELT é comum em plataformas analíticas modernas porque separa carregamento e transformação, facilita modularidade e aproveita o poder computacional de Data Warehouses em nuvem. Ferramentas como dbt podem atuar na etapa de transformação.

## Orquestração

Orquestrar é coordenar e automatizar processos e cadeias de tarefas. Em dados, isso envolve definir dependências, agendamentos, tentativas, monitoramento e tratamento de falhas.

Benefícios importantes:

- gerenciamento consistente de workloads;
- escalabilidade de tarefas;
- visualização das dependências;
- redução de processos manuais e custos operacionais;
- monitoramento e diagnóstico de falhas.

Entre as ferramentas citadas na aula estão Apache Airflow, Azure Data Factory, Dagster e Databricks Workflows.

Além de dados, a orquestração pode ser aplicada a serviços, contêineres e recursos de nuvem.
