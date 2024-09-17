# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: de 1 até 10, de 1 em 1, de 10 até 0, de 2 em 2 e uma contagem personalizada.

def contador(i, f, p):
    if p == 0:
        p = 1
    print(f"\nContagem de {i} até {f} de {p} em {p}:")
    if i < f:
        for n in range(i, f + 1, p):
            print(f"{n} ", end="")
        print()
    elif i > f:
        if p > 0:
            p *= -1
        for n in range(i, f - 1, p):
            print(f"{n} ", end="")
        print()


contador(1, 10, 1)
contador(10, 0, 2)

print()

i = int(input("Informe o início da contagem: "))
f = int(input("Informe o fim da contagem: "))
p = int(input("Informe de quanto em quanto será a contagem: "))

contador(i, f, p)
