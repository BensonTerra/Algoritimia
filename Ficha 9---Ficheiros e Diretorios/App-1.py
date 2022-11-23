"""

"""
import os #biblioteca os

#Variaveis globais
pasta = "files"
ficheiro = "files/lista.txt"
#
if not os.path.exists(pasta):
    os.mkdir(pasta)
#
def inserirDado():
    """
    Cria bloco de notas.txt
    """

    pais = ""
    continente = ""
    pais = input("Digite um país: ")
    continente = input("Digite o continente: ")
    if paisExiste(pais) == True:
        print("O país %s já foi adicionado" %pais)
        input()
    else:
        guardarFicheiro(pais,continente)
    input()
#
def guardarFicheiro(pais,continente):
    linha = pais + ";" + continente + "\n"
    f = open(ficheiro, "a", encoding="utf-8")
    f.write(linha)
    f.close()
#
def paisExiste(pais):
    if not os.path.exists(ficheiro):
        print("O ficheiro não existe")
        input()
        return False
    else:
        f = open(ficheiro, "r", encoding="utf-8")
        linhas = f.readlines()
        f.close()
        for linha in linhas:
            print("%s"%(linha.split(";")[0]))
            if pais == linha.split(";")[0]:
                return True
        else:
            return False
#       
def consultaPaíses(continente):
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        if continente == "" or continente + '\n' == linha.split(";")[1]:
            print("\t\t%s | %s"%((linha.split(";")[0]),(linha.split(";")[1])))
    input()





autoStart="y"
op=" "
#
while autoStart == "Y" or autoStart == "y":
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  Inserir país")
        print("\t\t2 -  Consultar países")
        print("\t\t3 -  Consultar por continente")
        print("\t\t4 -  Consultar numeros de países")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            print("\n")
            inserirDado()
        elif op == '2':
            consultaPaíses('')
        elif op == '3':
            continente = input("qual contine:")

            consultaPaíses(continente)


    autoStart = input("Repetir(Y/N) ?: ")