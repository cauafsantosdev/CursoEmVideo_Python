# Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório.

def voto(a):
    from datetime import date
    ano = date.today().year
    idade = ano - a
    if idade < 16:
        return f"Com {idade} anos: Ainda não pode votar"
    elif idade < 18 or idade > 69:
        return f"Com {idade} anos: O voto é FACULTATIVO"
    else:
        return f"Com {idade} anos: O voto é OBRIGATÓRIO"

a = int(input("Digite seu ano de nascimento: "))

print(voto(a))
