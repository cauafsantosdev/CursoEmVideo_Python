# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la. Cada litro de tinto pinta uma área de 2m²

l = float(input("Qual a largura da parede? "))
a = float(input("Qual a altura da parede? "))

area = l * a
tinta = area / 2

print(f"A área total da parede é de {area}m², necessitará de {tinta} litros de tinta para pintá-la")
