# Faça um programa que jogue par ou ímpar com o computador e só pare quando o usuário perder, mostrando o total de vitórias consecutivas

from random import randint

c = 0

while True:
    j = input("PAR ou ÍMPAR? ").lower()
    while j != "par" and j != "ímpar":
        j = input("Resposta inválida, PAR ou ÍMPAR? ").lower()
    n = int(input("Jogue um número: "))
    cpu = randint(0, 10)
    t = n + cpu
    print(f"\nO computador jogou {cpu}, resultando em {t}")
    if j == "par": 
        if t % 2 != 0:
            print(f"Deu ímpar, PERDEU após {c} vitórias")
            break
        if t % 2 == 0:
            c += 1
            print("Deu par, GANHOU!\n")
    elif j == "ímpar":
        if t % 2 == 0:
            print(f"Deu par, PERDEU após {c} vitórias!")
            break
        if t % 2 != 0:
            c += 1
            print("Deu ímpar, GANHOU!\n")
    print("Próxima rodada...\n")
