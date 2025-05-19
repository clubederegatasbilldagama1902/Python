# QUESTÃO 1

# Cria duas listas vazias para armazenar números
lista_par = []    # Armazenará números pares
lista_impar = []  # Armazenará números ímpares

print("Digite '0' para sair! ")  # Instrução para o usuário

# Loop infinito para receber números
while True:
    numero = int(input("Digite um número "))  # Solicita um número ao usuário

    if numero == 0:  # Condição de saída do loop
        break
    
    # Verifica se o número é par
    if numero % 2 == 0:
        lista_par.append(numero)  # Adiciona à lista de pares
    else:  # Observação: Aqui deveria ser 'else' em vez do segundo 'if'
        lista_impar.append(numero)  # Adiciona à lista de ímpares

# Calcula totais e médias
soma_par = sum(lista_par)      # Soma dos números pares
qntd_par = len(lista_par)      # Quantidade de números pares
soma_impar = sum(lista_impar)  # Soma dos números ímpares
qntd_impar = len(lista_impar)  # Quantidade de números ímpares

# Calcula as médias (observação: pode dar erro se as listas estiverem vazias)
media_par = soma_par / qntd_par      # Média dos pares
media_impar = soma_impar / qntd_impar  # Média dos ímpares

# Exibe os resultados
print(f"A média dos números pares é: {media_par} \n A média dos números impares é: {media_impar}")

#=+=+=+=+=+=+=+==+=+=+=+=+=+=+==+=+=+=+=+=+=+==+=+=+=+=+=+=+==+=+=+=+=+=+=+==+=+=+=+=+=+=+==+=+=+=+=+=+=+=

# QUESTÃO 2

# Cria listas para armazenar alturas por gênero
lista_masculino = []  # Armazenará alturas masculinas
lista_feminino = []    # Armazenará alturas femininas

print("Digite '0' para sair! ")  # Instrução para o usuário

# Loop para coleta de dados
while True:
    altura = float(input("Digite a sua altura "))  # Solicita altura

    if altura == 0:  # Condição de saída
        break
    else:
        genero = str(input("Digite 'M' para masculino ou 'F' para feminino "))

        # Problema: a condição está errada - deveria ser genero.upper() == "M"
        if genero == "M" or 'm':  # Esta condição sempre será verdadeira!
            lista_masculino.append(altura)
        elif genero == "F" or "f":  # Mesmo problema aqui
            lista_feminino.append(altura)

# Calcula quantidades
qntd_masculino = len(lista_masculino)  # Conta homens
qntd_feminino = len(lista_feminino)    # Conta mulheres

# Problema: simplesmente concatena listas sem calcular mínimo/máximo
menor_altura = lista_masculino + lista_feminino  
maior_altura = lista_masculino + lista_feminino

# Exibe resultados (com problemas)
print(f"A quantidade de pessoas do gênero masculino no grupo é de: {qntd_masculino}")
print(f"A quantidade de pessoas do gênero feminino no grupo é de: {qntd_feminino}")
# As variáveis menor_altura e maior_altura estão incorretas
print(f"A maior altura do grupo é de: {maior_altura} \n A menor altura do grupo é de: {menor_altura}")
