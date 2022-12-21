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
destaque = "🟢"
modo = 0
#variaveis globais fim

def iniciarJogo():
    global modo
    modo = 0
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
        op = input("\t\t    Opção: ")#Seletor de Modo
        if op == "1":
            reset()
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
            if(tabuleiro[x][y] == "🔵"):
                print("",tabuleiro[x][y], end=" |")
            elif(tabuleiro[x][y] == "🔴"):
                print("", tabuleiro[x][y], end=" |")
            elif(tabuleiro[x][y] == destaque):
                print("", tabuleiro[x][y], end=" |")
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
        posiçao[1]=0
        posiçao[0]=0
        return posiçao

def gravidade(cordenada):
    #calcula a casa abaixo da coluna escolhida linha[0]coluna[x]
    casaInferior = [None,None]
    casaInferior[0] = cordenada[0] + 1
    casaInferior[1] = cordenada[1]
    #print(cordenada)
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
    if(tabuleiro[cordenada[0]][cordenada[1]] == "🔵"):
        #input()
        #print("ocupado")
        return False
    elif(tabuleiro[cordenada[0]][cordenada[1]] == "🔴"):
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
    global destaque
    win = 0
    #verifica na horizontal
    for y in range(linha):
        for x in range (colunas - 3):
            if tabuleiro[y][x+0] == ficha and tabuleiro[y][x+1] == ficha and tabuleiro[y][x+2] == ficha and tabuleiro[y][x+3] == ficha:
                print("Horizontal")
                os.system("cls")

                win = 1
                return win
    
    #verifica na vertical
    for x in range(colunas):
        for y in range(linha-3):
            if tabuleiro[y][x] == ficha and tabuleiro[y+1][x] and tabuleiro[y+2][x] and tabuleiro[y+3][x] == ficha:
                print("Vertical")
                os.system("cls")
                tabuleiro[y+0][x]=destaque
                tabuleiro[y+1][x]=destaque
                tabuleiro[y+2][x]=destaque
                tabuleiro[y+3][x]=destaque
                win = 1
                return win

    #verifica na diagonal, superior esquerdo para inferior direito
    for x in range(linha - 3):
        for y in range(colunas - 3):
            if tabuleiro[x][y] == ficha and tabuleiro[x+1][y+1] == ficha and tabuleiro[x+2][y+2] == ficha and tabuleiro[x+3][y+3] == ficha:
                print("Diagonal 1")
                os.system("cls")

                win = 1
                return True
    
    #verifica na diagonal, superior direito para inferior esquerdo
    for x in range(linha - 3):
        for y in range(3,colunas):
            if tabuleiro[x][y] == ficha and tabuleiro[x+1][y-1] == ficha and tabuleiro[x+2][y-2] == ficha and tabuleiro[x+3][y-3] == ficha:
                print("Diagonal 2")
                os.system("cls")

                win=1
                return True

    return win #caso não cumpra nenhuma das condições anteriores

def PlayerX(ficha):
    global turnoPlayer
    global vitoria
    fim = 0
    while vitoria == 0:
        os.system("cls")
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
                modificarTabuleiro(cordenadaFinal,ficha)
                input()
            mostrarTabuleiro()

            if modo == 1:
                turnoPlayer = 1
            elif modo == 2:
                turnoPlayer += 1
            fim = 1
            vitoria = checarVitoria(ficha)
            break
        if fim == 1:
            break
    vitoriaFuncao(vitoria)
        
def vitoriaFuncao(vitoria):
    if vitoria == 1:
        mostrarTabuleiro()
        print("")
        print("vitoria da ficha: %s"%ficha)

def reset():
    global tabuleiro
    tabuleiro = [ ["","","","","","",""],
                ["","","","","","",""],
                ["","","","","","",""],
                ["","","","","","",""],
                ["","","","","","",""],
                ["","","","","","",""]]
    global modo
    modo = 0
    global turnoPlayer
    turnoPlayer = 0

autoStart="y"

while autoStart == "Y" or autoStart == "y":
    global turnoPlayer
    os.system("cls")#Limpar tela
    modo = iniciarJogo()
    if(modo == 1): #modo de jogo 1 jogador
        turnoPlayer = 1
        loop = True
        while vitoria == 0:
            #-------------------------------------Vez do Jogador 1------------------------------------------#
            if(turnoPlayer == 1 ):
                ficha="🔵"
                PlayerX(ficha)
            #-------------------------------------jogador vs maquina----------------------------------------#
    elif(modo == 2): #modo de jogo 1 jogador
        turnoPlayer = 0
        loop = True
        while vitoria == 0:
            #-------------------------------------Vez do Jogador 1------------------------------------------#
            if(turnoPlayer % 2 == 0):
                ficha="🔵"
                PlayerX(ficha)
            #-------------------------------------Vez do Jogador 2------------------------------------------#
            elif(turnoPlayer % 2 != 2):
                ficha="🔴"
                PlayerX(ficha)
        
    autoStart = input("\nRepetir(Y/N) ?: ")    