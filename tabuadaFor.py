while True:
    o = int(input("Digite um número: "))

    for num in range(1,10+1):

        soma = o + num
        multiplicacao = o * num
        divisao = o / num
        subtracao = o - num
        print(f"{o:.0f} + {num} = {soma:2.0f} {"|": ^2} {o:.0f} x {num} = {multiplicacao:2.0f} {"|": ^5} {multiplicacao:2.0f} / {o:2.0f} = {num:.0f} {"|": ^5} {soma:.0f} - {o:2.0f} = {num:.0f}")
    mat = str(input("Deseja continuar? SIM/NAO: ")).upper()
    if mat == 'NAO':
        break