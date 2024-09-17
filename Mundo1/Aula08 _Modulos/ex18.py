# Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin
from math import cos
from math import tan

a = float(input("Informe o ângulo: "))

if a == int(a):
    a = int(a)

print(f"O seno de {a} é {sin(a):.3f}")
print(f"O cosseno de {a} é {cos(a):.3f}")
print(f"A tangente de {a} é {tan(a):.3f}")
