# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior ou não existe valor maior, os dois são iguais.

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if x > y:
    print(f"{x} é maior que {y}")
elif y > x:
    print(f"{y} é maior que {x}")
else:
    print(f"{x} e {y} são iguais")
