# Crie um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as pessoas mais leves

l = []

while True:
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso em Kg: "))
    l.append([nome, peso])
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

print(f"\nForam cadastradas {len(l)} pessoas")

l = sorted(l, key=lambda x:x[1])
leve = l[:len(l)//2]
pesado = sorted(l[len(l)//2:], reverse = True)

print(f"\nAs mais leves são: ")
for nome, peso in leve:
    print(f"- {nome} com {peso:.2f}Kgs")
    
print(f"\nAs mais pesadas são: ")
for nome, peso in pesado:
    print(f"- {nome} com {peso:.2f}Kgs")
    
