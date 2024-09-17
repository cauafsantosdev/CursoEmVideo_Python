# Dentro do pacote utilidadesCeV, criado no ex111, temos um módulo chamado dado. Nele, crie uma função chamada leiaDInheiro() que funcione como um input mas com validação de dados para aceitar apenas valores monetários

from utilidadesCeV import moeda, dado


n = dado.leiaDinheiro()
pa = dado.leiaPorcentagem("Deseja aumentar o preço em quantos %? Se não, digite 0. ")
pr = dado.leiaPorcentagem("Deseja reduzir o preço em quantos %? Se não, digite 0. ")
print()
moeda.resumo(n, pa, pr)