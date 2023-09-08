"""
docstring
"""
import os #biblioteca os
import random #biblioteca random

listName = ["Alexandre Dias", "Carla Dias", "Fábio Carvalho", "Pedro Fonseca", "Alexandre Diogo"]

def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 - Procurar um nome")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            name = input("\n\tIntroduza um nome de pesquisa: ")
            searchName(listName,name)
            input()

def searchName(listName, nameFind):
    print()
    res = 0
    for name in listName:
        #print(name)
        name = name.lower()
        nameFind = nameFind.lower()
        nameArray = name.split(" ")
        if nameFind in nameArray:
            res+=1
    print("A função serachName achou %i nome(s)"%res)

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim