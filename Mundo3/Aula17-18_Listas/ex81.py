# Crie um programa que leia vários números e os coloque em uma lista. Depois mostre: quantos números foram digitados, a lista em ordem decrescente e se o valor 5 foi digitado ou não

l = []

while True:
    n = int(input("Insira um número: "))
    if n not in l:
        l.append(n)
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

l = sorted(l, reverse = True)

print(f"\nForam digitados {len(l)} valores")
print(l)

if 5 in l:
    print(f"O número 5 foi digitado e está na posição {l.index(5)}")
else:
    print("O número 5 não foi digitado")
