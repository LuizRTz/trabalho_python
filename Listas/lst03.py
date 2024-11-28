numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

pares = [n for n in numeros if n % 2 == 0]
print("Números pares:", pares)
