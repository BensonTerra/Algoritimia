'''
Escreva a função shortName que deve receber um nome completo e 
devolve uma string com o primeiro e último nome (primeiro nome 
próprio e último apelido).
'''

import os #biblioteca os
autoStart="y"

def shortName(nome):
    nomeCurto=""
    posFirstName=nome.find(" ")
    nomeCurto=nomeCurto+nome[:posFirstName]
    posLastName=nome.rfind(" ")
    nomeCurto=nomeCurto+nome[posLastName:]
    print(nomeCurto)


while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    nome=input("Digite seu nome: ")#Input para introduzir um nome
    shortName(nome)#Atribui um nome a função shortName

    autoStart = input("Repetir(Y/N) ?: ")