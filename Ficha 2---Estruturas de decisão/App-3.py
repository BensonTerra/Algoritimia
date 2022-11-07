genero=input("Defina seu genero(M/F): ")
altura=int(input("Defina sua altura(cm): "))
if(genero=="M" or genero=="m"):
    k=4
else:
    k=2
pesoIdeal=(altura-100)-(altura-150)/k
print(pesoIdeal)   