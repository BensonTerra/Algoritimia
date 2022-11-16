"""

"""
def selelect_sub_menu(num):
    while num != "0":
        if num == 1:
            Tirar_ticket()
            print("\nFunção 1")
        elif num == "2":
            print("\nFunção 2")
        elif num == "3":
            print("\nFunção 3")
        elif num == "0":
            print("\nFunção 0")

def Tirar_ticket():
    ticket = []
    x=1
    ticket.append(x)
    x+=1
    print(ticket)
    return


import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    option = " "
    lista= []
    try:
        os.system("cls")
        print("\t\t\tMenu")
        print("")
        print("\t\t 1 – Tirar Ticket")
        print("\t\t 2 – Atendimento")
        print("\t\t 3 - Estado da fila de espera")
        print("")
        print("\t\t 0 - Sair\n")
        option = input("\tOpção: ")
        selelect_sub_menu(option)
        break
    except ValueError:
        print("Digite novamente")
    else:
        autoStart = input("\nRepetir(Y/N) ?: ")