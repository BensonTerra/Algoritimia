#Um número perfeito

import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    somarResto=0
    valores="0"
    print("\n" * 5)
    numero=int(input("\tEscreva um numero: "))
    for i in range(1,numero):
        resto=numero%i
        if resto==0:
            somarResto= somarResto + i #resto
            valores=  valores +", "+ str(i) #estudar essa parte melhor

    if somarResto ==numero:
        print("numero perfeito")
    else:
        print("numero inperfeito")
    
    print("numeros possiveis: %s"%valores)
        
    autoStart = input("Repetir(Y/N) ?: ")