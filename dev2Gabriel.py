def afundados(frota, tabuleiro):
    total_afundados = 0

    
    for navios in frota.values():
        for navio in navios:
            afundado = all(tabuleiro[linha][coluna] == 'X' for linha, coluna in navio)
            if afundado:
                total_afundados += 1

    return total_afundados

