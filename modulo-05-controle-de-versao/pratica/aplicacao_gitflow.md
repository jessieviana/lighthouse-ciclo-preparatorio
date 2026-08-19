# Aplicação prática do GitFlow

Usei o próprio repositório do Ciclo Preparatório para praticar o fluxo estudado.

## Fluxo realizado

1. Mantive a `main` como versão estável e a `develop` como branch de integração.
2. Criei uma feature a partir da `develop`.
3. Conferi as alterações com `git status` e `git diff`.
4. Preparei somente os arquivos relacionados à tarefa.
5. Criei um commit com mensagem descritiva.
6. Publiquei a feature no GitHub.
7. Abri um pull request da feature para a `develop`.
8. Revisei os arquivos, realizei o merge e apaguei a branch remota.
9. Voltei para a `develop`, executei o pull e apaguei a feature local.

## Exemplos neste repositório

- [PR #9 - conclusão dos exercícios do módulo 04](https://github.com/jessieviana/lighthouse-ciclo-preparatorio/pull/9)
- [PR #10 - organização e atribuição dos exemplos](https://github.com/jessieviana/lighthouse-ciclo-preparatorio/pull/10)

Esses pull requests mostram a separação entre desenvolvimento e versão estável,
o uso de commits focados e a revisão da direção do merge antes da integração.
