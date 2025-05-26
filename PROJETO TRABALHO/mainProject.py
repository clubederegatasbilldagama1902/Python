import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Separator
import tkinter as tk

# Cores
purple = "#442e73"
lightPurple = "#664983"
tiffany = "#0ABAB2"
lightGolden = "#FADA55"
blue = "#0A7AB2"
white = "#FFFFFF"

# Janela
window = ttk.Window(themename="cyborg")
window.title("Plataforma de Jogos")
window.geometry("1600x700")
window.configure(background=purple)
window.resizable(width=False, height=False)

# Estilo principal
style = ttk.Style()

# Estilo dos botões
style.configure("Custom.TButton",
                background=lightPurple,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("Custom.TButton",
          background=[("active", "#573a87")])

style.configure("CustomTwo.TButton",
                background=tiffany,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("CustomTwo.TButton",
          background=[("active", "#573a87")])

# Frames (cores aplicadas diretamente, sem estilos)
frameSelect = tk.Frame(window, width=1300, height=600)
frameSelect.configure(background=lightPurple)

frameInsert = tk.Frame(window, width=1300, height=600)
frameInsert.configure(background=tiffany)

frameUpdate = tk.Frame(window, width=1300, height=600)
frameUpdate.configure(background=lightGolden)

frameDelete = tk.Frame(window, width=1300, height=600)
frameDelete.configure(background=blue)

frameSelectVisible = False
frameInsertVisible = False
frameUpdateVisible = False
frameDeleteVisible = False

# Funções para alternar os frames
def selectFrame():
    global frameSelectVisible, frameInsertVisible, frameUpdateVisible, frameDeleteVisible
    if frameSelectVisible:
        frameSelect.place_forget()
        frameSelectVisible = False
    else:
        frameSelect.place(x=200, y=15)
        frameSelectVisible = True
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False
        frameDelete.place_forget()
        frameDeleteVisible = False

def insertFrame():
    global frameInsertVisible, frameSelectVisible, frameUpdateVisible, frameDeleteVisible
    if frameInsertVisible:
        frameInsert.place_forget()
        frameInsertVisible = False
    else:
        frameInsert.place(x=200, y=15)
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
        frameUpdate.place(x=200, y=15)
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
        frameDelete.place(x=200, y=15)
        frameDeleteVisible = True
        frameSelect.place_forget()
        frameSelectVisible = False
        frameInsert.place_forget()
        frameInsertVisible = False
        frameUpdate.place_forget()
        frameUpdateVisible = False

# Linha superior
line = Separator(window, orient=HORIZONTAL)
line.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=30)

# Linha vertical
canvasLine = tk.Canvas(window, width=10, height=420, bg=purple, highlightthickness=0)
canvasLine.grid(row=1, column=1, rowspan=4, sticky="ns", padx=10, pady=10)

# Função para linha arredondada em canvas
def drawRoundedRect(canvas, x, y, width, height, color):
    radius = width // 2
    canvas.create_oval(x, y, x + width, y + width, fill=color, outline="")
    canvas.create_rectangle(x, y + radius, x + width, y + height - radius, fill=color, outline="")
    canvas.create_oval(x, y + height - width, x + width, y + height, fill=color, outline="")

drawRoundedRect(canvasLine, 0,0 ,10, 559, white)

# INFORMAÇÃO DO JOGO

labelGameInformation = ttk.Label(frameSelect, text="Informação do Jogo", background=lightPurple, font=("Times New Roman", 20))
labelGameInformation.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky=NSEW, ipady=20)

# INFORMAÇÕES DO USUÁRIO

labelPlayerInformation = ttk.Label(frameSelect, text="Informação do Usuário", background=lightPurple, font=("Times New Roman", 20))
labelPlayerInformation.grid(row=3, column=0, columnspan=3, pady=20, padx=20, sticky=NSEW, ipady=20)

# Botões
buttonSelect = ttk.Button(window, text="Select", style="Custom.TButton", command=selectFrame)
buttonSelect.grid(row=1, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonInsert = ttk.Button(window, text="Insert", style="Custom.TButton", command=insertFrame)
buttonInsert.grid(row=2, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonUpdate = ttk.Button(window, text="Update", style="Custom.TButton", command=updateFrame)
buttonUpdate.grid(row=3, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonDelete = ttk.Button(window, text="Delete", style="Custom.TButton", command=deleteFrame)
buttonDelete.grid(row=4, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

# FUNÇÃO DO BOTÃO SELECT

# BOTÕES COM FUNÇÕES PARA PROCURAR INFORMAÇÕES DOS JOGOS
buttonSearchIDGame = ttk.Button(frameSelect, text="ID do Jogo", style="CustomTwo.TButton", command=selectFrame)
buttonSearchIDGame.grid(row=1, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonSearchNameGame = ttk.Button(frameSelect, text="Nome", style="CustomTwo.TButton", command=selectFrame)
buttonSearchNameGame.grid(row=1, column=1, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonSearchGenderGame = ttk.Button(frameSelect, text="Gênero", style="CustomTwo.TButton", command=selectFrame)
buttonSearchGenderGame.grid(row=1, column=2, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonSearchPriceGame = ttk.Button(frameSelect, text="Preço", style="CustomTwo.TButton", command=selectFrame)
buttonSearchPriceGame.grid(row=1, column=3, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonSearchProducerGame = ttk.Button(frameSelect, text="Produtor", style="CustomTwo.TButton", command=selectFrame)
buttonSearchProducerGame.grid(row=1, column=4, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonSearchAgeGame = ttk.Button(frameSelect, text="Idade", style="CustomTwo.TButton", command=selectFrame)
buttonSearchAgeGame.grid(row=1, column=5, pady=20, padx=20, sticky=NSEW, ipady=20)

# BOTÕES PARA PROCURAR INFORMAÇÕES DO USUÁRIO

buttonSearchNamePlayer = ttk.Button(frameSelect, text="Nome", style="CustomTwo.TButton", command=selectFrame)
buttonSearchNamePlayer.grid(row=8, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonSearchIDPlayer = ttk.Button(frameSelect, text="ID do Usuário", style="CustomTwo.TButton", command=selectFrame)
buttonSearchIDPlayer.grid(row=8, column=1, pady=20, padx=20, sticky=NSEW, ipady=20)

# BOTÃO PARA PROCURAR INFORMAÇÃO NO CARRINHO

# Loop principal
window.mainloop()
