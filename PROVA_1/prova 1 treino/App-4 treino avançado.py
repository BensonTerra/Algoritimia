'''
Considere uma fábrica que dispõe de uma linha de produção de máscaras, constituída por 6 postos de trabalho.
Implemente um programa que leia, para cada posto de trabalho, a produção (nº de máscaras produzidas) e o tecido
gasto (em cm).

Com base nestes dados, implemente as seguintes funções:
• Função que devolva os dois postos de trabalho que produziram maior número de máscaras
• Função que devolva qual o posto de trabalho que gastou mais tecido
'''

import os #biblioteca os
autoStart="y"

def organizarListaProducao(lista):
    listaOrdenadaProducao = sorted(lista, key = lambda x: x[1],reverse=True)
    print(listaOrdenadaProducao)
    maiorProducao(listaOrdenadaProducao)

def organizarListaConsumo(lista):
    listaOrdenadaConsumo = sorted(lista, key = lambda x: x[2],reverse=True)
    print(listaOrdenadaConsumo)
    maiorConsumo(listaOrdenadaConsumo)

def maiorProducao(lista):
    print("O posto %i e %i foram os que mais produziram"%(lista[0][0],lista[1][0]))

def maiorConsumo(lista):
    print("O posto %i foi o que mais gastou"%(lista[0][0]))

while autoStart == "Y" or autoStart == "y":
    os.system("cls")

    fabrica = []
    posto = []
    mascaras=10
    centimetros=20
    for i in range(1,7):
        os.system("cls")
        print("Posto: %i"%i)
        #mascaras=int(input("Mascaras produzidas: "))

        #centimetros=int(input("Tecido gasto em cm: "))

        print("-"*30)
        
        posto.append(i)
        posto.append(mascaras)
        posto.append(centimetros)
        #print(posto)
        
        fabrica.append(posto[0:])
        print(fabrica)

        print("-"*30)
        posto.clear()
        mascaras+=5
        centimetros+=5
    print(fabrica)
    organizarListaProducao(fabrica)
    organizarListaConsumo(fabrica)

    autoStart = input("Repetir(Y/N) ?: ")