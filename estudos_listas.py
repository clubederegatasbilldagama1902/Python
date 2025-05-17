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



def lin():
    print("=+"*46)

lista = []
porcentagem = []
print("Digite '0' para quebrar o código!")

while True:

    num = int(input("Digite um número: "))
    if num == 0:
        break
    lista.append(num)

lista.insert(1,33)

qntd = len(lista)
soma = sum(lista)
maximo = max(lista)
minimo = min(lista)
lin()
print(f"Os valores da lista são: {lista}")
lin()
print(f"A quantidade de números na lista é: {qntd} \n A soma dos números da lista é: {soma} ")
lin()
print(f"O maior número dentro da lista é: {maximo} \n O menor valor da lista é: {minimo}")
lin()
crescente = list(sorted(lista))
decrescente = list(reversed(crescente))

print(f"A ordem crescente dos números é: {crescente} \nA ordem decrescente dos número é: {decrescente}")
lin()
for var in lista:
    if var > 10:
        porcentagem.append(var)

print(f"A porcentagem dos números maiores que 10 é: {(len(porcentagem) * 100 / len(lista))}%")
lin()
media = soma / qntd
print(f"A média dos números é: {media: .3f}")
lin()
pesquisa = int(input("Digite o valor pra pesquisa: "))

if pesquisa in lista:
    print("Valor digitado encontrado!")
    lin()
    posicao = lista.index(pesquisa)
    print(f"A posição do número digitado é: {posicao}")
    lin()
else:
    print("O valor digitado não se encontra na lista")
    lin()