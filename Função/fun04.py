def maior(a, b, c):
    return max(a, b, c)

# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Exibe o maior número
resultado = maior(num1, num2, num3)
print(f"O maior número entre {num1}, {num2} e {num3} é {resultado}.")
