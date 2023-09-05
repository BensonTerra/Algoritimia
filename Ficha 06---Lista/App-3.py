"""
Crie um programa que leia a pontuação de 10 participantes num concurso de programação (a pontuação deve estar validada entre 0 a 20, por uma estrutura try-except). 
O programa deve invocar uma função, positiveList que receba a lista das 10 pontuações e devolva uma nova lista apenas com as pontuações positivas (>=10).
"""
import os #biblioteca os
autoStart="y"

def positiveList(lista):
    counter = 0
    listaPositiva = []
    for i in range(0, len(lista)):
        if lista[i]>=10:
            listaPositiva.append(lista[i])
    return listaPositiva

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        score = []
        i=1
        nota= 10
        while i <=10:
            nota =int(input("Nota do aluno nº %i: "%i))
            if nota<0 or nota>20:
                raise ValueError()
            score.append(nota)
            #nota+=1 #macro
            i+=1
        listapositiva=positiveList(score)
        print("Scores superior a 10: %s"%listapositiva)
    except ValueError:
        print("Valor invalido: %i"%nota)
    else:

        autoStart = input("Repetir(Y/N) ?: ")
