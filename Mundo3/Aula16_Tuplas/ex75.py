# Desenvolva um programa que leia quatro valores e guarde-os em uma tupla. No final mostre quantas vezes apareceu o valor 9, em que posição foi digitado o primeiro valor 3 e quais foram os números pares

t = (int(input("Insira um número: ")),
     int(input("Insira outro número: ")),
     int(input("Insira mais um número: ")),
     int(input("Insira o último número: ")))
p = ()
par = False

if 9 in t:
    print(f"O número 9 aparece {t.count(9)} vezes")
else:
    print(f"Não há nenhum 9 na tupla")

if 3 in t:
    print(f"O número 3 aparece pela primeira vez na posição {t.index(3) + 1}")
else:
    print(f"Não há nenhum 3 na tupla")   

for i in t:
    if i % 2 == 0:
        par = True
        p += i,

if par == True:
    print(f"Os números pares são: ", end="")
    print(", ".join(map(str, p)))
else:
    print("Não há números pares")
