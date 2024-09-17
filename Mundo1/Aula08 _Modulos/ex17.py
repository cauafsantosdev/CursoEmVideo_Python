# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e mostre o comprimento de sua hipotenusa

from math import hypot

cat_op = float(input("Informe a medida do cateto oposto: "))
cat_adj = float(input("Informe a medida do cateto adjacente: "))

hip = hypot(cat_op, cat_adj)

if hip == int(hip):
    hip = int(hip)
    print(f"O comprimento da hipotenusa é de: {hip}")
else:
    print(f"O comprimento da hipotenusa é de: {hip:.2f}")

