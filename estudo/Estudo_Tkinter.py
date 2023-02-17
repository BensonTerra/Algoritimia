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
pastaPrograma_1 = "estudo/pastaEstudoTkinter"
ficheiroPrograma_1 = "estudo/pastaEstudoTkinter/listaTkinter.txt"
#---#



"""----------------------------------------------------------------------------------------
                                          Programa 1                                       """

#função ficheiroCiclo, cria a pasta e um arquivo .txt para primeira vez que é rodado
def primeiroCiclo_Programa_1():
    if not os.path.exists(pastaPrograma_1):
        os.mkdir(pastaPrograma_1)
        f = open(ficheiroPrograma_1, "a", encoding="utf-8")
        initialComment = "Readme"
        f.write(initialComment)
        f.close()
primeiroCiclo_Programa_1()

#Tela 0
def TelaInicial():
    panned2Width = 0.75 * appWidth
    panned2Height = appHeight
    panned2 = PanedWindow(window, bg = "gray",width = panned2Width, height = appHeight)
    panned2.place(x=panned1Width , y=0)

#Tela 1
def tela1():
    #-----------------------------------------------------------------------------------------------------------------------------#
    menubar = Menu(window)
    #-----------------------------------------------------------------------------------------------------------------------------#
    navegacao = Menu(menubar, tearoff=0)

    menubar.add_cascade(label = "Telas", menu = navegacao)
    navegacao.add_command(label="Tela Inicial", command = TelaInicial)
    navegacao.add_command(label="Programa 1")
    navegacao.add_command(label="Tela 3")
    navegacao.add_command(label="Tela 4")
    navegacao.add_command(label="Teste", command= lambda: indexCapture(treePanel))
    #---#
    menubar.add_command(label="CLS", command = lambda: os.system("cls"))
    menubar.add_command(label="Exit", command = window.destroy)
    window.config(menu =  menubar)
    #-----------------------------------------------------------------------------------------------------------------------------#
    panned2Width = 0.75 * appWidth
    panned2Height = appHeight
    panned2 = PanedWindow(window, bg = "gray",width = panned2Width, height = appHeight)
    panned2.place(x=panned1Width , y=0)
    #-----------------------------------------------------------------------------------------------------------------------------#
    labelFrame1 = LabelFrame(panned2, width = 0.98 * panned2Width, height = 0.98 * panned2Height, bg = "gray")
    labelFrame1.place(x = 0.01 * panned2Width, y = 0.01 * panned2Height)
    #-----------------------------------------------------------------------------------------------------------------------------#
    linhaNomeheight = 0.01 * panned2Height
    #-----------------------------------------------------------------------------------------------------------------------------#
    label1 = Label(labelFrame1, width = 12, height = 1, text = "Primeiro Nome:", bg = "gray", font = ("Arial", 12))
    label1.place(x = 0.01 * panned2Width, y = linhaNomeheight)
    #---#
    txtPrimeiroNomeVar = StringVar()
    entry1 = Entry(labelFrame1, width = 10, font = ("Arial", 12),textvariable = txtPrimeiroNomeVar)
    entry1.place(x = 0.12 * panned2Width, y = 0.01 * panned1Height)
    #-----------------------------------------------------------------------------------------------------------------------------#
    label2 = Label(labelFrame1, width = 12, height = 1, text = "Ultimo Nome:", bg = "gray", font = ("Arial", 12))
    label2.place(x = 0.215 * panned2Width, y = linhaNomeheight)
    #---#
    txtUltimoNomeVar = StringVar()
    entry2 = Entry(labelFrame1, width = 10, font = ("Arial", 12), textvariable = txtUltimoNomeVar)
    entry2.place(x = 0.32 * panned2Width, y = 0.01 * panned1Height)
    #-----------------------------------------------------------------------------------------------------------------------------#
    labelFrame2 = LabelFrame(labelFrame1, width = 0.4 * panned2Width, height = 0.15 * panned2Height, font = ("Arial", 12))
    labelFrame2.place(x = 0.01 * panned2Width, y = 0.05 * panned2Height)
    labelFrame2Width = 0.4 * panned2Width
    labelFrame2Height = 0.15 * panned2Height
    #---#
    selected = StringVar()
    selected.set("Docente")
    rd1 = Radiobutton(labelFrame2, text = "Docente", value = "Docente", font = ("Arial", 12), variable = selected)
    rd2 = Radiobutton(labelFrame2, text = "Estudante", value = "Estudante", font = ("Arial", 12), variable = selected)
    rd3 = Radiobutton(labelFrame2, text = "Externo", value = "Externo", font = ("Arial", 12), variable = selected)
    rd1.place(x = 0.05 * labelFrame2Width, y = 0.3 * labelFrame2Height)
    rd2.place(x = 0.38 * labelFrame2Width, y = 0.3 * labelFrame2Height)
    rd3.place(x = 0.70 * labelFrame2Width, y = 0.3 * labelFrame2Height)
    #-----------------------------------------------------------------------------------------------------------------------------#
    labelFrame3 = LabelFrame(labelFrame1, width = 0.4 * panned2Width, height = 0.2 * panned2Height, font = ("Arial", 12))
    labelFrame3.place(x = 0.01 * panned2Width, y = 0.205 * panned2Height)
    labelFrame3Width = 0.4 * panned2Width
    labelFrame3Height = 0.2 * panned2Height
    #---#
    treePanel = ttk.Treeview(labelFrame3, columns=('Usuario','Perfil'),show='headings',height=6)
    treePanel.heading('Usuario', text='Usuario')
    treePanel.column('Usuario', width = int(0.67 * labelFrame3Width), anchor='c')
    #---#
    treePanel.heading('Perfil', text='Perfil')
    treePanel.column('Perfil', width = int(0.25 * labelFrame3Width), anchor='c')
    #---#
    scrollBar1 = ttk.Scrollbar(labelFrame3, orient='vertical', command=treePanel.yview())
    scrollBar1.place(x = 0.94 * labelFrame3Width,y = 0, height = 0.95 * labelFrame3Height)
    #---#
    treePanel.place(x = 0.01 * labelFrame3Width,y = 0.01 * labelFrame3Height)
    carregarAtualizarTreeView(treePanel)
    #-----------------------------------------------------------------------------------------------------------------------------#
    labelFrame4 = LabelFrame(labelFrame1, width = 0.4 * panned2Width, height = 0.39 * panned2Height, font = ("Arial", 12))
    labelFrame4.place(x = 0.01 * panned2Width, y = 0.41 * panned2Height)
    labelFrame4Width = 0.4 * panned2Width
    labelFrame4Height = 0.25 * panned2Height
    #---#ler ficheiro
    btnLerFicheiro = Button(labelFrame4, text = "Ler Ficheiro", compound=LEFT, relief = "sunken", 
                    width = 43, height = 3, font=("Arial", 12), command = lambda: carregarAtualizarTreeView(treePanel))
    btnLerFicheiro.place(x = 0.01 * labelFrame4Width, y = 0.05 * labelFrame4Height)
    #---#adicionar
    btnLerAdicionar = Button(labelFrame4, text = "Adicionar", compound=LEFT, relief = "sunken", 
                    width = 43, height = 3, font=("Arial", 12),command = lambda: adicionar(txtPrimeiroNomeVar.get(),txtUltimoNomeVar.get(),selected.get(),treePanel))
    btnLerAdicionar.place(x = 0.01 * labelFrame4Width, y = 0.42 * labelFrame4Height)
    #---#remover
    btnRemover = Button(labelFrame4, text = "Remover", compound=LEFT, relief = "sunken", 
                    width = 43, height = 3, font=("Arial", 12), command = lambda: removerUser(treePanel))
    btnRemover.place(x = 0.01 * labelFrame4Width, y = 0.79 * labelFrame4Height)
    #---#contar contas
    btnContar = Button(labelFrame4, text = "Contagem", compound=LEFT, relief = "sunken", 
                    width = 43, height = 3, font=("Arial", 12), command = contar)
    btnContar.place(x = 0.01 * labelFrame4Width, y = 1.16 * labelFrame4Height)
    
