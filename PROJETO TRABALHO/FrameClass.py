# FramesClasses.py
import tkinter as tk
import ttkbootstrap as ttk

class SelectFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=800, height=600)
        self.create_widgets()

    def create_widgets(self):
        # Label para seção de informações do jogo
        self.label_game_information = ttk.Label(self,
                                                text="Informação do Jogo",
                                                background="#664983",
                                                font=("Times New Roman", 20))
        self.label_game_information.place(x=20, y=20)

        # Label para seção de informações do usuário
        self.label_player_information = ttk.Label(self,
                                                  text="Informação do Usuário",
                                                  background="#664983",
                                                  font=("Times New Roman", 20))
        self.label_player_information.place(x=20, y=360)


class InsertFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)
        self.widgets = {}

    def show_game_fields(self):
        # Limpa o frame atual
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        # Campos para Jogo
        game_fields = [
            {"text": "ID Jogo", "var_name": "id_game", "column": 0},
            {"text": "Nome", "var_name": "name_game", "column": 1},
            {"text": "Gênero", "var_name": "gender_game", "column": 2},
            {"text": "Preço", "var_name": "price_game", "column": 3},
            {"text": "Produtora", "var_name": "producer_game", "column": 4},
            {"text": "Idade", "var_name": "age_game", "column": 5}
        ]

        self.create_fields(self.fields_frame, game_fields)

    def show_player_fields(self):
        # Limpa o frame atual
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        # Campos para Usuário
        player_fields = [
            {"text": "ID do Usuário", "var_name": "id_player", "column": 0},
            {"text": "Nome", "var_name": "name_player", "column": 1},
            {"text": "Idade", "var_name": "age_player", "column": 2},
            {"text": "País", "var_name": "country_player", "column": 3},
            {"text": "Status", "var_name": "status_player", "column": 4},
            {"text": "Jogos Criados", "var_name": "games_created_player", "column": 5}
        ]

        self.create_fields(self.fields_frame, player_fields)

    def create_fields(self, parent, fields):
        for field in fields:
            x_pos = 30 + field["column"] * 180

            # Label
            label = ttk.Label(
                parent,
                text=field["text"],
                background="#664983",
                font=("Calibri", 14)
            )
            label.place(x=x_pos, y=20)

            # Entry
            entry = tk.Entry(
                parent,
                width=20,
                bg="#C6B4C9",
                fg="#664983",
                font=("Calibri", 10)
            )
            entry.place(x=x_pos, y=50)

            # Armazena no dicionário
            self.widgets[field["var_name"]] = entry


class UpdateFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)
        # Adicione widgets específicos do frame de atualização aqui


class DeleteFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=1300, height=600)
        # Adicione widgets específicos do frame de exclusão aqui


class CartFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background="#664983", width=470, height=600)
        self.create_widgets()

    def create_widgets(self):
        self.label_cart_information = ttk.Label(self,
                                                text="Carrinho",
                                                background="#442e73",
                                                font=("Times New Roman", 20))
        self.label_cart_information.place(x=200, y=20)
