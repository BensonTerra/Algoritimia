"""
Teste de uma plataforma de agenda via terminal usando pyhton, com possibilidade remoção de tarefas especifica do ficheiro .txt
"""
import os  # biblioteca os
import datetime
from tkinter import *  # biblioteca tkinter
from tkinter import ttk # biblioteca tkinter treeview
from tkinter import messagebox # biblioteca tkinter messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
from PIL import ImageTk,Image    # Imagens .jpg ou .png

#Variaveis globais
pasta = "estudo/pastaEstudoTkinter"
ficheiro = "estudo/pastaEstudoTkinter/listaTkinter.txt"

#função ficheiroCiclo, cria a pasta e um arquivo .txt para primeira vez que é rodado
def primeiroCiclo():
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        f = open(ficheiro, "a", encoding="utf-8")
        initialComment = "Readme"
        f.write(initialComment)
        f.close()
primeiroCiclo()

#Interface grafica
window = Tk()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1366                             # tamanho (pixeis) da window a criar
appHeight = 768
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.resizable(0,0)
window.title("Revisão Tkinter")



window.mainloop()