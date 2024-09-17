# Adicione ao módulo moeda uma função chamada resumo() que mostre na tela as informações geradas pelas funções que o módulo possui até aqui

from utilidadesCeV import moeda


n = float(input("Informe o preço: R$"))
pa = float(input("\nDeseja aumentar o preço em quantos %? Se não, digite 0. "))
pr = float(input("\nDeseja reduzir o preço em quantos %? Se não, digite 0. "))

print()
moeda.resumo(n, pa, pr)