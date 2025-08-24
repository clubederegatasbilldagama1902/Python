notas = [200,100,50,20,10,5,2]
qntd_nota = [50,50,50,50,50,50,50]
valor = 0
for nota in range(0,7):
    notas2 = notas[nota]*qntd_nota[nota]
    valor += notas2
print(f"Nesse caixa, tem disponível: R$ {valor:.2f}")

while True:
    saque = float(input("Digite quanto você quer sacar: "))

    if saque > valor:
        print(f"""Saque indisponível! Valor maior do que disponível!
    O valor máximo para saque permitido neste terminal é de: R$ {valor:.2f}""")

    resto = saque

    for dinheiro in range(0,7):
        if resto / notas[dinheiro] >= 1:
            qntd_nota = resto // notas[dinheiro]
            resto += - (qntd_nota * notas[dinheiro])
            print(f"A quantidade de notas de R$ {notas[dinheiro]} é de: {qntd_nota:.0f} notas")

    new_saque = str(input("Deseja realizar um novo saque? Sim/Não: ")).strip().upper()

    valor -= saque

    print(f'Neste caixa tem R${valor:.2f} em notas de {notas} ')

    if valor == 0:
        print('voce conseguiu estourar o caixa')
        break

    if new_saque == "NAO":
        break
