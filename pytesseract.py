import cv2 as marcelo
import pytesseract
def linha():
    print("+=+=+="*56)
carrinho = []
preco = []
qntd = []
soma = []

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\Tesseract.exe'

img = marcelo.imread('1.jpg')

textooo = pytesseract.image_to_string(img)

lista = textooo.split('\n')
produto = lista[0]
preço = lista[2]
print(lista)
print(produto)
print(preço)

print("Digite [0] para finalizar as compras")
linha()
while True:

    produto = str(input("Digite o que você deseja comprar: "))

    if produto == '0':
        break
    linha()

    valor = float(input("Digite o preço desse produto: R$ "))
    linha()
    qntd_produto = int(input("Digite a quantidade de produtos que você deseja adicionar ao seu carrinho: "))
    linha()

    preco.append(valor)
    carrinho.append(produto)
    qntd.append(qntd_produto)
    soma.append(valor * qntd_produto)

valor_dinheiro = sum(soma)

print(f"No seu carrinho tem:")
for compra in range(0,len(carrinho)):
    print(f'{carrinho[compra]} custando {preco[compra]} e você comprou {qntd[compra]}')
print(f"O valor total da sua compra é: R$ {valor_dinheiro}")
