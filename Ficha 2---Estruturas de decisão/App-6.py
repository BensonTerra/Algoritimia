genero=input("Defina seu genero(M/F): ")
idade=int(input("Defina sua idade: "))
if(genero=="M" or genero=="m"):
    FCM=220
else:
    FCM=226
BPM=FCM-idade
print(BPM)   
