# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

a1 = input("Nome do aluno 1: ")
a2 = input("Nome do aluno 2: ")
a3 = input("Nome do aluno 3: ")
a4 = input("Nome do aluno 4: ")

l = [a1, a2, a3, a4]

shuffle(l)

print(f"A ordem das apresentações será: \n1. {l[0]}\n2. {l[1]}\n3. {l[2]}\n4. {l[3]}")
