"""
Gerar uma lista com 10 numeros aleatorios não repetido e o usuario de ve advinhar os mesmos
"""

import os #biblioteca os
import random #biblioteca random
import time #biblioteca time

lista = []

#criaçao da lista de 10 numeros a ser aadvinhados
def primeroCiclo():
    global lista
    lista = []
    for i in range(10):
        num = random.randint(1, 20)
        if num in lista:
            num = random.randint(1, 20)
        lista.append(num)
    #print(lista)
primeroCiclo()

#sistema do jogo
def jogo():
    i=0
    global lista
    while i < 11:
        os.system("cls")
        num = 0
        while int(num) != lista[i]:
            os.system("cls")
            print(lista[i])
            num = int(input("digite um numero de 1 a 20 para advinhar: "))
            #num = lista[i]
            if int(num) == lista[i]:
                print("Acertou, o número indicado existe na lista na posição %i"%(i+1))
                i+=1
                input()
            else:
                print("O número indicado não existe")
                input()
            print(i)
            #time.sleep(2)
            if i == 10:
                print("GAME OVER!")
                input()
                break
        break

    input()
    
#menu do jogo    
def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 --- jogar")
        print("\t\t0 --- Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            print("teste 1")
            jogo()

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim