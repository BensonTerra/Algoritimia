"""
Elabore a função aboveAverage que receba uma lista com 10 números inteiros (número inseridos pelo utilizador) e que devolva quantos desses números estão acima da 
média.
"""
import os #biblioteca os
autoStart="y"

def aboveAverage(lista):
    count=0
    media=sum(lista)/len(lista)
    for i in range(len(lista)):
        if lista[i]>media:
            count+=1
    print("Existe no conjunto %i superior que a media"%count)
        
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    lista = []
    for i in range(10):
        num=int(input("Digite o %iº numero: "%(i+1)))
        lista.append(num)
    #print(lista)
    aboveAverage(lista)

    autoStart = input("Repetir(Y/N) ?: ")