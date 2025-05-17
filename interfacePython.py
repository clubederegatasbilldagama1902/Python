import tkinter #biblioteca para janelas
from tkinter import NSEW
from PIL import Image , ImageTk

black = "#000000"

red = "#ff0000"
blue = "#4a88e8"
green = "#00ff00"
white = "#FFFFFF"
aqua = "#00ffff"
purple = "#800080"
olive = "#808000"
brown = "#800000"
yellow = "#ffff00"

#janela
janela = tkinter.Tk() #Tk = biblioteca
janela.title("La ele")
janela.geometry("540x540")
janela.configure(background=black)
janela.resizable(width=False ,height=False)

#frames
frame1 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame1.grid(row=0,column=0,pady=0,padx=3,sticky=NSEW)

frame2 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame2.grid(row=0,column=1,pady=0,padx=3,sticky=NSEW)

frame3 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame3.grid(row=0,column=2,pady=0,padx=3,sticky=NSEW)

frame4 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame4.grid(row=1,column=0,pady=3,padx=3,sticky=NSEW)

frame5 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame5.grid(row=1,column=1,pady=3,padx=3,sticky=NSEW)

frame6 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame6.grid(row=1,column=2,pady=3,padx=3,sticky=NSEW)

frame7 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame7.grid(row=2,column=0,pady=3,padx=3,sticky=NSEW)

frame8 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame8.grid(row=2,column=1,pady=3,padx=3,sticky=NSEW)

frame9 = tkinter.Frame(janela,width=177,bg=black,height=177)
frame9.grid(row=2,column=2,pady=3,padx=3,sticky=NSEW)

#sla

icone1 = Image.open("imagem1.jpeg")
icone1 = icone1.resize((165,165))
icone1_tk = ImageTk.PhotoImage(icone1)

icone2 = Image.open("imagem2.jpg")
icone2 = icone2.resize((165,165))
icone2_tk = ImageTk.PhotoImage(icone2)

icone3 = Image.open("imagem3.jpeg")
icone3 = icone3.resize((165,165))
icone3_tk = ImageTk.PhotoImage(icone3)

icone4 = Image.open("imagem4.jpeg")
icone4 = icone4.resize((165,165))
icone4_tk = ImageTk.PhotoImage(icone4)

icone5 = Image.open("imagem5.jpg")
icone5 = icone5.resize((165,165))
icone5_tk = ImageTk.PhotoImage(icone5)

icone6 = Image.open("imagem6.jpeg")
icone6 = icone6.resize((165,165))
icone6_tk = ImageTk.PhotoImage(icone6)

icone7 = Image.open("imagem7.jpg")
icone7 = icone7.resize((165,165))
icone7_tk = ImageTk.PhotoImage(icone7)

icone8 = Image.open("imagem8.jpeg")
icone8 = icone8.resize((165,165))
icone8_tk = ImageTk.PhotoImage(icone8)

icone9 = Image.open("imagem9.png")
icone9 = icone9.resize((165,165))
icone9_tk = ImageTk.PhotoImage(icone9)

#Adicionar ícones em cada frame

label_icone1 = tkinter.Label(frame1,image=icone1_tk,bg=black)
label_icone1.pack(pady=10)

label_icone2 = tkinter.Label(frame2,image=icone2_tk,bg=black)
label_icone2.pack(pady=10)

label_icone3 = tkinter.Label(frame3,image=icone3_tk,bg=black)
label_icone3.pack(pady=10)

label_icone4 = tkinter.Label(frame4,image=icone4_tk,bg=black)
label_icone4.pack(pady=10)

label_icone5 = tkinter.Label(frame5,image=icone5_tk,bg=black)
label_icone5.pack(pady=10)

label_icone6 = tkinter.Label(frame6,image=icone6_tk,bg=black)
label_icone6.pack(pady=10)

label_icone7 = tkinter.Label(frame7,image=icone7_tk,bg=black)
label_icone7.pack(pady=10)

label_icone8 = tkinter.Label(frame8,image=icone8_tk,bg=black)
label_icone8.pack(pady=10)

label_icone9 = tkinter.Label(frame9,image=icone9_tk,bg=black)
label_icone9.pack(pady=10)

janela.mainloop()
