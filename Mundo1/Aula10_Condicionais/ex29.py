# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa custa R$7 por cada Km acima do limite.

v = int(input("Qual a velocidade do carro em Km/h? "))
m = 7
e = v - 80

if v < 0:
    print("Tem coisa errada aí!")
else:
    if v <= 80:
        print("Tudo certo, siga assim!")
    else:
        print(f"Está acima da velocidade! Multa de R${m * e:.2f}")
