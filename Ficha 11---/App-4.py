"""
Implemente um simulador de Índice de Massa Corporal, em que IMC = massa / (altura * altura) 
"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
from tkinter import *  # biblioteca tkinter
#Bibloiotecas inportadads fim

#
def funcaoIMC():
    if altura.get() == 0:
        print("Insira valor para altura")
    else:
        os.system("cls")
        alturaFinal = altura.get() / 100
        resultado = peso.get() / (alturaFinal ** 2)
        """
        print("peso: %i"%peso.get())
        print("altura: %i"%altura.get())
        print(resultado)
        """
        varIMC.set("{0:.2f}".format(resultado))
#

#codigo principal inicio
window = Tk()
window.geometry("700x400")
window.title("Teste.txt")
#-----------------------------------------------------------------------------------------------------------------------------#
frame = LabelFrame(window,width = 690, height = 390,)
frame.place(x=5 , y=5)
#-----------------------------------------------------------------------------------------------------------------------------#
frame1 = LabelFrame(frame,width = 260, height = 370)
frame1.place(x=10 , y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
frame2 = LabelFrame(frame,width = 405,height = 370)
frame2.place(x=275, y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
frame3 = LabelFrame(frame2,width = 390,height =100)
frame3.place(x=5,y=5)
#-----------------------------------------------------------------------------------------------------------------------------#
frame4 = LabelFrame(frame2,width = 390,height =100)
frame4.place(x=5,y=110)
#-----------------------------------------------------------------------------------------------------------------------------#
lblPeso = Label(frame3,width = 5, height = 1, text = "Peso:")
lblPeso.place(x=5,y=20)
#-----#
peso = IntVar()
txtPesoIdeal = Entry(frame3, width = 10, justify=CENTER, textvariable = peso)
txtPesoIdeal.place(x=45, y=20)
#-----------------------------------------------------------------------------------------------------------------------------#
lblAltura = Label(frame3,width = 5, height = 1, text = "Altura:")
lblAltura.place(x=5,y=55)
#-----#
altura = IntVar()
txtAltura = Entry(frame3, width = 10, justify=CENTER, textvariable = altura)
txtAltura.place(x=45, y=55)
#-----------------------------------------------------------------------------------------------------------------------------#
lblIMC = Label(frame3,width = 5, height = 1, text = "IMC:")
lblIMC.place(x=120,y=20)
#-----#
varIMC = StringVar()
txtIMC = Entry(frame3, width = 10, justify=CENTER, state=DISABLED, textvariable=varIMC)
txtIMC.place(x=160, y=20)
#-----------------------------------------------------------------------------------------------------------------------------#
btnCalcularIMC = Button(frame4,width = 24, height = 2, font= ("arial", 19), text = "Calcular IMC", command=funcaoIMC)
btnCalcularIMC.place(x=10, y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
frame5 = LabelFrame(frame2,width = 390,height =145)
frame5.place(x=5,y=215)
#-----------------------------------------------------------------------------------------------------------------------------#

window.mainloop