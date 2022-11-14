"""

"""

dia_semana = ["Domingo", "Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]

import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    try:
        lista= []
        numLeituras =int(input("Numeros de leituras: "))
        os.system("cls")
        dia = 0
        for i in range(numLeituras):
            if dia > 6:
                dia=0
            valor = int(input("Numeros de visitantes na %s: "%dia_semana[dia]))
            #valor = int(input("Numeros de visitantes na %i: "%dia))
            dia+=1
            lista.append(valor)
        print(lista)
    except ValueError:
        print("Digite novamente")
    else:
        autoStart = input("Repetir(Y/N) ?: ")