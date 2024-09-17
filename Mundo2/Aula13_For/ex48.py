# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        s += i

print(f"A soma de todos os ímpares múltiplos de 3 entre 1 e 500 é {s}")
