try:
    with open("numeros.txt", "r") as file:
        numeros = file.readlines()
        soma = sum(int(numero.strip()) for numero in numeros)
        print(f"A soma dos números é: {soma}")
except FileNotFoundError:
    print("Erro: o arquivo 'numeros.txt' não foi encontrado.")
