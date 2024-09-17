# Faça um programa que mostre a tabuada de vários números, um de cada vez. O programa deverá parar quando o usuário digitar um número negativo

c = 0

print("Insira um número para ver sua tabuada, para parar insira um número negativo.")

while True:
    n = int(input("Tabuada de: "))
    if n < 0:
        break
    while c <= 10:
        print(f"{n} x {c} = {n * c}")
        c = c + 1
    print()
    c = 0
