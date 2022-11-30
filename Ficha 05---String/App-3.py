#Crie a função capicua que receba um texto como parâmetro de entrada e devolva True ou False, conforme o texto seja uma capicua ou não.

import os #biblioteca os
autoStart="y"

def capicua(text):
    textInverted=""
    for i in range(len(text)-1,-1,-1):
        #print(text[i])
        textInverted = textInverted + text[i]
    #print(textInverted)
    if text == textInverted:
        print("A palavra %s é capicua" % text)
    else:
        print("A palavra %s não é capicua" % text)
    
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    frase=input("Digite um texto: ")
    capicua(frase)

    autoStart = input("Repetir(Y/N) ?: ")