"""
Este programa cria uma matriz (lista de listas) com base no número de linhas e colunas especificadas.
Em seguida, ele inverte a matriz transpondo suas linhas e colunas e a exibe em formato de tabela.
"""
#---------------------------------------------------------------#
def cria_lista(nlin,ncol):
    lista = []
    for x in range (nlin):
        lista.append([])
        for y in range (ncol):
            pos = int(input("linha %i|Coluna: %i: "%(x+1,y+1)))
            lista[x].append(pos)
    return lista
#---------------------------------------------------------------#
def invert(lista):
    print("%i"%(len(lista)))
    print("Lista original em modo tabela:")
    for x in range (len(lista)):
        for y in range (len(lista)):
            print(lista[x][y], end= " ")#lista[x][y]
        print()
    #---------------------------------------#
    print("")
    #---------------------------------------#
    print("Lista transposta em modo tabela:")
    for x in range (len(lista)):
        for y in range (len(lista)):
            print(lista[y][x], end= " ")#lista[y][x]
        print()

import os #biblioteca os
autoStart="y"
#---------------------------------------------------------------#
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    try:
        lista = cria_lista(3,3)
        print(lista)
        invert(lista)

    except ValueError:
        print("Digite novamente")
    else:
        autoStart = input("\nRepetir(Y/N) ?: ")