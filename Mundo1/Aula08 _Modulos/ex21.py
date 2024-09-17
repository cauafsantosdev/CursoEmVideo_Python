# Faça um programa em Python que abra e reproduza um arquivo mp3

from os import system

file = "sample.mp3"
print(f"Tocando {file}")
system("mpg123 " + file)
