"""
Implemente um programa que permita gerir uma ToDoList (lista de tarefas a executar)
"""

#Bibloiotecas inportadasa inicio
import os  # biblioteca os
from tkinter import *  # biblioteca tkinter
#Bibloiotecas inportadads fim

#Variaveis globais inicio
pasta = "files"
ficheiro = "files/list.txt"
#Variaveis globais fim
#
#Verfica a existencia da pasta incio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim

f = open(ficheiro,"w",encoding="utf8")
for i in range(10):
    line = "teste " + str(i+1) + "\n"
    f.write(line)
f.close()

#Função adicionarTarefa a lista Inicio
def adicionarTarefa():
    texto = tarefas.get()
    print(texto)
    lbLista.insert(END,texto)
    tarefas.set("")
    numerosTarefas()
#Função adicionarTarefa a lista Fim

#Função removerTarefa a lista Inicio
def removerTarefa():
    pos = lbLista.curselection()
    print(pos)
    lbLista.delete(pos)
    uploadLista()
    numerosTarefas()
#Função removerTarefa a lista Fim

#Função Clear a lista Inicio
def clearLista():
    lbLista.delete(0,END)
    numerosTarefas()
#Função Clear a lista arquivo Fim

#Função uploadLista para arquivo Inicio
def uploadLista():
    lista = []
    count = lbLista.size()
    print(count)
    f = open(ficheiro,"w", encoding="utf-8")
    for i in range(count):
        elemento = lbLista.get(i) + "\n"
        f.write(elemento)
    f.close()
    numerosTarefas()
#Função uploadLista para arquivo Fim

#Função downloadLista para arquivo Inicio
def downloadLista():
    clearLista()
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    #print(linhas)
    for linha in linhas:
        linha = linha.replace("\n","")
        lbLista.insert(END, linha)
    numerosTarefas()
#Função downloadLista para arquivo Fim

#Função ordenarLista para arquivo Inicio
def ordenarLista():
    lista = []
    f = open(ficheiro, "r")
    linhas = f.readlines()
    f.close()
    print(linhas)
    for linha in linhas:
        linha = linha.removesuffix("\n")
        lista.append(linha)
    lista.sort()
    clearLista()
    for linha in lista:
        lbLista.insert(END, linha)
    print(lista)
    numerosTarefas()
#Função ordenarLista para arquivo Fim

#Função numerosTarefas Inicio
def numerosTarefas():
    count = lbLista.size()
    tarefas_restantes.set(count)
#Função numerosTarefas Fim

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
lbLista = Listbox(frame1,width =40, height = 22, justify=CENTER)
lista = []
for pais in lista:
    lbLista.insert(END,pais)
lbLista.place(x=5 , y=5)
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
txtTarefaIns = Label(frame3,width = 15,height =1,text="Tarefa")
txtTarefaIns.place(x=1,y=35)
#-----------------------------------------------------------------------------------------------------------------------------#
tarefas = StringVar()
txtTarefaInserir = Entry(frame3,width =45, textvariable=tarefas)
txtTarefaInserir.place(x=80, y=35)
#-----------------------------------------------------------------------------------------------------------------------------#
btnAdicionar = Button(frame4,width = 10, height = 1,text="Adicionar", command=adicionarTarefa)
btnAdicionar.place(x=10,y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
btnRemover = Button(frame4,width = 10, height = 1,text="Remover",command=removerTarefa)
btnRemover.place(x=95,y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
btnClear = Button(frame4,width = 10, height = 1,text="Clear",command=clearLista)
btnClear.place(x=180,y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
btnUpload = Button(frame4,width = 10, height = 1,text="Upload",command=uploadLista)
btnUpload.place(x=10,y=50)
#-----------------------------------------------------------------------------------------------------------------------------#
btnDownload = Button(frame4,width = 10, height = 1,text="Download",command=downloadLista)
btnDownload.place(x=95,y=50)
#-----------------------------------------------------------------------------------------------------------------------------#
btnSort = Button(frame4,width = 10, height = 1,text="Ordenar",command=ordenarLista)
btnSort.place(x=180,y=50)
#-----------------------------------------------------------------------------------------------------------------------------#
txtTarefa = Label(frame4,width = 15, height = 1,text="Tarefas Restantes")
txtTarefa.place(x=270,y=10)
#-----------------------------------------------------------------------------------------------------------------------------#
tarefas_restantes = IntVar()
txtTarefaNum = Entry(frame4,width =5,state="disable", justify= CENTER, textvariable=tarefas_restantes)
txtTarefaNum.place(x=305, y=50)


window.mainloop()