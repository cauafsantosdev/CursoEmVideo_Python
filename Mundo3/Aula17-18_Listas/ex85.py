# Crie um programa que leia 7 valores númericos e os cadastre em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

l = [[], []]

for i in range(0, 7):
    n = int(input(f"Digite o {i + 1}º número: "))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)

l[0].sort()
l[1].sort()

print(f"\nOs pares são {l[0]}\nOs ímpares são {l[1]}")
