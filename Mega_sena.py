import random

def escolher_numeros():
    numeros = list(range(1, 61))  # Lista de números de 1 a 60
    escolhidos = random.sample(numeros, 6)  # Escolhe 6 números aleatórios sem repetição
    return escolhidos

numeros_escolhidos = escolher_numeros()
print(numeros_escolhidos)