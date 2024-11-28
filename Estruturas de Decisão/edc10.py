# Solicita um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Função para verificar se o número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Verifica se o número é primo e exibe a mensagem
if eh_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
