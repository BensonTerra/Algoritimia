"""
Teste de uma plataforma de agenda via terminal usando pyhton, com possibilidade remoção de tarefas especifica do ficheiro .txt
"""
import os #biblioteca os

#Variaveis globais
pasta = "pastaEstudo"
ficheiro = "pastaEstudo/lista.txt"

#função ficheiroCiclo, cria a pasta e um arquivo .txt para primeira vez que é rodado
def primeiroCiclo():
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        f = open(ficheiro, "a", encoding="utf-8")
        initialComment = "Readme"
        f.write(initialComment)
        f.close()
primeiroCiclo()

#função ler ficheiro, permite ler o ficheiro sem que seja necessario repeitir codigo no restante do sistema
def lerFicheiro():
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    return linhas
lerFicheiro()

#função limpar, remove e reescrever ficheiro baseada na escolha linha a ser removida
def limparEscreverFicheiro(linhas,index):
    ptr = 0
    index = index - 1
    f = open(ficheiro, "w", encoding="utf-8")
    for linha in linhas:
        print(linha)
        if ptr != index:   #Permite apagar se pointer(ptr) for igual ao index indicado
            f.write(linha) #Apaga a linha 
        ptr += 1
    f.close()

#função adicionar
def adicionar():
    os.system("cls")
    nome = input("Insira seu nome: ")
    tarefa = input("Insira a descrição da tarefa: ")
    prioridade = input("Insira o nivel de prioridade(0 a 5): ")
    f = open(ficheiro, "a", encoding="utf-8")
    data = nome + ";" + tarefa +  ";" + prioridade + "\n"
    f.write(data)
    f.close()

#função remover
def remover():
    os.system("cls")
    linhas = lerFicheiro()
    i = 1
    print(30*"-")
    for linha in linhas:
        pos = str(i)
        linha = linha.replace("\n","")
        linha = linha.split(";")
        line = "    " + pos + " | " + linha[0] + " | " + linha[1] + " | " + linha[2]
        print(line)
        i = int(pos)
        i+=1
    index = int(input("\nNumero da tarefa a ser removida: "))
    limparEscreverFicheiro(linhas,index)
    os.system("cls")
    verFicheiro()

#função mostar, permite a construção de uma tabela simples sem que o mesmo necessite de repetição no corpo do programa
def mostrarTabela(linhas):
    i = 1
    print(30*"-")
    for linha in linhas:
        pos = str(i)
        line = "    " + pos + " | " + linha[0] + " | " + linha[1] + " | " + linha[2]
        print(line)
        i = int(pos)
        i+=1

#função filtrar
def filtrarTabela(nivelPrioridade):
    linhas = lerFicheiro()
    lista = []
    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        if linha[2] == nivelPrioridade and linha[2] != "":
            lista.append(linha)
        #print(lista)
    mostrarTabela(lista)
    """
    linhasOrdenada = []
    linhasOrdenada = sorted(lista, key = lambda x: x[2],reverse=True)
    print(linhasOrdenada)
    input()
    mostrar(linhasOrdenada)
    """
    input()

#função ver conteudo ficheiro
def verFicheiro():
    linhas = lerFicheiro()
    i = 1
    print(30*"-")
    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        pos = str(i)
        line = "    " + pos + " | " + linha[0] + " | " + linha[1] + " | " + linha[2]
        print(line)
        i = int(pos)
        i+=1
    input()

#função menuInicar
def menuIniciar():
    os.system("cls")
    op=" "
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 - Adicionar")
        print("\t\t2 - Remover")
        print("\t\t3 - Filtrar")
        print("\t\t4 - Ver ficheiro")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            print("\n")
            adicionar()
        elif op == '2':
            print("\n")
            remover()
        elif op == '3':
            print("\n")
            filtroOpcao = ["1","2","3","4","5"]
            nivel = input("\tFiltrar tarefas de 1 a 5, 0 para sair: ")
            if nivel in filtroOpcao:
                filtrarTabela(nivel)
            else:
                continue
        elif op == '4':
            print("\n")
            verFicheiro()


autoStart="y"
while autoStart.upper() == "Y":
    menuIniciar()
    autoStart = input("Repetir(Y/N) ?: ")