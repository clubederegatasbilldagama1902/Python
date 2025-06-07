# -----------------------> IMPORTAÇÕES DE BIBLIOTECAS <-----------------------

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Separator
import tkinter as tk
import customtkinter
from customtkinter import CTkImage
import PIL
from PIL import Image
from PIL import ImageTk
from FrameClass import *
from ButtonClass import AppButton
import warnings  # Para gerenciar avisos

warnings.filterwarnings("ignore", category=UserWarning)  # Ignora avisos específicos

# -----------------------> DEFINIÇÃO DE CORES <-----------------------

# Cores Hexadecimais
purple = "#442e73"  # Roxo escuro (cor principal)
light_purple = "#664983"  # Roxo mais claro
light_lilac = "#987FAB"  # Lilás claro
medium_lilac = "#A676B0"  # Lilás médio
white = "#FFFFFF"  # Branco puro

# -----------------------> CONFIGURAÇÃO DA JANELA PRINCIPAL <-----------------------

# Cria a janela principal com tema "cyborg" (escuro com elementos roxos)
window = ttk.Window(themename="cyborg")
window.title("Plataforma de Jogos")  # Título da janela
window.geometry("1600x700")  # Define tamanho fixo da janela
window.configure(background=purple)  # Cor de fundo principal
window.resizable(width=False, height=False)  # Impede redimensionamento

# -----------------------> CONFIGURAÇÃO DE ESTILOS <-----------------------

style = ttk.Style()  # Objeto para gerenciar estilos

# Estilo personalizado para botões principais
style.configure("Custom.TButton",
                background=light_purple,  # Cor de fundo
                foreground="white",  # Cor do texto
                font=("Segoe UI", 14, "bold"),  # Fonte
                padding=20,  # Espaçamento interno
                borderwidth=0)  # Remove borda
# Define comportamento ao passar mouse
style.map("Custom.TButton",
          background=[("active", "#573a87")])  # Cor mais clara quando ativo

