# Importações de bibliotecas
import ttkbootstrap as ttk  # Biblioteca para estilização do Tkinter
from ttkbootstrap.constants import *  # Constantes do ttkbootstrap
from ttkbootstrap.widgets import Separator  # Widget Separator do ttkbootstrap
import tkinter as tk  # Biblioteca padrão para GUI
import customtkinter  # Biblioteca para widgets personalizados
import PIL  # Biblioteca para manipulação de imagens
from PIL import Image, ImageTk  # Classes específicas para imagens

# Definição de cores usadas na interface
purple = "#442e73"
lightPurple = "#664983"
tiffany = "#0ABAB2"
lightGolden = "#FADA55"
blue = "#0A7AB2"
white = "#FFFFFF"

# Configuração da janela principal
window = ttk.Window(themename="cyborg")  # Cria janela com tema "cyborg"
window.title("Plataforma de Jogos")  # Título da janela
window.geometry("1600x700")  # Dimensões da janela
window.configure(background=purple)  # Cor de fundo
window.resizable(width=False, height=False)  # Janela não redimensionável

# Configuração de estilos
style = ttk.Style()

# Estilo para botões personalizados
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
                background=tiffany,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("CustomTwo.TButton",
          background=[("active", "#573a87")])

# Carregamento e preparação de imagens para os botões
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

# Criação de frames para cada operação CRUD
frameSelect = tk.Frame(window, width=1300, height=600)
frameSelect.configure(background=lightPurple)

frameInsert = tk.Frame(window, width=1300, height=600)
frameInsert.configure(background=tiffany)

frameUpdate = tk.Frame(window, width=1300, height=600)
frameUpdate.configure(background=lightGolden)

frameDelete = tk.Frame(window, width=1300, height=600)
frameDelete.configure(background=blue)

# Variáveis para controlar a visibilidade dos frames
frameSelectVisible = False
frameInsertVisible = False
frameUpdateVisible = False
frameDeleteVisible = False

# Funções para mostrar/esconder os frames
def selectFrame():
    global frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameDeleteVisible
    if frameSelectVisible:
        frameSelect.place_forget()  # Esconde o frame
        frameSelectVisible = False
    else:
        frameSelect.place(x=250, y=15)  # Mostra o frame
        frameSelectVisible = True
        # Esconde os outros frames
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False

# Funções similares para os outros frames
def insertFrame():
    global frameInsertVisible, frameSelectVisible, frameUpdateVisible, frameDeleteVisible
    if frameInsertVisible:
        frameInsert.place_forget()
        frameInsertVisible = False
    else:
        frameInsert.place(x=250, y=15)
        frameInsertVisible = True
        frameSelect.place_forget()
        frameSelectVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False

def updateFrame():
    global frameUpdateVisible, frameSelectVisible, frameInsertVisible, frameDeleteVisible
    if frameUpdateVisible:
        frameUpdate.place_forget()
        frameUpdateVisible = False
    else:
        frameUpdate.place(x=250, y=15)
        frameUpdateVisible = True
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False

def deleteFrame():
    global frameDeleteVisible, frameSelectVisible, frameInsertVisible, frameUpdateVisible
    if frameDeleteVisible:
        frameDelete.place_forget()
        frameDeleteVisible = False
    else:
        frameDelete.place(x=250, y=15)
        frameDeleteVisible = True
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False

# Elementos de UI - Linha separadora horizontal
line = Separator(window, orient=HORIZONTAL)
line.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=30)

# Linha vertical personalizada
canvasLine = tk.Canvas(
    window,
    width=10,
    height=420,
    bg=purple,
    highlightthickness=0,
    borderwidth=0,
    relief='flat'
)
canvasLine.grid(row=1, column=1, rowspan=4, sticky="ns", padx=10, pady=10)
canvasLine.configure(bg=purple)
canvasLine.config(bd=0, highlightthickness=0)  # Remove bordas

# Função para desenhar linha vertical com extremidades arredondadas
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

# Labels para informações do jogo e do usuário
labelGameInformation = ttk.Label(frameSelect,
                                 text="Informação do Jogo",
                                 background=lightPurple,
                                 font=("Times New Roman", 20))
labelGameInformation.grid(row=0,
                          column=0,
                          columnspan=3,
                          pady=20,
                          padx=20,
                          sticky=NSEW,
                          ipady=20)

labelPlayerInformation = ttk.Label(frameSelect,
                                   text="Informação do Usuário",
                                   background=lightPurple,
                                   font=("Times New Roman", 20))
labelPlayerInformation.grid(row=3,
                            column=0,
                            columnspan=3,
                            pady=20,
                            padx=20,
                            sticky=NSEW,
                            ipady=20)

# Botões principais (CRUD)
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
buttonSelect.grid(row=1, column=0, pady=20, padx=20)

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
buttonInsert.grid(row=2, column=0, pady=20, padx=20)

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
buttonUpdate.grid(row=3, column=0, pady=20, padx=20)

buttonDelete = customtkinter.CTkButton(master=window,
                                       text="Delete",
                                       width=150,
                                       height=90,
                                       fg_color=lightPurple,
                                       hover_color="#A676B0",
                                       text_color="white",
                                       font=("Segoe UI", 20, "bold"),
                                       command=lambda: deleteFrame(),
                                       image=insertImage,  # Observação: está usando insertImage em vez de deleteImage
                                       compound="left",
                                       anchor="w")
buttonDelete.grid(row=4, column=0, pady=20, padx=20)

# Botões de busca no frame Select
buttonSearchIDGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="ID do Jogo",
                                             width=50,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchIDGameSelect.grid(row=1, column=0, pady=20, padx=20)

buttonSearchNameGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Nome",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchNameGameSelect.grid(row=1, column=1, pady=20, padx=20)

buttonSearchGenderGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Gênero",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchGenderGameSelect.grid(row=1, column=2, pady=20, padx=20)

buttonSearchPriceGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Preço",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchPriceGameSelect.grid(row=1, column=3, pady=20, padx=20)

buttonSearchProducerGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Produtor",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchProducerGameSelect.grid(row=1, column=4, pady=20, padx=20)

buttonSearchAgeGameSelect = customtkinter.CTkButton(master=frameSelect,
                                             text="Idade",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchAgeGameSelect.grid(row=1, column=5, pady=20, padx=20)

# Botões para busca de informações do usuário
buttonSearchNamePlayer = customtkinter.CTkButton(master=frameSelect,
                                             text="Nome",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchNamePlayer.grid(row=8, column=0, pady=20, padx=20)

buttonSearchIDPlayer = customtkinter.CTkButton(master=frameSelect,
                                             text="Id do Usuário",
                                             width=100,
                                             height=85,
                                             fg_color="#3d2e4c",
                                             hover_color="#a676b0",
                                             text_color="white",
                                             font=("Segoe UI", 20, "bold"),
                                             command= lambda: selectFrame())
buttonSearchIDPlayer.grid(row=8, column=1, pady=20, padx=20)

# Inicia o loop principal da interface
window.mainloop()
