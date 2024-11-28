entrada = input("Digite uma lista de números inteiros separados por espaços: ")
numeros = list(map(int, entrada.split()))

soma = sum(numeros)
print(f"A soma dos números é: {soma}")
