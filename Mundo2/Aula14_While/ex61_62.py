# 61 - Refaça o exercício 51, da progressão aritmética, mas usando while
# 62 - Pergunte se o usuário quer mostrar mais algum termo após o décimo termo. Caso o usuário digite 0 encerre o programa

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite sua razão: "))
c = 1

while c <= 10:
    pa = a1 + (c - 1) * r
    print(pa, end=" ")
    c += 1

print()

a = int(input("Quantos termos a mais deseja mostrar? "))

if a != 0:
    a += c
    while c <= a:
        pa = a1 + (c - 1) * r
        print(pa, end=" ")
        c += 1
    print()
