# Crie um programa que leia vários números inteiros e pare quando o usuário digitar 999. No final, mostre quantos números foram digitados e qual foi a soma de todos eles.

c = s = n = 0

print("Digite quantos números quiser, ao terminar digite 999\n")

while n != 999:
    c += 1
    s += n
    n = int(input(f"Insira um número: "))

print(f"Foram digitados {c - 1} números e a soma entre eles é igual a {s}")
