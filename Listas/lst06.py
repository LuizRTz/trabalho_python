numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
maiores_que_media = len([n for n in numeros if n > media])

print(f"Quantidade de números maiores que a média ({media}): {maiores_que_media}")
