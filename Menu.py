# Menu.py

import pygame
import sys
from Game import Main, Map, Config, Colors, Cadastro, Rank

pygame.init()

cell_size = Map.MapClass.cell_size
map_width = Map.MapClass.map_width
map_height = Map.MapClass.map_height
screen_width = cell_size * map_width
screen_height = cell_size * map_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Projeto Snake Game")
clock = pygame.time.Clock()

fonte_titulo = pygame.font.Font("Assets/text/Pixeltype.ttf", 60)
fonte_opcao = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)

opcoes = ["Start", "Options", "Ranking", "Exit"]
opcao_selecionada = 0
botoes = [
    pygame.Rect(screen_width // 2 - 100, screen_height // 3, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 90, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 180, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 270, 200, 50),
]

Cadastro

rodando = True
while rodando:
    # --- LÓGICA DE TEMA COMPLETA ---
    if Config.dictConfigs['Theme'] == 0: Tema = Colors.Tema_Base
    elif Config.dictConfigs['Theme'] == 1: Tema = Colors.Tema_claro
    elif Config.dictConfigs['Theme'] == 2: Tema = Colors.Tema_Synthwave
    elif Config.dictConfigs['Theme'] == 3: Tema = Colors.Tema_Floresta
    elif Config.dictConfigs['Theme'] == 4: Tema = Colors.Tema_Oceano
    else: Tema = Colors.Tema_Base

    screen.fill(Tema.cor_fundo_tela)
    
    titulo = fonte_titulo.render("Snake Game", True, Tema.cor_letras)
    screen.blit(titulo, (screen_width // 2 - titulo.get_width() // 2, screen_height // 4))
    user_name = fonte_opcao.render(f"User: {Cadastro.nome_cadastrado}", True, Colors.AMARELO)
    screen.blit(user_name, (10, 720))

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    for i, botao in enumerate(botoes):
        cor_texto_botao = Tema.cor_fundo_tela
        cor_botao = Tema.cor_letras
        if botao.collidepoint(mouse_pos):
            cor_botao = Tema.cor_selecao
            if mouse_click:
                cor_botao = Colors.CINZA
                opcao_selecionada = i
        if i == opcao_selecionada:
            cor_botao = Tema.cor_selecao

        pygame.draw.rect(screen, cor_botao, botao, border_radius=8)
        texto = fonte_opcao.render(opcoes[i], True, cor_texto_botao)
        screen.blit(texto, (botao.centerx - texto.get_width() // 2, botao.centery - texto.get_height() // 2))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if botoes[0].collidepoint(mouse_pos): Main.main(map_width, map_height, screen, cell_size, clock)
            elif botoes[1].collidepoint(mouse_pos): Config.gameConfigs(screen, screen_width, screen_height, fonte_opcao)
            elif botoes[2].collidepoint(mouse_pos): Rank.exibir_ranking()
            elif botoes[3].collidepoint(mouse_pos): rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN: opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
            if evento.key == pygame.K_UP: opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
            if evento.key == pygame.K_RETURN:
                if opcao_selecionada == 0: Main.main(map_width, map_height, screen, cell_size, clock)
                elif opcao_selecionada == 1: Config.gameConfigs(screen, screen_width, screen_height, fonte_opcao)
                elif opcao_selecionada == 2: Rank.exibir_ranking(Tema)
                elif opcao_selecionada == 3: rodando = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()