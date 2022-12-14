"""

"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
from tkinter import *  # biblioteca tkinter
#Bibloiotecas inportadads fim






#codigo principal inicio
window = Tk()
window.geometry("700x400")
window.title("Teste.txt")
#-----------------------------------------------------------------------------------------------------------------------------#
frame = LabelFrame(window,width = 690, height = 390)
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



window.mainloop()