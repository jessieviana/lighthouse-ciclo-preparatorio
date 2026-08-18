# S26 - Prática de Módulos
# Objetivo: explorar módulos nativos do Python (math, os e datetime).

import math
import os
from datetime import datetime


print("--- Explorando módulos nativos ---")

raiz = math.sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz}")

agora = datetime.now()
print(f"Data e hora atuais: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

pasta_atual = os.getcwd()
print(f"Diretório atual de trabalho: {pasta_atual}")
