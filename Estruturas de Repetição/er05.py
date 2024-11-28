numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    print(f"O resultado da soma é: {numero1 + numero2}")
elif operador == "-":
    print(f"O resultado da subtração é: {numero1 - numero2}")
elif operador == "*":
    print(f"O resultado da multiplicação é: {numero1 * numero2}")
elif operador == "/":
    if numero2 != 0:
        print(f"O resultado da divisão é: {numero1 / numero2}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operador inválido.")
