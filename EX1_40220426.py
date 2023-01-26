# Numero: 40220426
# Nome: Francisco João Moreira de Castro Neves Gameiro

import os # Biblioteca 'os' importada

jogadas = 0

def preencheTabuleiro(listaBidimensional):
    """
    Esta função vai gerar um número inteiro entre [1, 30] para cada posição do tabuleiro que não serão repetidos.
    """
    from random import randint # Função 'randint' da biblioteca 'random' importada

    for i in range(len(listaBidimensional)):
        for j in range(len(listaBidimensional[i])):
            del listaBidimensional[i][j]
            repete = True
            while repete == True:
                listaBidimensional[i].insert(j, randint(1, 30))
                for l in range(len(listaBidimensional)):
                    if listaBidimensional[i][j] not in listaBidimensional[l]:
                        repete = False

def imprimeTabuleiro(listaTab, listaTabAleat, lin, col):
    """
    Esta função vai modificar o tabuleiro de modo a revelar o valor de uma dada célula da tabela através da linha (variável lin) e coluna (variável col).
    """
    del listaTab[lin-1][col-1]
    listaTab[lin-1].insert(col-1, listaTabAleat[lin-1][col-1])

def somarTabuleiro(lista):
    """
    Esta função devolve a soma de todas a células do tabuleiro
    """
    soma = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            soma += lista[i][j]
    
    return soma


tabuleiro = [[0,0,0],
             [0,0,0],
             [0,0,0]] # Inicialização da lista bidimensional tabuleiro

tabuleiroAleatorio = [[0,0,0],
                      [0,0,0],
                      [0,0,0]] # Inicialização da lista bidimensional tabuleiroAleatório, que receberá valores aleatórios.

preencheTabuleiro(tabuleiroAleatorio)

while True:
    os.system('cls')
    print('\tTabuleiro de Jogo\n' + '-'*35)
    for i in range(len(tabuleiro)):
        print('{}               {}                {}'.format(tabuleiro[i][0], tabuleiro[i][1], tabuleiro[i][2],))
        print('-'*35)

    try:
        linha = int(input('\nIndique a linha da célula a desvendar: '))
        coluna = int(input('\nIndique a coluna da célula a desvendar: '))

        jogadas += 1

        imprimeTabuleiro(tabuleiro, tabuleiroAleatorio, linha, coluna)

        nPontos = somarTabuleiro(tabuleiro)

        if nPontos >= 100:
            break
    except:
        input('\nValor inválido!\nPressione ENTER para continuar.')

print('\nParabéns!\nConseguiste {} pontos em {} jogadas'.format(nPontos, jogadas))
input('\nPressione ENTER para fechar.')



EX1_40220426.py