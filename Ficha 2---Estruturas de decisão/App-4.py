peso=float(input("Digite seu Peso: "))
altura=float(input("Digite sua altura(m): "))
IMC=peso/altura**2
print("%.2f"%IMC)
if(IMC<18.5):
    print("Abaixo do peso")
elif(IMC>=18.6 and IMC<=24.9):
    print("Saudável")
elif(IMC>=25 and IMC<=29.9):
    print("Sobrepeso")
elif(IMC>=30 and IMC<=34.9):
    print("Obesidade Grau 1")
elif(IMC>=35 and IMC<=39.9):
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")