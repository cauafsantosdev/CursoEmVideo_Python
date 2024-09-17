# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

menor = 0
maior = 0

for i in range(1, 8):
    ano = int(input("Em que ano a {i}º pessoa nasceu? "))
    if 2024 - ano >= 18:
        maior += 1
    else:
        menor += 1

print(f"Temos {menor} menores de idade e {maior} maiores de idade")
