# Faça um programa que leia uma frase e mostre quantas vezes aparece a letra "A", em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez

frase = input("Digite uma frase: ")

frase = frase.lower()

print(f"A letra A aparece {frase.count('a')} vezes")
print(f"Aparece pela primeira vez em {frase.find('a')}")
print(f"E pela última vez em {frase.rfind('a')}")
