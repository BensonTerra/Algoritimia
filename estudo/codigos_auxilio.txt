#função ler ficheiro, permite ler o ficheiro por linhas sem que seja necessario repeitir codigo no restante do sistema
"""
def lerFicheiroLinhas():
    f = open(ficheiro, "r", encoding="utf-8")
    linhas = f.readlines()
    num = len(linhas)
    print(num)

    for linha in linhas:
        linha = linha.replace("\n","")
        linha = linha.split(";")
        print(linha)
    f.close()
"""