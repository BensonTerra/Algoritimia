import random
resposta=random.randint(1,50)
print(resposta)
count=1
num=int(input("Introduza um numero de 1 a 50: "))

while resposta!=num and count<11:
    if num<resposta:
        print("Maior")
        count+=1
    else:
        print("menor")
        count+=1
    num=int(input("Introduza um numero de 1 a 50: "))
if num==resposta:
    print("parabens. tentativa %i"%count)
else:  
    print("limite de jogadas atingido")
