#Bibloiotecas inportadasa inicio
import os #biblioteca os
from tkinter import * #biblioteca tkinter
import time #biblioteca time
#Bibloiotecas inportadads fim
#
#Variaveis globais inicio
k = 0
#Variaveis globais fim
#
#Define K para peso ideal incio
def PesoIdealFuncao():
    global k
    if selected.get() == "Masculino":
        k = 4
    else:
        k = 2
    peso = (altura.get() - 100)

#Define K para peso ideal fim
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
altura = IntVar()
txtAltura = Entry(frame1, width = 10, textvariable = altura) #entrada da altura
txtAltura.place(x = 100, y = 10)
#-----------------------------------------------------------------------------------------------------------------------------#
frame2 = LabelFrame(frame1,text = "Genero",width = 200, height = 150, fg= "blue")
frame2.place(x=10 , y=50)
#-----------------------------------------------------------------------------------------------------------------------------#
selected = StringVar()
selected.set("Masculino")
rd1 = Radiobutton(frame2, text = "Masculino", value = "Masculino", variable = selected)
rd1.place(x = 20, y =20)
rd2 = Radiobutton(frame2, text = "Feminino", value = "Feminino", variable = selected)
rd2.place(x = 20, y =80)
#-----------------------------------------------------------------------------------------------------------------------------#
frame3 = LabelFrame(frame1,text = "Peso Ideal",width = 200, height = 150, fg= "blue")
frame3.place(x=220 , y=50)
#-----------------------------------------------------------------------------------------------------------------------------#
lblPesoIdeal = Label(frame3, text = "Peso Ideal:", font = ("arial", 10), fg = "blue")
lblPesoIdeal.place(x = 10, y = 10)
#-----------------------------------------------------------------------------------------------------------------------------#
btnPesoIdeal = Button(frame3, width = 20, height = 3,font = ("arial", 10), text = "Calcular peso ideal", fg = "green", bd = 2, command = PesoIdealFuncao) #comando
btnPesoIdeal.place(x = 10, y = 40)
#-----------------------------------------------------------------------------------------------------------------------------#
txtPesoIdeal = Text(frame3,width = 10, height = 1)
txtPesoIdeal.place(x = 80, y = 10)
#codigo principal fim




window.mainloop()