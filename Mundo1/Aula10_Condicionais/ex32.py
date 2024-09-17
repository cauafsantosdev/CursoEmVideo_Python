# Faça um programa que leia um ano qualquer e diga se ele é bissexto

a = int(input("Informe um ano: "))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
	print(f"{a} é bissexto")
else:
    print(f"{a} não é bissexto")
