# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input("Digite seu nome: ")

if "Silva" in nome:
    print(f"{nome} é só mais um Silva")
else:
    print(f"{nome} é mais do que um Silva")
