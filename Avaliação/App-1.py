#Benson Leme Terra 40220440
'''
Implemente um programa em Python que leia um texto e em seguida chame a função removeDuplicates.

Esta função recebe o texto como argumento de entrada e deve devolver: o referido texto, mas sem palavras repetidas
Assim como o nº de palavras (diferentes) repetidas que foram removidas.
'''

def removeDuplicates(texto):
    #texto = " " + texto + " "
    resposta = ""
    lista = []
    lista = texto.split()
    #print(lista)
    for i in range(len(lista)):
        word = lista[i]
        #print(word)
        rep = lista.count(word)
        #print(rep)
        #print("palavra: %s | vezes: %s "%(word,rep))
        if rep > 1:
            pos_1 = lista.index()
    

                        
    




import os #biblioteca os
autoStart="y"
texto ="este é um texto do teste de AED texto de AED"

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        #texto = input("Texto: ")
        removeDuplicates(texto)

    except ValueError:
        print("Valor inválido")
    except:
        print("Erro desconhecido")
    else:
        autoStart = input("Repetir(Y/N) ?: ")
    
    