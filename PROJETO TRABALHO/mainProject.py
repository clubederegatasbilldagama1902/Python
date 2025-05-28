# -----------------------> IMPORTAÇÕES DE BIBLIOTECAS <-----------------------

# Importações para interface gráfica e estilização
import ttkbootstrap as ttk  # Framework para estilização do Tkinter
from ttkbootstrap.constants import *  # Constantes do ttkbootstrap
from ttkbootstrap.widgets import Separator  # Componente de separação visual
import tkinter as tk  # Biblioteca padrão para GUI

# Importações para componentes personalizados
import customtkinter  # Biblioteca para widgets modernos
from customtkinter import CTkImage  # Componente de imagem personalizado

# Importações para manipulação de imagens
import PIL  # Biblioteca Python Imaging Library
from PIL import Image, ImageTk  # Classes para trabalhar com imagens

# Importações para banco de dados
import mysql.connector  # Conector para MySQL
import warnings  # Para gerenciar avisos

warnings.filterwarnings("ignore", category=UserWarning)  # Ignora avisos específicos

# -----------------------> DEFINIÇÃO DE CORES <-----------------------

# Cores Hexadecimais
purple = "#442e73"  # Roxo escuro (cor principal)
lightPurple = "#664983"  # Roxo mais claro
lightLilac = "#987FAB"  # Lilás claro
mediumLilac = "#A676B0"  # Lilás médio
tiffany = "#0ABAB2"  # Azul esverdeado (estilo Tiffany)
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
                background=lightPurple,  # Cor de fundo
                foreground="white",  # Cor do texto
                font=("Segoe UI", 14, "bold"),  # Fonte
                padding=20,  # Espaçamento interno
                borderwidth=0)  # Remove borda
# Define comportamento ao passar mouse
style.map("Custom.TButton",
          background=[("active", "#573a87")])  # Cor mais clara quando ativo

