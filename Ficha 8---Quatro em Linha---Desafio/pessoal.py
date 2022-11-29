import os #biblioteca os

colunasLetras = ["A","B","C","D","E","F","G"]

tabuleiro = [ ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""],
              ["","","","","","",""]]
#variaveis globais inicio
linha = 6
colunas = 7
vitoria = 0
#vitorias = 0
turnoPlayer = 1
#variaveis globais fim

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
                print("",tabuleiro[x][y], end="  |")
            elif(tabuleiro[x][y] == "2"):
                print("", tabuleiro[x][y], end="  |")
            else:
                print(" ", tabuleiro[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def colunaLetraParaNumero(string):
    global colunasLetras
    posiçao = [None,None]#Referencia ao tabuleiro [LINHA,COLUNA]
    if(string.upper() in colunasLetras):
        if string.upper() == "A":
            posiçao[1] = 0 #coluna 0/1
        elif string.upper() == "B":
            posiçao[1] = 1 #coluna 1/2
        elif string.upper() == "C":
            posiçao[1] = 2 #coluna 2/3
        elif string.upper() == "D":
            posiçao[1] = 3 #coluna 3/4
        elif string.upper() == "E":
            posiçao[1] = 4 #coluna 4/5
        elif string.upper() == "F":
            posiçao[1] = 5 #coluna 5/6
        elif string.upper() == "G":
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
    while colunaDisponivel(casaInferior) == True:
        cordenada[0] += 1
        if cordenada[0] == 5 and tabuleiro[cordenada[0]][cordenada[1]] == "": #quando a peça esta na ultima camada/linha do tabuleiro
            return cordenada
        elif tabuleiro[cordenada[0]][cordenada[1]] != "":
            cordenada[0] = cordenada[0] - 1
            cordenada[1] = cordenada[1]
            return cordenada
           
    while colunaDisponivel(casaInferior) == False:
        return cordenada   

def colunaDisponivel(cordenada):
    if(tabuleiro[cordenada[0]][cordenada[1]] == "1"):
        #input()
        #print("ocupado")
        return False
    elif(tabuleiro[cordenada[0]][cordenada[1]] == "2"):
        #input()
        #print("ocupado")
        return False
    else:
        #input()
        #print("livre")
        return True

def modificarTabuleiro(cordenada,ficha):
    tabuleiro[cordenada[0]][cordenada[1]] = ficha

def checarVitoria(ficha):
    win = 0
    #verifica na horizontal
    for y in range(linha):
        for x in range (colunas - 3):
            if tabuleiro[y][x] == ficha and tabuleiro[y][x+1] == ficha and tabuleiro[y][x+2] == ficha and tabuleiro[y][x+3] == ficha:
                print("Horizontal")
                input()
                win = 1
                return win
    #verifica na vertical
    for x in range(colunas):
        for y in range(linha-3):
            if tabuleiro[y][x] == ficha and tabuleiro[y+1][x] and tabuleiro[y+2][x] and tabuleiro[y+3][x] == ficha:
                print("Vertical")
                input()
                win = 1
                return win           
    return win #caso não cumpra nenhuma das condições anteriores

def PlayerX(ficha):
    global turnoPlayer
    global vitoria
    fichaX=ficha
    fim = 0
    mostrarTabuleiro()
    while True:
        mostrarTabuleiro()
        colunaSelecionada = input("\nSelecione uma coluna para por a ficha: ")
        #print(colunaSelecionada)
        while colunaSelecionada != "":
            cordenada = colunaLetraParaNumero(colunaSelecionada)
            #print(cordenada)
            #verificar se o coluna esta ocupado ou ha algo abaixo
            cordenadaFinal = gravidade(cordenada)
            #print(cordenadaFinal)
            if colunaDisponivel(cordenadaFinal) == True:
                modificarTabuleiro(cordenadaFinal,fichaX)
                #os.system("cls")
            mostrarTabuleiro()
            vitoria = checarVitoria(ficha)
            turnoPlayer+=1
            fim = 1
            break
        if fim == 1:
            break
    if vitoria == 1:
        print("vitoria da ficha: ")
        input()

turnoPlayer = 0
modo = 0
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")#Limpar tela
    modo = iniciarJogo()
            #-------------------------------------jogador vs maquina----------------------------------------#
    if(modo == 2): #modo de jogo 1 jogador
        turnoPlayer = 0
        loop = True
        while loop == True:
            #-------------------------------------Vez do Jogador 1------------------------------------------#
            if(turnoPlayer % 2 == 0):
                ficha="1"
                PlayerX(ficha)
            #-------------------------------------Vez do Jogador 2------------------------------------------#
            elif(turnoPlayer % 2 != 2):
                ficha="2"
                PlayerX(ficha)
    autoStart = input("\nRepetir(Y/N) ?: ")    