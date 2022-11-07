'''
Implemente a função printCharLine que receba dois argumentos: 
um texto e o nº de caracteres que se pretende imprimir por cada 
linha.
'''

import os #biblioteca os
autoStart="y"

def reverseWord(texto):
    resposta=""
  #  texto = " " + texto
    nSpaces=texto.count(" ")
    for i in range (nSpaces):
        pos=texto.rfind(" ")
        #print(pos)
        #print(texto[pos+1:])
        resposta=resposta+texto[pos+1:]+" "
        texto=texto[0:pos]
    resposta=resposta+texto
    print(resposta)


    
        
    

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        frase=input("Digite uma frase: ")
        reverseWord(frase)
    except ValueError:
        print("Valor inválido")
    except:
        print("Erro desconhecido")
    else:
        break
    
    autoStart = input("Repetir(Y/N) ?: ")