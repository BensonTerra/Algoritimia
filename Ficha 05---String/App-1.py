#Elabore um programa que leia uma frase e escreva os seus caracteres por ordem inversa

import os #biblioteca os
autoStart="y"

def ordemInversa(text):
    #text=str(input("Digite um texto: "))
    textInverted="Ordem inversa: "    
    for i in range(len(text)-1,-1,-1):
        #print(text[i])
        textInverted = textInverted + text[i]
    print(textInverted) 
    
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    frase=input("Digite um texto: ")
    ordemInversa(frase)

    autoStart = input("Repetir(Y/N) ?: ")