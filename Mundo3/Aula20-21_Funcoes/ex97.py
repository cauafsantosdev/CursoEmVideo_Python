# Faça um programa que tenha uma função chamada escreva, que receba um texto como parâmetro e mostre uma mensagem com tamanho adaptável

def escreva(texto):
    print("-" * (len(texto) + 2))
    print(f" {texto}")
    print("-" * (len(texto) + 2))
    
    
texto = input("Digite algo: ")
print()
escreva(texto)
