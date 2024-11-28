dias_da_semana = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Sábado",
    7: "Domingo"
}

numero = int(input("Digite um número de 1 a 7: "))
print(f"O dia da semana correspondente é: {dias_da_semana.get(numero, 'Número inválido!')}")

