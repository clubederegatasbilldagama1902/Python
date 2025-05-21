import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Separator
import tkinter as tk

# Cores
purple = "#442e73"
purpleTwoColor = "#664983"
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
                background=purpleTwoColor,
                foreground="white",
                font=("Segoe UI", 14, "bold"),
                padding=20,
                borderwidth=0)
style.map("Custom.TButton",
          background=[("active", "#573a87")])

# Frames (cores aplicadas diretamente, sem estilos)
frameSelect = tk.Frame(window, width=1300, height=400)
frameSelect.configure(background=purpleTwoColor)

frameInsert = tk.Frame(window, width=1300, height=400)
frameInsert.configure(background=tiffany)

frameUpdate = tk.Frame(window, width=1300, height=400)
frameUpdate.configure(background=lightGolden)

frameDelete = tk.Frame(window, width=1300, height=400)
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
canvasLine = tk.Canvas(window, width=10, height=400, bg=purple, highlightthickness=0)
canvasLine.grid(row=1, column=1, rowspan=4, sticky="ns", padx=10, pady=10)

def roundedRect(canvas, x1, y1, x2, y2, radius=5, **kwargs):
    points = [
        x1+radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

roundedRect(canvasLine, 0, 0, 10, 1000, radius=5, fill=white, outline="")

# Botões
buttonSelect = ttk.Button(window, text="Select", style="Custom.TButton", command=selectFrame)
buttonSelect.grid(row=1, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonInsert = ttk.Button(window, text="Insert", style="Custom.TButton", command=insertFrame)
buttonInsert.grid(row=2, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonUpdate = ttk.Button(window, text="Update", style="Custom.TButton", command=updateFrame)
buttonUpdate.grid(row=3, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

buttonDelete = ttk.Button(window, text="Delete", style="Custom.TButton", command=deleteFrame)
buttonDelete.grid(row=4, column=0, pady=20, padx=20, sticky=NSEW, ipady=20)

# Loop principal
window.mainloop()
