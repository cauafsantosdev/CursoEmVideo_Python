# Crie uma programa que tenha uma tupla totalmente preenchida por uma contagem por extenso de 0 até 20. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

t = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

n = int(input("Digite um número entre 0 e 20: "))

while n < 0 or n > 20:
    n = int(input("Valor inválido. Digite um número entre 0 e 20: "))

print(f"{n} = {t[n]}")
