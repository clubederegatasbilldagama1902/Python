def line():
    print("+=+="*69)

largura = int(input("Digite a largura do seu terreno: "))
comprimento = int(input("Digite o comprimento do seu terreno: "))

investimento = 225 + 500 + 1200 + 2824
area = largura * comprimento
covas = area * 4
pes = covas * 3
espigas = pes * 3
venda = espigas * 0.83
lucro = venda - investimento
gasto_mes = lucro / 12

line()
print(f"\nA área total do terreno é: {area}\n")
line()
print(f"\nO total a ser investido: R$ {investimento}\n")
line()
print(f"\nO total de covas no terreno por m²: {covas}\n")
line()
print(f"\nA quantidade de pes por cova serão de: {pes}\n")
line()
print(f"\nO total de espigas a serem colhidas será de: {espigas}\n")
line()
print(f"\nO total adquirido com a venda das espigas será de: R$ {venda: .2f}\n")
line()
print(f"\nO lucro com a venda das espigas será de: R$ {lucro: .2f}\n")
line()
print(f"\nPoderá ser gastado por mês até acabar o dinheiro: R$ {gasto_mes: .2f}\n")
line()
