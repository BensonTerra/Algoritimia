"""
docstring
"""
import os #biblioteca os
import random #biblioteca random

totalNumeros = []

def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 - Gerar número")
        print("\t\t2 - Ver todos numeros")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            gerarNumero()
            input()
        elif op == '2':
            verNumeros()
            input()

def gerarNumero():
    os.system("cls")
    #print("Gerar número")
    num = random.randint(1,100)
    if num != 100:
        if num not in totalNumeros:
            print("\n\t\tNumero gerado = %i\n"%num)
            totalNumeros.append(num)
            cont = input("Deseja gerar outro numero?(Y/N)")
            if cont.upper() == "Y":
                gerarNumero()
            else:
                os.system("cls")
                verNumeros()
        else:
            gerarNumero()
    else:
        totalNumeros.sort(reverse=True)
        print("Todos os numeros gerados: %r "%totalNumeros)


def verNumeros():
    print("Todos os numeros gerados: %r "%totalNumeros)

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim