# Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

s = 0
jogador = {}
geral = []

while True:
    jogador['nome'] = input("Digite o nome do jogador: ")
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    print()

    for i in range(0, jogador['partidas']):
        jogador[f'gol{i}'] = int(input(f"Quantos gols na partida {i + 1}? "))
        s += jogador[f'gol{i}']
    jogador['total'] = s
    geral.append(jogador.copy())
    s = 0
    
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        break
    print()

x = input("\nDeseja ver as estatísticas de qual jogador? ")

while True:
    encontrado = False
    for i in range(0, len(geral)):
        if x == geral[i]['nome']:
            encontrado = True
            print(f"\nEstatísicas de {geral[i]['nome']}:\n")
            for j in range(0, len(geral[i]) - 3):
                print(f"Partida {j + 1} - {geral[i][f'gol{j}']} gols")
    
            print(f"\nTotalizando {geral[i]['total']} gols em {geral[i]['partidas']} partidas, média de {geral[i]['total'] / geral[i]['partidas']:.2f} gols por partida.")
    
    if encontrado == False:
        print(f"Jogador {x} não foi encontrado")
    
    fim = input("\nDeseja ver as estatísticas de mais algum jogador? [S/N] ")
    while fim != "S" and fim != "N":
        fim = input("Deseja ver as estatísticas de mais algum jogador? [S/N] ").upper()
    if fim == "S":
        x = input("Qual jogador? ")
    if fim == "N":
        break
    print()
