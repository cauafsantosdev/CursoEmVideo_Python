# Refaça o exercício 64 utilizando break

c = s = 0

print("Digite quantos números quiser, ao terminar digite 999\n")

while True:
    n = int(input(f"Insira um número: "))
    if n == 999:
        break
    c += 1
    s += n

print(f"Foram digitados {c} números e a soma entre eles é igual a {s}")
