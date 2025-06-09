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
                                              font=("Calibri", 20))  # Fonte e tamanho
        self.label_game_information.place(x=20, y=20)  # Posicionamento

        # Label para seção de informações do usuário
        self.label_player_information = ttk.Label(self,
                                                text="Informação do Usuário",
                                                background="#664983",
                                                font=("Calibri", 20))
        self.label_player_information.place(x=20, y=360)  # Posicionamento abaixo


class InsertFrame(tk.Frame):
    """Frame para operações de inserção (INSERT) de dados"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)  # Configurações visuais


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
                                              background="#664983",  # Roxo escuro
                                              font=("Calibri", 20))  # Fonte e tamanho
        self.label_cart_information.place(x=200, y=20)  # Posicionamento centralizado
