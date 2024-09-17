# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número: "))
primo = True

for i in range(2, 8):
    if n % i == 0:
        primo = False

if primo == True:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")
