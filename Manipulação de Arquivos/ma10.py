entrada = input("Digite a sua entrada para o diário: ")

try:
    with open("diario.txt", "a") as file:
        file.write(entrada + "\n")
    print("Entrada adicionada ao diário.")
except FileNotFoundError:
    with open("diario.txt", "w") as file:
        file.write(entrada + "\n")
    print("Arquivo diário criado e entrada adicionada.")
