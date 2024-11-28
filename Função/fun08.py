def contar_vogais(s):
    contador = 0
    for char in s:
        if char.lower() in "aeiouáéíóúãõ":
            contador += 1
    return contador

# Solicita a frase ao usuário
frase = input("Digite uma frase para contar as vogais: ")

# Exibe o número de vogais
resultado = contar_vogais(frase)
print(f"A frase tem {resultado} vogais.")
