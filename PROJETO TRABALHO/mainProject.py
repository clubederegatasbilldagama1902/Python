# -----------------------> Importações de bibliotecas <-----------------------

import ttkbootstrap as ttk  # Biblioteca para estilização do Tkinter
from ttkbootstrap.constants import *  # Constantes do ttkbootstrap
from ttkbootstrap.widgets import Separator  # Widget Separator do ttkbootstrap
import tkinter as tk  # Biblioteca padrão para GUI
import customtkinter # Biblioteca para widgets personalizados
from customtkinter import CTkImage
import PIL  # Biblioteca para manipulação de imagens
from PIL import Image, ImageTk # Classes específicas para imagens
import mysql.connector
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# -----------------------> Definição de cores usadas na interface <-----------------------

purple = "#442e73"
lightPurple = "#664983"
tiffany = "#0ABAB2"
lightGolden = "#FADA55"
blue = "#0A7AB2"
white = "#FFFFFF"

# -----------------------> Configuração da janela principal <-----------------------

window = ttk.Window(themename="cyborg")  # Cria janela com tema "cyborg"
window.title("Plataforma de Jogos")  # Título da janela
window.geometry("1600x700")  # Dimensões da janela
window.configure(background=purple)  # Cor de fundo
window.resizable(width=True, height=True)  # Janela não redimensionável

# -----------------------> Configuração de estilos <-----------------------

style = ttk.Style()

# -----------------------> Estilo para botões personalizados <-----------------------

