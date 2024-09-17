# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

x = input("Digite uma frase: ")
frase = x.replace(" ", "").lower()
invertida = frase[::-1]

if frase == invertida:
    print(f"{x} é um palíndromo")
else:
    print(f"{x} não é um palíndromo")
