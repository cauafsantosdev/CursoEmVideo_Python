# Refaça o exercício 9 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando for.

n = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada de {n}:")

for i in range(0, 11):
    print(f"{n} x {i} = {n * i}")
