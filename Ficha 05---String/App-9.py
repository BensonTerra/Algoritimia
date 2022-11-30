"""
Escreva a função countWord que receba um texto e uma palavra de 
pesquisa. A função deve devolver o número de ocorrências dessa 
palavra no texto, e as posições onde ocorre.
"""
# Função que o nº de ocorrência de uma palavra, num texto
def countWord(text, txtFind):
    """
    It receives a string text, and a string word to find 
    It returns de number of occurences and positions
    """
    text = " " + text + " "
    txtFind = " " + txtFind + " "
    num = text.count(txtFind)     # nº de ocorrencias
    print(num)

    posSearch=0           
    positions=""     # variável de saida com as diversas posições no texto
    for i in range(num):
        posWords = text.find(txtFind, posSearch) # pesquisa (find) no texto a partir da posição ant
        print(posWords)
        if posWords != -1:
            positions+= " " + str(posWords+1)   
            posSearch = posWords + 1
        else:
            break
    return num, positions     # devolve nº ocorrencias (num) e posições (positions)

text = input("Texto:")
txtFind = input("Pesquisa:")
num, positions = countWord(text, txtFind)
print("A palavra {0} ocorre {1} vezes no texto. Nas posições:{2}" .format(txtFind, num, positions))

#refazer o codigo para melhor entedimento pessoal
#prioridade para o dia 7/11/2022



