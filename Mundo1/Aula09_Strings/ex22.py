# Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.

nome = input("Digite seu nome: ")

print(nome.upper())
print(nome.lower())

nome_junto = nome.replace(" ", "")
print(f"{nome} possui {len(nome_junto)} letras")

primeiro_nome = nome.split()
print(f"{primeiro_nome[0]} possui {len(primeiro_nome[0])} letras")
