livro = {
    "título": input("Digite o título do livro: "),
    "autor": input("Digite o autor do livro: "),
    "ano": int(input("Digite o ano de publicação do livro: "))
}

novo_ano = int(input("Digite o novo ano de publicação: "))
livro["ano"] = novo_ano

print(livro)

