# -----------------------> IMPORTAÇÕES DE BIBLIOTECAS <-----------------------

from PIL import Image  # Para manipulação de imagens
from PIL import ImageTk  # Para integração de imagens com Tkinter
from FrameClass import *  # Importa classes personalizadas de frames
from ButtonClass import AppButton  # Classe personalizada para botões
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
    """Carrega uma imagem, redimensiona e converte para formato compatível com Tkinter"""
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
frame_select = SelectFrame(window)  # Frame para consulta de dados
frame_insert = InsertFrame(window)  # Frame para inserção de dados
frame_update = UpdateFrame(window)  # Frame para atualização de dados
frame_delete = DeleteFrame(window)  # Frame para exclusão de dados
frame_cart = CartFrame(window)      # Frame para o carrinho de compras

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
    """Controla a exibição do frame de seleção/consulta e do carrinho"""
    global frame_select_visible, frame_insert_visible, \
        frame_update_visible, frame_delete_visible, frame_cart_visible

    # Se o frame já está visível, esconde
    if frame_select_visible:
        frame_select.place_forget()
        frame_cart.place_forget()
        frame_select_visible = False
        frame_cart_visible = False
    else:
        # Mostra o frame de seleção e carrinho
        frame_select.place(x=250, y=15)
        frame_cart.place(x=1055, y=15)

        frame_select_visible = True
        frame_cart_visible = True

        # Esconde todos os outros frames
        frame_insert.place_forget()
        frame_update.place_forget()
        frame_delete.place_forget()

        frame_insert_visible = False
        frame_update_visible = False
        frame_delete_visible = False


def insert_frame():
    """Controla a exibição do frame de inserção de dados"""
    global frame_insert_visible, frame_select_visible, \
        frame_update_visible, frame_delete_visible, frame_cart_visible
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

def update_frame():
    """Controla a exibição do frame de UPDATE"""
    global frame_update_visible, frame_select_visible, \
        frame_insert_visible, frame_delete_visible, frame_cart_visible
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


def delete_frame():
    """Controla a exibição do frame de DELETE"""
    global frame_delete_visible, frame_select_visible, \
        frame_insert_visible, frame_update_visible, frame_cart_visible
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


def game_frame():
    """Controla a exibição do frame de informações de jogos"""
    global frame_game_visible, frame_player_visible, \
        label_entry_id_game, entry_id_game, \
        label_entry_name_game, entry_name_game, \
        label_entry_gender_game, entry_gender_game, \
        label_entry_price_game, entry_price_game, \
        label_entry_producer_game, entry_producer_game, \
        label_entry_age_game, entry_age_game

    if frame_game_visible:
        label_entry_id_game.place_forget()
        label_entry_name_game.place_forget()
        label_entry_gender_game.place_forget()
        label_entry_price_game.place_forget()
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
        label_entry_id_game.place(x=30, y=165)
        label_entry_name_game.place(x=190,y=165)
        label_entry_gender_game.place(x=350, y=165)
        label_entry_price_game.place(x=510,y=165)
        label_entry_producer_game.place(x=670, y=165)
        label_entry_age_game.place(x=830, y=165)

        entry_id_game.place(x=30, y=200)
        entry_name_game.place(x=190,y=200)
        entry_gender_game.place(x=350, y=200)
        entry_price_game.place(x=510,y=200)
        entry_producer_game.place(x=670, y=200)
        entry_age_game.place(x=830, y=200)

        frame_game_visible = True
        frame_player_visible = False

def player_frame():
    """Controla a exibição do frame de informações de jogadores"""
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
        label_entry_id_player.place(x=30, y=165)
        label_entry_name_player.place(x=190,y=165)
        label_entry_age_player.place(x=350, y=165)
        label_entry_country_player.place(x=510,y=165)
        label_entry_status_player.place(x=670, y=165)
        label_entry_games_created_player.place(x=830, y=165)

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
canvas_line.place(x=200, y=100)     # Posiciona o canvas na janela
canvas_line.configure(bg=purple)    # Configura cor de fundo
canvas_line.config(bd=0, highlightthickness=0)  # Remove bordas

def draw_rounded_line(canvas, x, y1, y2, width, color):
    """Desenha uma linha vertical com extremidades arredondadas"""
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

# -----------------------> CAMPOS DE ENTRADA NO FRAME DE JOGOS <-----------------------

# Label para o campo de ID do Jogo
label_entry_id_game = ttk.Label(frame_insert,
                               text="ID Jogo",
                               background=light_purple,
                               font=("Calibri", 20))

# Campo de entrada para o ID do Jogo
entry_id_game = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_id_game.configure(bg="#C6B4C9")

# Label para o campo de Nome do Jogo
label_entry_name_game = ttk.Label(frame_insert,
                                 text="Nome",
                                 background=light_purple,
                                 font=("Calibri", 20))

