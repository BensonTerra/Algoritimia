#Elabore um programa que leia uma frase e determine:
# Número de caracteres
# Número de espaços
# Número de vogais

import os #biblioteca os
autoStart="y"

def analise(text):
    caracteres = len(text)
    espaços = text.count(" ")
    vogais=["a","e","i","o","u"]
    vogal=0
    for i in range(caracteres):
        if text[i] in vogais:
            vogal+=1
    print("O texto possui %i caracteres, %i espaços e %i vogais"%(caracteres, espaços,vogal))

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    frase=input("Digite um texto: ")
    analise(frase)

    autoStart = input("Repetir(Y/N) ?: ")