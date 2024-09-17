# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() só que fazendo a validação para aceitar apenas um valor numérico

def leiaInt(a):
    while True:
        n = input(a)
        if n.isnumeric():
            break
        else:
            print(f"\033[0;31mERRO! Digite um número válido\033[m\n")
    return int(n)


n = leiaInt("Digite um número: ")
print(f"O número digitado foi {n}")
