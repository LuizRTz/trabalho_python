numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
numeros[numeros.index(maior)] = 0

print("Lista atualizada:", numeros)
