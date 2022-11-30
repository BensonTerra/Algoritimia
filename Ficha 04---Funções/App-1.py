#fibonacci em uma função a parte

import os #biblioteca os
autoStart="y" #Valor inicia da variavel autoStart em string.

def fibonacci(nTermos): #Função fibonacci 
    os.system("cls") #Limpar tela terminal
    termoP2=1 #Valor inical da variavel termoP2
    termoP1=0 #Valor inicial da variavel termoP1
    termos="0" #Valor inicial, em string, da variavel termos

    #nTermos=int(input("Escreva um numero: "))
    if nTermos>=1: #Ciclco de verificação para numero de termos é maior ou igual a 1
        termos= "0"
    else: #Ciclco de verificação para caso não cumpra a condição anterior
        termos=termos+", 1"
    
    for i in range(nTermos):
        termoP3=termoP2+termoP1 #Calculo do terceiro termo
        termos = termos +", "+str(termoP3) #Açteração e adição do termoP3 à sequencia 
        termoP1=termoP2 #TermoP1 assume o valor termoP2
        termoP2=termoP3 #Temop2 assume o valor termoP3
    print("primeiros %i termos da sequencia: %s" % (nTermos, termos)) #Reproduçao no terminal da sequencia fibonacci

while autoStart == "Y" or autoStart == "y": #Ciclo de repetição
    os.system("cls")
    numero=int(input("Digite um numero: ")) #Introdução de um numero para função fibonacci
    fibonacci(numero) #Função fibonacci no codigo principal
    autoStart = input("Repetir(Y/N) ?: ") #Reoetir ciclo
