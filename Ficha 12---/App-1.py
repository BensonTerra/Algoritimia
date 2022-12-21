"""
Implemente um simulador de Índice de Massa Corporal, em que IMC = massa / (altura * altura) 

frame3 = LabelFrame(frame2,width = 390,height =100)
frame3.place(x=5,y=5)

"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
from tkinter import *  # biblioteca tkinter
from tkinter import ttk # biblioteca tkinter treeview
from tkinter import messagebox # biblioteca tkinter messagebox
#Bibloiotecas inportadads fim

def donothing():
    print("Testing")



#codigo principal inicio
window = Tk()
window.geometry("1000x450")
window.title("Registro")
#-----------------------------------------------------------------------------------------------------------------------------#
menubar = Menu(window)
#-----------------------------------------------------------------------------------------------------------------------------#
filemenu = Menu(menubar, tearoff=0)
#1
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Movimentos", command=donothing)
filemenu.add_command(label="Consultas", command=donothing)
filemenu.add_command(label="Exit", command=window.quit)
window.config(menu=filemenu)

"""filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
window.config(menu=menubar)"""


#-----------------------------------------------------------------------------------------------------------------------------#
#                                       TELA 1-PRINCIPAL
#-----------------------------------------------------------------------------------------------------------------------------#
frame0 = LabelFrame(window,width = 990, height = 440)
frame0.place(x=5 , y=5)
#-----------------------------------------------------------------------------------------------------------------------------#
frame1 = LabelFrame(frame0,width = 660, height = 425)
frame1.place(x=5 , y=5)
#-----------------------------------------------------------------------------------------------------------------------------#
imagem1 = Canvas(frame1, width = 650, height = 400)
img = PhotoImage(file = "./files/imagemRegistro.png")
imagem1.create_image(325,200, anchor = "center", image = img)
imagem1.place(x=0,y=0)
#-----------------------------------------------------------------------------------------------------------------------------#
frame2 = LabelFrame(frame0,width = 310, height = 425)
frame2.place(x=670 , y=5)
#-----------------------------------------------------------------------------------------------------------------------------#
txtRegister = Label(frame2, width = 0, height = 1, text = " Programa de Registros", font = ("arial", 20))
txtRegister.place(x = 0,y = 108)
#-----------------------------------------------------------------------------------------------------------------------------#
#                                       TELA 2-MOVIMENTOS
#-----------------------------------------------------------------------------------------------------------------------------#

window.mainloop()