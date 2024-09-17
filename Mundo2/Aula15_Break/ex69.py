# Crie um programa que leia a idade e o sexo de várias pessoas e pergunte ao usuário se ele quer continuar cadastrando pessoas ou não. Ao final mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos

maior = homem = mulher = 0

while True:
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo: [M/F] ").upper()
    if idade > 18:
        maior += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade <= 20:
        mulher += 1
    fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
            break
    while fim != "S" and fim != "N":
        fim = input("Resposta inválida, deseja continuar? [S/N] ").upper()
    print()

print(f"\n{maior} pessoas tem mais de 18 anos\n{homem} homens foram cadastrados\n{mulher} mulheres tem menos de 20 anos.")
