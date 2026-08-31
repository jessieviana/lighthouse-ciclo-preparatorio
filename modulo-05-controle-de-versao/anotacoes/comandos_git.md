# Comandos Git praticados

| Comando | O que faz |
|---|---|
| `git status` | Mostra branch e estado dos arquivos |
| `git switch -c feature/nome` | Cria uma feature e muda para ela |
| `git diff` | Mostra alterações ainda não preparadas |
| `git diff --cached` | Mostra alterações na staging area |
| `git add caminho` | Prepara arquivos específicos para o commit |
| `git commit -m "mensagem"` | Registra as alterações preparadas |
| `git push -u origin branch` | Publica a branch e configura seu rastreamento |
| `git pull origin develop` | Atualiza a `develop` local a partir do remoto |
| `git branch -d branch` | Apaga uma branch local já integrada |
| `git log --oneline` | Exibe o histórico resumido de commits |

## Cuidados que pratiquei

- verificar `git status` antes de preparar ou enviar arquivos;
- usar `git add` com um caminho específico para evitar arquivos inesperados;
- conferir a direção do PR: `feature` para `develop`;
- testar as alterações antes do commit;
- apagar a feature somente depois do merge;
- evitar `git reset --hard`, pois ele pode descartar mudanças locais;
- usar `.gitignore` para ambientes virtuais, credenciais e arquivos temporários.
