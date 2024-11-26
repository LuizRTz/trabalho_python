# Solicita o preço do produto e a porcentagem de desconto
preco = float(input("Digite o preço do produto: "))
desconto_percent = float(input("Digite a porcentagem de desconto: "))

# Calcula o valor do desconto
desconto = (desconto_percent / 100) * preco

# Calcula o preço final
preco_final = preco - desconto

# Exibe os resultados
print(f"O valor do desconto é {desconto} e o preço final do produto é {preco_final}.")
