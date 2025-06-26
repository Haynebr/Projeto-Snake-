import pygame
import sys
import json
from Game import Colors, Cadastro

pygame.init()

# Configurações de resolução da tela
largura, altura = 1225, 750
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ranking de Jogadores")

# Cores padronizadas

# Fonte
fonte_titulo = pygame.font.Font("Assets/text/Pixeltype.ttf", 60)
fonte_ranking = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)


# Função para carregar ranking
def carregar_ranking():
    try:
        with open("ranking.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar ranking
def salvar_ranking(ranking):
    with open("ranking.json", "w") as f:
        json.dump(ranking, f, indent=4)

# Função para exibir o ranking
def exibir_ranking(Tema):
    tela.fill(Tema.cor_fundo_tela)

    ranking = carregar_ranking()
    ranking_ordenado = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)

    # Título
    titulo = fonte_titulo.render("RANKING", True, Tema.cor_selecao)
    rect_titulo = titulo.get_rect(center=(largura // 2, 50))
    tela.blit(titulo, rect_titulo)

    # Mostrar top 5
    y = 120
    for i, jogador in enumerate(ranking_ordenado[:5], start=1):
        linha = fonte_ranking.render(f"{i}. {jogador['nome']} - {jogador['pontuacao']}", True, Tema.cor_letras)
        rect_linha = linha.get_rect(center=(largura // 2, y))
        tela.blit(linha, rect_linha)
        pygame.draw.rect(tela, Tema.cor_borda_tela, rect_linha.inflate(20, 10), 2)
        y += 50

    pygame.display.update()

    # Espera até o usuário fechar
    aguardando = True
    while aguardando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN:
                aguardando = False


def add_to_rank(score):
    nome = Cadastro.nome_cadastrado
    ranking = carregar_ranking()

    atualizado = False
    for jogador in ranking:
        if jogador["nome"] == nome:
            if score > jogador["pontuacao"]:
                jogador["pontuacao"] = score
            atualizado = True
            break
        
    if not atualizado:
        ranking.append({"nome": nome, "pontuacao": score})

    salvar_ranking(ranking)