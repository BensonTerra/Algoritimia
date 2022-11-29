import os #biblioteca os

#Variaveis globais
pasta = "files"
ficheiro = "files/tempertatura.txt"

if not os.path.exists(pasta):
    os.mkdir(pasta)

def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  consulatar dados")
        print("\t\t2 -  Consultar estatistica")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            consultaDados()
            #print("teste")
            input()
        if op == '2':
            consultaEstatisca()
            #print("teste")
            input()

def tabela():
    print("\t\t+--------------------Data---------Hora------temperatura-----------------+")
    print("\t\t+-----------------------------------------------------------------------+")
            
def consultaDados():
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    print(linhas)
    print(len(linhas))
    input()
    f.close()
    os.system("cls")
    tabela()
    count = 0
    for linha in linhas:
        if count >5:
            print("\t\tPrima enter")
            input()
            os.system("cls")
            count = 0
            tabela()
        print("\t\t\t\t %s | %s |    %s"%((linha.split(";")[0]),(linha.split(";")[1]),(linha.split(";")[2])))
        count+=1

def consultaEstatisca():
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    lista = []
    #print(len(linhas))
    #input()
    for linha in linhas:
        temperatura = linha.split(";")[2]
        temperatura = temperatura[1:3]
        lista.append(int(temperatura))
        #print(lista)
    lista.sort(reverse=True)
    #print(lista)
    media = sum(lista) / len(lista)
    print("\nMaior temperatura registrada = %.2f"%max(lista))
    print("Menor temperatura registrada = %.2f"%min(lista))
    print("Media temperatura registrada = %.2f"%media)
    input()


autoStart="y"

while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")


    