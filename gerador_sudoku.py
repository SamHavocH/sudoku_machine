import random

def gera_tabuleiro():
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    preenche_tabuleiro(tabuleiro)
    return tabuleiro

def preenche_tabuleiro(tabuleiro):
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for numero in numeros:
                    if verifica_numero(tabuleiro, i, j, numero):
                        tabuleiro[i][j] = numero
                        if preenche_tabuleiro(tabuleiro):
                            return True
                        tabuleiro[i][j] = 0
                return False
    return True

def verifica_numero(tabuleiro, linha, coluna, numero):
    for i in range(9):
        if tabuleiro[linha][i] == numero or tabuleiro[i][coluna] == numero:
            return False
    linha_inicial = (linha // 3) * 3
    coluna_inicial = (coluna // 3) * 3
    for i in range(linha_inicial, linha_inicial + 3):
        for j in range(coluna_inicial, coluna_inicial + 3):
            if tabuleiro[i][j] == numero:
                return False
    return True

def gera_desafio(tabuleiro, dificuldade='facil'):
    desafio = [linha[:] for linha in tabuleiro]  # Copia o tabuleiro
    if dificuldade == 'facil':
        num_remover = 40  # Remover poucos números
    elif dificuldade == 'medio':
        num_remover = 60  # Remover uma quantidade mediana
    elif dificuldade == 'dificil':
        num_remover = 70  # Remover muitos números
    else:
        raise ValueError("Dificuldade deve ser 'facil', 'medio' ou 'dificil'.")

    for _ in range(num_remover):
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        while desafio[linha][coluna] == 0:  # Garante que não remova um número já removido
            linha = random.randint(0, 8)
            coluna = random.randint(0, 8)
        desafio[linha][coluna] = 0  # Remove um número
    return desafio
