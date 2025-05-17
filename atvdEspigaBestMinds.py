# Função para imprimir uma linha decorativa
def line():
    print("+=+="*69)

# Solicita as dimensões do terreno ao usuário
largura = int(input("Digite a largura do seu terreno: "))  # Largura em metros
comprimento = int(input("Digite o comprimento do seu terreno: "))  # Comprimento em metros

# Cálculo do investimento total fixo
investimento = 225 + 500 + 1200 + 2824  # Valores pré-definidos de custos

# Cálculos agrícolas:
area = largura * compprimento  # Calcula área total do terreno em m²
covas = area * 4  # Calcula número de covas (4 por m²)
pes = covas * 3  # Calcula número de pés de milho (3 por cova)
espigas = pes * 3  # Calcula número de espigas (3 por pé)
venda = espigas * 0.83  # Calcula valor total de venda (R$ 0,83 por espiga)

# Cálculos financeiros:
lucro = venda - investimento  # Calcula lucro total
gasto_mes = lucro / 12  # Calcula gasto mensal permitido (dividindo por 12 meses)

# Exibição dos resultados formatados:
line()
print(f"\nA área total do terreno é: {area}\n")  # Mostra área calculada
line()
print(f"\nO total a ser investido: R$ {investimento}\n")  # Mostra investimento
line()
print(f"\nO total de covas no terreno por m²: {covas}\n")  # Mostra covas
line()
print(f"\nA quantidade de pes por cova serão de: {pes}\n")  # Mostra pés de milho
line()
print(f"\nO total de espigas a serem colhidas será de: {espigas}\n")  # Mostra espigas
line()
print(f"\nO total adquirido com a venda das espigas será de: R$ {venda: .2f}\n")  # Valor de venda
line()
print(f"\nO lucro com a venda das espigas será de: R$ {lucro: .2f}\n")  # Lucro calculado
line()
print(f"\nPoderá ser gastado por mês até acabar o dinheiro: R$ {gasto_mes: .2f}\n")  # Gasto mensal
line()
