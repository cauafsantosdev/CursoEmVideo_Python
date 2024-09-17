# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.

soma = 0
maior = 0
menor = 0

for i in range(1, 5):
    print(f"- {i}º Pessoa -")
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    sexo = input("Informe seu sexo: ").lower()
    soma += idade
    print()
    if sexo == "masculino" and idade > maior:
        velho = nome
    if sexo == "feminino" and idade < 20:
        menor += 1

print(f"A média de idade do grupo é de {soma / 4:.2f}\nO homem mais velho é o {velho}\nE existem {menor} mulheres com menos de 20 anos")
