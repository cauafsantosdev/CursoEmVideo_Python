# Melhore o exercício 28, agora o usuário deve tentar adivinhar o número até acertar, mostrando no final quantas tentativas foram necessárias

from random import randint

sorteado = randint(0, 10)
c = 1
n = int(input("Chute um número: "))

while n != sorteado:
    print("Errou!\n")
    n = int(input("Tente novamente: "))
    c += 1
    
print(f"Acertou! Em {c} tentativas!")
