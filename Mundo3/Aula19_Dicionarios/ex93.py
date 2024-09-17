# Crie um programa que leia o nome de um jogador e quantas partidas ele jogou. Em seguida leia quantos gols ele fez em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

s = 0
jogador = {}

jogador['nome'] = input("Digite o nome do jogador: ")
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

print()

for i in range(0, jogador['partidas']):
    jogador[f'gol{i}'] = int(input(f"Quantos gols na partida {i + 1}? "))
    s += jogador[f'gol{i}']


print(f"\nEstatísicas de {jogador['nome']}:\n")

for i in range(0, len(jogador) - 2):
    print(f"Partida {i + 1} - {jogador[f'gol{i}']} gols")
    
print(f"\nTotalizando {s} gols em {jogador['partidas']} partidas, média de {s / jogador['partidas']:.2f} gols por partida.")
