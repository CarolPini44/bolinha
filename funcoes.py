def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicoes = []
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    if orientacao == 'vertical':
        for i in range(tamanho):
            lista_posicoes.append([linha + i, coluna])

    elif orientacao == 'horizontal':
        for i in range(tamanho):
            lista_posicoes.append([linha, coluna + i])
    
    return lista_posicoes

y = define_posicoes(2, 4 ,'vertical', 3)
print(y)
    

