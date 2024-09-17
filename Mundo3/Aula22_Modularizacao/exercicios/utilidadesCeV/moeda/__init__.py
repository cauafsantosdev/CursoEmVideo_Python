def aumentar(n=0, p=0, f=False):
    return n + (n * p / 100) if not f else moeda((n + (n * p / 100)))


def diminuir(n=0, p=0, f=False):
    return n - (n * p / 100) if not f else moeda((n - (n * p / 100)))


def dobro(n=0, f=False):
    return n * 2 if not f else moeda((n * 2))


def metade(n=0, f=False):
    return n / 2 if not f else moeda((n / 2))


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:.2f}".replace(".", ",")


def resumo(n=0, pa=0, pr=0):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    print(f"{'Preço analisado:':<20}", end="")
    print(moeda(n))
    print(f"{'Dobro do preço:':<20}", end="")
    print(dobro(n, True))
    print(f"{'Metade do preço:':<20}", end="")
    print(metade(n, True))
    print(f"{(f'{pa:.0f}% de aumento:' if pa == int(pa) else f'{pa:.2f}% de aumento:'):<20}", end="")
    print(aumentar(n, pa, True))
    print(f"{(f'{pr:.0f}% de redução:' if pr == int(pr) else f'{pr:.2f}% de redução:'):<20}", end="")
    print(diminuir(n, pr, True))
    print("-" * 30)