# Segundo estilo de botão (pode ser usado para diferenciação)
style.configure("CustomTwo.TButton",
                background=lightPurple,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("CustomTwo.TButton",
          background=[("active", "#573a87")])

# -----------------------> PREPARAÇÃO DE IMAGENS PARA OS BOTÕES <-----------------------

# Função auxiliar para carregar e preparar imagens
def loadImage(path, size=(25, 25)):
    # Carrega uma imagem, redimensiona e converte para formato Tkinter
    image = Image.open(path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)

# Carrega ícones para os botões CRUD
selectImage = loadImage("select.png")  # Ícone para select
insertImage = loadImage("insert.png")  # Ícone para insert
updateImage = loadImage("update.png")  # Ícone para update
deleteImage = loadImage("delete.png")  # Ícone para delete

# -----------------------> CRIAÇÃO DE FRAMES (ÁREAS DE CONTEÚDO) <-----------------------

# Frame para operações de SELECT
frameSelect = tk.Frame(window, width=800, height=600)
frameSelect.configure(background=lightPurple)

# Frame para operações de INSERT
frameInsert = tk.Frame(window, width=1300, height=600)
frameInsert.configure(background=lightPurple)

# Frame para operações de UPDATE
frameUpdate = tk.Frame(window, width=1300, height=600)
frameUpdate.configure(background=lightPurple)

# Frame para operações de DELETE
frameDelete = tk.Frame(window, width=1300, height=600)
frameDelete.configure(background=lightPurple)

# Frame para o carrinho de compras
frameCart = tk.Frame(window, width=470, height=600)
frameCart.configure(background=lightPurple)

# -----------------------> CONTROLE DE VISIBILIDADE DOS FRAMES <-----------------------

# Variáveis booleanas para rastrear qual frame está visível
frameSelectVisible = False
frameInsertVisible = False
frameUpdateVisible = False
frameDeleteVisible = False
frameCartVisible = False
frameGameVisible = False
framePlayerVisible = False

# -----------------------> FUNÇÕES PARA GERENCIAR FRAMES <-----------------------

def selectFrame():
    #Controla a exibição do frame de seleção/consulta e carrinho
    global frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameDeleteVisible, frameCartVisible

    # Se o frame já está visível, esconde
    if frameSelectVisible:
        frameSelect.place_forget()
        frameSelectVisible = False
        frameCart.place_forget()
        frameCartVisible = False
    else:
        # Mostra o frame de seleção e carrinho
        frameSelect.place(x=250, y=15)
        frameSelectVisible = True
        frameCart.place(x=1055, y=15)
        frameCartVisible = True

        # Esconde todos os outros frames
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False

def insertFrame():  #Controla a exibição do frame de inserção
    global frameInsertVisible, frameSelectVisible, frameUpdateVisible, frameDeleteVisible, frameCartVisible
    if frameInsertVisible:
        frameInsert.place_forget()
        frameInsertVisible = False
    else:
        frameInsert.place(x=250, y=15)
        frameInsertVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameUpdate.place_forget()
        frameDelete.place_forget()
        frameCart.place_forget()

        frameSelectVisible = False
        frameUpdateVisible = False
        frameDeleteVisible = False
        frameCartVisible = False

def updateFrame():  #Controla a exibição do frame de UPDATE
    global frameUpdateVisible, frameSelectVisible, frameInsertVisible, frameDeleteVisible, frameCartVisible
    if frameUpdateVisible:
        frameUpdate.place_forget()
        frameUpdateVisible = False
    else:
        frameUpdate.place(x=250, y=15)
        frameUpdateVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameInsert.place_forget()
        frameDelete.place_forget()
        frameCart.place_forget()

        frameSelectVisible = False
        frameInsertVisible = False
        frameDeleteVisible = False
        frameCartVisible = False

def deleteFrame():      #Controla a exibição do frame de DELETE
    global frameDeleteVisible, frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameCartVisible
    if frameDeleteVisible:
        frameDelete.place_forget()
        frameDeleteVisible = False
    else:
        frameDelete.place(x=250, y=15)
        frameDeleteVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameInsert.place_forget()
        frameUpdate.place_forget()
        frameCart.place_forget()

        frameSelectVisible = False
        frameInsertVisible = False
        frameUpdateVisible = False
        frameCartVisible = False

def gameFrame():    #Controla a exibição do frame de informações de jogos
    global frameGameVisible, framePlayerVisible, \
        labelEntryIDGame, entryIDGame, \
        labelEntryNameGame, entryNameGame, \
        labelEntryGenderGame, entryGenderGame, \
        labelEntryPriceGame, entryPriceGame, \
        labelEntryProducerGame, entryProducerGame, \
        labelEntryAgeGame, entryAgeGame

    if frameGameVisible:
        labelEntryIDGame.place_forget()
        labelEntryNameGame.place_forget()
        labelEntryGenderGame.place_forget()
        labelEntryPriceGame.place_forget()
        labelEntryProducerGame.place_forget()
        labelEntryAgeGame.place_forget()

        entryIDGame.place_forget()
        entryNameGame.place_forget()
        entryGenderGame.place_forget()
        entryPriceGame.place_forget()
        entryProducerGame.place_forget()
        entryAgeGame.place_forget()

        frameGameVisible = False
    else:
        labelEntryIDGame.place(x=30, y=165)
        labelEntryNameGame.place(x=190,y=165)
        labelEntryGenderGame.place(x=350, y=165)
        labelEntryPriceGame.place(x=510,y=165)
        labelEntryProducerGame.place(x=670, y=165)
        labelEntryAgeGame.place(x=830, y=165)

        entryIDGame.place(x=30, y=200)
        entryNameGame.place(x=190,y=200)
        entryGenderGame.place(x=350, y=200)
        entryPriceGame.place(x=510,y=200)
        entryProducerGame.place(x=670, y=200)
        entryAgeGame.place(x=830, y=200)

        frameGameVisible = True
        framePlayerVisible = False

def playerFrame():  #Controla a exibição do frame de informações de jogadores
    global framePlayerVisible, frameGameVisible, \
        labelEntryIDPlayer, entryIDPlayer, \
        labelEntryNamePlayer, entryNamePlayer, \
        labelEntryAgePlayer, entryAgePlayer, \
        labelEntryCountryPlayer, entryCountryPlayer, \
        labelEntryStatusPlayer, entryStatusPlayer, \
        labelEntryGamesCreatedPlayer, entryGamesCreatedPlayer

    if framePlayerVisible:
        labelEntryIDPlayer.place_forget()
        labelEntryNamePlayer.place_forget()
        labelEntryAgePlayer.place_forget()
        labelEntryCountryPlayer.place_forget()
        labelEntryStatusPlayer.place_forget()
        labelEntryGamesCreatedPlayer.place_forget()

        entryIDPlayer.place_forget()
        entryNamePlayer.place_forget()
        entryAgePlayer.place_forget()
        entryCountryPlayer.place_forget()
        entryStatusPlayer.place_forget()
        entryGamesCreatedPlayer.place_forget()

        framePlayerVisible = False
    else:
        labelEntryIDPlayer.place(x=30, y=165)
        labelEntryNamePlayer.place(x=190,y=165)
        labelEntryAgePlayer.place(x=350, y=165)
        labelEntryCountryPlayer.place(x=510,y=165)
        labelEntryStatusPlayer.place(x=670, y=165)
        labelEntryGamesCreatedPlayer.place(x=830, y=165)

        entryIDPlayer.place(x=30,y=200)
        entryNamePlayer.place(x=190,y=200)
        entryAgePlayer.place(x=350, y=200)
        entryCountryPlayer.place(x=510,y=200)
        entryStatusPlayer.place(x=670, y=200)
        entryGamesCreatedPlayer.place(x=830, y=200)

        framePlayerVisible = True
        frameGameVisible = False

# -----------------------> ELEMENTOS VISUAIS ADICIONAIS <-----------------------

# Cria uma linha vertical decorativa com extremidades arredondadas
canvasLine = tk.Canvas(
    window,
    width=10,
    height=520,
    bg=purple,
    highlightthickness=0,  # Remove destaque da borda
    borderwidth=0,  # Remove borda
    relief='flat'  # Estilo plano
)
canvasLine.place(x=200, y=100)
canvasLine.configure(bg=purple)
canvasLine.config(bd=0, highlightthickness=0)  # Remove bordas


def drawRoundedLine(canvas, x, y1, y2, width, color):
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
drawRoundedLine(canvasLine, 0, 0, 489, 10, lightLilac)

# -----------------------> LABELS INFORMATIVOS <-----------------------

# Label para seção de informações do jogo
labelGameInformation = ttk.Label(frameSelect,
                                 text="Informação do Jogo",
                                 background=lightPurple,
                                 font=("Times New Roman", 20))
labelGameInformation.place(x=20, y=20)

# Label para seção de informações do usuário
labelPlayerInformation = ttk.Label(frameSelect,
                                   text="Informação do Usuário",
                                   background=lightPurple,
                                   font=("Times New Roman", 20))
labelPlayerInformation.place(x=20, y=360)

# Label para o carrinho
labelCartInformation = ttk.Label(frameCart,
                                 text="Carrinho",
                                 background=purple,
                                 font=("Times New Roman", 20))
labelCartInformation.place(x=200, y=20)

# -----------------------> BOTÕES PRINCIPAIS (CRUD) <-----------------------

# Botão para operações SELECT
buttonSelect = customtkinter.CTkButton(master=window,
                                       text="Select",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,  # Cor de fundo
                                       hover_color=mediumLilac,  # Cor ao passar mouse
                                       text_color="white",  # Cor do texto
                                       font=("Segoe UI", 20, "bold"),  # Fonte
                                       command=lambda: selectFrame(),  # Ação ao clicar
                                       image=selectImage,  # Ícone
                                       compound="left",  # Posição do ícone
                                       anchor="w")  # Alinhamento
buttonSelect.place(x=20, y=120)

# Botão para operações INSERT - estrutura similar
buttonInsert = customtkinter.CTkButton(master=window,
                                       text="Insert",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color=mediumLilac,
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command=lambda: insertFrame(),
                                       image=insertImage,
                                       compound="left",
                                       anchor="w")
buttonInsert.place(x=20, y=240)

# Botão para operações UPDATE
buttonUpdate = customtkinter.CTkButton(master=window,
                                       text="Update",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color=mediumLilac,
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command=lambda: updateFrame(),
                                       image=updateImage,
                                       compound="left",
                                       anchor="w")
buttonUpdate.place(x=20, y=360)

# Botão para operações DELETE
buttonDelete = customtkinter.CTkButton(master=window,
                                       text="Delete",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color=mediumLilac,
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command=lambda: deleteFrame(),
                                       image=deleteImage,
                                       compound="left",
                                       anchor="w")
buttonDelete.place(x=20, y=480)

# ----------------------> BOTÕES DE BUSCA NO FRAME SELECT <-----------------------

# Botões para buscar jogos por diferentes critérios
buttonSearchIDGameSelect = customtkinter.CTkButton(master=frameSelect,
                                                   text="ID do Jogo",
                                                   width=50,
                                                   height=85,
                                                   fg_color="#3d2e4c",  # Roxo mais escuro
                                                   hover_color="#a676b0",  # Lilás
                                                   text_color="white",
                                                   font=("Segoe UI", 20, "bold"),
                                                   command=lambda: selectFrame())
buttonSearchIDGameSelect.place(x=20, y=160)

buttonSearchNameGameSelect = customtkinter.CTkButton(master=frameSelect,
                                                     text="Nome",
                                                     width=100,
                                                     height=85,
                                                     fg_color="#3d2e4c",
                                                     hover_color="#a676b0",
                                                     text_color="white",
                                                     font=("Segoe UI", 20, "bold"),
                                                     command=lambda: selectFrame())
buttonSearchNameGameSelect.place(x=150, y=160)

buttonSearchGenderGameSelect = customtkinter.CTkButton(master=frameSelect,
                                                       text="Gênero",
                                                       width=100,
                                                       height=85,
                                                       fg_color="#3d2e4c",
                                                       hover_color="#a676b0",
                                                       text_color="white",
                                                       font=("Segoe UI", 20, "bold"),
                                                       command=lambda: selectFrame())
buttonSearchGenderGameSelect.place(x=280, y=160)

buttonSearchPriceGameSelect = customtkinter.CTkButton(master=frameSelect,
                                                      text="Preço",
                                                      width=100,
                                                      height=85,
                                                      fg_color="#3d2e4c",
                                                      hover_color="#a676b0",
                                                      text_color="white",
                                                      font=("Segoe UI", 20, "bold"),
                                                      command=lambda: selectFrame())
buttonSearchPriceGameSelect.place(x=410, y=160)

buttonSearchProducerGameSelect = customtkinter.CTkButton(master=frameSelect,
                                                         text="Produtor",
                                                         width=100,
                                                         height=85,
                                                         fg_color="#3d2e4c",
                                                         hover_color="#a676b0",
                                                         text_color="white",
                                                         font=("Segoe UI", 20, "bold"),
                                                         command=lambda: selectFrame())
buttonSearchProducerGameSelect.place(x=540, y=160)

buttonSearchAgeGameSelect = customtkinter.CTkButton(master=frameSelect,
                                                    text="Idade",
                                                    width=100,
                                                    height=85,
                                                    fg_color="#3d2e4c",
                                                    hover_color="#a676b0",
                                                    text_color="white",
                                                    font=("Segoe UI", 20, "bold"),
                                                    command=lambda: selectFrame())
buttonSearchAgeGameSelect.place(x=670, y=160)

# -----------------------> BOTÕES PARA BUSCA DE USUÁRIOS <-----------------------

buttonSearchNamePlayerSelect = customtkinter.CTkButton(master=frameSelect,
                                                 text="Nome",
                                                 width=100,
                                                 height=85,
                                                 fg_color="#3d2e4c",
                                                 hover_color="#a676b0",
                                                 text_color="white",
                                                 font=("Segoe UI", 20, "bold"),
                                                 command=lambda: selectFrame())
buttonSearchNamePlayerSelect.place(x=20, y=500)

buttonSearchIDPlayerSelect = customtkinter.CTkButton(master=frameSelect,
                                               text="Id do Usuário",
                                               width=100,
                                               height=85,
                                               fg_color="#3d2e4c",
                                               hover_color="#a676b0",
                                               text_color="white",
                                               font=("Segoe UI", 20, "bold"),
                                               command=lambda: selectFrame())
buttonSearchIDPlayerSelect.place(x=150, y=500)

# -----------------------> BOTÕES PARA O CARRINHO <-----------------------

buttonSearchProductCartSelect = customtkinter.CTkButton(master=frameCart,
                                                  text="Produtos",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command=lambda: selectFrame())
buttonSearchProductCartSelect.place(x=150, y=100)

buttonViewCart = customtkinter.CTkButton(master=frameCart,
                                         text="Ver o carrinho",
                                         width=200,
                                         height=85,
                                         fg_color="#3d2e4c",
                                         hover_color="#a676b0",
                                         text_color="white",
                                         font=("Segoe UI", 20, "bold"),
                                         command=lambda: selectFrame())
buttonViewCart.place(x=20, y=460)

buttonRemoveProductCartSelect = customtkinter.CTkButton(master=frameCart,
                                                  text="Remover Produto",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command=lambda: selectFrame())
buttonRemoveProductCartSelect.place(x=240, y=460)

# -----------------------> BOTÕES NO FRAME DE INSERÇÃO <-----------------------

buttonInsertInformationGameInsert = customtkinter.CTkButton(master=frameInsert,
                                                      text="Jogo",
                                                      width=100,
                                                      height=85,
                                                      fg_color="#3d2e4c",
                                                      hover_color="#a676b0",
                                                      text_color="white",
                                                      font=("Segoe UI", 20, "bold"),
                                                      command=lambda: gameFrame())
buttonInsertInformationGameInsert.place(x=520, y=40)

buttonInsertInformationPlayerInsert = customtkinter.CTkButton(master=frameInsert,
                                                        text="Usuário",
                                                        width=100,
                                                        height=85,
                                                        fg_color="#3d2e4c",
                                                        hover_color="#a676b0",
                                                        text_color="white",
                                                        font=("Segoe UI", 20, "bold"),
                                                        command=lambda: gameFrame())
buttonInsertInformationPlayerInsert.place(x=640, y=40)

buttonInsertfromGameAndPlayer = customtkinter.CTkButton(master=frameInsert,
                                                        text="Inserir",
                                                        width=100,
                                                        height=85,
                                                        fg_color="#3d2e4c",
                                                        hover_color="#a676b0",
                                                        text_color="white",
                                                        font=("Segoe UI", 20, "bold"),
                                                        command=lambda: gameFrame())
buttonInsertfromGameAndPlayer.place(x=580, y=500)

# -----------------------> CAMPOS DE ENTRADA NO FRAME DE JOGOS <-----------------------

# Label para o campo de ID do Jogo
labelEntryIDGame = ttk.Label(frameInsert,
                             text="ID Jogo",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para o ID do Jogo
entryIDGame = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryIDGame.configure(bg="#C6B4C9")

# Label para o campo de Nome do Jogo
labelEntryNameGame = ttk.Label(frameInsert,
                             text="Nome",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para o Nome do Jogo
entryNameGame = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryNameGame.configure(bg="#C6B4C9")

# Label para o campo de Gênero do Jogo
labelEntryGenderGame = ttk.Label(frameInsert,
                             text="Gênero",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para o Gênero do Jogo
entryGenderGame = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryGenderGame.configure(bg="#C6B4C9")

# Label para o campo de Preço do Jogo
labelEntryPriceGame = ttk.Label(frameInsert,
                             text="Preço",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para o Preço do Jogo
entryPriceGame = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryPriceGame.configure(bg="#C6B4C9")

# Label para o campo de Produtora do Jogo
labelEntryProducerGame = ttk.Label(frameInsert,
                             text="Produtora",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para a Produtora do Jogo
entryProducerGame = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryProducerGame.configure(bg="#C6B4C9")

# Label para o campo de Idade indicada do Jogo
labelEntryAgeGame = ttk.Label(frameInsert,
                             text="Idade",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para a Idade indicada do Jogo
entryAgeGame = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryAgeGame.configure(bg="#C6B4C9")

# Label para o campo de ID do Usuário (Jogador)
labelEntryIDPlayer = ttk.Label(frameInsert,
                             text="ID do Usuário",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para o ID do Usuário
entryIDPlayer = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryIDPlayer.configure(bg="#C6B4C9")

# Label para o campo de Nome do Usuário
labelEntryNamePlayer = ttk.Label(frameInsert,
                             text="Nome",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para o Nome do Usuário
entryNamePlayer = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryNamePlayer.configure(bg="#C6B4C9")

# Label para o campo de Idade do Usuário
labelEntryAgePlayer = ttk.Label(frameInsert,
                             text="Idade",
                             background=lightPurple,
                             font=("Calibri", 20))

# Campo de entrada para a Idade do Usuário
entryAgePlayer = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryAgePlayer.configure(bg="#C6B4C9")

# Label para o campo de País do Usuário
labelEntryCountryPlayer = ttk.Label(frameInsert,
                                    text="País",
                                    background=lightPurple,
                                    font=("Calibri",20))

# Campo de entrada para o País do Usuário
entryCountryPlayer = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryCountryPlayer.configure(bg="#C6B4C9")

# Label para o campo de Status do Usuário
labelEntryStatusPlayer = ttk.Label(frameInsert,
                                    text="Status",
                                    background=lightPurple,
                                    font=("Calibri",20))

# Campo de entrada para o Status do Usuário
entryStatusPlayer = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryStatusPlayer.configure(bg="#C6B4C9")

# Label para o campo de quantidade de Jogos Criados pelo Usuário
labelEntryGamesCreatedPlayer = ttk.Label(frameInsert,
                                    text="Jogos Criados",
                                    background=lightPurple,
                                    font=("Calibri",20))

# Campo de entrada para a quantidade de Jogos Criados pelo Usuário
entryGamesCreatedPlayer = tk.Entry(frameInsert,width=20, bg=purple, fg=lightPurple, font=("Calibri",10))
entryGamesCreatedPlayer.configure(bg="#C6B4C9")

# -----------------------> INÍCIA O LOOP PRINCIPAL DA INTERFACE <-----------------------

window.mainloop()  # Mantém a janela aberta e responde a eventos
