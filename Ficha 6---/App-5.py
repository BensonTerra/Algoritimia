
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] #postos de trabalho
faturação = [800,900,1100,1210,1320,1570,1400,1300,750,900,1400,1350] #mascaras

def maior_faturacao(lista):
    """
     return the month of higher value 
    """
    maior = max(lista)
    print(maior)
    pos = lista.index(maior)
    print(pos)
    mes = meses[pos]
    print(mes)
    return mes

def menor_faturacao(lista):
       # Função que devolve o mes de menor faturacao
    menor = min(lista)
    pos = lista.index(menor)
    mes = meses[pos]
    return mes

def media_faturacao(lista):
       # Função que devolve a media de faturacao mensal
    return sum(lista) / len(lista)



# Inicio do programa-----
faturacao = []
for i in range(12):         # ciclo para ler a faturação dos 12 meses
    while True:       # ciclo para validar a inserção de valores válidos
        try:
            valor =faturação[i]
            print("Faturação do mês {0} : {1}" .format(meses[i],valor))
            #valor = int(input("Faturação do mês {0} : " .format(meses[i])))
        except ValueError:
            print("O valor inserido é inválido. Pf tente novamente!")
        else:
            faturacao.append(valor)                # Acrescenta à lista de faturacao
            print(faturacao)
            break
mes_maior = maior_faturacao(faturacao)
mes_menor = menor_faturacao(faturacao)
media = media_faturacao(faturacao)

print("\n Mês de maior faturação  :", mes_maior)
print("\nMês de menor faturação  :", mes_menor)
print("\n Valor médio de faturação {:.2f}:" .format(media))

