# -----------------------> Importações de bibliotecas <-----------------------

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

# -----------------------> Definição de cores usadas na interface <-----------------------

# Paleta de cores personalizada para a aplicação
purple = "#442e73"  # Roxo escuro (cor principal)
lightPurple = "#664983"  # Roxo mais claro
lightLilac = "#987FAB"  # Lilás claro
mediumLilac = "#A676B0"  # Lilás médio
tiffany = "#0ABAB2"  # Azul esverdeado (estilo Tiffany)
white = "#FFFFFF"  # Branco puro

# -----------------------> Configuração da janela principal <-----------------------

# Cria a janela principal com tema "cyborg" (escuro com elementos roxos)
window = ttk.Window(themename="cyborg")
window.title("Plataforma de Jogos")  # Título da janela
window.geometry("1600x700")  # Define tamanho fixo da janela
window.configure(background=purple)  # Cor de fundo principal
window.resizable(width=False, height=False)  # Impede redimensionamento

# -----------------------> Configuração de estilos <-----------------------

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

# -----------------------> Carregamento e preparação de imagens para os botões <-----------------------

# Carrega e prepara ícones para os botões CRUD
selectImage = Image.open("select.png")  # Abre imagem do arquivo
selectImage = selectImage.resize((25, 25))  # Redimensiona para 25x25 pixels
selectImage = ImageTk.PhotoImage(selectImage)  # Converte para formato Tkinter

# Repete o processo para os outros ícones
insertImage = Image.open("insert.png")
insertImage = insertImage.resize((25, 25))
insertImage = ImageTk.PhotoImage(insertImage)

updateImage = Image.open("update.png")
updateImage = updateImage.resize((25, 25))
updateImage = ImageTk.PhotoImage(updateImage)

deleteImage = Image.open("delete.png")
deleteImage = deleteImage.resize((25, 25))
deleteImage = ImageTk.PhotoImage(deleteImage)

# -----------------------> Criação de frames (áreas de conteúdo) <-----------------------

# Frame para operações de SELECT/consulta
frameSelect = tk.Frame(window, width=800, height=600)
frameSelect.configure(background=lightPurple)

# Frame para operações de INSERT/inserção
frameInsert = tk.Frame(window, width=1300, height=600)
frameInsert.configure(background=lightPurple)

# Frame para operações de UPDATE/atualização
frameUpdate = tk.Frame(window, width=1300, height=600)
frameUpdate.configure(background=lightPurple)

# Frame para operações de DELETE/exclusão
frameDelete = tk.Frame(window, width=1300, height=600)
frameDelete.configure(background=lightPurple)

# Frame para o carrinho de compras
frameCart = tk.Frame(window, width=470, height=600)
frameCart.configure(background=lightPurple)

# Frame para informações de jogos
frameGame = tk.Frame(window, width=1300, height=600)
frameGame.configure(background=lightPurple)

# Frame para informações de jogadores/usuários
framePlayer = tk.Frame(window, width=1300, height=600)
framePlayer.configure(background=tiffany)  # Usa a cor Tiffany para diferenciação

# -----------------------> Controle de visibilidade dos frames <-----------------------

# Variáveis booleanas para rastrear qual frame está visível
frameSelectVisible = False
frameInsertVisible = False
frameUpdateVisible = False
frameDeleteVisible = False
frameCartVisible = False
frameGameVisible = False
framePlayerVisible = False


# -----------------------> Funções para gerenciar a exibição dos frames <-----------------------

def selectFrame():
    """Controla a exibição do frame de seleção/consulta e carrinho"""
    global frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameDeleteVisible, frameCartVisible, frameGameVisible, framePlayerVisible

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
        frameGame.place_forget()
        frameGameVisible = False
        framePlayer.place_forget()
        framePlayerVisible = False


# As funções seguintes seguem a mesma lógica para outros frames
def insertFrame():
    """Controla a exibição do frame de inserção"""
    global frameInsertVisible, frameSelectVisible, frameUpdateVisible, frameDeleteVisible, frameCartVisible, frameGameVisible, framePlayerVisible
    if frameInsertVisible:
        frameInsert.place_forget()
        frameInsertVisible = False
    else:
        frameInsert.place(x=250, y=15)
        frameInsertVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameSelectVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False
        frameCart.place_forget()
        frameCartVisible = False
        frameGame.place_forget()
        frameGameVisible = False
        framePlayer.place_forget()
        framePlayerVisible = False


def updateFrame():
    """Controla a exibição do frame de atualização"""
    global frameUpdateVisible, frameSelectVisible, frameInsertVisible, frameDeleteVisible, frameCartVisible, frameGameVisible, framePlayerVisible
    if frameUpdateVisible:
        frameUpdate.place_forget()
        frameUpdateVisible = False
    else:
        frameUpdate.place(x=250, y=15)
        frameUpdateVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False
        frameCart.place_forget()
        frameCartVisible = False
        frameGame.place_forget()
        frameGameVisible = False
        framePlayer.place_forget()
        framePlayerVisible = False


