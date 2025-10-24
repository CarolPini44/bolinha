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

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]

    return frota

frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3
y = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(y)

