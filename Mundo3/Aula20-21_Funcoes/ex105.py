# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas, a maior nota, a menor nota, a média da turma e a situação (opcional). Adicione também as docstrings da função

def notas(a):
    """
        -> Função para analisar conjunto de notas
        - Parâmetro a: conjunto a ser analisado
        - Return: Dicionário com quantidade de alunos, maior e menor nota, média da turma e situação geral 
    """
    s = 0
    for i in a:
        s += i
    media = round(s / len(a), 2)
    if media >= 7:
        situacao = "Aprovados"
    elif media >= 3:
        situacao = "Em exame"
    else:
        situacao = "Reprovados"
    turma = {
        "Quantidade de alunos": len(a),
        "Maior nota": max(a),
        "Menor nota": min(a),
        "Média da turma": media,
        "Situação geral": situacao
    }
    return turma
    
lista = []
while True:
    nota = float(input("Informe a nota: "))
    lista.append(nota)
        
    fim = ""
    while fim != "S" and fim != "N":
        fim = input("Deseja continuar? [S/N] ").upper()
    if fim == "N":
        print()
        break
    print()

print("INFORMAÇÕES DA TURMA:")
for k, v in notas(lista).items():
    print(f"- {k}: {v}")

