    id = 1
    ptr = 1
    f = open(ficheiro, "w", encoding="utf8")
    print(treeView.selection())
    for i in treeView.selection()[0]:
        index = 0
        index = i
        print(index)
    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        #print(linha)
        if linha[0] != index:
            data = str(id) + ";" + linha[1] + ";" + linha[2] + ";" + linha[3] + "\n"
            f.write(data)
            id+=1
        else:
            f.write("")
        ptr+=1
    f.close()
    treeView.delete(*treeView.get_children())
    carregarAtualizarTreeView(treeView)