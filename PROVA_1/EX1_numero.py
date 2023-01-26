"""
docstring
"""
tabuleiro =[["0","0","0"],["0","0","0"],["0","0","0"]]
import os #biblioteca os
import random #biblioteca random
#---------------------GERADOR DE MATRIZES-----------------#
def cria_Matriz(num):
    lista = []
    for x in range (num):
        lista.append([])
        for y in range (num):
            pos = random.randint(1,30)
            lista[x].append(pos)
    print("")
    #print(lista)
    input()
    return lista

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
            jogo(tabuleiro)
            print("teste")
    
def jogo(lista):
    for x in range (len(lista)):
        for y in range (len(lista)):
            print(lista[x][y], end= " ")
        print()

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    tabuleiroReal = cria_Matriz(3)
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim