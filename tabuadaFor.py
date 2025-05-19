# Loop infinito que só termina quando o usuário escolher parar
while True:
    # Solicita ao usuário um número inteiro
    o = int(input("Digite um número: "))

    # Loop que itera pelos números de 1 a 10 (inclusive)
    for num in range(1, 10+1):
        # Realiza as 4 operações matemáticas básicas
        soma = o + num          # Adição
        multiplicacao = o * num # Multiplicação
        divisao = o / num       # Divisão
        subtracao = o - num     # Subtração
        
        # Imprime os resultados formatados em uma tabela visual
        print(f"{o:.0f} + {num} = {soma:2.0f} {"|": ^2} "  # Adição
              f"{o:.0f} x {num} = {multiplicacao:2.0f} {"|": ^5} "  # Multiplicação
              f"{multiplicacao:2.0f} / {o:2.0f} = {num:.0f} {"|": ^5} "  # Divisão inversa
              f"{soma:.0f} - {o:2.0f} = {num:.0f}")  # Subtração inversa
    
    # Pergunta se o usuário deseja continuar
    mat = str(input("Deseja continuar? SIM/NAO: ")).upper()
    
    # Se a resposta for "NAO", encerra o loop
    if mat == "NAO":
        break  # Sai do loop while True
