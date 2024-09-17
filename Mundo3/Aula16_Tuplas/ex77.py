# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, mostras as vogais de cada palavra

t = ()
c = 0

while True:
    x = input("Digite uma palavra: ").lower()
    t += x, 
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

print()

for i in t:
    print(f"As vogais de {i.upper()} são: ", end="")
    for j in i:
        if j in "aáãâeéêioóôuú":
            print(j, end=" ")
    print()
