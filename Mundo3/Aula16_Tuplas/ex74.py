# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

t = ()
c = 0

for i in range(0, 5):
    n = randint(0, 1001)
    t += (n, )

print("Tupla = ", end="")

while c < len(t) - 1:
    print(t[c], end=" | ")
    c += 1
    if c == len(t) - 1:
        print(t[c])

print(f"O menor valor é {min(t)}\nO maior valor é {max(t)}")
