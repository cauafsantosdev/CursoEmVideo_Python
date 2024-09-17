# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = input("Digite um número de até 4 digitos: ")

if len(n) == 1:
    u = n[0]
    print(f"Unidade: {u}")
elif len(n) == 2:
    d = n[0]
    u = n[1]
    print(f"Unidade: {u}\nDezena: {d}")   
elif len(n) == 3:
    c = n[0]
    d = n[1]
    u = n[2]
    print(f"Unidade: {u}\nDezena: {d}\nCentena: {c}")
else:
    m = n[0]
    c = n[1]
    d = n[2]
    u = n[3]
    print(f"Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}")


print()

n = int(n)

if n < 10:
    print(f"Unidade: {n}")
elif n < 100:
    d1 = n % 10
    d2 = (n // 10) % 10
    print(f"Unidade: {d1}\nDezena: {d2}")
elif n < 1000:
    d1 = n % 10
    d2 = (n // 10) % 10
    d3 = (n // 100) % 10
    print(f"Unidade: {d1}\nDezena: {d2}\nCentena: {d3}")
else:
    d1 = n % 10
    d2 = (n // 10) % 10
    d3 = (n // 100) % 10
    d4 = n // 1000
    print(f"Unidade: {d1}\nDezena: {d2}\nCentena: {d3}\nMilhar: {d4}")
