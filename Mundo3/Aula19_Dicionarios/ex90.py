# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = {}

aluno['Nome'] = input("Nome do aluno: ")
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

if aluno['Média'] >= 7:
    aluno['Resultado'] = "aprovado"
elif aluno['Média'] >= 3:
    aluno['Resultado'] = "está em exame"
else:
    aluno['Resultado'] = "reprovado"

print()

for k, v in aluno.items():
    print(f"{k} é igual a {v}")
