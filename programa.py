from funcoes import*

frota = {}

tamanhos = {"porta-aviões": 4, "navio-tanque": 3, "contratorpedeiro": 2, "submarino": 1}
quantidades = {"porta-aviões": 1, "navio-tanque": 2, "contratorpedeiro": 3, "submarino": 4}

for navio, tamanho in tamanhos.items():
    i = 0
    while i < quantidades[navio]:
        print("Insira as informações referentes ao navio", navio, "que possui tamanho", tamanho)
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if navio == "submarino":
            orientacao = "vertical"
        else:
            escolha = int(input("[1] Vertical [2] Horizontal> "))
            if escolha == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'
        if posicao_valida(frota,linha,coluna,orientacao,tamanho):
            frota = preenche_frota(frota,navio,linha,coluna,orientacao,tamanho)
            i +=1
        else:
            print("Esta posição não está válida!")
print(frota)