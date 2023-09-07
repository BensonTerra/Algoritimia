"""
Este programa calcula e analisa os dados de faturação mensal para um ano.

Inclui as seguintes funções:
- maior_faturacao(lista): Retorna o mês com a maior faturação.
- menor_faturacao(lista): Retorna o mês com a menor faturação.
- media_faturacao(lista): Calcula a média da faturação mensal.

O usuário é solicitado a inserir os valores de faturação para cada mês, e o programa
calcula e exibe as seguintes informações:
- O mês com a maior faturação.
- O mês com a menor faturação.
- A média da faturação mensal com base nos valores inseridos.
"""
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] #postos de trabalho
faturação = [800,900,1100,1210,1320,1570,1400,1300,750,900,1400,1350] #mascaras

def maior_faturacao(lista): #Função que devolve o mes com de maior faturação
    """
     return the month of higher value 
    """
    maior = max(lista)
    #print(maior)
    pos = lista.index(maior)
    #print(pos)
    mes = meses[pos]
    #print(mes)
    return mes

def menor_faturacao(lista): #Função que devolve o mes de menor faturacao
    menor = min(lista)
    pos = lista.index(menor)
    mes = meses[pos]
    return mes

def media_faturacao(lista): # Função que devolve a media de faturacao mensal
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
            print("O valor inserido é inválido. Por favor tente novamente!")
        else:
            faturacao.append(valor)                # Acrescenta à lista de faturacao
            #print(faturacao)
            break
mes_maior = maior_faturacao(faturacao)
mes_menor = menor_faturacao(faturacao)
media = media_faturacao(faturacao)

print("\nMês de maior faturação  :", mes_maior)
print("\nMês de menor faturação  :", mes_menor)
print("\n Valor médio de faturação {:.2f}:" .format(media))

