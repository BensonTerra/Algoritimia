"""
Altere o programa anterior de modo a incluir também a leitura dos nomes dos participantes no concurso
"""
import os #biblioteca os
autoStart="y"

def positiveList(listaNomes,listaNotas):
    counter = 0
    pNomes = []
    pNotas = []
    for i in range(0, len(listaNomes)):
        if listaNotas[i]>=10:
            pNomes.append(listaNomes[i])
            pNotas.append(listaNotas[i])
    return pNomes, pNotas

while autoStart == "Y" or autoStart == "y":
    try:
        os.system("cls")
        aluno = []
        score = []
        i=1
        nota=10
        while i <=3:
            nome=str(input("Digite um nome: "))
            #nota =int(input("Nota do aluno nº %i: "%i))
            if nota<0 or nota>20:
                raise ValueError()
            aluno.append(nome)
            score.append(nota)
            nota+=1
            i+=1
        pNomes,pNotas = positiveList(aluno,score)

        print("Aluno com nota superior a 10: %s" % pNomes)
        print("Notas superiores a 10: %s" % pNotas)
    except ValueError:
        print("Valor invalido: %i"%nota)
    else:

        autoStart = input("Repetir(Y/N) ?: ")
