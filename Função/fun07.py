def calcular_preco_final(preco, desconto):
    return preco * (1 - desconto / 100)

# Solicita os valores ao usuário
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

# Exibe o preço final
preco_final = calcular_preco_final(preco, desconto)
print(f"O preço final do produto com {desconto}% de desconto é {preco_final:.2f}.")
