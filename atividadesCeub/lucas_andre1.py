#QUESTÃO 1

# Inicialização de variáveis
notas = 0      # Variável temporária para armazenar cada nota
alunos = 50    # Número total de alunos (constante)
soma = 0       # Acumulador para somar todas as notas

# Loop para coletar as notas de cada aluno
for num in range(alunos):  # Repete 50 vezes (de 0 a 49)
    notas = float(input(f'Digite a nota do aluno {num+1}: '))  # Solicita a nota (num+1 para exibir de 1 a 50)
    soma = soma + notas  # Adiciona a nota ao acumulador

# Cálculo e exibição da média
media = soma/alunos  # Divide a soma total pelo número de alunos
print(f'A Média dos alunos é: {media}')  # Mostra o resultado

#=+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+=

#QUESTÃO 2

# Loop através de temperaturas Fahrenheit de 45 a 80
for fahrenheit in range(45, 81, 1):  # De 45 a 80 (81 não incluso), passo 1
    celsius = 5/9*(fahrenheit-32)  # Fórmula de conversão F → C
    print(f'{fahrenheit:.1f}ºF / {celsius:.3f} ºC')  # Exibe com 1 e 3 casas decimais

#=+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+==+=+=+=+=+=

#QUESTÃO 3

import random  # Importa o módulo para geração de números aleatórios

# Loop para gerar 5 números aleatórios
for i in range(5):  # Executa 5 vezes
    num_sorteado = random.randint(0, 95)  # Gera inteiro entre 0 e 95 (inclusive)
    print(f'{num_sorteado}')  # Exibe o número sorteado
