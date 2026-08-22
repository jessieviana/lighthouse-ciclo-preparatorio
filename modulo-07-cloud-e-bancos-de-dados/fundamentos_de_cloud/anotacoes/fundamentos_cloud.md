# Fundamentos de Cloud

## O que é computação em nuvem

Computação em nuvem é a disponibilização de recursos de tecnologia pela internet. Em vez de comprar e manter toda a infraestrutura física, uma organização pode utilizar processamento, armazenamento, bancos de dados, redes e outros serviços conforme a necessidade.

Esse modelo facilita o início de projetos, reduz o tempo necessário para disponibilizar recursos e permite adaptar a capacidade do ambiente à demanda.

## Características importantes

### Recursos sob demanda

Serviços podem ser provisionados quando necessários, geralmente por console, linha de comando, API ou infraestrutura como código.

### Escalabilidade

É a capacidade de aumentar ou reduzir recursos para atender mudanças de carga. A escala pode ser vertical, alterando a capacidade de uma máquina, ou horizontal, adicionando mais instâncias.

### Elasticidade

É o ajuste dinâmico da capacidade de acordo com a demanda. Ela evita tanto a falta de recursos quanto o desperdício causado por infraestrutura ociosa.

### Pagamento conforme o uso

Muitos serviços cobram pelos recursos consumidos. Essa flexibilidade exige acompanhamento, orçamento e otimização contínua.

### Alta disponibilidade

Provedores organizam a infraestrutura em regiões e zonas de disponibilidade. Distribuir componentes pode reduzir o impacto de falhas, mas essa resiliência precisa ser planejada na arquitetura.

## Modelos de serviço

| Modelo | O que oferece | Responsabilidade do cliente |
|---|---|---|
| IaaS | Infraestrutura, redes, máquinas virtuais e armazenamento | Sistema operacional, aplicações, dados e parte das configurações de segurança |
| PaaS | Plataforma gerenciada para executar aplicações | Código, dados e configurações da aplicação |
| SaaS | Software pronto acessado como serviço | Uso, acesso, dados inseridos e configurações disponíveis |

Quanto mais gerenciado é o serviço, menor tende a ser o esforço operacional do cliente. Em contrapartida, também pode existir menos controle sobre a infraestrutura.

## Modelos de implantação

- **nuvem pública:** recursos oferecidos por um provedor e compartilhados com isolamento entre clientes;
- **nuvem privada:** ambiente dedicado a uma única organização;
- **nuvem híbrida:** integração entre ambientes locais ou privados e serviços de nuvem;
- **multicloud:** utilização de mais de um provedor conforme necessidades técnicas ou estratégicas.
