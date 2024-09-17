# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = float(input("Digite o salário do funcionário: "))

print(f"Receberá um aumento de 15%, totalizando R${s + (s * 15 / 100):.2f}")
