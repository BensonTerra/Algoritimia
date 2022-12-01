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
#Guardar o ficheiro inicio
def guardarFicheiro():
    linha = txtTexto.get("0.0","end")
    f = open(ficheiro, "a", encoding="utf-8")
    f.write(linha)
    f.close()
    time.sleep(1)
#Guardar o ficheiro fim
#
#Limpar texto inicio
def limparTexto():
    txtTexto.delete("0.0","end")
#Limpar texto fim
#
#Ler ficheiros inicio
def lerFicheiro():
    limparTexto()
    f = open(ficheiro,"r")
    texto = f.read()
    txtTexto.insert("end",texto)
    f.close()
#Ler ficheiros fim
#
#codigo principal inicio
window = Tk()
window.geometry("700x400")
window.title("Teste.txt")
#-----------------------------------------------------------------------------------------------------------------------------#
txtTexto = Text(window, width = 60, height = 16, wrap = "word")
txtTexto.place(x = 200, y = 60)
#-----------------------------------------------------------------------------------------------------------------------------#
btnGuardarFicheiro = Button(window, width = 20,height= 3,font = ("arial", 10), text = "Guardar Ficheiro", fg = "green", bd = 2, command = guardarFicheiro)
btnGuardarFicheiro.place(x = 20, y = 60)
#-----------------------------------------------------------------------------------------------------------------------------#
btnLimparFicheiro = Button(window, width = 20, height = 3,font = ("arial", 10), text = "Limpar texto", fg = "green", bd = 2, command = limparTexto)
btnLimparFicheiro.place(x = 20, y = 160)
#-----------------------------------------------------------------------------------------------------------------------------#
btnLerFicheiro = Button(window, width = 20, height = 3,font = ("arial", 10), text = "Ler Ficheiro", fg = "green", bd = 2, command = lerFicheiro)
btnLerFicheiro.place(x = 20, y = 260)
#codigo principal fim




window.mainloop()