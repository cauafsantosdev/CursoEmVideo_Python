# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu ICM e mostre seu status, abaixo de 18.5 = abaixo do peso; 18.5 até 25 = peso ideal; 23 até 30 = sobrepeso; 20 até 40 = obesidade; acima de 40 = obesidade mórbida

p = float(input("Digite seu peso em kg: "))
a = float(input("Digite sua altura em metros: "))

imc = p / (a * a)

if imc < 18.5:
    print(f"{imc:.2f} está abaixo do peso.")
elif imc <= 24.99:
    print(f"{imc:.2f} está no peso ideal.")
elif imc <= 29.99:
    print(f"{imc:.2f} está com sobrepeso.")
elif imc <= 39.99:
    print(f"{imc:.2f} está com obesidade.")
else:
    print(f"{imc:.2f} está com obesidade mórbida.")
