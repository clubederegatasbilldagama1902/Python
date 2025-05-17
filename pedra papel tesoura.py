# Importa a função choice para escolher aleatoriamente um item de uma lista
from random import choice

# Definição de variáveis de cores ANSI para estilizar o terminal
blue = "\33[1;49;34m"
red = "\33[1;49;31m"
yellow = "\33[1;49;33m"
green = "\33[1;49;32m"
nc = "\33[m"  # Reset de cor (no color)

# Lista com as opções possíveis do jogo
lista = ["pedra", "papel", "tesoura"]

# O computador escolhe uma opção aleatória ao iniciar o programa (mas deveria estar dentro da função!)
pc = choice(lista)

# Função principal do jogo
def jogo():
    # Mostra o menu de opções para o usuário com cores
    print(f"""{blue}Escolha uma opção:
    [1] Pedra
    [2] Papel
    [3] Tesoura{nc}""")

    # Usuário escolhe uma das opções (1, 2 ou 3)
    escolha = int(input(f"{yellow}Sua escolha é: {nc}"))

    # Converte a escolha numérica para a string correspondente
    usuario = "pedra" if escolha == 1 else "papel" if escolha == 2 else "tesoura"

    # Verifica empate
    if pc == usuario.lower():
        print(f"{green}O pc escolheu {pc} vocês empataram!{nc}")
    else:
        # Lógica para verificar vencedor com base nas regras do jogo
        if pc == "pedra":
            if usuario == "papel":
                print(f"{blue}Você ganhou do computador! O computador escolheu {pc}{nc}")
            elif usuario == "tesoura":
                print(f"{red}Você perdeu! O computador escolheu {pc}{nc}")
        elif pc == "papel":
            if usuario == "pedra":
                print(f"{red}Você perdeu! O computador escolheu {pc}{nc}")
            else:
                print(f"{blue}Você ganhou do computador! O computador escolheu {pc}{nc}")
        elif pc == "tesoura":
            if usuario == "pedra":
                print(f"{blue}Você ganhou do computador! O computador escolheu {pc}{nc}")
            else:
                print(f"{red}Você perdeu! O computador escolheu {pc}{nc}")

# Executa o jogo pela primeira vez
jogo()

# Loop que permite jogar várias vezes
while True:
    jogar = str(input("Você deseja jogar novamente? Digite [SIM] para continuar ou [NAO] para parar o jogo: ")).upper()

    if jogar == "SIM":
        jogo()  # Reinicia o jogo
    elif jogar == "NAO":
        break  # Sai do loop e encerra o programa
    else:
        print("Palavra não aceita! Digite [SIM] para continuar ou [NAO] para parar o jogo!")
