# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
maior = 0
menor = 0

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

c = int(input("Informe o terceiro número: "))

if c > maior:
    maior = c
if c < menor:
    menor = c

print(f"Entre {a}, {b} e {c}, o maior número é {maior} e o menor número é {menor}")