# Segundo estilo de botão (pode ser usado para diferenciação)
style.configure("CustomTwo.TButton",
                background=light_purple,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("CustomTwo.TButton",
          background=[("active", "#573a87")])

# -----------------------> PREPARAÇÃO DE IMAGENS PARA OS BOTÕES <-----------------------

# Função auxiliar para carregar e preparar imagens
def load_image(path, size=(25, 25)):
    # Carrega uma imagem, redimensiona e converte para formato Tkinter
    image = Image.open(path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)

# Carrega ícones para os botões CRUD
select_image = load_image("select.png")  # Ícone para select
insert_image = load_image("insert.png")  # Ícone para insert
update_image = load_image("update.png")  # Ícone para update
delete_image = load_image("delete.png")  # Ícone para delete

# -----------------------> CRIAÇÃO DE FRAMES (ÁREAS DE CONTEÚDO) <-----------------------

# Frame para operações de SELECT
frame_select = SelectFrame(window)
frame_insert = InsertFrame(window)
frame_update = UpdateFrame(window)
frame_delete = DeleteFrame(window)
frame_cart = CartFrame(window)

# -----------------------> CONTROLE DE VISIBILIDADE DOS FRAMES <-----------------------

# Variáveis booleanas para rastrear qual frame está visível
frame_select_visible = False
frame_insert_visible = False
frame_update_visible = False
frame_delete_visible = False
frame_cart_visible = False
frame_game_visible = False
frame_player_visible = False

# -----------------------> FUNÇÕES PARA GERENCIAR FRAMES <-----------------------

def select_frame():
    #Controla a exibição do frame de seleção/consulta e carrinho
    global frame_select_visible, frame_insert_visible, frame_update_visible, frame_delete_visible, frame_cart_visible

    # Se o frame já está visível, esconde
    if frame_select_visible:
        frame_select.place_forget()
        frame_select_visible = False
        frame_cart.place_forget()
        frame_cart_visible = False
    else:
        # Mostra o frame de seleção e carrinho
        frame_select.place(x=250, y=15)
        frame_select_visible = True
        frame_cart.place(x=1055, y=15)
        frame_cart_visible = True

        # Esconde todos os outros frames
        frame_insert.place_forget()
        frame_insert_visible = False
        frame_update.place_forget()
        frame_update_visible = False
        frame_delete.place_forget()
        frame_delete_visible = False


def insert_frame():  #Controla a exibição do frame de inserção
    global frame_insert_visible, frame_select_visible, frame_update_visible, frame_delete_visible, frame_cart_visible
    if frame_insert_visible:
        frame_insert.place_forget()
        frame_insert_visible = False
    else:
        frame_insert.place(x=250, y=15)
        frame_insert_visible = True
        # Esconde os outros frames
        frame_select.place_forget()
        frame_update.place_forget()
        frame_delete.place_forget()
        frame_cart.place_forget()

        frame_select_visible = False
        frame_update_visible = False
        frame_delete_visible = False
        frame_cart_visible = False

def update_frame():  #Controla a exibição do frame de UPDATE
    global frame_update_visible, frame_select_visible, frame_insert_visible, frame_delete_visible, frame_cart_visible
    if frame_update_visible:
        frame_update.place_forget()
        frame_update_visible = False
    else:
        frame_update.place(x=250, y=15)
        frame_update_visible = True
        # Esconde os outros frames
        frame_select.place_forget()
        frame_insert.place_forget()
        frame_delete.place_forget()
        frame_cart.place_forget()

        frame_select_visible = False
        frame_insert_visible = False
        frame_delete_visible = False
        frame_cart_visible = False


def delete_frame():  #Controla a exibição do frame de DELETE
    global frame_delete_visible, frame_select_visible, frame_insert_visible, frame_update_visible, frame_cart_visible
    if frame_delete_visible:
        frame_delete.place_forget()
        frame_delete_visible = False
    else:
        frame_delete.place(x=250, y=15)
        frame_delete_visible = True
        # Esconde os outros frames
        frame_select.place_forget()
        frame_insert.place_forget()
        frame_update.place_forget()
        frame_cart.place_forget()

        frame_select_visible = False
        frame_insert_visible = False
        frame_update_visible = False
        frame_cart_visible = False


def game_frame():    #Controla a exibição do frame de informações de jogos
    global frame_game_visible, frame_player_visible, \
        label_entry_id_game, entry_id_game, \
        label_entry_name_game, entry_name_game, \
        label_entry_gender_game, entry_gender_game, \
        label_entry_price_game, entry_price_game, \
        label_entry_producer_game, entry_producer_game, \
        label_entry_age_game, entry_age_game

    if frame_game_visible:
        label_entry_id_game .place_forget()
        label_entry_name_game .place_forget()
        label_entry_gender_game.place_forget()
        label_entry_price_game .place_forget()
        label_entry_producer_game.place_forget()
        label_entry_age_game.place_forget()

        entry_id_game.place_forget()
        entry_name_game.place_forget()
        entry_gender_game.place_forget()
        entry_price_game.place_forget()
        entry_producer_game.place_forget()
        entry_age_game.place_forget()

        frame_game_visible = False

    else:
        # Posição dos Labels
        label_entry_id_game.place(x=30, y=165)
        label_entry_name_game.place(x=190,y=165)
        label_entry_gender_game.place(x=350, y=165)
        label_entry_price_game.place(x=510,y=165)
        label_entry_producer_game.place(x=670, y=165)
        label_entry_age_game.place(x=830, y=165)

        # Posição dos Campos de Entrada
        entry_id_game.place(x=30, y=200)
        entry_name_game.place(x=190,y=200)
        entry_gender_game.place(x=350, y=200)
        entry_price_game.place(x=510,y=200)
        entry_producer_game.place(x=670, y=200)
        entry_age_game.place(x=830, y=200)

        frame_game_visible = True
        frame_player_visible = False


def player_frame():     #Controla a exibição do frame de informações de jogadores
    global frame_player_visible, frame_game_visible, \
        label_entry_id_player, entry_id_player, \
        label_entry_name_player, entry_name_player, \
        label_entry_age_player, entry_age_player, \
        label_entry_country_player, entry_country_player, \
        label_entry_status_player, entry_status_player, \
        label_entry_games_created_player, entry_games_created_player

    if frame_player_visible:
        label_entry_id_player.place_forget()
        label_entry_name_player.place_forget()
        label_entry_age_player.place_forget()
        label_entry_country_player.place_forget()
        label_entry_status_player.place_forget()
        label_entry_games_created_player.place_forget()

        entry_id_player.place_forget()
        entry_name_player.place_forget()
        entry_age_player.place_forget()
        entry_country_player.place_forget()
        entry_status_player.place_forget()
        entry_games_created_player.place_forget()

        frame_player_visible = False

    else:
        # Posição dos Labels
        label_entry_id_player.place(x=30, y=165)
        label_entry_name_player.place(x=190,y=165)
        label_entry_age_player.place(x=350, y=165)
        label_entry_country_player.place(x=510,y=165)
        label_entry_status_player.place(x=670, y=165)
        label_entry_games_created_player.place(x=830, y=165)

        # Posição dos Campos de Entrada
        entry_id_player.place(x=30,y=200)
        entry_name_player.place(x=190,y=200)
        entry_age_player.place(x=350, y=200)
        entry_country_player.place(x=510,y=200)
        entry_status_player.place(x=670, y=200)
        entry_games_created_player.place(x=830, y=200)

        frame_player_visible = True
        frame_game_visible = False

# -----------------------> ELEMENTOS VISUAIS ADICIONAIS <-----------------------

# Cria uma linha vertical decorativa com extremidades arredondadas
canvas_line = tk.Canvas(
    window,
    width=10,
    height=520,
    bg=purple,
    highlightthickness=0,  # Remove destaque da borda
    borderwidth=0,  # Remove borda
    relief='flat'  # Estilo plano
)
canvas_line.place(x=200, y=100)
canvas_line.configure(bg=purple)
canvas_line.config(bd=0, highlightthickness=0)  # Remove bordas

def draw_rounded_line(canvas, x, y1, y2, width, color):
    # Desenha uma linha vertical com extremidades arredondadas
    radius = width // 2
    # Desenha a linha vertical principal
    canvas.create_rectangle(
        x, y1 + radius,
           x + width, y2 - radius,
        fill=color,
        outline=color,
        width=0
    )
    # Desenha as extremidades arredondadas (semicírculos)
    canvas.create_oval(
        x, y1,
        x + width, y1 + width,
        fill=color,
        outline=color,
        width=0
    )
    canvas.create_oval(
        x, y2 - width,
           x + width, y2,
        fill=color,
        outline=color,
        width=0
    )

# Aplica a função para desenhar a linha
draw_rounded_line(canvas_line, 0, 0, 489, 10, light_lilac)

# -----------------------> INÍCIA O LOOP PRINCIPAL DA INTERFACE <-----------------------

if __name__ == "__main__":

    app_buttons = AppButton(
        window,
        light_purple,
        medium_lilac,
        frame_select,
        frame_insert,
        frame_cart,
        select_image,
        insert_image,
        update_image,
        delete_image,
        select_frame,
        insert_frame,
        update_frame,
        delete_frame,
        game_frame)

    # Criação dos botões
    app_buttons.create_main_buttons()
    app_buttons.create_select_frame_buttons()
    app_buttons.create_cart_frame_buttons()
    app_buttons.create_insert_frame_buttons()

    window.mainloop()
