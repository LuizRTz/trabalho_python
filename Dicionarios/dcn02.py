alunos = {}
for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

for nome, nota in alunos.items():
    print(f"{nome}: {nota}")

