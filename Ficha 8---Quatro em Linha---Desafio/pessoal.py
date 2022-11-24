import random
import os #biblioteca os

colunasLetras = ["A","B","C","D","E","F","G","H"]

campoJogo = [["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""]]

colunas = 7
linha = 6

def iniciarJogo():
    op=""
    while op !="0":
        os.system("cls")
        print("\n\t\t\tOla, Bem vindo ao 4 em linha")
        print("\t\t\tEscolha um dos modos de jogo:\n")
        print("\t\t1 -  1 jogador")
        print("\t\t2 -  2 jogadores")
        #-------------------------------------------------#
        print("\t\t3 -  ranking", end=" ")
        print("\t\t| Work in Progress")
        print("\t\t4 -  razão de vitorias", end=" ")
        print("\t| Work in Progress")
        #-------------------------------------------------#
        print("\t\t0 - Sair\n")
        op = input("\t\t    Opção: ")

autoStart="y"
while autoStart == "Y" or autoStart == "y":
    os.system("cls")#Limpar tela
    iniciarJogo()
        
    autoStart = input("Repetir(Y/N) ?: ")


    