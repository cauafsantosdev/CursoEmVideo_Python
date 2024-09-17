# Crie um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas

d = int(input("Qual a distância da viagem em Km? "))
p1 = 0.50
p2 = 0.45

if d <= 200:
    print(f"A passagem custará R${d * p1:.2f}")
else:
    print(f"A passagem custará R${d * p2:.2f}")
