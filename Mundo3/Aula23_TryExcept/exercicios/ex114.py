# Crie um programa que diga se o site Pudim está acessível no computador

import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento.")
else:
    print("O site Pudim está perfeitamente acessível!")
