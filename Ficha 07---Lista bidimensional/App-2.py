"""
docstring
"""
#---------------------GERADOR DE MATRIZES-----------------#
def cria_Matriz(num):
    lista = []
    for x in range (num):
        lista.append([])
        for y in range (num):
            pos = random.randint(10,100)
            lista[x].append(pos)
    print("")
    print(lista)
    input()
    return lista
#--------------------MATRIZ TRANSPOSTA--------------------#
def invert(lista):
    #print("%i"%(len(lista)))
    print("Lista original em modo tabela:")
    for x in range (len(lista)):
        for y in range (len(lista)):
            print(lista[x][y], end= " ")
        print()
    #---------------------------------------#
    print("")
    #---------------------------------------#
    print("Lista transposta em modo tabela:")
    for x in range (len(lista)):
        for y in range (len(lista)):
            print(lista[y][x], end= " ")
        print()
    input()
#-------------------------MAIOR---------------------------#
def maior(lista):
    listaMaior = []
    for x in range (len(lista)):
        for y in range (len(lista)):
            num = lista[x][y]
            listaMaior.append(num)
    #print(lista)
    print("O maior elemento da matriz é: %i"%max(listaMaior))
    input()
#---------------------------------------------------------#        

import os #biblioteca os
import random #biblioteca random
op="1"

lista = []

while op != '0':
    os.system('cls')                # clear screen
    print("\n\t\t\tMENU\n")
    print("\t\t1 - Inicializar matriz")
    print("\t\t2 - Matriz transposta")
    print("\t\t3 - Maior")
    print("\t\t4 - todas as anteriores")#pessoal
    print("\t\t0 - Sair")
    op = input("\t\t\n    Opção: ")
    print("")
    if op == '1':
        num = int(input("Dimensão da Matriz: "))
        lista = cria_Matriz(num)
    elif op == '2':
        listaTrasnspota = invert(lista)
    elif op == '3':
        maior(lista)
    elif op == '4':
        listaTrasnspota = invert(lista)
        maior(lista)
