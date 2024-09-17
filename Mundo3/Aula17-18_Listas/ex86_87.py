# Crie um programa que faça uma matriz 3x3 e a preencha com os valores fornecidos pelo usuário

l = [[], [], []]
s = 0

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f"Digite o valor para [{i},{j}]: "))
        l[i].append(n)
        if n % 2 == 0:
            s += n

print()

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{l[i][j]:^5}]", end="")
    print()
    
print(f"\nA soma de todos os valores pares digitados é {s}")
print(f"A soma dos valores da terceira coluna é {l[0][2] + l[1][2] + l[2][2]}")

l[1].sort()
print(f"O maior valor da segunda linha é {l[1][2]}")
