nome_arquivo = input("Digite o nome do arquivo: ")
texto = input("Digite o texto a ser gravado no arquivo: ")

with open(nome_arquivo, "w") as file:
    file.write(texto)
