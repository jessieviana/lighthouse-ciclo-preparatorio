import os
import json

# A lógica aqui seria, a partir do pesudocódigo de permissão para a festa
# Criarmos um código com os módulos que criasse um txt com uma frase de convite

with open("convidados.json", "r") as opened_file:
    convidados = json.load(opened_file)

for convidado in convidados:
    nome = convidado["nome"]
    if convidado["idade"] >= 21:
        convite = f"Olá {nome}, gostaria de te convidar à minha festa!"
        pasta="convites"
        os.makedirs(pasta, exist_ok=True)
        file_path = os.path.join(pasta, f"{nome}.txt")
        with open(file_path, "w") as new_file:
            new_file.write(convite)
    else:
        print(f"Cai fora {nome}lito!")
