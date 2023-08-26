"""
Gerar uma lista com 10 numeros aleatorios não repetido e o usuario de ve advinhar os mesmos
"""

import os #biblioteca os
import random #biblioteca random

listaResposta = []
listaUsuario = ["*", "*", "*", "*", "*"]
nArrayMax = 5

#criaçao da lista de 10 numeros a ser aadvinhados
def primeroCiclo():
    global listaResposta
    numeros_possiveis = list(range(1, 21))
    listaResposta = random.sample(numeros_possiveis, nArrayMax);print(listaResposta.sort())
primeroCiclo()

#sistema do jogo
def jogo():
    i = 0
    global listaResposta
    global nArrayMax
    print(listaResposta)
    nArray = 0
    max_tentativas = 10

    while nArray < 5 and i < max_tentativas:
        limparTela()
        print(listaResposta)
        print(listaUsuario)
        print(i)

        try:
            num = int(input("Digite um número de 1 a 20 para adivinhar: "))
        except ValueError:
            print("Caracter não aceito")
            i += 1
            input()
            continue
        
        if num in listaResposta and num not in listaUsuario:
            index = listaResposta.index(num)
            listaUsuario[index] = num
            print("Você acertou! O número %i esta na posição %i"%(num,index+1))
            nArray += 1
        elif num in listaUsuario:
            print("Você já digitou esse número")
            i += 1
        else:
            print("O número indicado não existe")
            i += 1
        
        input()
    
    limparTela()
    if nArray == nArrayMax:
        print("\n\t\t\tPARABÉNS!!!\n")
        print("\t\t\tVocê venceu")
    else:
        print("\n\t\t\tGAME OVER!\n")
        print("\t\t\tVocê não conseguiu adivinhar todos os números a tempo")
    input()
    
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset():
    global listaUsuario
    listaUsuario = ["*", "*", "*", "*", "*"]

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
            reset()
            jogo()

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim