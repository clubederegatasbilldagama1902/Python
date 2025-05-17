# Importação das bibliotecas necessárias
import tkinter  # Biblioteca para criação de interfaces gráficas
from tkinter import NSEW  # Constante para alinhamento
import pygame  # Biblioteca para reprodução de áudio
import os  # Biblioteca para manipulação de arquivos do sistema
import PIL  # Biblioteca para processamento de imagens
from PIL import Image, ImageTk  # Classes específicas para trabalhar com imagens
from tkinter import Button, Listbox, SINGLE, Scrollbar, Label, END, RIDGE, RAISED, ACTIVE  # Componentes da interface
from pygame import mixer, mixer_music  # Módulos para controle de áudio

# Definição de cores em formato hexadecimal
black = "#000000"
white = "#FFFFFF"
green = "#00ff00"
blue = "#4a88e8"
silver = "#1C1C1C"
grey = "#1D1F2A"

# Configuração da janela principal
janela = tkinter.Tk()  # Cria a janela principal
janela.title("LucasGames_1902")  # Define o título da janela
janela.geometry("1000x1000")  # Define o tamanho da janela
janela.configure(background=black)  # Define a cor de fundo
janela.resizable(width=False, height=False)  # Impede redimensionamento

# Criação dos frames (áreas divididas da janela)
frame1 = tkinter.Frame(janela, width=980, bg=silver, height=200)  # Frame do player de música
frame1.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

frame2 = tkinter.Frame(janela, width=980, bg=silver, height=30)  # Frame para mostrar a música atual
frame2.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

frame3 = tkinter.Frame(janela, width=980, bg=grey, height=735)  # Frame para a playlist
frame3.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

# Funções do player de música

# Carrega imagem do botão pause
upause = Image.open('upause.png')
upause = upause.resize((50, 50))
upause = ImageTk.PhotoImage(upause)

# Função para tocar música selecionada
def play_music():
    atual = lista_de_musicas.get(ACTIVE)  # Obtém a música selecionada
    musica_atual['text'] = atual  # Atualiza o label com a música atual
    mixer.music.load(atual)  # Carrega a música
    mixer.music.play()  # Inicia a reprodução

# Variável global para controle do estado de pause
pausar = False

# Função para pausar/despausar a música
def pause_music():
    global pausar
    if pausar:
        pPause.config(image=upause)  # Altera a imagem do botão
        mixer.music.pause()  # Pausa a música
    else:
        pPause.config(image=pause)  # Altera a imagem do botão
        mixer.music.unpause()  # Despausa a música
    pausar = not pausar  # Inverte o estado

# Função para voltar para a música anterior
def back_music():
    tocando = musica_atual['text']
    index = mp3.index(tocando)
    ultimo = len(mp3) - 1
    if index != 0:
        newindex = index - 1
        anterior = mp3[newindex]
        mixer.music.load(anterior)
        mixer.music.play()
        # Atualiza a interface
        lista_de_musicas.delete(0, END)
        lista_de_musicas.select_set(newindex)
        runplaylist()
        lista_de_musicas.select_set(newindex)
        lista_de_musicas.config(selectmode=SINGLE)
        musica_atual['text'] = anterior
    else:
        # Volta para a última música se estiver na primeira
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

# Função para avançar para a próxima música
def next_music():
    tocando = musica_atual['text']
    index = mp3.index(tocando)
    ultimo = len(mp3) - 1
    if index != ultimo:
        newindex = index + 1
        proxima = mp3[newindex]
        mixer.music.load(proxima)
        mixer.music.play()
        # Atualiza a interface
        lista_de_musicas.delete(0, END)
        lista_de_musicas.select_set(newindex)
        runplaylist()
        lista_de_musicas.select_set(newindex)
        lista_de_musicas.config(selectmode=SINGLE)
        musica_atual['text'] = proxima
    else:
        # Volta para a primeira música se estiver na última
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

# Função para parar a reprodução
def stop_music():
    mixer.music.stop()

# Configuração dos botões do player com imagens

# Botão Play
play = Image.open("play2.png")
play = play.resize((50, 50))
play = ImageTk.PhotoImage(play)
pPlay = Button(frame1, command=play_music, image=play, height=50, bg=silver, border=0)
pPlay.place(x=470, y=80)

# Botão Pause
pause = Image.open("pause.png")
pause = pause.resize((50, 50))
pause = ImageTk.PhotoImage(pause)
pPause = Button(frame1, command=pause_music, image=pause, height=50, bg=silver, border=0)
pPause.place(x=400, y=80)

# Botão Next
next = Image.open("next.png")
next = next.resize((50, 50))
next = ImageTk.PhotoImage(next)
pNext = Button(frame1, command=next_music, image=next, height=50, bg=silver, border=0)
pNext.place(x=590, y=80)

# Botão Back
back = Image.open("prev.png")
back = back.resize((50, 50))
back = ImageTk.PhotoImage(back)
pBack = Button(frame1, command=back_music, image=back, height=50, bg=silver, border=0)
pBack.place(x=330, y=80)

# Botão Stop
stop = Image.open("stop.png")
stop = stop.resize((50, 50))
stop = ImageTk.PhotoImage(stop)
pStop = Button(frame1, command=stop_music, image=stop, height=50, bg=silver, border=0)
pStop.place(x=520, y=80)

# Configuração da playlist
lista_de_musicas = Listbox(frame3, width=95, height=50, selectmode=SINGLE, 
                          font=('verdana 11'), bg=grey, fg=green, border=0)
lista_de_musicas.grid(row=0, column=0, padx=8)

# Barra de rolagem
scr = Scrollbar(frame3)
scr.grid(row=0, column=1, sticky=NSEW)
lista_de_musicas.config(yscrollcommand=scr.set)
scr.config(command=lista_de_musicas.yview)

# Label para mostrar a música atual
musica_atual = Label(frame2, text='Bora bill', bg=silver, fg=white, font=('verdana 11'))
musica_atual.place(x=10, y=3)

# Carrega músicas da pasta padrão de música do usuário
os.chdir(rf'C:\Users\{os.getlogin()}\Music')
pastamusic = os.listdir()
mp3 = [nomes for nomes in pastamusic if nomes.endswith('.mp3')]  # Filtra apenas arquivos MP3

# Função para popular a playlist
def runplaylist():
    for music in mp3:
        lista_de_musicas.insert(END, music)

runplaylist()  # Executa a função para carregar as músicas
mixer.init()  # Inicializa o mixer do pygame
janela.mainloop()  # Inicia o loop principal da interface
