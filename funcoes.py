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


def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome not in frota:
        frota[nome] = []
    frota[nome].append(posicao)
    return frota


def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
         tabuleiro[linha][coluna] = "X"
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro