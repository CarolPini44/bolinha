from funcoes import posicao_valida, define_posicoes, preenche_frota

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
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                posicionado = True
            else:
                print("Esta posição não está válida!")

    print(frota)

if __name__ == "__main__":
    main()

