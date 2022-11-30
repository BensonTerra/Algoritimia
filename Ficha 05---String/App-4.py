'''
Escreva a função removeSpaces que receba um texto e sustitua as 
sequências de dois ou mais espaços por um único espaço. A função 
deve imprimir o texto resultante.
'''

import os #biblioteca os
autoStart="y"

def spaceRemover(texto):
    caracteres = len(texto) #Numeros caracteres da variavel texto
    while texto.find("  ") !=-1: #Enquanto existir "  " no texto o ciclo não para
        texto = texto.replace("  ", " ")#Remove um espaço em excesso
    print(texto)#Printa o texto final

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    frase=input("Digite um texto: ")#Input para introduzir um texto
    spaceRemover(frase)#Atribui a varivel frase a função spaceRemover

    autoStart = input("Repetir(Y/N) ?: ")