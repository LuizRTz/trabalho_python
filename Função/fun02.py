def é_par(numero):
    return numero % 2 == 0

# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if é_par(numero):
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")
