import os
import random

listaResposta = []
listaUsuario = [50, 50, 50, 50, 50]

def gerar_numeros_aleatorios():
    numeros_possiveis = list(range(1, 21))
    return random.sample(numeros_possiveis, 5)
listaResposta = gerar_numeros_aleatorios()
def jogo():
    i = 0
    global listaResposta
    nArray = 0
    max_tentativas = 10

    while nArray < 5 and i < max_tentativas:
        limpar_tela()
        print(listaResposta)
        print(listaUsuario)
        print(i)

        try:
            num = int(input("Digite um número de 1 a 20 para adivinhar: "))
        except ValueError:
            print("Caracter não aceito")
            i += 1
            input()
            continue
        
        if num in listaResposta and num not in listaUsuario:
            index = listaResposta.index(num)
            listaUsuario[index] = num
            print(f"Você acertou! O número {num} está na lista na posição {index + 1}")
            nArray += 1
        elif num in listaUsuario:
            print("Você já digitou esse número")
            i += 1
        else:
            print("O número indicado não existe")
            i += 1
        
        input()
    
    limpar_tela()
    if nArray == 5:
        print("\n\t\t\tPARABÉNS!!!\n")
        print("\t\t\tVocê venceu")
    else:
        print("\n\t\t\tGAME OVER!\n")
        print("\t\t\tVocê não conseguiu adivinhar todos os números a tempo")
    input()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    op = " "
    limpar_tela()
    while op != "0":
        limpar_tela()
        print("\n\t\t\tMENU\n")
        print("\t\t1 --- Jogar")
        print("\t\t0 --- Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            jogo()

autoStart = "S"
while autoStart.upper() == "S":
    menu()
    autoStart = input("Repetir (S/N) ?: ")
