# Conceitos de Git e GitHub

## Repositório

É o diretório versionado pelo Git. O repositório local fica no computador; o
remoto fica em uma plataforma como o GitHub. O remoto chamado `origin` está
vinculado à cópia local deste projeto.

## Branch

É uma ramificação do histórico. Ela permite desenvolver uma mudança sem alterar
diretamente a versão estável. Neste repositório, uso:

- `main`: versão estável;
- `develop`: integração dos módulos em desenvolvimento;
- `feature/...`: mudança específica e temporária.

## Commit

Registra um conjunto de alterações preparado na staging area. Cada commit possui
um identificador único, autor, data e mensagem. Mensagens objetivas ajudam a
entender por que a alteração foi realizada.

## Pull request

É uma proposta para integrar uma branch em outra. Antes do merge, o GitHub mostra
os commits e arquivos alterados, permitindo revisar a direção e o conteúdo.

## Clone e fork

- `clone`: cria uma cópia local de um repositório remoto;
- `fork`: cria outro repositório a partir de um projeto existente, geralmente
  para contribuir quando não há permissão de escrita no original.

## GitFlow aplicado

As features nascem da `develop`, recebem commits e são enviadas ao GitHub. Depois
da revisão em pull request, são mescladas novamente na `develop`. A `main` só é
atualizada quando o conjunto do trabalho está pronto para uma versão estável.
