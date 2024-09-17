# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5.0 = reprovado, média entre 5.0 e 6.9 = recuperação, média acima de 7.0 = aprovado

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

if (n1 + n2) / 2 >= 7:
	print("Aprovado")
elif (n1 + n2) / 2 >= 5:
	print("Recuperação")
else:
	print("Reprovado")
