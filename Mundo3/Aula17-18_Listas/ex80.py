# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista já na posição correta de inserção (sem usar sorted). No final, mostre a lista ordenada na tela

l = []

for i in range(0, 5):
    n = int(input("Insira um número: "))
    if n not in l:
        if i == 0 or n > l[-1]:
            l.append(n)
        else:
            p = 0
            while p < len(l):
                if n < l[p]:
                    l.insert(p, n)
                    break
                p += 1

print(f"\n{l}")
