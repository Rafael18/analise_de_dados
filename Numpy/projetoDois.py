import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    """Coloca a peça do jogador na posição escolhida"""
    tabuleiro[linha][coluna] = peca

def vetifica_vitoria(tabuleiro, peca):
    """Verifica se o jogador ganhou o jogo"""
    linhas = np.any(np.all(tabuleiro == peca, axis= 1))
    colunas = np.any(np.all(tabuleiro == peca, axis= 0))
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    return linhas or colunas or diagonais

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro de forma legivel para o jogador"""
    for linha in tabuleiro:
        print(" | ".join(str(x) if x != 0 else " " for x in linha))
        print("-" * 8)

#TODO
def jogo():
    """Função principal para rodar o jogo da velha"""
    print('FALTA TERMINAR')