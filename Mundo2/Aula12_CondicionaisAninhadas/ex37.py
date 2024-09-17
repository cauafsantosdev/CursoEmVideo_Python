#  Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: [1] para binário, [2] para octal, [3] para hexadecimal

n = int(input("Digite um número: "))
b = int(input("\nDigite [1] para converter para binário\nDigite [2] para converter para octal\nDigite [3] para converter para hexadecimal\n-> "))

if b == 1:
    c = bin(n)
    print(f"\n{n} convertido para base binária torna-se {c[2:]}")
elif b == 2:
    c = oct(n)
    print(f"\n{n} convertido para base octal torna-se {c[2:]}")
elif b == 3:
    c = hex(n)
    print(f"\n{n} convertido para base hexadecimal torna-se {c[2:]}")
else:
    print("\nOpção inválida.")
