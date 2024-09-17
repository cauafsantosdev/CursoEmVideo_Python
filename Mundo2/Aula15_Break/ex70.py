nome = ""
# Crie um programa que leia o nome e o preço de vários produtos, perguntando ao usuário se ele deseja continuar ou não. Ao final mostre qual o total gasto na compra, quantos produtos custam mais de R$1000 e qual o nome do produto mais barato

caro = barato = c = total = 0

while True:
    produto = input("Insira o nome do produto: ")
    preco = float(input(f"Qual o valor de {produto}? R$"))
    c = c + 1
    total += preco
    if c == 1:
        barato = preco
        nome = produto
    if preco > 1000:
        caro += 1
    if preco < barato:
        barato = preco
        nome = produto
    fim = input("Deseja adicionar mais algum produto? [S/N] ")
    while fim != "S" and fim != "N":
        fim = input("Resposta inválida, deseja adicionar mais algum produto? [S/N] ").upper()
    if fim == "N":
        break
    print()
    
print(f"\nO total gasto foi R${total:.2f}\n{caro} produtos custaram mais de R$1000\nE {nome}, que custou R${barato:.2f} foi o produto mais barato.")
