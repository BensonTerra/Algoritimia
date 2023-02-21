"""----------------------------------------------------------------------------------------"""
"""                                                                                        """
"""                                       Codigos Genericos                                """
"""                                                                                        """
"""----------------------------------------------------------------------------------------"""

#Função ler ficheiro, permite ler o ficheiro sem que seja necessario repeitir codigo no restante do sistema
    def lerFicheiro():
        f = open(ficheiro, "r", encoding="utf-8")
        linhas = f.readlines()
        f.close()
        #print(linhas)
        return linhas

#Função para definir um identificador numerico, ou id, para cada dado a ser inserido
#ex : id + ";" + "dados do exercicio / resultado: 1;dados..."

    def lerFicheiroId():
        f = open(ficheiro, "r", encoding="utf-8")
        linhas = f.readlines()
        num = len(linhas)
        #print(num)
        return num


"""----------------------------------------------------------------------------------------"""
"""                                                                                        """
"""                                       Treeview Codigos                                 """
"""                                                                                        """
"""----------------------------------------------------------------------------------------"""

#Carregar treeView com dados de um file.txt
    def carregarAtualizarTreeView(treeView):
        linhas = lerFicheiro()
        treeView.delete(*treeView.get_children())
        for linha in linhas:
            linha = linha.replace("\n","")
            linha = linha.split(";")
            linha[1] = linha[1] + " " + linha[2]
            treeView.insert("", END, values = (linha[1], linha[3]))

#Função para deletar uma linha e reescrever o file.txt 
    def indexCapture_TREEVIEW(treeView):
        idSelecionado = treeView.focus()

        item_id = treeView.index(idSelecionado)
        item_id = item_id + 1
        print(item_id)
        return item_id

#Função para remover elementos da treeView e atualizar a mesma
    def removerUser(treeView):
        os.system("cls")
        print("remover")
        linhas = lerFicheiro()
        print(linhas)
        index = indexCapture_TREEVIEW(treeView)
        print(index)
        #---#
        idUser = 1
        ptr = 1
        acessos = open(ficheiro, "w", encoding="utf8")
        for linha in linhas:
            linha = linha.replace("\n","")
            linha = linha.split(";")
            print(ptr)
            if ptr != index:
                print("funciona")
                data = """ * * * """
                acessos.write(data)
                idUser+=1
            ptr+=1
        acessos.close()
        treeView.delete(*treeView.get_children())
        carregarAtualizarTreeView(treeView)




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