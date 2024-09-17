# Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(a, b):
    if a == "":
        a = "<desconhecido>"
    if b == "":
        b = 0
    print(f"O jogador {a} marcou {b} gols")


jogador = input("Informe o nome do jogador: ")
gols = input("Informe quantos gols ele marcou: ")

ficha(jogador, gols)
