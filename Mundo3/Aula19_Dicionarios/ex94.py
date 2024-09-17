# Crie um programa que leia nome, sexo e diade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: quantas pessoas foram cadastradas, a média de idade do grupo, uma lista com todas as mulheres e uma lista com todas as pessoas com idade acima da média

pessoa = {}
geral = []
s = 0

while True:
    pessoa['nome'] = input("Digite o nome: ")
    pessoa['idade'] = int(input("Digite a idade: "))
    pessoa['sexo'] = input("Digite o sexo: [M/F] ").upper()
    geral.append(pessoa.copy())
    s += pessoa['idade']
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()
    
media = s / len(geral)

print(f"\nForam cadastradas {len(geral)} pessoas")
print(f"A média de idade entre elas é de {media:.2f} anos")

print("\nAs mulheres cadastradas foram:\n")

for i in range(0, len(geral)):
    if geral[i]['sexo'] == "F":
        print(f"- {geral[i]['nome']}")

print("\nAs pessoas com idade a cima da média são:\n")

for i in range(0, len(geral)):
    if geral[i]['idade'] > media:
        print(f"- {geral[i]['nome']} ({geral[i]['idade']} anos)")
