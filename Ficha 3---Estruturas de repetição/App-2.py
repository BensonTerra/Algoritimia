count=1
maior=0
soma=0
limite=int(input("Defina quantos numeros a ler: "))
for i in range (limite):
    numero=int(input("Escreva um valor %i: "%count))
    soma+=numero
    count+=1
    if numero > maior:
        maior = numero
media=soma/limite
print("Media = %.2f"%media)
print("Maior = %i"%maior)