def deleteFrame():
    """Controla a exibição do frame de exclusão"""
    global frameDeleteVisible, frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameCartVisible, framePlayerVisible
    if frameDeleteVisible:
        frameDelete.place_forget()
        frameDeleteVisible = False
    else:
        frameDelete.place(x=250, y=15)
        frameDeleteVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameCart.place_forget()
        frameCartVisible = False
        framePlayer.place_forget()
        framePlayerVisible = False


def gameFrame():
    """Controla a exibição do frame de informações de jogos"""
    global frameGameVisible, frameDeleteVisible, frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameCartVisible, framePlayerVisible
    if frameGameVisible:
        frameGame.place_forget()
        frameGameVisible = False
    else:
        frameGame.place(x=250, y=15)
        frameGameVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameCart.place_forget()
        frameCartVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False
        framePlayer.place_forget()
        framePlayerVisible = False


def playerFrame():
    """Controla a exibição do frame de informações de jogadores"""
    global framePlayerVisible, frameGameVisible, frameDeleteVisible, frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameCartVisible
    if framePlayerVisible:
        framePlayer.place_forget()
        framePlayerVisible = False
    else:
        framePlayer.place(x=250, y=15)
        framePlayerVisible = True
        # Esconde os outros frames
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False
        frameCart.place_forget()
        frameCartVisible = False
        frameGame.place_forget()
        frameGameVisible = False


# -----------------------> Elementos de design personalizados <-----------------------

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
drawRoundedLine(canvasLine, 0, 0, 489, 10, lightLilac)

# -----------------------> Rótulos (labels) informativos <-----------------------

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

# -----------------------> Botões principais (CRUD) <-----------------------

# Botão para operações SELECT (consultar)
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

# Botão para operações INSERT (inserir) - estrutura similar
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

# Botão para operações UPDATE (atualizar)
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

# Botão para operações DELETE (excluir)
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

# -----------------------> Botões de busca no frame Select <-----------------------

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

# -----------------------> Botões para busca de usuários <-----------------------

buttonSearchNamePlayer = customtkinter.CTkButton(master=frameSelect,
                                                 text="Nome",
                                                 width=100,
                                                 height=85,
                                                 fg_color="#3d2e4c",
                                                 hover_color="#a676b0",
                                                 text_color="white",
                                                 font=("Segoe UI", 20, "bold"),
                                                 command=lambda: selectFrame())
buttonSearchNamePlayer.place(x=20, y=500)

buttonSearchIDPlayer = customtkinter.CTkButton(master=frameSelect,
                                               text="Id do Usuário",
                                               width=100,
                                               height=85,
                                               fg_color="#3d2e4c",
                                               hover_color="#a676b0",
                                               text_color="white",
                                               font=("Segoe UI", 20, "bold"),
                                               command=lambda: selectFrame())
buttonSearchIDPlayer.place(x=150, y=500)

# -----------------------> Botões para o carrinho <-----------------------

buttonSearchProductCart = customtkinter.CTkButton(master=frameCart,
                                                  text="Produtos",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command=lambda: selectFrame())
buttonSearchProductCart.place(x=150, y=100)

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

buttonRemoveProductCart = customtkinter.CTkButton(master=frameCart,
                                                  text="Remover Produto",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command=lambda: selectFrame())
buttonRemoveProductCart.place(x=240, y=460)

# -----------------------> Botões no frame de inserção <-----------------------

buttonInsertInformationGame = customtkinter.CTkButton(master=frameInsert,
                                                      text="Jogo",
                                                      width=50,
                                                      height=85,
                                                      fg_color="#3d2e4c",
                                                      hover_color="#a676b0",
                                                      text_color="white",
                                                      font=("Segoe UI", 20, "bold"),
                                                      command=lambda: gameFrame())
buttonInsertInformationGame.place(x=540, y=40)

buttonInsertInformationPlayer = customtkinter.CTkButton(master=frameInsert,
                                                        text="Usuário",
                                                        width=100,
                                                        height=85,
                                                        fg_color="#3d2e4c",
                                                        hover_color="#a676b0",
                                                        text_color="white",
                                                        font=("Segoe UI", 20, "bold"),
                                                        command=lambda: playerFrame())
buttonInsertInformationPlayer.place(x=640, y=40)

# -----------------------> Campos de entrada no frame de jogos <-----------------------

labelEntryIDJogo = ttk.Label(frameGame,
                             text="ID Jogo",
                             background=lightPurple,
                             font=("Times New Roman", 20))
labelEntryIDJogo.place(x=200, y=165)

entryIDJogo = tk.Entry(frameGame, width=25, bg="#C6B4C9")  # Campo de entrada com fundo lilás claro
entryIDJogo.place(x=200, y=200)

# -----------------------> Inicia o loop principal da interface <-----------------------

window.mainloop()  # Mantém a janela aberta e responde a eventos
