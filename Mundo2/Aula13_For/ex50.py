# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for impar, desconsidere-o.

s = 0

for i in range(1, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        s += n

print(f"\nA soma dos números pares é: {s}")
