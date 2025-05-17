#QUESTÃO 1

notas = 0
alunos = 50
soma = 0

for num in range(alunos):
    notas = float(input(f'Digite a nota do aluno {num+1}: '))
    soma = soma + notas

media = soma/alunos
print(f'A Média dos alunos é: {media}')

#QUESTÃO 2

for fahrenheit in range(45, 81, 1):
    celsius = 5/9*(fahrenheit-32)
    print(f'{fahrenheit:.1f}ºF / {celsius:.3f} ºC')

#QUESTÃO 3

import random

for i in range(5):
    num_sorteado = random.randint(0, 95)
    print(f'{num_sorteado}')