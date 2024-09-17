# 107 - Crie um módulo chamado moeda que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Crie também um programa que importe e use essas funções
# 108 - Adapte o código do ex107, criando uma função moeda() que mostre o valor como um valor monetário formatado
# 109 - Modifique as funções do ex107 para que elas aceitem mais um parâmetro, cujo qual vai dizer se os valores retornados serão formatados pela função moeda() ou não

from utilidadesCeV import moeda


n = float(input("Informe o preço: R$"))

while True:
    f = input("Deseja formatar os valores? [S/N] ")
    if f in "Ss":
        f = True
        break
    elif f in "Nn":
        f = False
        break
    else:
        print(f"Opção inválida, tente novamente.\n")

while True:
    x = int(input("\n[1] para aumentar o preço\n[2] para diminuir o preço\n[3] para ver o dobro do preço\n[4] para ver a metade do preço\n[5] para sair\n-> "))
    if x == 1:
        p = float(input("\nDeseja aumentar o preço em quantos %? "))
        print(f"{moeda.moeda(n)} + {p}% = {moeda.aumentar(n, p, f)}")
    elif x == 2:
        p = float(input(f"\nDeseja diminuir o preço em quantos %? "))
        print(f"{moeda.moeda(n)} - {p}% = {moeda.diminuir(n, p, f)}")
    elif x == 3:
        print(f"\nO dobro de {moeda.moeda(n)} é {moeda.dobro(n, f)}")
    elif x == 4:
        print(f"\nA metade de {moeda.moeda(n)} é {moeda.metade(n, f)}")
    elif x == 5:
        break
    else:
        print("Opção inválida, tente novamente.")