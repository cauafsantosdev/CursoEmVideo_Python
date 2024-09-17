# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a carteira for diferente de 0, o dicionário também receberá o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

ano = 2024
trabalhador = {}

trabalhador['Nome'] = input("Digite seu nome: ")

trabalhador['nascimento'] = int(input("Digite seu ano de nascimento: "))
trabalhador['Idade'] = ano - trabalhador['nascimento']
del trabalhador['nascimento']

trabalhador['Carteira de Trabalho'] = int(input("Digite o número da sua carteira de trabalho: "))

if trabalhador['Carteira de Trabalho'] != 0:
    trabalhador['Ano de Contratação'] = int(input("Digite seu ano de contratação: "))
    salario = float(input("Digite seu salário: "))
    trabalhador['Salário'] = f"R${salario:.2f}"
    trabalhador['Aposentadoria'] = f"Faltam {35 - (ano - trabalhador ['Ano de Contratação'])} anos"
    print()
    for k, v in trabalhador.items():
        print(f"{k}: {v}")
else:
    print()
    for k, v in trabalhador.items():
        print(f"{k}: {v}")
