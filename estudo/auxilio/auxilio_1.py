""" Mostrar dados do elementos selecionado de uma tree
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))
"""

#Remoção de itens de uma lista

#metodo complexo de remover elemento de lista com base em ficheiro
    ptr = 0
    acessos = open(ficheiro, "w", encoding="utf8")
    for i in lista.curselection():
        index = i
        print(index)
    for linha in linhas:
        print(linha)
        print(index)
        if ptr != index:
            print("funciona")
            acessos.write(linha)
        ptr += 1
    acessos.close()


#metodo simples de remover elemento de lista
def removerTarefa():
    pos = lbLista.curselection()
    print(pos)
    lbLista.delete(pos)


#Limpar lista

#Função Clear a lista Inicio
def clearLista():
    lbLista.delete(0,END)