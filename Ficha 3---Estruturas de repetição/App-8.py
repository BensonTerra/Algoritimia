import os #biblioteca os
autoStart="y"

while autoStart == "Y" or autoStart == "y":
    os.system("cls")
    termoP2=1
    termoP1=0
    termos="0"

    nTermos=int(input("Escreva um numero: "))
    if nTermos>=1:
        termos= "0"
    else:
        termos=termos+", 1"
    
    for i in range(nTermos):
        termoP3=termoP2+termoP1
        termos = termos +", "+str(termoP3)
        termoP1=termoP2
        termoP2=termoP3
    print("primeiros %i termos da sequencia: %s" % (nTermos, termos))
    autoStart = input("Repetir(Y/N) ?: ")


