# S40 - Código Limpo
# Objetivo: praticar princípios de código limpo e legível
# (nomes claros, funções pequenas, separação de responsabilidades).


def calcular_total(precos):
    return sum(precos)


def aplicar_desconto(valor, percentual):
    return valor * (1 - percentual / 100)


def formatar_reais(valor):
    return f"R$ {valor:.2f}"


def exibir_resumo_compra(precos, percentual_desconto):
    total = calcular_total(precos)
    total_com_desconto = aplicar_desconto(total, percentual_desconto)

    print(f"Total sem desconto: {formatar_reais(total)}")
    print(f"Desconto aplicado: {percentual_desconto}%")
    print(f"Total final: {formatar_reais(total_com_desconto)}")


precos = [35.90, 18.50, 42.00]
exibir_resumo_compra(precos, percentual_desconto=10)