"""----------------------------------------------------------------------------------------
                                      Funções do Sistema                                   """

#função adicionar ao txt e treeview
def adicionar(PrimeiroNome, UltimoNome, Tipo,treeView):
    os.system("cls")
    #print(PrimeiroNome)
    #print(UltimoNome)
    numsUsers = lerFicheiroId()
    #print(numsUsers)
    idUser = numsUsers + 1
    idUser = str(idUser)
    #print(idUser)
    while PrimeiroNome != "" and UltimoNome != "":
        print("Dentro do ciclo")
        f = open(ficheiroPrograma_1, "a", encoding="utf-8")
        data = idUser + ";" + PrimeiroNome + ";" + UltimoNome + ";" + Tipo + "\n"
        f.write(data)
        f.close()
        carregarAtualizarTreeView(treeView)
        break
    if PrimeiroNome == "" or UltimoNome == "":
        messagebox.showinfo(title = "Dados invalidos", message = "Primeiro Nome invalidou ou vazio")

#função ler ficheiro, permite ler o ficheiro sem que seja necessario repeitir codigo no restante do sistema
def lerFicheiro():
    f = open(ficheiroPrograma_1, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    #print(linhas)
    return linhas

#função para definir um inteiro indice para cada inscrição
def lerFicheiroId():
    f = open(ficheiroPrograma_1, "r", encoding="utf-8")
    linhas = f.readlines()
    num = len(linhas)
    #print(num)
    return num

#função para carregar e atualziar a treeView
def carregarAtualizarTreeView(treeView):
    linhas = lerFicheiro()
    treeView.delete(*treeView.get_children())
    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        linha[1] = linha[1] + " " + linha[2]
        treeView.insert("", END, values = (linha[1], linha[3]))

#função para capturar index do elemento selecionado na treeView
def indexCapture(treeView):
    idSelecionado = treeView.focus()

    item_id = treeView.index(idSelecionado)
    item_id = item_id +1
    print(item_id)
    return item_id

#Função para remover elementos da treeView e atualizar a mesma
def removerUser(treeView):
    os.system("cls")
    print("remover")
    linhas = lerFicheiro()
    #print(linhas)
    index = indexCapture(treeView)
    #print(index)
    #---#
    idUser = 1
    ptr = 1
    acessos = open(ficheiroPrograma_1, "w", encoding="utf8")
    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        #print(ptr)
        if ptr != index:
            #print("funciona")
            data = str(idUser) + ";" + linha[1] + ";" + linha[2] + ";" + linha[3] + "\n"
            acessos.write(data)
            idUser+=1
        ptr+=1
    acessos.close()
    treeView.delete(*treeView.get_children())
    carregarAtualizarTreeView(treeView)

#Função permite contar quantos são os usuarios por tipos
def contar():
    linhas = lerFicheiro()
    Docente = 0
    Estudante = 0
    Externo = 0
    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        if linha[3] == "Docente":
            Docente+=1
        elif linha[3] == "Estudante":
            Estudante+=1
        elif linha[3] == "Externo":
            Externo+=1
    data = "A plataforma possui: " + str(Docente) + " " + "docentes" + "," + " " + str(Estudante) + " " + "estudantes" + "," + " " + str(Externo) + " " + "externos"
    messagebox.showinfo(title = "Numero de inscrições", message = data)



"""----------------------------------------------------------------------------------------"""
"""                                    Interface grafica                                   """
window = Tk()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1366                          # tamanho (pixeis) da window a criar
appHeight = 768
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.resizable(0,0)
window.title("Revisão Tkinter")
#-----------------------------------------------------------------------------------------------------------------------------#
menubar = Menu(window)
#-----------------------------------------------------------------------------------------------------------------------------#
navegacao = Menu(menubar, tearoff=0)

menubar.add_cascade(label = "Telas", menu = navegacao)
navegacao.add_command(label="Tela Inicial", command = TelaInicial)
navegacao.add_command(label="Programa 1")
navegacao.add_command(label="Tela 3")
navegacao.add_command(label="Tela 4")
navegacao.add_command(label="Teste")
#---#
menubar.add_command(label="CLS", command = lambda: os.system("cls"))
menubar.add_command(label="Exit", command = window.destroy)
window.config(menu =  menubar)
#-----------------------------------------------------------------------------------------------------------------------------#
panned1Width = 0.25 * appWidth
panned1Height = appHeight
panned1 = PanedWindow(window, bg = "black",width = panned1Width, height = appHeight)
panned1.place(x=0 , y=0)
#-----------------------------------------------------------------------------------------------------------------------------#
btnOpcao1 = Button(panned1, text = "Programa 1", compound=LEFT, relief = "sunken", 
                    width = 10, height = 3, font="calibri, 11",
                    command = tela1)
btnOpcao1.place (x = 0.025 * panned1Width, y = 0.01 * panned1Height)
#-----------------------------------------------------------------------------------------------------------------------------#
btnOpcao2 = Button(panned1, text = "BTN2", compound=LEFT, relief = "sunken", 
                    width = 10, height = 3, font="calibri, 11",
                    command=None)
btnOpcao2.place (x = 0.35 * panned1Width, y = 0.01 * panned1Height)
#-----------------------------------------------------------------------------------------------------------------------------#
btnOpcao3 = Button(panned1, text = "BTN3", compound=LEFT, relief = "sunken", 
                    width = 10, height = 3, font="calibri, 11",
                    command=None)
btnOpcao3.place (x = 0.675 * panned1Width, y = 0.01 * panned1Height)
#-----------------------------------------------------------------------------------------------------------------------------#
btnOpcao4 = Button(panned1, text = "BTN4", compound=LEFT, relief = "sunken", 
                    width = 10, height = 3, font="calibri, 11",
                    command=None)
btnOpcao4.place (x = 0.025 * panned1Width, y = 0.105 * panned1Height)
#-----------------------------------------------------------------------------------------------------------------------------#
btnOpcao5 = Button(panned1, text = "BTN5", compound=LEFT, relief = "sunken", 
                    width = 10, height = 3, font="calibri, 11",
                    command=None)
btnOpcao5.place (x = 0.35 * panned1Width, y = 0.105 * panned1Height)
#-----------------------------------------------------------------------------------------------------------------------------#
btnOpcao6 = Button(panned1, text = "BTN6", compound=LEFT, relief = "sunken", 
                    width = 10, height = 3, font="calibri, 11",
                    command=None)
btnOpcao6.place (x = 0.675 * panned1Width, y = 0.105 * panned1Height)

TelaInicial()

window.mainloop()
