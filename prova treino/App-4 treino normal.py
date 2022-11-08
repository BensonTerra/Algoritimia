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

def maior_producao_e_consumo(lista1, lista2):
    setor = ""
    gasto = ""
    for i in range(2):
        
        maior1 = max(lista1)
        #print(maior1)
        pos1 = lista1.index(maior1) 
        #print(pos1)              
        setor = setor + str(postos[pos1]) + " "       
        #print(setor)

        del lista1[pos1]
        
    maior2 = max(lista2)
    #print(maior2)
    pos2 = lista2.index(maior2)    
    #print(pos2)
    gasto = gasto + str(postos[pos2]) + " "
    #print(gasto)
    #del lista2[pos2]

    return setor,gasto

postos = [1,2,3,4,5,6]
mascaras = [10,11,12,9,8,8]
centimetros = [50,53,55,50,47,45]
i=0
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    try:
        while i!=len(postos):
            os.system("cls")
            #print("Posto: %i"%(i +1))
            #masc= int(input("Mascaras produzidas no posto %i: "%(i+1)))
            #cent= int(input("Centimetros de tecido gasto no posto %i: "%(i+1)))
            #mascaras.append(masc)
            #centimetros.append(cent)
            print("Mascaras produzidas: %s"%mascaras)
            print("Centimetros gastos: %s"%centimetros)
            i+=1
        setorMproducao, setorMconsumo = maior_producao_e_consumo(mascaras,centimetros)
        print("Maior produção nos postos: %s"%setorMproducao)
        print("Maior maior consumo nos postos: %s"%setorMconsumo)
    except ValueError:
        print("Digite novamente")
    else:
        autoStart = input("Repetir(Y/N) ?: ")
