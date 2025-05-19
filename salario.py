# Função que imprime uma linha divisória
def linha():
    print("=+=+"*69)  # Imprime o padrão "=+=+" repetido 69 vezes

# Loop principal do programa
while True:
    # Solicita informações do usuário
    salario = float(input("Digite quanto você ganha por mês: "))
    sindicato = str(input("Digite [Sim] para caso você pague o sindicato ou [Não] para caso você não pague o sindicato: ")).upper()
    
    # Calcula o salário anual
    ano = salario * 12
    print(f"Você recebe por ano: R$ {ano:.2f}")

    # Verifica a faixa salarial e calcula os descontos
    if salario <= 2112:  # Primeira faixa (isento de IR)
        if sindicato == "SIM":
            valor_sindicato = salario * 0.05  # 5% para sindicato
            inss = salario * 0.11  # 11% de INSS
            desconto = valor_sindicato + inss
            liquido = salario - desconto
            print(f"Você paga ao sindicato: R$ {valor_sindicato:.2f}")
            print("Você não paga imposto de renda")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
            break
        elif sindicato == "NAO":
            inss = salario * 0.11
            desconto = inss  # Corrigido: era 'salario - inss' que não faz sentido
            liquido = salario - desconto
            print("Você não paga imposto de renda")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
            break
        else:
            print("Palavra digitada não aceita!")

    elif salario <= 2826.55:  # Segunda faixa (7.5% IR)
        if sindicato == "SIM":
            valor_sindicato = salario * 0.05
            imposto = salario * 0.075  # 7.5% de IR
            inss = salario * 0.11
            desconto = imposto + inss + valor_sindicato
            liquido = salario - desconto
            print(f"Você paga ao sindicato: R$ {valor_sindicato:.2f}")
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
            break
        elif sindicato == "NAO":
            inss = salario * 0.11
            imposto = salario * 0.075
            desconto = imposto + inss
            liquido = salario - desconto
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
            break

    elif salario <= 3751.05:  # Terceira faixa (15% IR)
        if sindicato == "SIM":
            valor_sindicato = salario * 0.05
            imposto = salario * 0.15  # 15% de IR
            inss = salario * 0.11
            desconto = imposto + inss + valor_sindicato
            liquido = salario - desconto
            print(f"Você paga ao sindicato: R$ {valor_sindicato:.2f}")
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
        else:
            imposto = salario * 0.15
            inss = salario * 0.11
            desconto = imposto + inss
            liquido = salario - desconto
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")

    elif salario <= 4664.68:  # Quarta faixa (22.5% IR)
        if sindicato == "SIM":
            valor_sindicato = salario * 0.05
            imposto = salario * 0.225  # 22.5% de IR
            inss = salario * 0.11
            desconto = imposto + inss + valor_sindicato
            liquido = salario - desconto
            print(f"Você paga ao sindicato: R$ {valor_sindicato:.2f}")
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
        else:
            imposto = salario * 0.225
            inss = salario * 0.11
            desconto = imposto + inss
            liquido = salario - desconto
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")

    else:  # Quinta faixa (27.5% IR - acima de R$ 4664.68)
        if sindicato == "SIM":
            valor_sindicato = salario * 0.05
            imposto = salario * 0.275  # 27.5% de IR
            inss = salario * 0.11
            desconto = imposto + inss + valor_sindicato
            liquido = salario - desconto
            print(f"Você paga ao sindicato: R$ {valor_sindicato:.2f}")
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
        else:
            imposto = salario * 0.275
            inss = salario * 0.11
            desconto = imposto + inss
            liquido = salario - desconto
            print(f"Você paga de imposto de renda: R$ {imposto:.2f}")
            print(f"Você paga de INSS: R$ {inss:.2f}")
            print(f"É descontado do seu salário: R$ {desconto:.2f}")
            print(f"Seu salário líquido é: R$ {liquido:.2f}")
