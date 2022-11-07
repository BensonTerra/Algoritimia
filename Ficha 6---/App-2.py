"""
Elabora uma função generateNumbers que permita gerar uma chave do Euromilhões 
de forma aleatória (5 números inteiros entre 1 e 50), assim como as estrelas (duas estrelas entre 1 e 12). 
"""
import os #biblioteca os
import random #biblioteca random
autoStart="y"

def generateNumber(limMin,limMax,numeros):
    lista = []
    for i in range(numeros):
        num=random.randint(limMin,limMax)
        if num in lista:
            num=random.randint(limMin,limMax)
        lista.append(num)
    lista.sort()
    #print(lista)
    return lista


        
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    numeros = []
    estrelas = []
    numeros = generateNumber(1,50,5)
    estrelas = generateNumber(1,12,2)

    print("\nChave euromilhões: %s\t Estrelas: %s\n"%(numeros,estrelas))

    autoStart = input("Repetir(Y/N) ?: ")
