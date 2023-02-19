"""
Programa de gestão de acessos  ao parque de estacionamento da ESMAD
"""
import os #biblioteca os
import time

#Variaveis Globais
gessList = ['00-CC-00','01-CC-01','02-CC-02','03-CC-03','04-CC-04', '05-CC-05','06-CC-06','07-CC-07','08-CC-08','09-CC-09']
parkList = ['01-CC-01','02-CC-02','03-CC-03','04-CC-04','09-CC-09']

def parkValidator(data):
    #print("parkValidator")
    if data in parkList:
        return True
    else:
        return False
    
def adcionarMatricula():
    os.system("cls")
    #print("adcionarMatricula")
    x = input("Digite o primeiro par de caracteres da matricula(00 a 99): ")
    y = input("Digite o segundo par de caracteres da matricula(AA a ZZ): ")
    z = input("Digite o terceiro par de caracteres damatricula(00 a 99): ")
    if len(str(x)) <= 2 and len(y) == 2 and len(str(z)) <= 2:
        data = str(x) + "-" + y.upper() + "-" + str(z)
        #print(data)
        control = parkValidator(data)
        #print(control)
        if control == False:
            if data in gessList:
                #print("entrada autorizada")
                parkList.append(data)
                #print(parkList)
            else:
                print("\n\tEntradas invalidas")
                input("\nPressione qualque tecla para continuar")
                adcionarMatricula()
        elif control == True:
            print("\n\tO veiculo já se encontra no sistema!!!")
            input("\nPressione qualque tecla para continuar")
    else:
        os.system("cls")
        print("\n\tEntradas invalidas")
        adcionarMatricula()

def removerMatricula():
    print("removermatricula")
    mostrarMatriculas()
    #print(parkList)
    index = int(input("\nNumero da matricula a ser removida: "))
    index = index - 1
    del parkList[index]
    #print(parkList)

def statusEstacionamento():
    os.system("cls")
    pos = 1
    print("\t      Status do estacionamento")
    print(50*"-")
    #print("statusEscionamento")
    for element in gessList:
        #print(element)
        control = parkValidator(element)
        if control == True:
            if pos < 10:
                line = "\t\t" + "0" + str(pos) + " | " + element +" | " + "🟢"
            else:
                line = "\t\t" + str(pos) + " | " + element +" | " + "🟢"
        else:
            if pos < 10:
                line = "\t\t" + "0" + str(pos) + " | " + element +" | " + "🔴"
            else:
                line = "\t\t" + str(pos) + " | " + element +" | " + "🔴"
        print(line)
        pos+=1
    print(50*"-")
    input("\nPressione qualque tecla para continuar")

def mostrarMatriculas():
    i = 1 
    print(30*"-")
    for element in parkList:
        pos = i
        line = " " + str(pos) + " | " + element
        print(line)
        i+=1

def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 --- Adicionar Matricula")
        print("\t\t2 --- Remover Matricula")       
        print("\t\t3 --- Status do Estacionamento") 
        print("\t\t0 --- Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            adcionarMatricula()
        elif op == '2':
            removerMatricula()
        elif op == '3':
            statusEstacionamento()

#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim