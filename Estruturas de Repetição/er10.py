numero = int(input("Digite um número de 1 a 7: "))

dias_da_semana = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}

if 1 <= numero <= 7:
    print(f"O dia da semana é: {dias_da_semana[numero]}")
else:
    print("Erro: O número deve estar entre 1 e 7.")
