"""

"""

#Variaveis globais
compVagas = 15
senha = 1

def adicionarCarro(vagas):
    """
    rebebe o carro e gera uma vaga
    """
    global compVagas
    if len(vagas) == compVagas:
        print("\n\n\t\tNão há mais vagas")
        input()
        return vagas
    global senha
    vagas.append(senha)
    print("\n\n\t\tVaga ocupada: %s"%senha)
    input()
    senha+=1 #proxima senha a sair
    return vagas

def removerCarro(vagas):
    """
    receives vagas list and implements ticket fulfillment
    """
    if len(vagas) == 0:
        print("\n\n\t\tNão há carros no estacionamento")
        input()
        return
    # atende senha que está na posição 0 da lista (mais à frente)     
    print("\n\n\t\tCarro de nº %s"%vagas[0])
    input()
    #del vagas[0]
    vagas.pop(0)
    return vagas

def estado(vagas):
    print("\n\t\tVagas ocupadas: %i " %(len(vagas)))
    print("\n\t\tVagas livres: %i "%(compVagas - len(vagas)))
    print("\n\t\tLocal das vagas: ", vagas)
    input()

import os #biblioteca os
autoStart="y"

vagas = []
op=" "
while autoStart == "Y" or autoStart == "y":
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  Adicionar carro")
        print("\t\t2 -  Remover carro")
        print("\t\t3 -  Estado do estacionamento")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            vagas = adicionarCarro(vagas)
        if op == '2':
            vagas = removerCarro(vagas)
        if op == '3':
            estado(vagas)

    autoStart = input("Repetir(Y/N) ?: ")