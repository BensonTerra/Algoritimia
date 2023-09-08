"""
docstring
"""
import os #biblioteca os
import random #biblioteca random

tabuleiro =[[0,0,0],
            [0,0,0],
            [0,0,0]]
posRes = random.randint(1,30)
colunaOptions = ["A","B","C"]
linhaOptions = ["1","2","3"]

def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  jogar")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            mostrarTabela(tabuleiro)
            #fim()
            print("teste")
    
def mostrarTabela(lista):
    os.system("cls")
    print("\n\t\t\t      Tabela")
    print("\t\t\t|A|\t|B|\t|C|\n")
    for x in range (3):
        print("\t", end="")
        for y in range (1):
            print("\t%s\t|%s|\t|%s|\t|%s|"%(x+1,lista[x][y],lista[x][y+1],lista[x][y+2]))
        print()
    input()
    jogar()

def jogar():
    linha  = input("Selecione uma linha dentre 1, 2 ou 3: ")
    linhaIndex = linhaOptions.index(linha);print(linhaIndex)
    coluna = input("Selecione uma coluna dentre A,B ou C: ")
    colunaIndex = colunaOptions.index(coluna.upper());print(colunaIndex)
    posRes = random.randint(1,30);print(posRes)

    try:
        res = input("Selecione uma valor de 1 a 30: ")
    except ValueError:
        print("Caracter não aceito")

    if int(res) == posRes and tabuleiro[linhaIndex][colunaIndex] == 0:
        print("True")
        tabuleiro[linhaIndex][colunaIndex]=int(res)
    else:
        print("False")
    fim()
    input()

def fim():

    soma = 0
    for linha in tabuleiro:
        print(linha)
        soma = linha[0] + linha[1] + linha[2]
        if soma < 90:
            print("< 90")
        elif  soma == 90:
            print("= 90")
        else:
            print("> 90")

    soma = 0
    for x in range(1):
        print(tabuleiro[x])
        print(tabuleiro[x+1])
        print(tabuleiro[x+2])
        for y in range(3):
            soma = tabuleiro[x][y] + tabuleiro[x+1][y] + tabuleiro[x+2][y];print(soma)
            if soma < 90:
                print("< 90")
            elif  soma == 90:
                print("= 90")
            else:
                print("> 90")
    
    input()
    mostrarTabela(tabuleiro)

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim