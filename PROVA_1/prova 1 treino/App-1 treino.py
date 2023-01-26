import os#biblioteca os

os.system("cls")
#genero=input("Defina seu genero(M/F): ")
genero="m"
#idade=int(input("Defina sua idade: "))
idade=35
FC=int(input("Frequencia caradiaca: "))
"""
print(genero)
print(idade)
print(FC)
"""
if(genero=="M" or genero=="m"):
    FCM=220-idade
else:
    FCM=226-idade
print(FCM)   #frequencia caradiaca maxima
"""
print("")
print(FCM*0.50) #frequencia caradiaca 0.50
print(FCM*0.61) #frequencia caradiaca 0.61
print(FCM*0.71) #frequencia caradiaca 0.71
print(FCM*0.81) #frequencia caradiaca 0.81
print(FCM*0.91) #frequencia caradiaca 0.91
print("")
"""
#mudanças
if(FC>=FCM*0.5 and FC<=FCM*0.6):
    print("teste 1")
elif(FC>=FCM*0.61 and FC<=FCM*0.7):
    print("teste 2")
elif(FC>=FCM*0.71 and FC<=FCM*0.8):
    print("teste 3")
elif(FC>=FCM*0.81 and FC<=FCM*0.9):
    print("teste 4")
elif(FC>=FCM*0.91 and FC<=FCM):
    print("teste 5")
else:
    print("perigo")



#fim mundanças

