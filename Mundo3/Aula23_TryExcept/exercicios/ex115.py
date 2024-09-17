# Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só terá 2 opções: cadastrar novas pessoas e listar todas as pessoas cadastradas

from modulo import cadastro

while True:
    x = cadastro.menu()
    if x == 1:
        cadastro.lista()
    elif x == 2:
        nome = cadastro.nome()
        idade = cadastro.idade()
        cadastro.cadastrar(nome, idade)
    elif x == 3:
        break