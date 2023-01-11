"""
O Instituto de metereologia pretende registar o valor total de pluviosidade ocorrida em 
cada mês, ao longo de um ano (de janeiro a dezembro). 
Implemente a função pluviosidade que receba a lista com a pluviosidade de cada mês, 
e imprima esses mesmos dados (lista de pluviosidade), mas ordenados por ordem decrescente de pluviosidade.
Upgrade versão 2.0: imprimir também os nomes dos respetivos meses, como na imagem!
"""

import os #biblioteca os
autoStart="y"

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
#pluviosidade = [150,190,225,270,145,110,90,60,80,120,175,185] #agua

def maior_pluviosidade(lista):
    """
     return the month of higher value 
    """
    listaProvisoria = lista
    print("Mês: Quantidade\n")
    maior = 0
    for i in range(len(listaProvisoria)):
        #print(listaProvisoria)
        maior = max(listaProvisoria)
        #print(maior)
        pos = listaProvisoria.index(maior)
        #print(pos)
        mes = meses[pos]
        #print(mes)
        listaProvisoria[pos] = 0
        #
        print("%s: %i"%(mes,maior))
        #
        
# Inicio do programa-----

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    try:
        pluviosidade= []
        for i in range(12):
            #valor = pluviosidade[i]
            valor = int(input("Faturação do mês %s: "%meses[i]))
            pluviosidade.append(valor)
        print("\n %s \n"%pluviosidade)
    except ValueError:
        print("Digite novamente")
    else:
        maior_pluviosidade(pluviosidade)
        autoStart = input("Repetir(Y/N) ?: ")
