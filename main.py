from gerador_sudoku import gera_tabuleiro, gera_desafio
from pdf_sudoku import cria_pdf
from PIL import Image

if __name__ == "__main__":
    # Dificuldades e número de desafios
    dificuldades = ['facil', 'medio', 'dificil']
    num_desafios = 25
    desafios = {dificuldade: [] for dificuldade in dificuldades}

    # Gera os desafios
    for dificuldade in dificuldades:
        for _ in range(num_desafios):
            tabuleiro_solucao = gera_tabuleiro()  # Gera a solução
            desafio = gera_desafio(tabuleiro_solucao, dificuldade=dificuldade)  # Gera o desafio
            desafios[dificuldade].append((desafio, tabuleiro_solucao))  # Armazena o desafio e a solução

    # Caminho para o PDF da imagem de fundo

    fundo_path = "assets/background_image.png"  # Substitua pelo caminho da sua imagem de fundo (JPEG ou PNG)

    print(fundo_path)  # Verifique se o caminho está correto

    try:
        img = Image.open(fundo_path)
        #img.show()  # Isso deve abrir a imagem se estiver correta
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")

    # Cria o PDF com os desafios e o fundo
    cria_pdf(dificuldades, desafios, fundo_path=fundo_path, filename="sudoku.pdf")