# Campo de entrada para o Nome do Jogo
entry_name_game = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_name_game.configure(bg="#C6B4C9")

# Label para o campo de Gênero do Jogo
label_entry_gender_game = ttk.Label(frame_insert,
                                  text="Gênero",
                                  background=light_purple,
                                  font=("Calibri", 20))

# Campo de entrada para o Gênero do Jogo
entry_gender_game = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_gender_game.configure(bg="#C6B4C9")

# Label para o campo de Preço do Jogo
label_entry_price_game = ttk.Label(frame_insert,
                                 text="Preço",
                                 background=light_purple,
                                 font=("Calibri", 20))

# Campo de entrada para o Preço do Jogo
entry_price_game = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_price_game.configure(bg="#C6B4C9")

# Label para o campo de Produtora do Jogo
label_entry_producer_game = ttk.Label(frame_insert,
                                    text="Produtora",
                                    background=light_purple,
                                    font=("Calibri", 20))

# Campo de entrada para a Produtora do Jogo
entry_producer_game = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_producer_game.configure(bg="#C6B4C9")

# Label para o campo de Idade indicada do Jogo
label_entry_age_game = ttk.Label(frame_insert,
                               text="Idade",
                               background=light_purple,
                               font=("Calibri", 20))

# Campo de entrada para a Idade indicada do Jogo
entry_age_game = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_age_game.configure(bg="#C6B4C9")







# Label para o campo de ID do Usuário (Jogador)
label_entry_id_player = ttk.Label(frame_insert,
                                text="ID do Usuário",
                                background=light_purple,
                                font=("Calibri", 20))

# Campo de entrada para o ID do Usuário
entry_id_player = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_id_player.configure(bg="#C6B4C9")

# Label para o campo de Nome do Usuário
label_entry_name_player = ttk.Label(frame_insert,
                                  text="Nome",
                                  background=light_purple,
                                  font=("Calibri", 20))

# Campo de entrada para o Nome do Usuário
entry_name_player = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_name_player.configure(bg="#C6B4C9")

# Label para o campo de Idade do Usuário
label_entry_age_player = ttk.Label(frame_insert,
                                 text="Idade",
                                 background=light_purple,
                                 font=("Calibri", 20))

# Campo de entrada para a Idade do Usuário
entry_age_player = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_age_player.configure(bg="#C6B4C9")

# Label para o campo de País do Usuário
label_entry_country_player = ttk.Label(frame_insert,
                                      text="País",
                                      background=light_purple,
                                      font=("Calibri", 20))

# Campo de entrada para o País do Usuário
entry_country_player = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_country_player.configure(bg="#C6B4C9")

# Label para o campo de Status do Usuário
label_entry_status_player = ttk.Label(frame_insert,
                                    text="Status",
                                    background=light_purple,
                                    font=("Calibri", 20))

# Campo de entrada para o Status do Usuário
entry_status_player = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_status_player.configure(bg="#C6B4C9")

# Label para o campo de quantidade de Jogos Criados pelo Usuário
label_entry_games_created_player = ttk.Label(frame_insert,
                                           text="Jogos Criados",
                                           background=light_purple,
                                           font=("Calibri", 20))

# Campo de entrada para a quantidade de Jogos Criados pelo Usuário
entry_games_created_player = tk.Entry(frame_insert, width=20, bg=purple, fg=light_purple, font=("Calibri", 10))
entry_games_created_player.configure(bg="#C6B4C9")

# -----------------------> INÍCIA O LOOP PRINCIPAL DA INTERFACE <-----------------------

if __name__ == "__main__":
    # Cria uma instância da classe AppButton que gerencia todos os botões
    app_buttons = AppButton(
        window,  # Janela principal
        light_purple,  # Cor principal dos botões
        medium_lilac,  # Cor secundária
        frame_select,  # Frame de consulta
        frame_insert,  # Frame de inserção
        frame_cart,  # Frame do carrinho
        select_image,  # Ícone para consulta
        insert_image,  # Ícone para inserção
        update_image,  # Ícone para atualização
        delete_image,  # Ícone para exclusão
        select_frame,  # Função para mostrar frame de consulta
        insert_frame,  # Função para mostrar frame de inserção
        update_frame,  # Função para mostrar frame de atualização
        delete_frame,  # Função para mostrar frame de exclusão
        game_frame,
        player_frame
    )

    # Criação dos botões na interface
    app_buttons.create_main_buttons()  # Botões principais CRUD
    app_buttons.create_select_frame_buttons()  # Botões do frame de consulta
    app_buttons.create_cart_frame_buttons()  # Botões do frame do carrinho
    app_buttons.create_insert_frame_buttons()  # Botões do frame de inserção

    # Inicia o loop principal da interface gráfica
    window.mainloop()
