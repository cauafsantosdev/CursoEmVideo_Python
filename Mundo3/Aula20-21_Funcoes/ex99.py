# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(n):
    c = 0
    maior = n[c]
    while c < len(n):
        print(f"{n[c]}", end=" ")
        if n[c] > maior:
            maior = n[c]
        c += 1
    print(f"foram digitados {len(n)} números")
    print(f"O maior número digitado foi {maior}")

n = []

while True:
    x = int(input("Digite um número: "))
    n.append(x)
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        print()
        break
    print()

maior(n)
