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

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

embarcacoes = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

for nome, tamanho, quantidade in embarcacoes:
    for i in range(quantidade):
        posicionado = False
        while not posicionado:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if tamanho == 1:
                orientacao = 'horizontal'  
            else:
                opc = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = 'vertical' if opc == 1 else 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
                preenche_frota(frota, nome, posicoes)
                posicionado = True
            else:
                print("Esta posição não está válida!")

print(frota)