import os #biblioteca os

colunasLetras = ["A","B","C","D","E","F","G",]

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
    posiçao = [None,None]#Referencia ao tabyuleiro [LINHA,COLUNA]
    if string.upper()[0] == "A":
        posiçao[1] = 0
    elif string.upper()[0] == "B":
        posiçao[1] = 1
    elif string.upper()[0] == "C":
        posiçao[1] = 2
    elif string.upper()[0] == "D":
        posiçao[1] = 3
    elif string.upper()[0] == "E":
        posiçao[1] = 4
    elif string.upper()[0] == "F":
        posiçao[1] = 5
    elif string.upper()[0] == "G":
        posiçao[1] = 6
    else:
        print("Letra invalida. Insira novamente")
        input()
    posiçao[0] = int(string[1])
    return posiçao


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
                print(espaçoSelecionado)
                cordenada = (espaçoSelecionado)

    
        
    autoStart = input("Repetir(Y/N) ?: ")


    