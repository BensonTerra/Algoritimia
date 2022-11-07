'''
Implemente a função romanNumeral que receba um número entre 1 e 
999 (pedido ao utilizador) e devolva o mesmo valor em numeração 
Romana
'''

import os #biblioteca os
autoStart="y"

def int_to_rom(num):
    resposta="numero em romano: "
    while num>0:
        if num>=900:
            num=num-900
            resposta+="CM"
        elif num>=500:
            num=num-500
            resposta+="D"
        elif num>=400:
            num=num-400
            resposta+="ID"
        elif num>=100:
            num=num-100
            resposta+="C"
        elif num>=90:
            num=num-90
            resposta+="XC"
        elif num>=50:
            num=num-50
            resposta+="L"
        elif num>=40:
            num=num-40
            resposta+="XL"
        elif num>=10:
            num=num-10
            resposta+="X"
        elif num>=9:
            num=num-9
            resposta+="IX"
        elif num>=5:
            num=num-5
            resposta+="V"
        elif num>=4:
            num=num-4
            resposta+="IV"
        else:
            num=num-1
            resposta+="I"
    print(resposta)

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        numero=int(input("Digite um numero: "))
        if numero<=0 or numero>999:
            raise ValueError
        else:
            int_to_rom(numero)
    except ValueError:
        print("Valor inválido")
    except:
        print("Erro desconhecido")
    else:
        autoStart = input("Repetir(Y/N) ?: ")
    


