count=1
maior=0
soma=0
for i in range(10):
    numero=int(input("Escreva um valor %i: "%count))
    soma+=numero
    count+=1
    if numero > maior:
        maior = numero
media=soma/10
print("Media = %.2f"%media)
print("Maior = %i"%maior)