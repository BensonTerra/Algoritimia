#valor medio de uma sequencia de numeros

import os #biblioteca os
autoStart="y"

def valorMedio(*valores):
    valorTotal=0
    for i in range(len(valores)):
        valorTotal=valorTotal + valores[i]
    media = valorTotal/len(valores)
    return media

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    resultado=valorMedio(10,20,30,40,50)
    print("%.2f\n"%(resultado))
    autoStart = input("Repetir(Y/N) ?: ")
