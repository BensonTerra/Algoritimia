"""
Implemente um simulador de Índice de Massa Corporal, em que IMC = massa / (altura * altura) 

frame3 = LabelFrame(frame2,width = 390,height =100)
frame3.place(x=5,y=5)

"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
from tkinter import *  # biblioteca tkinter
#Bibloiotecas inportadads fim




#codigo principal inicio
window = Tk()
window.geometry("1000x450")
window.title("Teste.txt")
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


window.mainloop()