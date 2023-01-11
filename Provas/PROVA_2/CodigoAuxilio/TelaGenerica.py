"""
Implemente um simulador de Índice de Massa Corporal, em que IMC = massa / (altura * altura) 

frame4 = LabelFrame(frame2,width = 390,height =100)
frame4.place(x=5,y=5)

"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
import datetime
from tkinter import *  # biblioteca tkinter
from tkinter import ttk # biblioteca tkinter treeview
from tkinter import messagebox # biblioteca tkinter messagebox
from tkinter import filedialog
from PIL import ImageTk,Image    # Imagens .jpg ou .png
#Bibloiotecas inportadads fim

#Variaveis globais inicio
pasta = "trabalho/files"
ficheiro = "trabalho/files/acessos.txt" #Numero;data_sistema;hora_sistema;tipo_acesso
#Variaveis globais fim

#Verfica a existencia da pasta inicio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim

def teste():
    print("teste")

#-----------------------------------------------------------------------------------------------------------------------------#
#Tela generica centralizada
#-----------------------------------------------------------------------------------------------------------------------------#
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1100                             # tamanho (pixeis) da window a criar
appHeight = 450
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title("App")
#-----------------------------------------------------------------------------------------------------------------------------#
#
#-----------------------------------------------------------------------------------------------------------------------------#
"""
#-----------------------------------------------------------------------------------------------------------------------------#
"""
#-----------------------------------------------------------------------------------------------------------------------------#
#Menu generico
#-----------------------------------------------------------------------------------------------------------------------------#
menubar = Menu(window)
#-----------------------------------------------------------------------------------------------------------------------------#
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Movimentos",)
filemenu.add_command(label="Consultas",)
filemenu.add_command(label="CLS", command= lambda: os.system("cls"))
filemenu.add_command(label="Exit", command=window.destroy)
#-----------------------------------------------------------------------------------------------------------------------------#
#
#-----------------------------------------------------------------------------------------------------------------------------#
window.config(menu=filemenu)   #Sem cascade
window.config(menu=menubar)    #Com cascade
#-----------------------------------------------------------------------------------------------------------------------------#

window.mainloop()