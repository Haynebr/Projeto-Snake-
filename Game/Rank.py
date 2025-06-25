import pygame
import sys
import json
from Game import Colors

pygame.init()

# Configurações de resolução da tela
largura, altura = 1225, 750
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ranking de Jogadores")

# Cores padronizadas
fundo = Colors.Tema_Base.cor_fundo_tela
cor_texto = Colors.Tema_Base.cor_letras
cor_titulo = Colors.Tema_Base.cor_texto_nome_do_poder
cor_borda = Colors.Tema_Base.cor_borda_tela

# Fonte
fonte_titulo = pygame.font.Font("Assets/text/Pixeltype.ttf", 60)
fonte_ranking = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)


# Função para carregar ranking
def carregar_ranking():
    try:
        with open("ranking.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Função para salvar ranking
def salvar_ranking(ranking):
    with open("ranking.json", "w") as f:
        json.dump(ranking, f, indent=4)

# Função para exibir o ranking
def exibir_ranking(ranking):
    tela.fill(fundo)

    # Título
    titulo = fonte_titulo.render("RANKING", True, cor_titulo)
    rect_titulo = titulo.get_rect(center=(largura // 2, 50))
    tela.blit(titulo, rect_titulo)

    # Ordenar ranking
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    # Mostrar top 5
    y = 120
    for i, (nome, pontuacao) in enumerate(ranking_ordenado[:5], start=1):
        linha = fonte_ranking.render(f"{i}. {nome} - {pontuacao}", True, cor_texto)
        rect_linha = linha.get_rect(center=(largura // 2, y))
        tela.blit(linha, rect_linha)

        # Borda opcional
        pygame.draw.rect(tela, cor_borda, rect_linha.inflate(20, 10), 2)
        y += 50

    pygame.display.update()

    # Espera até o usuário fechar
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                aguardando = False
            elif evento.type == pygame.KEYDOWN:
                aguardando = False


def main():
    
    nome = "Jogador1"
    pontuacao = 42 

    ranking = carregar_ranking()
    if nome in ranking:
        ranking[nome] = max(ranking[nome], pontuacao)
    else:
        ranking[nome] = pontuacao

    salvar_ranking(ranking)
    exibir_ranking(ranking)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
