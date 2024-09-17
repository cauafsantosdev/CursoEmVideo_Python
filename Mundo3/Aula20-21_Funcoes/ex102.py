# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show que será um valor lógico (opcional) indicando se sera mostrado na tela o processo de cálculo do fatorial

def fatorial(a, b):
    """
    -> Calcula o fatorial de um número:
    Parâmetro a = número que será calculado
    Parâmetro b = se será mostrado, ou não, o processo de fatorial
    """
    fat = 1
    for i in range(a, 0, -1):
        fat *= i
        if b:
            if i > 1:
                print(f"{i} x ", end="")
            else:
                print(f"{i} = ", end="")
    if not b:
        print(f"Fatorial de {a} = ", end="")
    return fat
        
        
n = int(input("Digite um número para calcular seu fatorial: "))
show = None

while show != True and show != False:
    if show == "S":
        show = True
    elif show == "N":
        show = False
    else:
        show = input("Deseja ver o processo de fatorial? [S/N] ").upper()

print()
print(fatorial(n, show))

