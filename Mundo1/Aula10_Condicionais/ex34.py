# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu amento. Para salários superiores a R$1.250, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%

s = float(input("Digite o salário do funcionário: "))

if s <= 1250:
    print(f"Receberá um aumento de 15%, totalizando R${s + (s * 15 / 100):.2f}")
else:
    print(f"Receberá um aumento de 10%, totalizando R${s + (s * 10 / 100):.2f}")
