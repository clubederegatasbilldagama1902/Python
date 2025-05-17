#Questão 1

def positivo_nulo_negativo():
    if valor >= 0:
        print("Número digitado é positivo")
    else:
        print("Número digitado é negativo")

if __name__ == "__main__":
    valor = int(input("Digite um número: "))
    positivo_nulo_negativo()


#Questão 2
def valor_absoluto():
    valor_absoluto_negativo = valor * -1
    if valor >= 0:
        print(f"O número absoluto é: {valor}")
    else:
        print(f"O número absoluto é: {valor_absoluto_negativo}")

if __name__ == "__main__":
    valor = int(input("Digite um número: "))
    valor_absoluto()


#Questão 3
def fatorial():
    y = 1
    for x in range(1,valor+1):
        y *= x
    print(f"O número fatorial é: {y}")

if __name__ == "__main__":
    valor = int(input("Digite um número: "))
    fatorial()
