a = input("Digite algo: ")

print(f"\nO tipo primitivo desse valor é {type(a)}")
print(f"Só tem espaços? {a.isspace()}")
print(f"É um número? {a.isnumeric()}")
print(f"É alfabético? {a.isalpha()}")
print(f"É alfanumérico? {a.isalnum()}")
print(f"Está em maísculas? {a.isupper()}")
print(f"Está em minúsculas? {a.islower()}")
print(f"Está capitalizada? {a.istitle()}")
