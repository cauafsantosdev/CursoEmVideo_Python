# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou o tempo de alisamento.

a = int(input("Digite seu ano de nascimento: "))
i = 2024 - a

if a > 2024:
    print("Ano inválido.")
elif i < 18:
    print(f"Faltam {18 - i} anos para se alistar")
elif i == 18:
    print(f"Está na hora de se alistar")
elif i == 19:
    print(f"Alistamento atrasado por {i - 18} ano")
else:
    print(f"Alistamento atrasado por {i - 18} anos")
