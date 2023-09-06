#Benson Leme Terra 40220440
'''
Implemente um programa em Python que leia um texto e em seguida chame a função removeDuplicates.

Esta função recebe o texto como argumento de entrada e deve devolver: o referido texto, mas sem palavras repetidas
Assim como o nº de palavras (diferentes) repetidas que foram removidas.
'''
#tentativa falha INICIO
"""
while numCiclos !=-0:
    word = lista[i]
    #print(word)
    rep = lista.count(word)
    #print(rep)
    pos1 = lista.index(word)
    #print(pos)
    print("Palavra: %s |repete %i vezes| indice: %i" % (word,rep,i))
    if rep > 1:
        pos2 = lista.index(word, pos1 + 1)
        print(pos2)
        del lista[pos2]
        print(lista)
        i += 1
    else:
        listaProvisoria.append(lista[i])
        resposta = resposta + listaProvisoria[i] + " "
        i += 1

return resposta
"""
#tentativa falha FIM

import os #biblioteca os
autoStart="y"

def removeDuplicates(texto):
    i=0
    lista = []
    listaProvisoria = []
    resposta = ""
    lista = texto.split(" ")
    print(lista)
    numCiclos = len(lista)

    for i in range (len(lista)):
        if lista[i] not in listaProvisoria:
            listaProvisoria.append(lista[i])
            #print(listaProvisoria)
            resposta = resposta + str(listaProvisoria[i]) + " "
        #else:
            #print("Palavra repetida: %s"%lista[i])
    #print(resposta)

    return resposta

texto ="este é um texto do teste de AED texto de AED"

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        #texto = input("Texto: ")
        resposta = removeDuplicates(texto)
        print(resposta)

    except ValueError:
        print("Valor inválido")
    except:
        print("Erro desconhecido")
    else:
        autoStart = input("Repetir(Y/N) ?: ")
    
    