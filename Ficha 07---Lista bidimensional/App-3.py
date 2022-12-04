"""

"""

#Variaveis globais
filas = 3
vagas = 5
compVagas = 15
senha = 1

def cria_lista():
    lista = []
    for x in range (filas):
        lista.append([])
        for y in range (vagas):
            lista[x].append(0)
    return lista

def adicionarCarro(parque):
    """
    recebe o carro e gera uma vaga
    """
    for x in range(filas):
        for y in range(vagas):
            if parque[x][y] == 0:
                parque[x][y] = 1
                print("\n\n\tlugar ocupado: Fila %i, Lugar %i"%(x+1, y+1))
                return parque
    print("\tO parque está completo! :(")
    return parque

def removerCarro(parque):
    try:
        removerFila= int(input("\n\n\tFila: "))
        removerVaga= int(input("\n\n\tVaga: "))
        if (removerFila > filas):
            raise ValueError
        if (removerVaga > vagas):
            raise ValueError
    except:
        print("\tA fila ou lugar não são validos")
    else:
        if parque[removerFila-1][removerVaga-1] == 0:
            print("\tO lugar indicado não está ocupado!")
        else:
            parque[removerFila-1][removerVaga-1] = 0
            print("\to lugar foi desocupado!")
    return parque

def estado(parque):
# Função de conta o nº de lugares livres e ocupados do parque
    VagasLivres =0
    Vagasocupadas = 0
    for i in range(filas):
        for j in range(vagas):
            if (parque[i][j]== 0):
                VagasLivres+=1
            else:
                Vagasocupadas+=1
    print("\n\n\t\tESTADO DO PARQUE")
    print("\tNº lugares livres  : %i"%VagasLivres)
    print("\tNº lugares ocupados: %i"%Vagasocupadas)
    print()

def esvaziarParque(parque):
    for x in range (filas):
        for y in range(vagas):
            parque[x][y] = 0
    print("\n\n\t parque de estacionamento esvaziado")

import os #biblioteca os

autoStart="y"
parque = cria_lista()
op=" "
while autoStart == "Y" or autoStart == "y":
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  Adicionar carro")
        print("\t\t2 -  Remover carro")
        print("\t\t3 -  Estado do estacionamento")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            parque = adicionarCarro(parque)
        elif op == '2':
            parque = removerCarro(parque)
        elif op == "3":
            estado(parque)
        elif op == "4":
            esvaziarParque(parque)
        input()

    autoStart = input("Repetir(Y/N) ?: ")