import tkinter #biblioteca para janelas
from tkinter import NSEW
import pygame #biblioteca para os controles
import os #biblioteca para a manipulação de arquivos
import PIL #biblioteca para trabalhar as imagens
from PIL import Image , ImageTk
from tkinter import Button , Listbox , SINGLE , Scrollbar , Label , END , RIDGE , RAISED , ACTIVE
from pygame import mixer , mixer_music


black = "#000000"
white = "#FFFFFF"
green = "#00ff00"
blue = "#4a88e8"
silver = "#1C1C1C"
grey = "#1D1F2A"

#janela
janela = tkinter.Tk() #Tk = biblioteca
janela.title("LucasGames_1902")
janela.geometry("1000x1000")
janela.configure(background=black)
janela.resizable(width=False ,height=False)

#frames
frame1 = tkinter.Frame(janela,width=980,bg=silver,height=200) #FRAME1=player
frame1.grid(row=0,column=0,pady=10,padx=10,sticky=NSEW)

frame2 = tkinter.Frame(janela,width=980,bg=silver,height=30) #FRAME PARA MUSICAS
frame2.grid(row=1,column=0,pady=5,padx=10,sticky=NSEW)

frame3 = tkinter.Frame(janela,width=980,bg=grey,height=735) #FRAME PARA PLAYLIST
frame3.grid(row=2,column=0,pady=5,padx=10,sticky=NSEW)

#funções

upause = Image.open('upause.png')
upause = upause.resize((50,50))
upause = ImageTk.PhotoImage(upause)
def play_music():
    atual = lista_de_musicas.get(ACTIVE)
    musica_atual['text'] = atual
    mixer.music.load(atual)
    mixer.music.play()


pausar = False
def pause_music():
    global pausar
    if pausar:
        pPause.config(image=upause)
        mixer.music.pause()
    else:
        pPause.config(image=pause)
        mixer.music.unpause()
    pausar = not pausar
def back_music():
    tocando = musica_atual['text']
    index = mp3.index(tocando)
    ultimo = len(mp3) - 1
    if index != 0:
        newindex = index - 1
        anterior = mp3[newindex]

        mixer.music.load(anterior)
        mixer.music.play()

        lista_de_musicas.delete(0, END)
        lista_de_musicas.select_set(newindex)
        runplaylist()
        lista_de_musicas.select_set(newindex)
        lista_de_musicas.config(selectmode=SINGLE)
        musica_atual['text'] = anterior
    else:
        newindex = ultimo

        proxima = mp3[newindex]

        mixer.music.load(proxima)
        mixer.music.play()

        lista_de_musicas.delete(0, END)

        lista_de_musicas.select_set(newindex)

        runplaylist()
        lista_de_musicas.select_set(newindex)
        lista_de_musicas.config(selectmode=SINGLE)
        musica_atual['text'] = proxima

def next_music():
    tocando = musica_atual['text']
    index = mp3.index(tocando)
    ultimo = len(mp3) - 1
    if index != ultimo:

        newindex = index + 1

        proxima = mp3[newindex]

        mixer.music.load(proxima)
        mixer.music.play()

        lista_de_musicas.delete(0, END)

        lista_de_musicas.select_set(newindex)

        runplaylist()
        lista_de_musicas.select_set(newindex)
        lista_de_musicas.config(selectmode=SINGLE)
        musica_atual['text'] = proxima

    else:
        newindex = 0

        proxima = pastamusic[newindex]

        mixer.music.load(proxima)
        mixer.music.play()

        lista_de_musicas.delete(0, END)

        lista_de_musicas.select_set(newindex)

        runplaylist()
        lista_de_musicas.select_set(newindex)
        lista_de_musicas.config(selectmode=SINGLE)
        musica_atual['text'] = proxima

def stop_music():
    mixer.music.stop()

#imagens
#play
play = Image.open("play2.png")
play = play.resize((50,50))
play = ImageTk.PhotoImage(play)

pPlay = Button(frame1,command=play_music,image=play,height=50,bg=silver,border=0)
pPlay.place(x=470,y=80)

#pause
pause = Image.open("pause.png")
pause = pause.resize((50,50))
pause = ImageTk.PhotoImage(pause)

pPause = Button(frame1,command=pause_music,image=pause,height=50,bg=silver,border=0)
pPause.place(x=400,y=80)

#next
next = Image.open("next.png")
next = next.resize((50,50))
next = ImageTk.PhotoImage(next)

pNext = Button(frame1,command=next_music,image=next,height=50,bg=silver,border=0)
pNext.place(x=590,y=80)

#back
back = Image.open("prev.png")
back = back.resize((50,50))
back = ImageTk.PhotoImage(back)

pBack = Button(frame1,command=back_music,image=back,height=50,bg=silver,border=0)
pBack.place(x=330,y=80)

#stop
stop = Image.open("stop.png")
stop = stop.resize((50,50))
stop = ImageTk.PhotoImage(stop)

pStop = Button(frame1,command=stop_music,image=stop,height=50,bg=silver,border=0)
pStop.place(x=520,y=80)

#playlist

lista_de_musicas = Listbox(frame3, width=95, height=50, selectmode=SINGLE, font=('verdana 11'), bg=grey, fg=green, border=0)
lista_de_musicas.grid(row=0, column=0, padx=8)

scr = Scrollbar(frame3)
scr.grid(row=0, column=1, sticky=NSEW)

lista_de_musicas.config(yscrollcommand=scr.set)
scr.config(command=lista_de_musicas.yview)

musica_atual = Label(frame2, text= 'Bora bill', bg= silver, fg= white,font=('verdana 11'))
musica_atual.place(x=10, y=3)

os.chdir(rf'C:\Users\{os.getlogin()}\Music')
pastamusic = os.listdir()
mp3 = [nomes for nomes in pastamusic if pastamusic if nomes.endswith('.mp3')]
def runplaylist():
    for music in mp3:
        lista_de_musicas.insert(END, music)

runplaylist()
mixer.init()
janela.mainloop()