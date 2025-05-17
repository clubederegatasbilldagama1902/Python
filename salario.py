def linha():
    print("=+=+"*69)

while True:

        salario = float(input("Digite quanto você ganha por mês: "))
        sindicato = str(input("Digite [Sim] para caso você pague o sindicato ou [Não] para caso você não pague o sindicato: ")).upper()
        ano = salario * 12
        print(f"Você recebe por ano: R$ {ano:.2f}")

        if salario <= 2112:
            if sindicato == "SIM":
                valor_sindicato = salario * 0.05
                inss = salario * 0.11
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
                desconto = salario - inss
                liquido = salario - desconto
                print("Você não paga imposto de renda")
                print(f"Você paga de INSS: R$ {inss:.2f}")
                print(f"É descontado do seu salário: R$ {desconto:.2f}")
                print(f"Seu salário líquido é: R$ {liquido:.2f}")
                break
            else:
                print("Palavra digitada não aceita!")

        elif salario <= 2826.55:
            if sindicato == "SIM":
                valor_sindicato = salario * 0.05
                imposto = salario * 0.075
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
        elif salario <= 3751.05:
            if sindicato == "SIM":
                valor_sindicato = salario * 0.05
                imposto = salario * 0.15
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

        elif salario <= 4664.68:
            if sindicato == "SIM":
                valor_sindicato = salario * 0.05
                imposto = salario * 0.225
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
        else:
            if sindicato == "SIM":
                valor_sindicato = salario * 0.05
                imposto = salario * 0.275
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