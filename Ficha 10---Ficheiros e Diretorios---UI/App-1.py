""" 1.1
Escreva a função escreveTexto(texto) que receba um texto (lido, p.e. através de um 
input) e o guarde num ficheiro binário, com a designação de dados.bin. Se o ficheiro 
não existir, deve ser criado com a path .\\ficheiros\\dados.bin.
"""
""" 1.2
Escreva a função lerTexto() que lê o conteúdo do ficheiro .\\ficheiros\\dados.bin e
devolve o texto correspondente. Imprima o resultado, devolvido pela função, na consola.
"""
#Bibloiotecas inportadasa inicio
import os #biblioteca os
#Bibloiotecas inportadads fim
#
#Variaveis globais inicio
pasta = "files"
ficheiro = "files/dados.bin"
#Variaveis globais fim
#
#Verfica a existencia da pasta incio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim
#
#Função Menu para melhor interface inicio
def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  Inserir texto")
        print("\t\t2 -  Consultar texto")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            EscreveTexto()
            print("teste")
        elif op == '2':
            LerTexto()
            print("teste")
#Função Menu para melhor interface fim
#
#EscreveTexto: recebe srtring e traduz para binario inicio
def EscreveTexto():
    texto = input("\nInsira o texto que deseja inserir: ")
    f = open(ficheiro,"ab")
    textoFinal = texto + "\n"
    textoBin = bytes(textoFinal,encoding="utf-8")
    f.write(textoBin)
    f.close()
#EscreveTexto: recebe srtring e traduz para binario fim
#
#lerTexto(): lê o conteúdo binario e traduz para srtring incio
def LerTexto():
    f = open(ficheiro,"rb")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        print(linha)
        input()
#lerTexto(): lê o conteúdo binario e traduz para srtring fim
#
#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim
