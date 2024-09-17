# Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

v = float(input("Qual o valor da casa? R$"))
s = float(input("Qual seu salário? R$"))
a = int(input("Em quantos anos irá pagar? "))

p = v / (a * 12)

if p > s * 30 / 100:
    print("\nEmpréstimo negado.")
else:
    print(f"\nEmpréstimo aceito por {a * 12} parcelas de R${p:.2f}") 
