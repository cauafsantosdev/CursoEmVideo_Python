# Crie um programa que leia um número inteiro e pergunte ao usuário se ele quer continuar inserindo números. No final, mostre a média entre todos os números, o maior e o menor número lido.

fim = "S"
c = s = menor = maior = 0

while fim != "N":
    n = int(input("Digite um número: "))
    fim = input("Deseja inserir mais números [S/N]? ").upper()
    print()
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

print(f"O menor número digitado foi {menor}\nO maior número digitado foi {maior}\nE a média entre todos os números digitados é igual a {s / (c):.2f}")
