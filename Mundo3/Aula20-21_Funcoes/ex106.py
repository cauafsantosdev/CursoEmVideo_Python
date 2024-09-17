# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará

def ajuda(a):
    msg = f'Acessando o manual do comando "{a}"'
    print("-" * (len(msg) + 2))
    print(msg)
    print("-" * (len(msg) + 2))
    print(help(a))


while True:
    inicio = "SISTEMA DE AJUDA PyTeacher"
    print("-" * (len(inicio) + 2))
    print(inicio)
    print("-" * (len(inicio) + 2))
    h = input("Função ou Biblioteca: ")
    if h == "fim":
        fim = "ATÉ LOGO!"
        print("-" * (len(fim) + 2))
        print(fim)
        print("-" * (len(fim) + 2))
        break
    else:
        print(ajuda(h))
