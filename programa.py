from funcoes import posicao_valida, define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, monta_tabuleiros, y

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
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if tamanho == 1:
                orientacao = 'horizontal'
            else:
                x = int(input("1 vertical e 2 horizontal >"))
                orientacao = 'vertical' if x == 1 else 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                posicionado = True
            else:
                print("Esta posição não está válida!")

def y(mensagem):
    entrada = input(mensagem)
    while True:
        if entrada.isdigit():
            valor = int(entrada)
            if valor >= 0 and valor <= 9:
                return valor
        print("Entrada inválida!")
        entrada = input(mensagem)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

soma_navios_op = 0
for lista in frota_oponente.values():
    for navio in lista:
        soma_navios_op = soma_navios_op + 1

ataques = []

jogar = True

while jogar:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha_de_ataque = y('')
    coluna_de_ataque = y('')
    repete = False
    i = 0
    while i < len(ataques):
        p = ataques[i]
        if p[0] == linha_de_ataque and p[1] == coluna_de_ataque:
            repete = True
        i+=1

    if repete == True:
        print('A posição linha', linha_de_ataque,  'e coluna', coluna_de_ataque, 'já foi informada anteriormente!')
    else:
        ataques.append([linha_de_ataque, coluna_de_ataque])
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_de_ataque, coluna_de_ataque)
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    afundades = afundados(frota_oponente, tabuleiro_oponente)
    if afundades == soma_navios_op:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogar = False
