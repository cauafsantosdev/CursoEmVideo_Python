# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0

for i in range(1, 6):
    peso = float(input("Digite seu peso em Kg: "))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f"O maior peso foi {maior:.2f}Kg e o menor peso foi {menor:.2f}Kg")
