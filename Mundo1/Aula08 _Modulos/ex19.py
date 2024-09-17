# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que leia o nome deles, escolha um e mostre o nome do escolhido

from random import choice

a1 = input("Nome do aluno 1: ")
a2 = input("Nome do aluno 2: ")
a3 = input("Nome do aluno 3: ")
a4 = input("Nome do aluno 4: ")

a = [a1, a2, a3, a4]

a = choice(a)

print(f"{a} apagará o quadro.")
