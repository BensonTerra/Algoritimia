"""
Elabore um programa que leia uma lista de 10 números inteiros. 
Em seguida, dado um determinado valor de pesquisa, invoque a função searchNumber(lista, pesquisa) que deve devolver as posições em que encontra o valor de pesquisa, 
na lista.
"""

from random import randint

def generatePassword(username):
        password = ""
        if username.find(" ") == -1:
            for i in range(len(username)):
                if (i+1)%2 == 0:
                    password += username[i]
                else:
                    password += str(randint(1,9))
            password += str(randint(1,9))
            password += str(len(username))
        else:
            password = 'Username Inválido!'

        return password

print(generatePassword('Carlos'))