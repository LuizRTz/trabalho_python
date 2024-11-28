def media(lista):
    return sum(lista) / len(lista)

# Solicita a lista de números ao usuário
numeros = list(map(float, input("Digite os números separados por espaço: ").split()))

# Exibe a média
resultado = media(numeros)
print(f"A média dos números é {resultado}.")
