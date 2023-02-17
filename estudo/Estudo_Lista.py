"""
detectar elementos que existem em duas lista em simultâneo
"""

import os #biblioteca os

os.system("cls")

lista_1 = [10,12,14,16,18,20,22,24,26,28]
lista_2 = [1,3,5,7,14,18,21,7,9,8]
numVezes = 0
resposta = ""

for i in lista_1:
    #print(i)
    for j in lista_2:
        #print(j)
        if i == j:
            resposta = resposta + str(i) + ", "
            numVezes+=1
respostaNum = len(resposta)
resposta = resposta[0:respostaNum-2]
resposta = resposta + "."

print("Existem %i elementos que se repetem, e eles são: %s" %(numVezes,resposta))
