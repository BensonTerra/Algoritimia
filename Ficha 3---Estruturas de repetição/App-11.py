import os #biblioteca os
autoStart="y"
while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    termoP1=0
    termoP2=0
    count=0

    modo=int(input("Selecionar modo(0 ou 1): "))
    nLeituras=int(input("Insira um numero de leituras: "))
    os.system("cls")
    if modo == 0:
        while nLeituras!=0:
            leitura=int(input("Insira um numero: "))
            nLeituras-=1
            count+=1
            print("%i"%count)
            os.system("cls")
            if leitura>termoP1:
                termoP2=termoP1
                termoP1=leitura
            elif leitura>termoP2:
                termoP2=leitura


    else:
        for i in range(nLeituras):
            leitura=int(input("Insira um numero: "))
            #1count+=1
            os.system("cls")
            if leitura>termoP1:
                termoP2=termoP1
                termoP1=leitura
            elif leitura>termoP2:
                termoP2=leitura

    os.system("cls")
    valores="numeros digitados: "
    valores = valores + str(termoP2) + "|"
    print("termoP2=%i"%termoP2)
            

    autoStart = input("\nRepetir(Y/N) ?: ")