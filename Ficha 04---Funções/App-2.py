#Implemente a função somatório que receba 2 números inteiros como argumento de entrada, e imprima o somatório de todos os números inteiros incluídos nesse intervalo.


import os#biblioteca os
autoStart="y"

def somatorio(Num1,Num2): #função somatorio
    resultado = 0 #valor inical da variavel resultado

    for i in range(Num1,Num2+1):
        #os.system("cls")
        #print("")
        #print(somatorio)
        print(i)
        #print("")
        resultado = resultado + i #novo valor da variavel somatorio
    print(resultado)
 

while autoStart == "Y" or autoStart == "y": #Cliclo de repetição
    os.system("cls") #Limpar tela do terminal
    limiteMin = int(input("Defina limite min: ")) #Limite minimo da função somatório
    limiteMax = int(input("Defina limite max: ")) #Limite maximo da função somatório
    somatorio(limiteMin,limiteMax) #Função somatório no programa principal


    autoStart = input("Repetir(Y/N) ?: ")

