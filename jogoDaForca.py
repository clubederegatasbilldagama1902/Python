# Importa o módulo random para seleção aleatória de palavras
import random

# Função que retorna uma lista de palavras para o jogo
def palavraescondida():
    lista = ["banana","lorenx","batata","amostradinho","receba","ceub","apendicite","guilherme","santiago","aula","samambaia"]
    return lista

# Função para imprimir uma linha decorativa
def linha():
    print("+=+="*56)

# Função para escolher uma palavra aleatória da lista
def escolher_palavra(palavra):
    return random.choice(palavra).strip()  # strip() remove espaços em branco

# Função para mostrar a palavra com letras adivinhadas
def mostrar_palavra(palavra, letra_advinhada):
    # Para cada letra na palavra, mostra se foi adivinhada, senão mostra espaço
    return " ".join([letra if letra in letra_advinhada else "_" for letra in palavra])

# Função principal do jogo da forca
def jogo_forca():
    vida = 6  # Número de vidas/tentativas
    coracao = '❤️'  # Símbolo de coração para representar vidas
    palavra_secreta = escolher_palavra(palavraescondida())  # Seleciona palavra aleatória
    qntd_letra = len(palavra_secreta)  # Conta letras da palavra
    letra_advinhada = set()  # Conjunto para letras corretas
    letra_errada = set()  # Conjunto para letras erradas

    linha()
    print(f"{'Jogo da forca':^224}")  # Título centralizado
    linha()
    print(f"Essa sua palavra tem {qntd_letra} letras")  # Mostra tamanho da palavra

    # Loop principal do jogo
    while vida > 0:
        print(mostrar_palavra(palavra_secreta, letra_advinhada))  # Mostra progresso
        print(f"Você tem {coracao * vida}")  # Mostra vidas restantes

        letra = str(input("Digite uma letra: ")).lower()  # Recebe letra do jogador

        # Verifica se letra já foi tentada
        if letra in letra_advinhada or letra in letra_errada:
            print("Você já digitou essa letra! Tente novamente!")

        # Verifica se letra está na palavra
        if letra in palavra_secreta:
            letra_advinhada.add(letra)
            # Verifica se jogador acertou todas as letras
            if set(palavra_secreta) == letra_advinhada:
                print(f"Você adivinhou a palavra secreta! A palavra secreta era: {palavra_secreta}")
                break
        else:
            letra_errada.add(letra)
            vida -= 1  # Perde uma vida
            if vida == 0:  # Game over
                print(f"Você perdeu o jogo! A palavra era: {palavra_secreta}")

# Inicia o jogo pela primeira vez
jogo_forca()

# Loop para perguntar se quer jogar novamente
while True:
    digite = str(input("Digite [SIM] para continuar ou [NAO] para fechar o jogo: ")).upper()

    if digite == "SIM":
        jogo_forca()  # Reinicia o jogo
    elif digite == "NAO":
        break  # Encerra o programa
    else:
        print("A palavra digitada não é aceita! Tente novamente!")  # Entrada inválida
