def inverter(s):
    return s[::-1]

# Solicita a palavra ao usuário
palavra = input("Digite uma palavra para inverter: ")

# Exibe a palavra invertida
resultado = inverter(palavra)
print(f"A palavra invertida é {resultado}.")
