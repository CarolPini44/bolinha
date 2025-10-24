def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for c in range(coluna, coluna + tamanho):
            posicoes.append([linha, c])
    elif orientacao == 'vertical':
        for r in range(linha, linha + tamanho):
            posicoes.append([r, coluna])
    return posicoes


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


def preenche_frota(frota, nome_do_navio, posicoes):
    if nome_do_navio in frota:
        frota[nome_do_navio].append(posicoes)
    else:
        frota[nome_do_navio] = [posicoes]
    return frota




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

