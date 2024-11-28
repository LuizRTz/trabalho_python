lista1 = []
lista2 = []
for i in range(5):
    num1 = int(input(f"Digite o {i+1}º número da primeira lista: "))
    lista1.append(num1)
    num2 = int(input(f"Digite o {i+1}º número da segunda lista: "))
    lista2.append(num2)

soma_listas = [lista1[i] + lista2[i] for i in range(5)]

print("Lista resultante da soma:", soma_listas)
