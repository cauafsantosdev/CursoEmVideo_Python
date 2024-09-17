# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

n = input("Digite seu nome: ")

nome = n.split()
primeiro = nome[0]
ultimo = nome[-1]

print(f"Primeiro nome: {primeiro}\nÚltimo nome: {ultimo}")
