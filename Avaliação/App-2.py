#Benson Leme Terra 40220440
'''

'''

import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")

    except ValueError:
        print("Valor inválido")
    except:
        print("Erro desconhecido")
    else:
        autoStart = input("Repetir(Y/N) ?: ")
    
    