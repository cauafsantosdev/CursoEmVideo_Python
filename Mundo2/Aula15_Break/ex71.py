# Crie um programa que simule o funcionamento de um caixa eletrônico. Leia o valor a ser sacada e informe o número de cédular que serão entregues. O caixa possui cédulas de R$50, R$20, R$10, R$5 e R$1

cinq = vinte = dez = cinco = um = 0

while True:
    valor = int(input("Quanto deseja sacar? R$"))
    v = valor
    while valor - 50 >= 0:
        valor -= 50
        cinq += 1
    while valor - 20 >= 0:
        valor -= 20
        vinte += 1
    while valor - 10 >= 0:
        valor -= 10
        dez += 1
    while valor - 5 >= 0:
        valor -= 5
        cinco += 1
    while valor - 1 >= 0:
        valor -= 1
        um += 1
    if valor == 0:
        break

print(f"\nR${v} foi sacado em:")
print(f"{cinq} notas de R$50" if cinq > 0 else "", end="\n" if cinq > 0 else "")
print(f"{vinte} notas de R$20" if vinte > 0 else "", end="\n" if vinte > 0 else "")
print(f"{dez} notas de R$10" if dez > 0 else "", end="\n" if dez > 0 else "")
print(f"{cinco} notas de R$5" if cinco > 0 else "", end="\n" if cinco > 0 else "")
print(f"{um} notas de R$1" if um > 0 else "", end="\n" if um > 0 else "")
