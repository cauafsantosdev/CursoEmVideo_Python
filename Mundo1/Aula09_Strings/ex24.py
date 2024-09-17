# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome de santo

cidade = input("Digite o nome da cidade: ")

if "Santo" in cidade[:6] or "São" in cidade[:6] or "Santa" in cidade[:6]:
    print(f"{cidade} começa com nome de santo")
else:
    print(f"{cidade} NÃO começa com nome de santo")
