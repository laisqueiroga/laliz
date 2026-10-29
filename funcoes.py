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

def posiciona_frota(frota):
    tabuleiro = []
    i = 0
    while i<10:
        lista = []
        j = 0
        while j<10:
            lista.append(0)
            j = j+1
        tabuleiro.append(lista)
        i = i+1
    for nome, posicoes in frota.items():
        for coordenadas in posicoes:
            l = 0
            while l<len(coordenadas):
                linha = coordenadas[l][0]
                coluna = coordenadas[l][1]
                tabuleiro[linha][coluna] = 1
                l = l+1
    return tabuleiro



