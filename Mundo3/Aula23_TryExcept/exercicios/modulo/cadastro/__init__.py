def menu():
    print("-" * 40)
    print(f"{'MENU PRINCIPAL':^40}")
    print("-" * 40)
    print("1 - Ver pessoas cadastradas\n2 - Cadastrar novas pessoas\n3 - Sair do sistema")
    print("-" * 40)
    while True:
        try:
            x = int(input("Sua opção: "))
        except:
            print(f"\033[0;31mERRO! Digite um número entre 1 e 3.\033[m\n")
        else:
            if x < 1 or x > 3:
                print(f"\033[0;31mERRO! Digite um número entre 1 e 3.\033[m\n")
            else:
                break
    return x


def nome(msg="Informe o nome: "):
    print("-" * 40)
    nome = input(msg)
    return nome


def idade(msg="Informe a idade: "):
    while True:
        try:
            idade = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m\n")
        else:
            return idade


def cadastrar(nome, idade):
    file = open("cadastro.txt", "a")
    file.write(f"{nome}\n")
    file.write(f"{idade}\n")
    file.close()


def lista():
    c = 0
    print("-" * 40)
    file = open("cadastro.txt", "r")
    for i in file:
        c += 1
        i = i.strip()
        if c % 2 != 0:
            print(f"{i:<30}", end="")
        else:
            print(f"{i} anos")
    file.close()