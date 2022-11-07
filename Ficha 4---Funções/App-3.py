#Função abundante,matemática

import os #biblioteca os
autoStart="y" #Valor inicia da variavel autoStart em string.

def abundante(num): #Função abundante
    somarDivisor=0
    valores="0"
    print("\n" * 5)
    #numero=int(input("\tEscreva um numero: "))
    for i in range(1,num): #Ciclo for de 1 a variavel num selecionada pelo usuario
        resto=num%i #
        if resto==0:
            somarDivisor= somarDivisor + i #divisores

    if somarDivisor>num:
        return True
    else:
        return False


while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    numero=int(input("Digite um numero: "))
    if abundante(numero):
        print("O numero %i é abundante: " % numero)
    else:
        print("O numero %i é inválido: " % numero)

    autoStart = input("Repetir(Y/N) ?: ")
