def leiaInt(a="Digite um número inteiro: "):
    while True:
        try:
            n = int(input(a))
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m\n")
        except KeyboardInterrupt:
            print(f"\n\033[0;31mO usuário não informou o valor\033[m\n")
            return 0
        else:
            return n

def leiaFloat(a="Digite um número real: "):
    while True:
        try:
            n = float(input(a))
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO! Digite um número real válido.\033[m\n")
        except KeyboardInterrupt:
            print(f"\n\033[0;31mO usuário não informou o valor\033[m\n")
            return 0
        else:
            return n