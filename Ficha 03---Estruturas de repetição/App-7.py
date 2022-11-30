import os #biblioteca os
autoStart="y"
primo=True
while autoStart == "Y" or autoStart == "y":#ciclo de verificação
    os.system("cls")
    numero=int(input("Introduza um numero: "))#introduzir um numero
    for i in range(2,numero):
        resto=numero % i
        if resto==0:
            primo=False
            break
    if primo== True:
        print("O numero %i é primo"%numero)
    else:
        print("O numero %i não é primo"%numero)
    autoStart = input("Repetir ?: Y/N: ")