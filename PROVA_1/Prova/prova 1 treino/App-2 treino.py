

import os #biblioteca os
autoStart="y"

#Modificação para melhorar o codigo inicio
def spaceRemover(texto):
    caracteres = len(texto) #Numeros caracteres da variavel texto
    while texto.find("  ") !=-1: #Enquanto existir "  " no texto o ciclo não para
        texto = texto.replace("  ", " ")#Remove um espaço em excesso
    print(texto)#Printa o texto final

    return texto
#modificação para melhorar o codigo fim

def imprime_palavras(texto): #texto1 para texto
    texto = texto + " "
    cont_pal=0 # 1 erro
    pal=""
    pos = texto.find(" ")
    while pos != -1:
        pal =  pal + texto[:pos+1] # 3 cont_pal lugar errado
        print(pal)
        cont_pal += 1
        texto =texto[pos+1:] #4 nova versão do texto
        pos = texto.find(" ") #2 erro

    return cont_pal
    


while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    texto=input("Escreva um texto: ")
    textoCorrigido = spaceRemover(texto)
    cont=imprime_palavras(textoCorrigido)
    print("O texto tem %i palavras"%cont)

    autoStart = input("Repetir(Y/N) ?: ")
