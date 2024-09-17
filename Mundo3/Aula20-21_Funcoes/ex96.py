# Faça um programa que tenha uma funçãi chamada area(), que recebea as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def area(l, c):
    a = l * c
    print(f"\nA área de um terreno {l:.2f}x{c:.2f} é de {a:.2f}m²")


l = float(input("Informe a largura do terreno: "))
c = float(input("Informe o comprimento do terreno: "))

area(l, c)
