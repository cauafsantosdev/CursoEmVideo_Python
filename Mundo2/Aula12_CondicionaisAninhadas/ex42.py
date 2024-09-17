# Refaça o desafio 35 dos triangulos, acrescetando o recurso de mostrar que tipo de triângulo será formado: equilátero possui todos os lados iguais, isósceles possui dois lados iguais e escaleno possui todos os lados diferentes.

a = float(input("Digite a medida do lado A: "))
b = float(input("Digite a medida do lado B: "))
c = float(input("Digite a medida do lado C: "))

if a <= b + c and b <= + c and c <= a + b:
	if a == b == c:
		print("É um triângulo equilátero")
	elif a == b or b == c or c == a:
		print("É um triângulo isósceles")
	else:
		print("É um triângulo escaleno")
else:
	print("Não é um triângulo")
