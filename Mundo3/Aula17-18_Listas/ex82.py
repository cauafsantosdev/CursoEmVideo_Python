# Crie um programa que vai ler vários números e colocá-los em uma lista. Depois crie 2 listas extras contendo apenas os números pares e os números ímpares. Ao final, mostre as três listas

l = []
par = []
impar = []

while True:
    n = int(input("Insira um número: "))
    l.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()
    
print(f"\nNúmeros digitados: {l}\nPares: {par}\nÍmpares: {impar}")
