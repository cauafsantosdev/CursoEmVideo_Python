# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 númros e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint

def sorteia(lista):
    print("Os números sorteados foram:", end="")
    for i in range(0, 5):
        lista.append(randint(0,100))
        print(f" {lista[i]}", end="")
    print()
    

def somaPar(lista):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f"A soma de todos os números pares sorteados é {s}")


n = []
sorteia(n)
somaPar(n)
