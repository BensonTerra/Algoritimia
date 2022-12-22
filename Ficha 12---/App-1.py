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
#Bibloiotecas inportadads fim

#Variaveis globais inicio
pasta = "files"
ficheiro = "files/acessos.txt" #Numero;data_sistema;hora_sistema;tipo_acesso
#Variaveis globais fim

#Verfica a existencia da pasta inicio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim

#Tela dos movimentos Inicio
def movimentos():
    print("Teste MOVIMENTOS")
    movWindow = Toplevel()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    appWidth = 1000                             # tamanho (pixeis) da window a criar
    appHeight = 450
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    movWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    #movWindow.geometry("1000x450")
    movWindow.title("Entradas e Saídas")
    movWindow.focus_force()
    movWindow.grab_set()
    
    #-----------------------------------------------------------------------------------------------------------------------------#
    menubar = Menu(movWindow)
    #-----------------------------------------------------------------------------------------------------------------------------#
    filemenu = Menu(menubar, tearoff=0)
    
    #menubar.add_cascade(label="File", menu=filemenu)
    #menubar.add_command(label="Debug", menu=filemenu)

    filemenu.add_command(label="Movimentos", command=movimentos, state="disabled")
    filemenu.add_command(label="Consultas", command=consultar)
    filemenu.add_command(label="CLS", command= lambda: os.system("cls"))
    filemenu.add_command(label="Exit", command=movWindow.quit)
    movWindow.config(menu=filemenu)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame0 = LabelFrame(movWindow,width = 990, height = 440)
    frame0.place(x=5 , y=5)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame1 = LabelFrame(frame0,width = 660, height = 425)
    frame1.place(x=5 , y=5)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame2 = LabelFrame(frame0,width = 310, height = 425)
    frame2.place(x=670 , y=5)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame3 = LabelFrame(frame1,width = 150, height = 150, text = "Numero do estudante: ",fg ="blue")     
    frame3.place(x=5 , y=5)
#---#
    Numero = StringVar()
    Numero.set("001")
    entNumero =Entry(frame3, width = 15,justify=CENTER, textvariable=Numero)
    entNumero.place(x=24,y=50)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame4 = LabelFrame(frame1,width = 150, height = 150, text="Tipo de entrada", fg="blue")
    frame4.place(x=5, y=160)
#---#
    selected = StringVar()
    selected.set("Entrada")
    rd1 = Radiobutton(frame4, text = "Entrada", value = "Entrada", variable = selected)
    rd1.place(x = 1, y = 30)
    rd2 = Radiobutton(frame4, text = "Saida", value = "Saida", variable = selected)
    rd2.place(x = 1, y = 60)
    #-----------------------------------------------------------------------------------------------------------------------------#
    btnRegistrar = Button(frame1, width=23, height=1, text="Registrar",font=("arial",35),command= lambda: registrarMovimentos(selected.get(),Numero.get(),lbLista))
    btnRegistrar.place(x=14,y=320)
    #-----------------------------------------------------------------------------------------------------------------------------#
    lbLista = Listbox(frame2,width =49, height = 25, justify=CENTER)
    lbLista.place(x=5 , y=5)
#---#
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    #print(linhas)
    for linha in linhas:
        linha = linha.removesuffix("\n")
        lbLista.insert(END, linha)
    #-----------------------------------------------------------------------------------------------------------------------------#
def registrarMovimentos(selected, numero, Listbox):
    data = str(datetime.date.today())
    hora = str(datetime.datetime.now().time().strftime("%H:%M:%S"))
    linha = str(numero) + ";" + data + ";" + hora + ";" +selected + "\n"
    acessos = open(ficheiro, "a", encoding="utf8")
    acessos.write(linha)
    acessos.close()
    Listbox.insert(END,linha)
    #-----------------------------------------------------------------------------------------------------------------------------#
def limparLista(Lista):
    Lista.delete(0,END)
    #-----------------------------------------------------------------------------------------------------------------------------#
#Tela dos movimentos Fim

#Tela de consulta inicio
def consultar():
    print("Teste CONSULTAS")
    movWindow = Toplevel()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    appWidth = 1000                             # tamanho (pixeis) da window a criar
    appHeight = 450
    x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
    y = (screenHeight/2) - (appHeight/2)
    movWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    #movWindow.geometry("1000x450")
    movWindow.title("Consultas")
    movWindow.focus_force()
    movWindow.grab_set()

    #-----------------------------------------------------------------------------------------------------------------------------#
    menubar = Menu(movWindow)
    #-----------------------------------------------------------------------------------------------------------------------------#
    filemenu = Menu(menubar, tearoff=0)
    
    #menubar.add_cascade(label="File", menu=filemenu)
    #menubar.add_command(label="Debug", menu=filemenu)

    filemenu.add_command(label="Movimentos", command=movimentos)
    filemenu.add_command(label="Consultas", command=consultar, state="disabled")
    filemenu.add_command(label="CLS", command= lambda: os.system("cls"))
    filemenu.add_command(label="Exit", command=movWindow.quit)
    movWindow.config(menu=filemenu)

    #-----------------------------------------------------------------------------------------------------------------------------#
    frame0 = LabelFrame(movWindow,width = 990, height = 440)
    frame0.place(x=5 , y=5)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame1 = LabelFrame(frame0,width = 660, height = 425)
    frame1.place(x=5 , y=5)
    #-----------------------------------------------------------------------------------------------------------------------------#
    frame2 = LabelFrame(frame0,width = 310, height = 425)
    frame2.place(x=670 , y=5)
#---#
    frame3 = LabelFrame(frame2,width = 150, height = 150, text = "Numero do estudante: ",fg ="blue")     
    frame3.place(x=5 , y=5)
#---#
    Numero = StringVar()
    Numero.set("000")
    entNumero =Entry(frame3, width = 15,justify=CENTER, textvariable=Numero)
    entNumero.place(x=24,y=50)
#---#
    frame4 = LabelFrame(frame2,width = 150, height = 150, text="Tipo de entrada", fg="blue")
    frame4.place(x=5, y=160)
#---#
    cbEntrada = StringVar()
    cbSaida   = StringVar()
    rd1 = Checkbutton(frame4, text = "Entrada", variable = cbEntrada)
    rd1.place(x = 1, y = 30)
    rd2 = Checkbutton(frame4, text = "Saida", variable = cbSaida)
    rd2.place(x = 1, y = 60)
#---#
    btnConsultar = Button(frame2, width=10, height=1, text="Consultar",font=("arial",35))
    btnConsultar.place(x=12,y=320)
    #-----------------------------------------------------------------------------------------------------------------------------#
def consultarMovimentos(cbEntrada, cbSaida,numEstudante,tree):
    """
    
    """
    tree.delete(*tree.get_children())










#codigo principal inicio
window = Tk()
#Get the current screen width and height
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             # tamanho (pixeis) da window a criar
appHeight = 450
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
#window.geometry("1000x450")
window.title("Registro")
#-----------------------------------------------------------------------------------------------------------------------------#
menubar = Menu(window)
#-----------------------------------------------------------------------------------------------------------------------------#
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Movimentos", command=movimentos)
filemenu.add_command(label="Consultas", command=consultar)
filemenu.add_command(label="CLS", command= lambda: os.system("cls"))
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=filemenu)

"""
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
window.config(menu=menubar)
"""


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
"""

"""
window.mainloop()