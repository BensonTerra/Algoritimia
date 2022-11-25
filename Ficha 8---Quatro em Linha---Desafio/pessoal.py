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
#vitorias = 0

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
    print("\n     0    1    2    3    4    5    6  ", end="")
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(linha):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(colunas):
            if(tabuleiro[x][y] == "1"):
                print("",tabuleiro[x][y], end=" |")
            elif(tabuleiro[x][y] == "2"):
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
            posiçao[1] = 0 #coluna 0/1
        elif string.upper()[0] == "B":
            posiçao[1] = 1 #coluna 1/2
        elif string.upper()[0] == "C":
            posiçao[1] = 2 #coluna 2/3
        elif string.upper()[0] == "D":
            posiçao[1] = 3 #coluna 3/4
        elif string.upper()[0] == "E":
            posiçao[1] = 4 #coluna 4/5
        elif string.upper()[0] == "F":
            posiçao[1] = 5 #coluna 5/6
        elif string.upper()[0] == "G":
            posiçao[1] = 6 #coluna 6/7
        posiçao[0] = 0 #linha 0
        return posiçao
    else:
        print("Letra invalida. Insira novamente")
        input()
        os.system("cls")
        mostrarTabuleiro()

def gravidade(cordenada):
    #calcula a casa abaixo da coluna escolhida linha[0]coluna[x]
    casaInferior = [None,None]
    casaInferior[0] = cordenada[0] + 1
    casaInferior[1] = cordenada[1]
    print(cordenada)
    #verifica se na posição abaixo possui algo(" ","1" ou "2")
    espaçoDisponivel(cordenada)

def espaçoDisponivel(cordenada):
    #while(tabuleiro[0][1] == ""):
    """
    if(tabuleiro[0][1] == ""):
        cordenada[0] += 1
        print(cordenada)
    """

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
                #print(cordenada)
                #verificar se o espaço esta ocupado ou ha algo abaixo
                gravidade(cordenada)

    
        
    autoStart = input("Repetir(Y/N) ?: ")


    