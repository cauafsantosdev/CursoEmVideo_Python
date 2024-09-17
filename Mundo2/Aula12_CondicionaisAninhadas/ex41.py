#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta   e mostre sua categoria, de acordo com a idade: até 9 anos é mirim, até 14 anos é infantil, até 19 anos é junior, até 20 anos é sênior, acima de 20 é master 

a = int(input("Digite seu ano de nascimento: "))
i = 2024 - a

if a > 2024:
    print("Ano inválido.")
elif i <= 9:
    print("Atleta mirim.")
elif i <= 14:
    print("Atleta infantil.")
elif i <= 19:
    print("Atleta junior.")
elif i == 20:
    print("Atleta sênior.")
else:
    print("Atleta master.")
