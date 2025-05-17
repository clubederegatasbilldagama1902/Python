#QUESTÃO 1

lista_par = []
lista_impar = []

print("Digite '0' para sair! ")

while True:
    numero = int(input("Digite um número "))

    if numero == 0:
        break
    if numero % 2 == 0:
        lista_par.append(numero)
    if numero != 0:
        lista_impar.append(numero)

soma_par = sum(lista_par)
qntd_par = len(lista_par)
soma_impar = sum(lista_impar)
qntd_impar = len(lista_impar)

media_par = soma_par / qntd_par
media_impar = soma_impar / qntd_impar

print(f"A média dos números pares é: {media_par} \n A média dos números impares é: {media_impar}")

#QUESTÃO 2

lista_masculino = []
lista_feminino = []

print("Digite '0' para sair! ")

while True:
    altura = float(input("Digite a sua altura "))

    if altura == 0:
        break

    else:
        genero = str(input("Digite 'M' para masculino ou 'F' para feminino "))

        if genero == "M" or 'm':
            lista_masculino.append(altura)
        elif genero == "F" or "f":
            lista_feminino.append(altura)

qntd_masculino = len(lista_masculino)
qntd_feminino = len(lista_feminino)
menor_altura = lista_masculino + lista_feminino
maior_altura = lista_masculino + lista_feminino

print(f"A quantidade de pessoas do gênero masculino no grupo é de: {qntd_masculino}")
print(f"A quantidade de pessoas do gênero feminino no grupo é de: {qntd_feminino}")
print(f"A maior altura do grupo é de: {maior_altura} \n A menor altura do grupo é de: {menor_altura}")
