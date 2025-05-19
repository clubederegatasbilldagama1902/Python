#list.clear() - apaga todos os elementos da lista
#list.del() - apaga um elemento especifico da lista
#list.apend() - insere um elemento na lista
#list.insert(i,x) - adiciona o elemento na posição desejada
#list.sort() - ordena a lista na ordem crescente
#list.sorted() - cria uma lista em ordem crescente]
#list.reverse() - inverte os elementos da lista
#list.max() - retorna o maior valor
#list.min() - retorna o menor valor
#list.sum() - retorna a soma dos elementos
#list.len() - conta quantos elementos existem
#list.count() - conta elementos especificos
#list.prod() - retorna o produto dos elementos
#list.extend() - insere uma lista no final de outra lista
#list.in() - verifica se um elemento pertence a lista

# Função que imprime uma linha decorativa
def lin():
    print("=+"*46)

# Criação de duas listas: uma para armazenar os números e outra para guardar os números maiores que 10
lista = []
porcentagem = []

# Informa ao usuário como sair do loop
print("Digite '0' para quebrar o código!")

# Loop para entrada dos números
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break  # Encerra o loop se o número digitado for 0
    lista.append(num)  # Adiciona o número à lista

# Insere o número 33 na posição 1 da lista (segunda posição)
lista.insert(1,33)

# Cálculo de estatísticas básicas
qntd = len(lista)        # Quantidade de elementos na lista
soma = sum(lista)        # Soma de todos os elementos
maximo = max(lista)      # Maior valor da lista
minimo = min(lista)      # Menor valor da lista

# Impressão das informações
lin()
print(f"Os valores da lista são: {lista}")
lin()
print(f"A quantidade de números na lista é: {qntd} \n A soma dos números da lista é: {soma} ")
lin()
print(f"O maior número dentro da lista é: {maximo} \n O menor valor da lista é: {minimo}")
lin()

# Ordena a lista em ordem crescente e decrescente
crescente = list(sorted(lista))
decrescente = list(reversed(crescente))

# Exibe a lista ordenada
print(f"A ordem crescente dos números é: {crescente} \nA ordem decrescente dos número é: {decrescente}")
lin()

# Verifica quais números são maiores que 10 e adiciona à lista 'porcentagem'
for var in lista:
    if var > 10:
        porcentagem.append(var)

# Calcula e exibe a porcentagem de números maiores que 10
print(f"A porcentagem dos números maiores que 10 é: {(len(porcentagem) * 100 / len(lista))}%")
lin()

# Calcula e exibe a média dos números
media = soma / qntd
print(f"A média dos números é: {media: .3f}")
lin()

# Permite ao usuário pesquisar um número na lista
pesquisa = int(input("Digite o valor pra pesquisa: "))

# Verifica se o número está na lista
if pesquisa in lista:
    print("Valor digitado encontrado!")
    lin()
    posicao = lista.index(pesquisa)  # Encontra a posição do número na lista
    print(f"A posição do número digitado é: {posicao}")
    lin()
else:
    print("O valor digitado não se encontra na lista")
    lin()
