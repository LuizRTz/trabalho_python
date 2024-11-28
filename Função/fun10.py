def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Solicita o número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada
print(f"Tabuada do {numero}:")
tabuada(numero)
