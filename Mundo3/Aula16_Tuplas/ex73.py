# Crie uma tupla preenchida com todos os times do Brasileirão na ordem de classificação. Depois mostre: A - Apenas os 6 primeiros colocados, B - Os últimos 4 colocados, C - Uma lista com os times em ordem alfabética, D - Em que posição está o seu time

t = ("Fortaleza", "Botafogo", "Palmeiras", "Flamengo", "São Paulo", "Bahia", "Cruzeiro", "Atlético Mineiro", "Athletico Paranaense", "Vasco", "Internacional", "Juventude", "Grêmio", "Bragantino", "Criciúma", "Fluminense", "Vitória", "Corinthians", "Cuiabá", "Atlético Goianiense")

x = int(input("Digite [1] para ver a tabela completa\nDigite [2] para ver o G-6\nDigite [3] para ver os times em ordem alfabética\nDigite [4] para ver todos os times em ordem alfabética\nDigite [5] para ver a posição do seu time\n-> "))

while x < 1 or x > 5:
    print("\nOpção inválida")
    x = int(input("Digite [1] para ver a tabela completa\nDigite [2] para ver o G-6\nDigite [3] para ver os times em ordem alfabética\nDigite [4] para ver todos os times em ordem alfabética\nDigite [5] para ver a posição do seu time\n-> "))

print()

if x == 1:
    for i in range(0, len(t)):
        print(f"{i + 1}º - {t[i]}")
elif x == 2:
    for i in range(0, 6):
        print(f"{i + 1}º - {t[i]}")
elif x == 3:
    for i in range(16, 20):
        print(f"{i + 1}º - {t[i]}")
elif x == 4:
    t = sorted(t)
    for i in range(0, len(t)):
        print(f"{i + 1} - {t[i]}")
else:
    time = input("Qual seu time? ").title()
    c = 0
    while t[c] != time:
        c += 1
    print(f"{time} está na {c + 1}º colocação") 
