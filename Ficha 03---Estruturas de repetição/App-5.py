import random
import os

novo_jogo = "Y"

while novo_jogo == "Y" or novo_jogo == "y":
    os.system("cls")
    resposta=random.randint(1,50)
    print(resposta)
    count=1
    num=int(input("Introduza um numero de 1 a 50: "))
    os.system("cls")
    while resposta!=num and count<11:
        if num<resposta:
            print("Maior")
            count+=1
        else:
            print("menor")
            count+=1
        print(resposta)
        num=int(input("Introduza um numero de 1 a 50: "))
        os.system("cls")
    if num==resposta:
        print("parabens. tentativa %i"%count)
    else:  
        print("limite de jogadas atingido")
    novo_jogo = input("Novo jogo ?: Y/N: ")
os.system("cls")
print("volte sempre")