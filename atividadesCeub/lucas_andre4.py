#QUESTÃO 1

def mensagem_inicial(valor):
    print("Alô Mundo!")
    print(f"O valor digitado é; {valor}")

if __name__ == "__main__":
    mensagem_inicial(10)

#QUESTÃO 2

def num(ano):
    idade = 2024 - ano
    return idade
if __name__ == "__main__":
    ano = int(input("Digite o ano que você nasceu: "))
    retorno = num(ano)
    print(f"Sua idade é: {retorno} anos")
