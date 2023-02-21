#Mostrar dados do elementos selecionado de uma treeView via event
    def item_selected_TREEVIEW(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
        tree.bind('<<TreeviewSelect>>', item_selected)





"""----------------------------------------------------------------------------------------"""
"""                                                                                        """
"""                                       Lista Codigos                                    """
"""                                                                                        """
"""----------------------------------------------------------------------------------------"""

#metodo complexo de remover e reescrecer elementos de uma lista com base em ficheiro
    def delete_elementSelected_rewriteFile(lista):
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

#metodo simples de remover elemento de lista selecionado
    def removerTarefa():
        pos = lbLista.curselection()
        print(pos)
        lbLista.delete(pos)

#Função Clear/ Limpar a lista
    def clearLista():
        lbLista.delete(0,END)

#Mostrar dados do elementos selecionado de uma Lista via event
    def item_selected_LISTBOX(event):
        """Zona basica para captura de dados para print e uso futuro"""
        index = lb.curselection()
        selected_item = lb.get(index)
        """"""
        print(selected_item)
        lb.bind("<<ListboxSelect>>", item_selected)