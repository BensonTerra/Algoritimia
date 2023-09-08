# Biblioteca Tkinter: UI
import math
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
from tkinter import messagebox   #  messagebox

ficheiroTrails = "40220440/EX3/ficheiros/trails.txt"
ficheiroUltraTrails = "40220440/EX3/ficheiros/ultratrails.txt"
favoritos = "40220440/EX3/ficheiros/favoritos.txt"
ficheiros = []
ficheiros.append(ficheiroTrails)
ficheiros.append(ficheiroUltraTrails)
ficheiros.append(favoritos)

def loadList(check1, check2,tree):
    print(check1.get())
    if check1.get() == 1 and check2.get() == 0:
        tree.delete(*tree.get_children())
        f = open(ficheiros[0], "r", encoding="utf-8")
        linhas = f.readlines()
        f.close()
        loadTree(linhas,tree)
    elif check1 == 0 and check2.get() == 1:
        tree.delete(*tree.get_children())
        f = open(ficheiros[1], "r", encoding="utf-8")
        linhas = f.readlines()
        f.close()
        loadTree(linhas,tree)
    elif check1.get() == 1 and check2.get() == 1:
        tree.delete(*tree.get_children())
        for i in range(len(ficheiros)):
            f = open(ficheiros[i], "r", encoding="utf-8")
            linhas = f.readlines()
            f.close()
            loadTree(linhas,tree)
    else:
        tree.delete(*tree.get_children())
    numProvas.set(str(len(tree.get_children())))

def loadTree(lista,tree):
    print(lista)
    for prova in lista:
        tree.insert("", "end", values = (prova.split(";")[0],prova.split(";")[1], prova.split(";")[2] ))

def selecionarImagem():
    global imagem
    fileName = filedialog.askopenfilename(  title="Selecionar imagem",initialdir="40220440/EX3/imagens",
                                            filetypes=(("png files","*.png"),("gif files","*.gif"),("all files","*.*")))
    print(fileName)
    imagem = PhotoImage(file = fileName)
    canvas.itemconfig(image_id,image=imagem)

def addFavorito(tree,lbox):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values'][0]
        print(record)
        lbox.insert("end",record)

def removeFavorito(lbox):
    for i in lbox.curselection():
        index = i
        print(index)
    lbox.delete(lbox.curselection())

def guardarFavorito(lbox):
    print(lbox.get())

# ---------------Main---------------------
#-----------------------------------------

window=Tk()   # invoca classe tk , cria a "main window"
window.geometry("1000x500")
window.title('Trails App')

choice1 = IntVar()
choice1.set(1)
choice2 = IntVar()

# CheckButton  Trail Curto / Ultra Trail
ck1 = Checkbutton(window, text = "Trail Curto", variable = choice1,)
ck2 = Checkbutton(window, text = "Ultra Trail ", variable = choice2)
ck1.place(x=50, y=20)
ck2.place(x=150, y=20)

# Button Pesquisar na Treeview

imagePesq = PhotoImage(file = "40220440\\EX3\\imagens\\pesquisar.png")
btnSearch = Button(window, width=35, height=35, image = imagePesq ,  relief = "flat", bd=3
                   , command = lambda: loadList(choice1, choice2,tree))
btnSearch.place(x=300, y=12)

# TreeView
tree = ttk.Treeview(window, columns = ("Prova", "Data", "Local"), show = "headings", height = 12, selectmode = "browse")
tree.column("Prova", width = 220, anchor = "w")
tree.column("Data", width = 100, anchor = "c")
tree.column("Local", width = 220, anchor = "c")

tree.heading("Prova", text = "Prova")
tree.heading("Data", text = "Data")
tree.heading("Local", text = "Local")
tree.place(x=20, y=70)

# Nº de provas
lbNumProvas = Label(window, text = "Nº de provas", font = ("Helvetica", "10"))
lbNumProvas.place(x=50, y=350)

numProvas = StringVar()
txt_num_provas = Entry(window, width=10, textvariable = numProvas)
txt_num_provas.place(x=150, y=350)

# Buttons para adicionar e remover da lista de favoritos
btnAddFav = Button(window, text = "Adicionar Favoritos", height=3, command = lambda: addFavorito(tree,lboxFav))
btnAddFav.place(x=570, y=120)

btnRemFav = Button(window, text = "Remover  Favoritos", height=3, command = lambda: removeFavorito(lboxFav))
btnRemFav.place(x=570, y=180)

# PAINEL de lista de favoritros
panel1 = PanedWindow(window, width = 300, height = 500, bd = "3", relief = "sunken" )
panel1.place(x=700, y=1)

lbl1= Label(panel1, text = "Favoritos", font = ("Helvetica", "11") )
lbl1.place(x=100, y=30)

lboxFav = Listbox(panel1, width=40, height=15)
lboxFav.place(x=20, y=50)


btnGuardar = Button(panel1, text = "Guardar Favoritos", height=3, width=35, command= lambda: guardarFavorito(lboxFav))
btnGuardar.place(x=20, y=320)


# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
canvas = Canvas(window, width = 300, height = 130, bd = 4, relief = "sunken")
canvas.place(x=250, y=350)

imagem = PhotoImage(file = "40220440/EX3/imagens/img1.png")
image_id = canvas.create_image(175, 100, image=imagem)

# Button para selecionar imagem do disco
btn_selecionar_img = Button(window, width=18, height = 2, text = "Selecionar Imagem", relief = "raised", bd=1, command = selecionarImagem)
btn_selecionar_img.place(x=100, y=420)

window.mainloop()   # event listening loop by calling the mainloop()