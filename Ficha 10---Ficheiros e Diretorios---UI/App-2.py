"""

"""
#Bibloiotecas inportadasa inicio
import os #biblioteca os
#Bibloiotecas inportadads fim
#
#Variaveis globais inicio
pasta = "files"
ficheiro = "files/texto2.txt"
#Variaveis globais fim
#
#Verfica a existencia da pasta incio
if not os.path.exists(pasta):
    os.mkdir(pasta)
#Verfica a existencia da pasta fim
#
#Função criptografar inicio
def criptografar(texto):
    textoFinal = ""
    textoCodificado = ""
    for i in texto:
        letra = ord(i)
        novaLetra = chr(letra + 3)
        textoCodificado += novaLetra
    return textoCodificado
#Função criptografar fim
#
#Função descriptografar inicio
def descriptografar(texto):
    textoFinal = ""
    textoDecodificado = ""
    for i in texto:
        letra = ord(i)
        novaLetra = chr(letra - 3)
        textoDecodificado += novaLetra
    return textoDecodificado
#Função descriptografar fim
#
#Função guardarFicheiro inicio
def guardarFicheiro(textoCodificado):
    f = open(ficheiro, "w", encoding="utf-8")
    f.write(textoCodificado)
    f.close()
#Função guardarFicheiro fim
#
#lerTexto(): lê o conteúdo inicio
def LerTexto():
    textoDecodificado = ""
    f = open(ficheiro,"r")
    linha = f.read()
    f.close()
    return linha
#lerTexto(): lê o conteúdo fim
#
#Função Menu para melhor interface inicio
def menu():
    op=" "
    os.system("cls")#Limpar tela
    while op !="0":
        os.system("cls")
        print("\n\t\t\tMENU\n")
        print("\t\t1 -  Inserir texto")
        print("\t\t2 -  Ler texto")
        print("\t\t0 - Sair\n")

        op = input("\t\t    Opção: ")
        if op == '1':
            texto = input("Insira o texto: ")
            textoCodificado = criptografar(texto)
            guardarFicheiro(textoCodificado)
            input()
        elif op == '2':
            textoCodificado = LerTexto()
            print("Codigo decriptado: %s"%(descriptografar(textoCodificado)))
            input()
#Função Menu para melhor interface fim
#
#Codigo principal incio
autoStart="y"
#-----------------------#
while autoStart.upper() == "Y":
    menu()
    autoStart = input("Repetir(Y/N) ?: ")
#Codigo principal fim