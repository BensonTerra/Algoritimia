"""
docstring
"""
import os #biblioteca os
import random #biblioteca random

tabuleiro =[["0","0","0"],
            ["0","0","0"],
            ["0","0","0"]]
pos = random.randint(1,30)

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
            print("teste")
    
def mostrarTabela(lista):
    os.system("cls")
    print("\n\t\t      Tabela\n")
    for x in range (3):
        print("\t", end="")
        for y in range (1):
            print("\t%s\t%s\t%s"%(lista[x][y],lista[x][y+1],lista[x][y+2]))
        print()
    input()

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim