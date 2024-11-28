try:
    with open("mensagem.txt", "r") as file:
        conteudo = file.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: o arquivo 'mensagem.txt' não foi encontrado.")
