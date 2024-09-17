# Crie um programa que faça o computador jogar pedra, papel, tesoura com você.

from random import randint

j = int(input("\nDigite 1 para jogar pedra\nDigite 2 para jogar papel\nDigite 3 para jogar tesoura\n-> "))

m = randint(1, 3)

if j == 1:
    if m == 1:
        print("\nPedra x Pedra = Empate")
    elif m == 2:
        print("\nPedra x Papel = Derrota")
    else:
        print("\nPedra x Tesoura = Vitória")
elif j == 2:
    if m == 1:
        print("\nPapel x Pedra = Vitória")
    elif m == 2:
        print("\nPapel x Papel = Empate")
    else:
        print("\nPapel x Tesoura = Derrota")
elif j == 3:
    if m == 1:
        print("\nTesoura x Pedra = Derrota")
    elif m == 2:
        print("\nTesoura x Papel = Vitória")
    else:
        print("\nTesoura x Tesoura = Empate")
