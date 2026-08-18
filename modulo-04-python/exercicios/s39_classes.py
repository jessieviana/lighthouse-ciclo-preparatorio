# S39 - Classes
# Objetivo: praticar a criação de classes, atributos, métodos,
# encapsulamento e polimorfismo.


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def exibir_dados(self):
        return f"{self.nome} recebe R$ {self.__salario:.2f}"

    def calcular_bonus(self):
        return self.__salario * 0.10


class Gerente(Funcionario):
    def calcular_bonus(self):
        return super().calcular_bonus() * 2


funcionarios = [
    Funcionario("Ana", 4000),
    Gerente("Bruno", 7000),
]

for funcionario in funcionarios:
    print(funcionario.exibir_dados())
    print(f"Bônus: R$ {funcionario.calcular_bonus():.2f}")
