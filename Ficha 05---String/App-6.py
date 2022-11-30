'''
Elabore a função standardName que deve receber um nome completo e
devolve uma string com o nome normalizado: inclui o primeiro e o 
último nome e abreviaturas de todos os outros nomes intercalares.
'''

import os #biblioteca os
autoStart="y"

def standartName(nome):
    nomeStandard = ""
    #primeiro nome INICIO
    pos = nome.find(" ")
    nomeStandard = nomeStandard + nome[:pos]
    nome=nome[pos:]
    #print(nomeStandard)
    #print(nome)
    while nome.find(" ")!=-1:
        if nome.count(" ")>1:
            pos = nome.find(" ")
            nomeStandard = nomeStandard + nome[pos:pos+2] + "."
            pos = nome.find(" ",pos+1)
            nome = nome[pos:]
        else:
            break

    #primeiro nome FIM

    #Ultimo nome INICIO
    nomeStandard = nomeStandard +nome[:]
    print(nomeStandard)
    #Ultimo nome FIM
    
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    #nome=input("Digite seu nome: ")
    nome="Carlos Alberto Costa Pereira"
    standartName(nome)

    autoStart = input("Repetir(Y/N) ?: ")