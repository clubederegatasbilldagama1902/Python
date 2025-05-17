import random

def palavraescondida():
    lista = ["banana","lorenx","batata","amostradinho","receba","ceub","apendicite","guilherme","santiago","aula","samambaia"]
    return lista
def linha():
    print("+=+="*56)

def escolher_palavra(palavra):
    return random.choice(palavra).strip()

def mostrar_palavra(palavra, letra_advinhada):
    return " ".join([letra if letra in letra_advinhada else "" for letra in palavra])

def jogo_forca():
    vida = 6
    coracao = '❤️'
    palavra_secreta = escolher_palavra(palavraescondida())
    qntd_letra = len(palavra_secreta)
    letra_advinhada = set()
    letra_errada = set()

    linha()

    print(f"{'Jogo da forca':^224}")

    linha()

    print(f"Essa sua palavra tem {qntd_letra} letras")

    while vida > 0:
        print(mostrar_palavra(palavra_secreta , letra_advinhada))
        print(f"Você tem {coracao * vida}")

        letra = str(input("Digite uma letra: "))

        if letra in letra_advinhada or letra in letra_errada:
            print("Você ja digitou essa letra! Tente novamente!")

        if letra in palavra_secreta:
            letra_advinhada.add(letra)
            if set(palavra_secreta) == letra_advinhada:
                print(f"Você adivinhou a palavra secreta! A palavra secreta era: {palavra_secreta}")
                break
        else:
            letra_errada.add(letra)
            vida -= 1
            if vida == 0:
                print(f"Você perdeu o jogo! A palavra era: {palavra_secreta}")

jogo_forca()

while True:
    digite = str(input("Digite [SIM] para continuar ou [NAO] para fechar o jogo: ")).upper()

    if digite == "SIM":
        jogo_forca()
    elif digite == "NAO":
        break
    else:
        print("A palavra digitada não é aceita! Tente novamente!")