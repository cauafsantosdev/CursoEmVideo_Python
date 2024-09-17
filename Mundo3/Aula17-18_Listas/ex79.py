# Crie um programa que leia vários valores numéricos e os cadastre em uma lista. Caso o número já exista na lista, não será adicionado. No final, mostre todos os valores únicos em ordem crescente

l = []

while True:
    n = int(input("Insira um número: "))
    if n not in l:
        l.append(n)
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

print(f"\n{sorted(l)}")
