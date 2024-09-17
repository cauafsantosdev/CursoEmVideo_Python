def leiaDinheiro(string='Informe o valor: R$'):
    while True:
        n = input(string)

        if "," in n:
            valido = n.replace(",", "")
            valido = valido.isnumeric()
            n = n.replace(",", ".")
        elif "." in n:
            valido = n.replace(".", "")
            valido = valido.isnumeric()
        else:
            valido = n.isnumeric()

        if valido:
            return float(n)
        else:
            print("Valor não monetário! Tente novamente.\n")


def leiaPorcentagem(string='Informe a porcentagem: '):
    while True:
        p = input(string)
        valido = p.isnumeric()

        if valido:
            return float(p)
        else:
            print("O valor inserido não é numérico! Tente novamente.\n")