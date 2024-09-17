# Faça um programa que ajude um jogador da Mega Sena a criar palpites. Primeiro vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

x = int(input("Quantos jogos serão gerados? "))
jogos = []

print()

for i in range(0, x):
    for j in range(0, 6):
        n = randint(1, 60)
        while n in jogos:
            n = randint(1, 60)
        jogos.append(n)
    jogos.sort()
    print(f"Jogo {i + 1}: {jogos}")
    jogos.clear()
    sleep(0.4)
