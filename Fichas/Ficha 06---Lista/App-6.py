"""
Elabore um programa que leia uma lista de 10 números inteiros. 
Em seguida, dado um determinado valor de pesquisa, invoque a função searchNumber(lista, pesquisa) que deve devolver as posições em que encontra o valor de pesquisa, 
na lista. 
Caso o valor de pesquisa não exista na lista, deve surgir uma mensagem adequada.
"""
import os #biblioteca os
autoStart="y"

def searchNumber(lista, pesquisa):
    positions = ""

    numCiclos = lista.count(pesquisa)     # nº de ocorrencias
    #print("Numeros de ocorrencias: %i"%numCiclos)

    if(numCiclos == 0):
        print("O numero que pediu não consta na lista: %i"%numCiclos)
    else:
        num = 0
        posNum = 0
        for i in range(numCiclos):
            posNum = lista.index(pesquisa, posNum+num)
            if lista[posNum] == pesquisa:
                #print("posição na lista(sistema): %i"%posNum)
                positions = positions + str(posNum+1) + "ª" + "|"
                num+=1
        return positions

#lista= [1,2,3,4,5,6,7,8,5,10]
posição = [1,2,3,4,5,6,7,8,9,10]

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    try:
        lista= []
        for i in range(10):
            num=int(input("O numero para a posição %i: "%posição[i])) #Input para introduzir um numero
            #print(num)
            lista.append(num)
        print(lista)
        pesquisa = int(input("Introduza o numero a ser procurado: "))
        resposta = searchNumber(lista, pesquisa)
        print("Lista: %s" %lista)
        print("Locais onde %i se encontra: %s posição"%(pesquisa,resposta))


    except ValueError:
        print("Digite novamente")
    else:
        autoStart = input("Repetir(Y/N) ?: ")