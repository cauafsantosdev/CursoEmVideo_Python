# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input("Qual o preço do produto? R$"))

print(f"Com 5% de desconto, o produto custará R${p - (p * 5) / 100:.2f}")
