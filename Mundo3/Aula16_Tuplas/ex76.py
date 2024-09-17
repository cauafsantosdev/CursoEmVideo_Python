# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre a listagem de preços, organizando os dados de forma tabular

t = ()

while True:
    produto = input("Qual o nome do produto? ")
    preco = float(input(f"Qual o preço de {produto}? R$"))
    t += produto, preco, 
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

print()
print(f"{'TABELA DE PREÇOS:':^40}")
print()

for i in range(0, len(t)):
    if i % 2 == 0:
        print(f"{t[i]:.<30}", end="")
    else:
        print(f"R${t[i]:>7.2f}")
        
