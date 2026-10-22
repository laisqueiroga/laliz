# laliz
#Projeto 1 Desoft
def define_posicoes(linha, coluna, orientacao,tamanho):
    lista = []
    if orientacao == "horizontal":
        i = 0
        while i<tamanho:
            lista.append([linha,coluna+i])
            i = i+1    
    elif orientacao == "vertical":
        i = 0
        while i<tamanho:
            lista.append([linha+i,coluna])
            i = i+1
    return lista
