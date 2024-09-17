# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

l = []

for i in range(0, 5):
    l.append(int(input("Digite um número: ")))

print(f"\nLista = {l}")
maior = max(l)
menor = min(l)

print(f"O maior valor é {max(l)} que está na posição {l.index(max(l))}")
print(f"O menor valor é {min(l)} que está na posição {l.index(min(l))}")
