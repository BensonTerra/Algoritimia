"""
Este programa calcula a média de visitantes ao longo de uma semana em diferentes dias.
"""

def media_visitantes(lista):
    media = sum(lista) / len(lista)
    return media

dia_semana = ["Domingo", "Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]

import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    try:
        lista = [1,2,3,4,5,6,7,8,9,10]
        #lista= []
        numLeituras = 10
        #numLeituras =int(input("Numeros de leituras: "))
        os.system("cls")
        dia = 0
        for i in range(numLeituras):
            if dia > 6:
                dia=0
            #valor = int(input("Numeros de visitantes na %s: "%dia_semana[dia]))
            dia+=1
            #lista.append(valor)
        print(lista)
        media = media_visitantes(lista)
        print("")
        print("Media de visitantes: %.2f"%media)
        print("")
    except ValueError:
        print("Digite novamente")
    else:
        autoStart = input("Repetir(Y/N) ?: ")