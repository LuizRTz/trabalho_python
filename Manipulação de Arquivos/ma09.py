import csv

try:
    with open("dados.csv", "r") as file:
        leitor = csv.reader(file)
        for linha in leitor:
            print("\t".join(linha))  # Organiza as colunas separadas por tabulação
except FileNotFoundError:
    print("Erro: o arquivo 'dados.csv' não foi encontrado.")
