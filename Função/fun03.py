def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicita o número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Exibe o resultado do fatorial
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")
