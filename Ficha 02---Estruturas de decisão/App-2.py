Lado1=float(input("valor do lado 1: "))
Lado2=float(input("valor do lado 2: "))
Lado3=float(input("valor do lado 3: "))
if(Lado1==Lado2 and Lado1==Lado3 and Lado2==Lado3):
    print("triangulo equilatero")
elif(Lado1==Lado2 or Lado1==Lado3):
    print("triangulo isosceles")
else:
    print("triangulo escaleno")