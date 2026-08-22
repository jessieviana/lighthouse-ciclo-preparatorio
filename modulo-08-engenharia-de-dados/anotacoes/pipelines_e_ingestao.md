# Pipelines e ingestão de dados

## Pipeline de dados

Um pipeline representa o caminho percorrido pelos dados desde uma ou mais fontes até o destino em que serão armazenados, transformados ou consumidos. Ele integra sistemas e reduz processos manuais, silos de informação e inconsistências.

## Camada de ingestão

A ingestão coleta dados das fontes e os leva para ambientes como Data Warehouses, Data Lakes ou Data Marts. Ela pode ocorrer de duas maneiras principais.

### Batch

- processa dados em blocos;
- normalmente depende de agendamento;
- atende bem a grandes volumes que não exigem atualização imediata;
- tende a ser mais simples de implementar e operar.

### Streaming

- processa eventos continuamente ou com baixa latência;
- pode utilizar filas e sistemas orientados a eventos;
- atende casos que exigem informações próximas do tempo real;
- aumenta a complexidade de ordenação, consistência, escalabilidade e tolerância a falhas.

## Escolha da estratégia

A decisão entre batch e streaming depende do valor gerado pela velocidade. Nem todo caso precisa de tempo real: frequência de uso, volume, custo, complexidade e requisitos de negócio devem orientar a arquitetura.

Também é necessário decidir como as atualizações serão carregadas, por exemplo:

- carga completa (*full refresh*);
- carga incremental;
- atualização ou inserção conforme a existência do registro (*upsert*).
