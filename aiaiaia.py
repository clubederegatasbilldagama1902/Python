import mysql.connector
from ttkbootstrap import Window, Treeview, Button, Label
from ttkbootstrap.constants import *

# Configuração da conexão MySQL
config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'seu_banco_de_dados',
}

def conectar_mysql():
    try:
        conexao = mysql.connector.connect(**config)
        cursor = conexao.cursor(dictionary=True)  # Retorna resultados como dicionários
        cursor.execute("SELECT * FROM sua_tabela LIMIT 10")  # Substitua pela sua consulta
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados
    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return []

def exibir_resultados():
    # Limpa a Treeview antes de inserir novos dados
    for row in tree.get_children():
        tree.delete(row)
    
    resultados = conectar_mysql()
    
    if resultados:
        # Cria as colunas com base nas chaves do primeiro resultado
        colunas = list(resultados[0].keys())
        tree["columns"] = colunas
        tree.heading("#0", text="ID")
        
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        # Insere os dados na Treeview
        for i, row in enumerate(resultados):
            tree.insert("", "end", text=str(i+1), values=list(row.values()))
    else:
        Label(janela, text="Nenhum resultado encontrado ou erro na conexão.", bootstyle=DANGER).pack()

# Cria a janela com ttkbootstrap
janela = Window(title="MySQL + ttkbootstrap", themename="darkly")
janela.geometry("800x600")

# Botão para buscar dados
btn_buscar = Button(janela, text="Buscar Dados", command=exibir_resultados, bootstyle=SUCCESS)
btn_buscar.pack(pady=10)

# Treeview para exibir os resultados
tree = Treeview(janela, bootstyle="info")
tree.pack(fill="both", expand=True, padx=10, pady=10)

janela.mainloop()
