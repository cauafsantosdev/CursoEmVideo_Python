# Escreva um programa que faça o computador sortear um número de 0 a 5 e peça ao usuário para adivinhar. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

sorteado = randint(0, 5)
n = int(input("Chute um número: "))

if n == sorteado:
    print("Parabéns, acertou!")
else:
    print("Errou!")
