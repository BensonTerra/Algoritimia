""" 
Função que recebe um texto e substitui a ocorrência de cada dígito decimal 
pelo seu nome em português
"""
def replaceNumbers(texto):
    """
    replace digits (between 0 and 9) by  
    """
    texto = texto.replace("0", "zero||")      #Para todos elemento 0, trocar para zero escrito.
    texto = texto.replace("1", "um||")        #Para todos elemento 1, trocar para um escrito.
    texto = texto.replace("2", "dois||")      #Para todos elemento 2, trocar para dois escrito.
    texto = texto.replace("3", "três||")      #Para todos elemento 3, trocar para três escrito.
    texto = texto.replace("4", "quatro||")    #Para todos elemento 4, trocar para quatro escrito.
    texto = texto.replace("5", "cinco||")     #Para todos elemento 5, trocar para cinco escrito.
    texto = texto.replace("6", "seis||")      #Para todos elemento 6, trocar para seis escrito.
    texto = texto.replace("7", "sete||")      #Para todos elemento 7, trocar para sete escrito.
    texto = texto.replace("8", "oito||")      #Para todos elemento 8, trocar para oito escrito.
    texto = texto.replace("9", "nove||")      #Para todos elemento 9, trocar para nove escrito.
    print(texto)



texto = input("Texto:")
replaceNumbers(texto)
