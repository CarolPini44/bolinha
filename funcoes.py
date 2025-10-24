def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicoes = []
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],]
    
    if orientacao == 'vertical':
        for i in range(tamanho):
            lista_posicoes.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            lista_posicoes.append([linha, coluna + i])
    
    return lista_posicoes

def preenche_frota(frota, nome_do_navio, linha, coluna, orientacao, tamanho):
    
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_do_navio not in frota:
        frota[nome_do_navio] = [posicoes]
    else:
        frota[nome_do_navio].append(posicoes)
        

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for linha in range(10):
        linha = []
        for coluna in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for navios in frota:
        for qnt_navio in frota[navios]:
            for pos in qnt_navio:
                linha = pos[0]
                coluna = pos[1]
                tabuleiro[linha][coluna] = 1  
    return tabuleiro

def afundados(frota, tabuleiro):
    total_afundados = 0

    
    for navios in frota.values():
        for navio in navios:
            afundado = all(tabuleiro[linha][coluna] == 'X' for linha, coluna in navio)
            if afundado:
                total_afundados += 1

    return total_afundados