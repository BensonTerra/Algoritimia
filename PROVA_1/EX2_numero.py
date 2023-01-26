# numero: 40220440
# Benson Leme Terra

"""
docstring
"""
import os #biblioteca os
import random #biblioteca random
#Variaveis globais
pasta = "files"
ficheiro = "files/atividades.txt"


if not os.path.exists(pasta):
    os.mkdir(pasta)

def menuPrincipal():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  Consultar atividades")
        print("\t\t2 -  Melhores tempos")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            menuSecundario()
            print("teste")
            input()
        elif op == '2':
            menuTerciario()

def menuSecundario():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  5k")
        print("\t\t2 -  10k")
        print("\t\t2 -  21k")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            consultarAtividades("5k")
            input()
        elif op == '2':
            consultarAtividades("10k")
            input()
        elif op == '3':
            consultarAtividades("21k")
            input()

def menuTerciario():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  5k")
        print("\t\t2 -  10k")
        print("\t\t2 -  21k")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            melhorTempo("5k")
            input()
        elif op == '2':

            input()
        elif op == '3':

            input()

def consultarAtividades(dist):
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    tabela()
    for linha in linhas:
        distancia = linha.split(";")[1]
        if dist == distancia:
            data = linha.split(";")[0]
            tempo = linha.split(";")[2]
            print("\t%s                 %s"%(data,tempo))
        elif dist == distancia:
            data = linha.split(";")[0]
            tempo = int(linha.split(";")[2])
            print("\t%s                 %s"%(data,tempo))
        elif dist == distancia:
            data = linha.split(";")[0]
            tempo = linha.split(";")[2]
            print("\t%s                 %s"%(data,tempo))
    input()

def melhorTempo(dist):
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    tabela()
    lista = []
    final = [[]]
    for linha in linhas:
        distancia = linha.split(";")[1]
        if dist == distancia:
            data = linha.split(";")[0]
            tempo = linha.split(";")[2]
            dados = data +";"+tempo
            lista.append(dados)

def tabela():
    print("\t\t Data              Tempo Registrado")
    print("---------------------------------------")

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menuPrincipal()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim