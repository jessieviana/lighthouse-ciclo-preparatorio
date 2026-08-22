# Segurança, custos e responsabilidades

## Responsabilidade compartilhada

Na nuvem, o provedor e o cliente dividem responsabilidades. De forma geral, o provedor protege a infraestrutura física e os serviços que opera, enquanto o cliente continua responsável por suas identidades, permissões, dados, configurações e aplicações.

O limite muda conforme o modelo escolhido. Em uma máquina virtual, o cliente administra mais componentes. Em um serviço totalmente gerenciado, o provedor assume uma parte maior da operação, mas o cliente ainda precisa configurar acessos e proteger os dados.

## Cuidados de segurança

- aplicar o princípio do menor privilégio;
- proteger credenciais e evitar armazená-las no código;
- utilizar autenticação multifator quando disponível;
- criptografar dados em trânsito e em repouso;
- manter logs e trilhas de auditoria;
- revisar configurações expostas à internet;
- realizar backups e testar a recuperação;
- definir responsabilidades e procedimentos para incidentes.

## Gestão de custos

O pagamento conforme o uso não significa custo baixo automaticamente. Recursos esquecidos, transferência de dados, armazenamento acumulado e capacidade superdimensionada podem aumentar a cobrança.

Algumas práticas importantes são:

- definir orçamentos e alertas;
- utilizar tags para identificar projetos e responsáveis;
- acompanhar relatórios de consumo;
- desligar recursos de estudo quando não estiverem sendo usados;
- escolher tamanhos adequados;
- avaliar serviços gerenciados considerando custo e esforço operacional;
- revisar a arquitetura de forma contínua.

## Decisão equilibrada

Uma boa arquitetura precisa equilibrar segurança, confiabilidade, desempenho, sustentabilidade operacional e custo. Otimizar apenas um desses pontos pode prejudicar os demais.
