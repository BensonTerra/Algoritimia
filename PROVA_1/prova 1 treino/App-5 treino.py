

def pares(numero):
    cont=0
    for i in range(len(numero)):
        if numero[i] % 2 == 0:
            cont += 1
    return cont

numero = []
n = int(input("Quantos numeros deseja ler: "))
for i in range(1,n+1):
    num = int(input("Introduza %i: "%i))
    numero.append(num)
pares(numero)
print("A lista contém {0} números pares".format(pares(numero)))
