# Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = input("Informe seu sexo (M ou F): ").upper()

while sexo != "M" and sexo != "F":
    print("Resposta inválida\n")
    sexo = input("Informe seu sexo (M ou F): ").upper()

if sexo == "M":
    print("Sexo Masculino")
else:
    print("Sexo Feminino")
