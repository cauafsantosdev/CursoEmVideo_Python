# Crie um programa que leia uma expressão qualquer que use parênteses. O programa deverá analisar se a expressão está com os parenteses abertos e fechados na ordem correta

e = input("Digite a expressão: ")
l = []

for i in e:
    if i == "(":
        l.append(i)
    elif i == ")":
        if len(l) > 0:
            l.pop()
        else:
            l.append(i)
            break

if len(l) > 0:
    print(f"{e} não é uma expressão válida")
else:
    print(f"{e} é uma expressão válida")

