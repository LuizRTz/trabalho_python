palavras = input("Digite uma lista de palavras separadas por espaços: ").split()
palavra_buscada = input("Digite a palavra que você deseja buscar: ")

if palavra_buscada in palavras:
    print(f"A palavra '{palavra_buscada}' está na lista.")
else:
    print(f"A palavra '{palavra_buscada}' não está na lista.")
