pessoas = {"João": 25, "Maria": 30, "Carlos": 22}
nome = input("Digite o nome de uma pessoa: ")

if nome in pessoas:
    print(f"{nome} foi encontrado no dicionário.")
else:
    print(f"{nome} não foi encontrado no dicionário.")

