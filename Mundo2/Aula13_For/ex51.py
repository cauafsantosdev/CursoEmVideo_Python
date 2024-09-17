# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite sua razão: "))

for i in range(1, 11):
    pa = a1 + (i - 1) * r
    print(pa, end=" ")

print()
