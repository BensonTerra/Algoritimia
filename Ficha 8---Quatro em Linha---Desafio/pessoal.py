import os #biblioteca os

colunasLetras = ["A","B","C","D","E","F","G"]

tabuleiro = [["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""],
             ["","","","","","",""]]

linha = 6
colunas = 7

def iniciarJogo():
    global modo
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
        if op == "1":
            modo = 1
            return modo
        elif op == "2":
            modo = 2
            return modo

def mostrarTabuleiro():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(linha):
        print("\n   +----+----+----+----+----+----+----+")
        print(x+1, " |", end="")
        for y in range(colunas):
            if(tabuleiro[x][y] == "🔵"):
                print("",tabuleiro[x][y], end=" |")
            elif(tabuleiro[x][y] == "🔴"):
                print("", tabuleiro[x][y], end=" |")
            else:
                print(" ", tabuleiro[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")
    input()

def colunaLetraParaNumero(string):
    global colunasLetras
    posiçao = [None,None]#Referencia ao tabuleiro [LINHA,COLUNA]
    if(string.upper()[0] in colunasLetras):
        if string.upper()[0] == "A":
            posiçao[1] = 0 #coluna 0
        elif string.upper()[0] == "B":
            posiçao[1] = 1 #coluna 1
        elif string.upper()[0] == "C":
            posiçao[1] = 2 #coluna 2
        elif string.upper()[0] == "D":
            posiçao[1] = 3 #coluna 3
        elif string.upper()[0] == "E":
            posiçao[1] = 4 #coluna 4
        elif string.upper()[0] == "F":
            posiçao[1] = 5 #coluna 5
        elif string.upper()[0] == "G":
            posiçao[1] = 6 #coluna 6
        posiçao[0] = int(string[1])
        return posiçao

    else:
        print("Letra invalida. Insira novamente")
        input()
        os.system("cls")
        mostrarTabuleiro()

def posicaoDisponivel()

turnoPlayer = 0
modo = 0
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")#Limpar tela
    iniciarJogo()
    if(modo == 1):
        turnoPlayer = 1
        if(turnoPlayer == 1):
            mostrarTabuleiro()
            while True:
                espaçoSelecionado = input("\nSelecione uma casa para por a ficha: ")
                #print(espaçoSelecionado)
                cordenada = colunaLetraParaNumero(espaçoSelecionado)
                #verificar se o espaço esta ocupado ou ha algo abaixo

    
        
    autoStart = input("Repetir(Y/N) ?: ")


    