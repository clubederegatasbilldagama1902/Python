# FramesClasses.py
import tkinter as tk  # Importa a biblioteca tkinter para interface gráfica
import ttkbootstrap as ttk  # Importa ttkbootstrap para estilos modernos

class SelectFrame(tk.Frame):
    """Frame para exibir informações de consulta (SELECT)"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Configurações básicas do frame
        self.configure(background="#664983", width=800, height=600)  # Roxo claro como fundo
        self.create_widgets()  # Chama o método para criar os widgets

    def create_widgets(self):
        """Cria os elementos visuais do frame de consulta"""
        # Label para seção de informações do jogo
        self.label_game_information = ttk.Label(self,
                                              text="Informação do Jogo",
                                              background="#664983",  # Cor de fundo
                                              font=("Times New Roman", 20))  # Fonte e tamanho
        self.label_game_information.place(x=20, y=20)  # Posicionamento

        # Label para seção de informações do usuário
        self.label_player_information = ttk.Label(self,
                                                text="Informação do Usuário",
                                                background="#664983",
                                                font=("Times New Roman", 20))
        self.label_player_information.place(x=20, y=360)  # Posicionamento abaixo


class InsertFrame(tk.Frame):
    """Frame para operações de inserção (INSERT) de dados"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)  # Configurações visuais
        self.widgets = {}  # Dicionário para armazenar os widgets criados

    def mostrar_campos_jogo(self):
        """Exibe os campos para inserção de dados de jogos"""
        # Remove widgets existentes (limpa o frame)
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Label):
                widget.destroy()

        self.widgets.clear()  # Limpa o dicionário de widgets

        # Define os campos necessários para cadastro de jogos
        campos_jogo = [
            {"text": "ID Jogo", "var_name": "id_game", "column": 0},
            {"text": "Nome", "var_name": "name_game", "column": 1},
            {"text": "Gênero", "var_name": "gender_game", "column": 2},
            {"text": "Preço", "var_name": "price_game", "column": 3},
            {"text": "Produtora", "var_name": "producer_game", "column": 4},
            {"text": "Idade", "var_name": "age_game", "column": 5}
        ]

        self.create_fields(self, campos_jogo)  # Cria os campos na interface

    def mostrar_campos_jogador(self):
        """Exibe os campos para inserção de dados de jogadores"""
        # Remove widgets existentes (limpa o frame)
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Label):
                widget.destroy()

        self.widgets.clear()  # Limpa o dicionário de widgets

        # Define os campos necessários para cadastro de jogadores
        campos_jogador = [
            {"text": "ID do Usuário", "var_name": "id_player", "column": 0},
            {"text": "Nome", "var_name": "name_player", "column": 1},
            {"text": "Idade", "var_name": "age_player", "column": 2},
            {"text": "País", "var_name": "country_player", "column": 3},
            {"text": "Status", "var_name": "status_player", "column": 4},
            {"text": "Jogos Criados", "var_name": "games_created_player", "column": 5}
        ]

        self.create_fields(self, campos_jogador)  # Cria os campos na interface

    def create_fields(self, parent, fields):
        """Método genérico para criação de campos de formulário"""
        for field in fields:
            x_pos = 30 + field["column"] * 180  # Calcula posição horizontal

            # Cria Label (etiqueta do campo)
            label = ttk.Label(
                parent,
                text=field["text"],
                background="#664983",  # Cor de fundo
                font=("Calibri", 20)  # Fonte e tamanho
            )
            label.place(x=x_pos, y=165)  # Posicionamento
            label.configure(background="#664983", font=("Calibri",20))

            # Cria Entry (campo de entrada de texto)
            entry = tk.Entry(
                parent,
                width=20,
                bg="#442e73",  # Cor de fundo (roxo escuro)
                fg="#664983",  # Cor do texto
                font=("Calibri", 10)  # Fonte e tamanho
            )
            entry.place(x=x_pos, y=200)  # Posicionamento
            entry.configure(background="#C6B4C9")  # Altera cor de fundo (lilás claro)

            # Armazena no dicionário para acesso posterior
            self.widgets[field["var_name"]] = entry


class UpdateFrame(tk.Frame):
    """Frame para operações de atualização (UPDATE) de dados"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)  # Configurações visuais
        # (Implementação dos widgets específicos ficaria aqui)


class DeleteFrame(tk.Frame):
    """Frame para operações de exclusão (DELETE) de dados"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)  # Configurações visuais
        # (Implementação dos widgets específicos ficaria aqui)


class CartFrame(tk.Frame):
    """Frame para exibir o carrinho de compras"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=470, height=600)  # Configurações visuais
        self.create_widgets()  # Chama o método para criar os widgets

    def create_widgets(self):
        """Cria os elementos visuais do frame do carrinho"""
        self.label_cart_information = ttk.Label(self,
                                              text="Carrinho",
                                              background="#442e73",  # Roxo escuro
                                              font=("Times New Roman", 20))  # Fonte e tamanho
        self.label_cart_information.place(x=200, y=20)  # Posicionamento centralizado
