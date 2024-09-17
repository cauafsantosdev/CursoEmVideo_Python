# Crie um programa que leia dois valores e mostre um menu na tela: [1] para somar, [2] para multiplicar, [3] para ver qual valor é maior, [4] para inserir novos números e [5] para sair do programa

x = int(input("Digite um número: "))
y = int(input("Digite um outro número: "))
o = 0

while o != 5:
    o = int(input("\nDigite [1] para somar\nDigite [2] para multiplicar\nDigite [3] para ver qual número é maior\nDigite [4] para inserir novos números\nDigite [5] para sair do programa:\n-> "))
    if o == 1:
        print(f"\n{x} + {y} = {x + y}")
    elif o == 2:
        print(f"\n{x} x {y} = {x * y}")
    elif o == 3:
        if x > y:
            print(f"\n{x} é maior que {y}")
        elif y > x:
            print(f"\n{y} é maior que {x}")
        else:
            print(f"\n{x} e {y} são iguais")
    elif o == 4:
        x = int(input("\nDigite um novo número: "))
        y = int(input("Digite um outro novo número: "))
    elif o == 5:
        print("\nPrograma encerrado.")
    else:
        print("\nNúmero inválido.")
