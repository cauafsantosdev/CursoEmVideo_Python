# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. NO final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado

from random import randint
from time import sleep

jogadores = {}
resultado = []

for i in range(0, 4):
    jogadores['nome'] = input("Digite o nome do jogador: ")
    jogadores['dado'] = randint(1, 6)
    sleep(0.3)
    print(f"{jogadores['nome']} jogou {jogadores['dado']}")
    resultado.append(jogadores.copy())

print()

resultado = sorted(resultado, key=lambda d: d['dado'], reverse = True)

print("RESULTADOS:\n")

for i in range(0, len(resultado)):
    print(f"{i + 1}º - {resultado[i]['nome']} ({resultado[i]['dado']})")
    sleep(0.4)
