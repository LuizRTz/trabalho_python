try:
    with open("original.txt", "r") as original_file:
        conteudo = original_file.read()

    with open("copia.txt", "w") as copia_file:
        copia_file.write(conteudo)

    print("Conteúdo copiado com sucesso!")
except FileNotFoundError:
    print("Erro: o arquivo 'original.txt' não foi encontrado.")