style.configure("Custom.TButton",
                background=lightPurple,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("Custom.TButton",
          background=[("active", "#573a87")])  # Cor quando ativo

# Segundo estilo de botão
style.configure("CustomTwo.TButton",
                background=lightPurple,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("CustomTwo.TButton",
          background=[("active", "#573a87")])

# -----------------------> Carregamento e preparação de imagens para os botões <-----------------------

selectImage = Image.open("select.png")  # Abre imagem
selectImage = selectImage.resize((25,25))  # Redimensiona
selectImage = ImageTk.PhotoImage(selectImage)  # Converte para formato Tkinter

insertImage = Image.open("insert.png")
insertImage = insertImage.resize((25,25))
insertImage = ImageTk.PhotoImage(insertImage)

updateImage = Image.open("update.png")
updateImage = updateImage.resize((25,25))
updateImage = ImageTk.PhotoImage(updateImage)

deleteImage = Image.open("delete.png")
deleteImage = deleteImage.resize((25,25))
deleteImage = ImageTk.PhotoImage(deleteImage)

# -----------------------> Criação de frames para cada operação CRUD <-----------------------

frameSelect = tk.Frame(window, width=800, height=600)
frameSelect.configure(background=lightPurple)

frameInsert = tk.Frame(window, width=1300, height=600)
frameInsert.configure(background=lightPurple)

frameUpdate = tk.Frame(window, width=1300, height=600)
frameUpdate.configure(background=lightGolden)

frameDelete = tk.Frame(window, width=1300, height=600)
frameDelete.configure(background=blue)

frameCart = tk.Frame(window, width=470, height=600)
frameCart.configure(background=tiffany)

# -----------------------> Variáveis para controlar a visibilidade dos frames <-----------------------

frameSelectVisible = False
frameInsertVisible = False
frameUpdateVisible = False
frameDeleteVisible = False
frameCartVisible = False

# -----------------------> Funções para mostrar/esconder os frames <-----------------------

def selectFrame():
    global frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameDeleteVisible, frameCartVisible
    if frameSelectVisible:
        frameSelect.place_forget()  # Esconde o frame
        frameSelectVisible = False
        frameCart.place_forget()
        frameCartVisible = False
    else:
        frameSelect.place(x=250, y=15)  # Mostra o frame
        frameSelectVisible = True
        frameCart.place(x=1055,y=15)
        frameCartVisible = True
        # Esconde os outros frames
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False

def insertFrame():
    global frameInsertVisible, frameSelectVisible, frameUpdateVisible, frameDeleteVisible, frameCartVisible
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

def updateFrame():
    global frameUpdateVisible, frameSelectVisible, frameInsertVisible, frameDeleteVisible, frameCartVisible
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

def deleteFrame():
    global frameDeleteVisible, frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameCartVisible
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

# -----------------------> Linha vertical personalizada <-----------------------

canvasLine = tk.Canvas(
    window,
    width=10,
    height=520,
    bg=purple,
    highlightthickness=0,
    borderwidth=0,
    relief='flat'
)
canvasLine.place(x=200, y=100)
canvasLine.configure(bg=purple)
canvasLine.config(bd=0, highlightthickness=0)  # Remove bordas

# -----------------------> Função para desenhar linha vertical com extremidades arredondadas <-----------------------

def drawRoundedLine(canvas, x, y1, y2, width, color):
    radius = width // 2
    # Desenha a linha vertical principal
    canvas.create_rectangle(
        x, y1 + radius,
        x + width, y2 - radius,
        fill=color,
        outline=color,
        width=0
    )
    # Desenha as extremidades arredondadas
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
drawRoundedLine(canvasLine, 0, 0, 489, 10, "#987FAB")

# -----------------------> Labels para informações do jogo e do usuário <-----------------------

labelGameInformation = ttk.Label(frameSelect,
                                 text="Informação do Jogo",
                                 background=lightPurple,
                                 font=("Times New Roman", 20))
labelGameInformation.place(x=20, y=20)

labelPlayerInformation = ttk.Label(frameSelect,
                                   text="Informação do Usuário",
                                   background=lightPurple,
                                   font=("Times New Roman", 20))
labelPlayerInformation.place(x=20, y=360)

labelCartInformation = ttk.Label(frameCart,
                                 text="Carrinho",
                                 background=purple,
                                 font=("Times New Roman",20))

labelCartInformation.place(x=200, y=20)

# -----------------------> Botões principais (CRUD) <-----------------------

buttonSelect = customtkinter.CTkButton(master=window,
                                       text="Select",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color="#A676B0",
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command= lambda: selectFrame(),
                                       image=selectImage,
                                       compound="left",
                                       anchor="w")
buttonSelect.place(x=20, y=120)

buttonInsert = customtkinter.CTkButton(master=window,
                                       text="Insert",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color="#A676B0",
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command= lambda: insertFrame(),
                                       image=insertImage,
                                       compound="left",
                                       anchor="w")
buttonInsert.place(x=20, y=240)

buttonUpdate = customtkinter.CTkButton(master=window,
                                       text="Update",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color="#A676B0",
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command=lambda: updateFrame(),
                                       image=updateImage,
                                       compound="left",
                                       anchor="w")
buttonUpdate.place(x=20, y=360)

buttonDelete = customtkinter.CTkButton(master=window,
                                       text="Delete",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color="#A676B0",
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command=lambda: deleteFrame(),
                                       image=deleteImage,
                                       compound="left",
                                       anchor="w")
buttonDelete.place(x=20, y=480)

# -----------------------> Botões de busca no frame Select <-----------------------

buttonSearchIDGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="ID do Jogo",
                                             width=50,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchIDGameSelect.place(x=20, y=160)

buttonSearchNameGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Nome",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchNameGameSelect.place(x=150, y=160)

buttonSearchGenderGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Gênero",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchGenderGameSelect.place(x=280, y=160)

buttonSearchPriceGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Preço",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchPriceGameSelect.place(x=410, y=160)

buttonSearchProducerGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Produtor",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchProducerGameSelect.place(x=540, y=160)

buttonSearchAgeGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Idade",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchAgeGameSelect.place(x=670, y=160)

# -----------------------> Botões para busca de informações do usuário(Nome e ID) <-----------------------

buttonSearchNamePlayer = customtkinter.CTkButton(master=frameSelect,
                                             text="Nome",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchNamePlayer.place(x=20, y=500)

buttonSearchIDPlayer = customtkinter.CTkButton(master=frameSelect,
                                             text="Id do Usuário",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchIDPlayer.place(x=150, y=500)

# -----------------------> Botão para busca de informação do carrinho <-----------------------

buttonSearchProductCart = customtkinter.CTkButton(master=frameCart,
                                                  text="Produtos",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command= lambda: selectFrame())
buttonSearchProductCart.place(x=150, y=100)

buttonViewCart = customtkinter.CTkButton(master=frameCart,
                                                  text="Ver o carrinho",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command= lambda: selectFrame())
buttonViewCart.place(x=20, y=460)

buttonRemoveProductCart = customtkinter.CTkButton(master=frameCart,
                                                  text="Remover Produto",
                                                  width=200,
                                                  height=85,
                                                  fg_color="#3d2e4c",
                                                  hover_color="#a676b0",
                                                  text_color="white",
                                                  font=("Segoe UI", 20, "bold"),
                                                  command= lambda: selectFrame())
buttonRemoveProductCart.place(x=240, y=460)

# -----------------------> Botões de inserir no frame Insert <-----------------------

buttonInsertInformationGame = customtkinter.CTkButton(master=frameInsert,
                                             text="Jogo",
                                             width=50,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: insertFrame())
buttonInsertInformationGame.place(x=540, y=40)

buttonInsertInformationPlayer = customtkinter.CTkButton(master=frameInsert,
                                             text="Usuário",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: insertFrame())
buttonInsertInformationPlayer.place(x=640, y=40)

# -----------------------> Inicia o loop principal da interface <-----------------------
window.mainloop()
