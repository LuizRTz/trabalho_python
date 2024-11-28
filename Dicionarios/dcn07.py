precos = {
    "Arroz": 5.99,
    "Feijão": 4.50,
    "Macarrão": 3.80,
    "Óleo": 7.20,
    "Açúcar": 2.99
}

produto = input("Digite o nome do produto: ")

if produto in precos:
    print(f"O preço do {produto} é R${precos[produto]:.2f}")
else:
    print(f"{produto} não foi encontrado.")

