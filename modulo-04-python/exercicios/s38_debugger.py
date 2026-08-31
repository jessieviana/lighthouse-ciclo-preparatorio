# S38 - Debugger
# Objetivo: praticar o uso do debugger do VSCode (breakpoints,
# step over/into, inspeção de variáveis) em um código com erro proposital.


def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    return total / quantidade


notas = [7.5, 8.0, 9.0, 6.5]

# Coloque um breakpoint na linha abaixo e inspecione as variáveis no VS Code.
media = calcular_media(notas)
print(f"Média: {media:.2f}")
