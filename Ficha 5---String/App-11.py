'''
Implemente a função printCharLine que receba dois argumentos: 
um texto e o nº de caracteres que se pretende imprimir por cada 
linha.
'''

import os #biblioteca os
autoStart="y"

def printCharLine(texto,nCaracteres):
    while len(texto) > nCaracteres:
        print(texto[0:nCaracteres])
        texto = texto[nCaracteres:]
    print(texto)
    

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        frase=input("Digite uma frase: ")
        numero=int(input("Digite um numero: "))
        printCharLine(frase, numero)
    except ValueError:
        print("Valor inválido")
    except:
        print("Erro desconhecido")
    else:
        break
    
    autoStart = input("Repetir(Y/N) ?: ")