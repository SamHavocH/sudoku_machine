from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

def cria_pdf(dificuldades, desafios, fundo_path=None, filename="sudoku.pdf"):
    # Cria um PDF temporário
    temp_pdf_path = "temp_sudoku.pdf"
    c = canvas.Canvas(temp_pdf_path, pagesize=letter)
    largura, altura = letter

    # Definindo margens
    margem_esquerda = 75
    margem_direita = 87
    margem_superior = 145
    margem_superior_grade = margem_superior + 35
    margem_superior_numeros = margem_superior + 20
    margem_inferior = 50

    # Tamanho da célula
    tamanho_celula = 50

    # Função para desenhar a grade
    def desenha_grade():
        # Linhas finas para a grade
        c.setLineWidth(1)
        for i in range(10):
            c.line(margem_esquerda, altura - margem_superior_grade - i * tamanho_celula, 
                    largura - margem_direita, altura - margem_superior_grade - i * tamanho_celula)
        for j in range(10):
            c.line(margem_esquerda + j * tamanho_celula, altura - margem_superior_grade, 
                    margem_esquerda + j * tamanho_celula, altura - margem_superior_grade - 9 * tamanho_celula)

        c.setLineWidth(2)
        for i in range(0, 10, 3):
            c.line(margem_esquerda, altura - margem_superior_grade - i * tamanho_celula, 
                    largura - margem_direita, altura - margem_superior_grade - i * tamanho_celula)
            c.line(margem_esquerda + i * tamanho_celula, altura - margem_superior_grade, 
                    margem_esquerda + i * tamanho_celula, altura - margem_superior_grade - 9 * tamanho_celula)

    # Função para desenhar o título e o conteúdo
    def desenha_conteudo(titulo, conteudo, y_inicial):
        c.setFont("Helvetica-Bold", 20)
        c.drawString(margem_esquerda, y_inicial, titulo)
        
        c.setFont("Helvetica", 16)
        y = y_inicial - 30  # Aumenta a distância do título para o conteúdo
        desenha_grade()
        for linha in conteudo:
            for j, num in enumerate(linha):
                if num != 0:
                    # Centraliza o número na célula
                    texto = str(num)
                    largura_texto = c.stringWidth(texto, "Helvetica", 16)
                    # Centraliza horizontalmente
                    x = margem_esquerda + j * tamanho_celula + (tamanho_celula - largura_texto) / 2
                    y_texto = y - (tamanho_celula / 2) - 10
                    c.drawString(x, y_texto, texto)
            y -= tamanho_celula

    # Função para desenhar o fundo
    def desenha_fundo():
        if fundo_path:
            try:
                c.drawImage(fundo_path, 0, 0, largura, altura)  # Ajusta a imagem para cobrir toda a página
            except Exception as e:
                print(f"Erro ao desenhar a imagem de fundo: {e}")

    # Desenho do índice

    # c.setFont("Helvetica", 16)
    # y_index = altura - margem_superior - 70
    # for dificuldade, desafios_dificuldade in desafios.items():
    #     for i, (desafio, solucao) in enumerate(desafios_dificuldade):
    #         c.drawString(margem_esquerda, y_index, f"{dificuldade.capitalize()} - Desafio {i + 1}")
    #         y_index -= 20
    #         if y_index < margem_inferior:
    #             c.showPage()
    #             desenha_fundo()  # Desenha o fundo na nova página
    #             c.setFont("Helvetica-Bold", 24)
    #             c.drawString(margem_esquerda, altura - margem_superior, "Índice de Desafios")
    #             c.setFont("Helvetica", 16)
    #             y_index = altura - margem_superior - 10

    # Adiciona uma nova página para cada desafio
    for dificuldade, desafios_dificuldade in desafios.items():
        for i, (desafio, solucao) in enumerate(desafios_dificuldade):
            c.showPage()
            desenha_fundo()  # Desenha o fundo na nova página
            desenha_conteudo(f"{dificuldade.capitalize()} - Desafio {i + 1}", desafio, altura - margem_superior)

    # Adiciona uma nova seção para as soluções
    c.showPage()
    desenha_fundo()  # Desenha o fundo na nova página
    c.setFont("Helvetica-Bold", 24)
    c.drawString(margem_esquerda, altura - margem_superior, "Soluções dos Desafios")
    
    # Desenha as soluções, cada uma em uma nova página
    for dificuldade, desafios_dificuldade in desafios.items():
        for i, (desafio, solucao) in enumerate(desafios_dificuldade):
            c.showPage()  # Adiciona uma nova página para cada solução
            desenha_fundo()  # Desenha o fundo na nova página
            desenha_conteudo(f"{dificuldade.capitalize()} - Solução {i + 1}", solucao, altura - margem_superior)

    c.save()