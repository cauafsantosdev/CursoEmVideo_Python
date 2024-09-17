# Crie um programa que leia o nome duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

boletim = []

while True:
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    media = (n1 + n2) / 2
    boletim.append([nome, n1, n2, media])
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

boletim.sort()

print("\nBOLETIM DA TURMA:\n")
for i in range(0, len(boletim)):
    print(f"{boletim[i][0]} - {boletim[i][3]:.2f}")

print()

while True:
    fim = input("Deseja ver as notas de algum aluno? [S/N] ").upper()
    if fim == "N":
        break
    elif fim == "S":
        aluno = input("Qual aluno? ")
        for i in range(0, len(boletim)):
            if aluno in boletim[i]:
                print(f"\n{boletim[i][0]} - {boletim[i][1]:.2f} + {boletim[i][2]:.2f} = {boletim[i][3]:.2f}")
        print()
