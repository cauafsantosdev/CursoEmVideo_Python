# Faça um programa que leia um número qualquer e mostre seu fatorial

n = int(input("Digite um número: "))
c = 1
f = 1

# Usando while
while c <= n:
    f *= c
    c += 1
    
print(f"O fatorial de {n} é {f}")

f = 1

# Usando for
for i in range(1, n + 1):
    f *= i
    
print(f"O fatorial de {n} é {f}")
