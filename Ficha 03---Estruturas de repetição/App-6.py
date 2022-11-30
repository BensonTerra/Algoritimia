import random #biblioteca random 
import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    ano=random.randint(1900,2020) #gerador de ano
    if ano%400==0 or(ano%4==0 and ano%100!=0):
        print("O ano %i é bisexto"%ano)
    else:
        print("O ano %i não é bisexto"%(ano))
    autoStart = input("Deseja um novo ano ?: Y/N: ")
