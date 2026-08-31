# Papel do engenheiro de dados e boas práticas

## Decisões de projeto

Antes de implementar um pipeline, é importante perguntar:

- com que frequência os dados serão utilizados;
- qual volume será extraído e processado;
- como os dados mudam na fonte;
- se a carga será completa, incremental ou por upsert;
- qual conjunto de tecnologias atende melhor ao caso;
- como o pipeline reagirá a falhas, aumento de volume e mudanças.

Essas respostas ajudam a evitar arquiteturas complexas ou caras sem necessidade.

## Boas práticas

- **Princípio do menor privilégio:** conceder apenas as permissões necessárias para cada usuário ou serviço.
- **Legibilidade:** manter código claro, nomes compreensíveis e organização que facilite futuras alterações.
- **Controle de versão:** registrar mudanças e permitir colaboração e recuperação.
- **Qualidade dos dados:** garantir dados completos, consistentes, confiáveis e disponíveis no momento adequado.
- **Observabilidade:** acompanhar execuções, falhas e comportamento dos fluxos.
- **Foco no negócio:** construir uma plataforma que permita transformar dados em informação útil e ação.

O papel do engenheiro de dados combina decisões sobre ingestão, infraestrutura, nuvem, implantação e confiabilidade. A tecnologia deve servir ao problema, e não ser escolhida apenas por popularidade.
