import os

os.system("cls")

lista_1 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
lista_2 = [12, 3, 5, 7, 14, 18, 21, 7, 9, 8]

# Convertemos a segunda lista em um conjunto para tornar a busca mais eficiente
conjunto_lista_2 = set(lista_2)

elementos_comuns = set()

for elemento in lista_1:
    if elemento in conjunto_lista_2:
        elementos_comuns.add(elemento)
        print(elementos_comuns)
        input()

elementos_comuns = sorted(list(elementos_comuns))

if elementos_comuns:
    resposta = ", ".join(map(str, elementos_comuns))
    print(f"Existem {len(elementos_comuns)} elementos que se repetem, e eles são: {resposta}.")
else:
    print("Não existem elementos comuns nas duas listas.")

input()
