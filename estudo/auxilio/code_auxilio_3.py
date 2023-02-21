# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x250")

# Create a Listbox widget
lb=Listbox(win, width=100, height=5, font=('TkMenuFont, 20'),justify= CENTER)
lb.pack()

# Once the list item is deleted, we can insert a new item in the listbox
def removerElemento(lista):
    for i in lista.curselection():
        index = i
        print(index)
    lista.delete(lista.curselection())

# Add items in the Listbox
lb.insert("end","item1","item2","item3","item4","item5")

# Add a Button to Edit and Delete the Listbox Item
ttk.Button(win, text="Delete", command = lambda: removerElemento(lb)).pack()

win.mainloop()