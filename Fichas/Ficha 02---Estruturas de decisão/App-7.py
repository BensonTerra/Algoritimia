peso=int(input("Escreva seu peso: "))
codigo=int(input("defina um valor de 1 ate 6: "))
planeta="nulo"
if(codigo==1):
    planeta="Mercúrio"
    gravidade=0.37
elif(codigo==2):
    planeta="Vénus"
    gravidade=0.88
elif(codigo==3):
    planeta="Marte"
    gravidade=0.38
elif(codigo==4):
    planeta="Júpiter"
    gravidade=2.64
elif(codigo==5):
    planeta="Saturno"
    gravidade=1.15
else:
    planeta="Urano"
    gravidade=1.17
pesoPlaneta=peso*gravidade
print("Peso equivalente em %s igual %.2f"%(planeta,pesoPlaneta))