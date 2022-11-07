#decimal para binario

import os #biblioteca os
autoStart="y"
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    valores="binario: "

    decimal=int(input("Insira um numero entre 1 e 99: "))
    while decimal >= 1:
        binario = decimal % 2
        decimal = decimal / 2
        valores = valores + str(int(binario)) + "|"
    print("%s"%valores)

    autoStart = input("Repetir(Y/N) ?: ")