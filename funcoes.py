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

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
   
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for r, c in posicoes:
        if r < 0 or r > 9 or c < 0 or c > 9:
            return False
    for lista_navios in frota.values():
        for navio in lista_navios:
            for parte in navio:
                if parte in posicoes:
                    return False

    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
