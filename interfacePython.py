# Importação de bibliotecas
import tkinter  # Biblioteca para criação de interfaces gráficas
from tkinter import NSEW  # Constante para posicionamento de elementos
from PIL import Image, ImageTk  # Biblioteca para manipulação de imagens

# Definição de cores em formato hexadecimal
black = "#000000"  # Preto
red = "#ff0000"    # Vermelho
blue = "#4a88e8"   # Azul
green = "#00ff00"  # Verde
white = "#FFFFFF"  # Branco
aqua = "#00ffff"   # Ciano
purple = "#800080" # Roxo
olive = "#808000"  # Oliva
brown = "#800000"  # Marrom
yellow = "#ffff00" # Amarelo

# Configuração da janela principal
janela = tkinter.Tk()  # Cria a janela principal
janela.title("La ele")  # Define o título da janela
janela.geometry("540x540")  # Define o tamanho da janela (largura x altura)
janela.configure(background=black)  # Define o fundo preto
janela.resizable(width=False, height=False)  # Impede redimensionamento

# Criação de 9 frames (quadros) para organizar a interface
# Cada frame tem tamanho 177x177 pixels e fundo preto
frame1 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame1.grid(row=0, column=0, pady=0, padx=3, sticky=NSEW)  # Posiciona na grade

frame2 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame2.grid(row=0, column=1, pady=0, padx=3, sticky=NSEW)

frame3 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame3.grid(row=0, column=2, pady=0, padx=3, sticky=NSEW)

frame4 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame4.grid(row=1, column=0, pady=3, padx=3, sticky=NSEW)

frame5 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame5.grid(row=1, column=1, pady=3, padx=3, sticky=NSEW)

frame6 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame6.grid(row=1, column=2, pady=3, padx=3, sticky=NSEW)

frame7 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame7.grid(row=2, column=0, pady=3, padx=3, sticky=NSEW)

frame8 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame8.grid(row=2, column=1, pady=3, padx=3, sticky=NSEW)

frame9 = tkinter.Frame(janela, width=177, bg=black, height=177)
frame9.grid(row=2, column=2, pady=3, padx=3, sticky=NSEW)

# Carregamento e redimensionamento das imagens
# Cada imagem é aberta, redimensionada para 165x165 e convertida para formato Tkinter
icone1 = Image.open("imagem1.jpeg")
icone1 = icone1.resize((165, 165))
icone1_tk = ImageTk.PhotoImage(icone1)

icone2 = Image.open("imagem2.jpg")
icone2 = icone2.resize((165, 165))
icone2_tk = ImageTk.PhotoImage(icone2)

icone3 = Image.open("imagem3.jpeg")
icone3 = icone3.resize((165, 165))
icone3_tk = ImageTk.PhotoImage(icone3)

icone4 = Image.open("imagem4.jpeg")
icone4 = icone4.resize((165, 165))
icone4_tk = ImageTk.PhotoImage(icone4)

icone5 = Image.open("imagem5.jpg")
icone5 = icone5.resize((165, 165))
icone5_tk = ImageTk.PhotoImage(icone5)

icone6 = Image.open("imagem6.jpeg")
icone6 = icone6.resize((165, 165))
icone6_tk = ImageTk.PhotoImage(icone6)

icone7 = Image.open("imagem7.jpg")
icone7 = icone7.resize((165, 165))
icone7_tk = ImageTk.PhotoImage(icone7)

icone8 = Image.open("imagem8.jpeg")
icone8 = icone8.resize((165, 165))
icone8_tk = ImageTk.PhotoImage(icone8)

icone9 = Image.open("imagem9.png")
icone9 = icone9.resize((165, 165))
icone9_tk = ImageTk.PhotoImage(icone9)

# Adiciona cada imagem em seu respectivo frame
label_icone1 = tkinter.Label(frame1, image=icone1_tk, bg=black)
label_icone1.pack(pady=10)  # Empacota com espaçamento vertical de 10 pixels

label_icone2 = tkinter.Label(frame2, image=icone2_tk, bg=black)
label_icone2.pack(pady=10)

label_icone3 = tkinter.Label(frame3, image=icone3_tk, bg=black)
label_icone3.pack(pady=10)

label_icone4 = tkinter.Label(frame4, image=icone4_tk, bg=black)
label_icone4.pack(pady=10)

label_icone5 = tkinter.Label(frame5, image=icone5_tk, bg=black)
label_icone5.pack(pady=10)

label_icone6 = tkinter.Label(frame6, image=icone6_tk, bg=black)
label_icone6.pack(pady=10)

label_icone7 = tkinter.Label(frame7, image=icone7_tk, bg=black)
label_icone7.pack(pady=10)

label_icone8 = tkinter.Label(frame8, image=icone8_tk, bg=black)
label_icone8.pack(pady=10)

label_icone9 = tkinter.Label(frame9, image=icone9_tk, bg=black)
label_icone9.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
