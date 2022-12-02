#Bibloiotecas inportadasa inicio
import os #biblioteca os
from tkinter import * #biblioteca tkinter
import time #biblioteca time
#Bibloiotecas inportadads fim
#
5#Variaveis globais inicio
pasta = "files"
ficheiro = "files/text.txt"
#Variaveis globais fim
#
#Verfica a existencia da pasta incio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim
#

#
#codigo principal inicio
window = Tk()
window.geometry("700x400")
window.title("Teste.txt")
#-----------------------------------------------------------------------------------------------------------------------------#
frame1 = LabelFrame(window,width = 680, height = 380)
frame1.place(x=10 , y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
lblAltura = Label(frame1, text = "Altura em cm:", font = ("arial", 10), fg = "blue")
lblAltura.place(x = 10, y = 10)
#-----------------------------------------------------------------------------------------------------------------------------#
txtAltura = Entry(frame1, width = 10)
txtAltura.place(x = 100, y = 10)
#-----------------------------------------------------------------------------------------------------------------------------#
#codigo principal fim




window.mainloop()