# Menu.py

import pygame
import sys
from Game import Main, Map, Config, Colors

pygame.init()

# --- Configurações Gerais ---
cell_size = Map.MapClass.cell_size
map_width = Map.MapClass.map_width
map_height = Map.MapClass.map_height

screen_width = cell_size * map_width
screen_height = cell_size * map_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Projeto Snake Game")
clock = pygame.time.Clock()

# Cores e Fontes
PRETO = Colors.PRETO
BRANCO = Colors.BRANCO
AMARELO = Colors.AMARELO
CINZA = Colors.CINZA

fonte_titulo = pygame.font.Font("Assets/text/Pixeltype.ttf", 60)
fonte_opcao = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)

# Opções do Menu
opcoes = ["Start", "Options", "Exit"]
opcao_selecionada = 0
botoes = [
    pygame.Rect(screen_width // 2 - 100, screen_height // 3, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 90, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 180, 200, 50),
]

rodando = True
# --- LOOP PRINCIPAL DO MENU ---
while rodando:
    screen.fill(PRETO)
    
    titulo = fonte_titulo.render("Snake Game", True, BRANCO)
    screen.blit(titulo, (screen_width // 2 - titulo.get_width() // 2, screen_height // 4))

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    for i, botao in enumerate(botoes):
        cor = BRANCO
        if botao.collidepoint(mouse_pos):
            cor = AMARELO
            if mouse_click:
                cor = CINZA
                opcao_selecionada = i
        
        if i == opcao_selecionada:
            cor = AMARELO

        pygame.draw.rect(screen, cor, botao, border_radius=8)
        texto = fonte_opcao.render(opcoes[i], True, PRETO)
        screen.blit(texto, (botao.centerx - texto.get_width() // 2, botao.centery - texto.get_height() // 2))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if botoes[0].collidepoint(mouse_pos): # Start
                Main.main(map_width, map_height, screen, cell_size, clock)
            elif botoes[1].collidepoint(mouse_pos): # Options
                Config.gameConfigs(screen, screen_width, screen_height, fonte_opcao)
            elif botoes[2].collidepoint(mouse_pos): # Exit
                rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
            if evento.key == pygame.K_UP:
                opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
            if evento.key == pygame.K_RETURN:
                if opcao_selecionada == 0: # Start
                    Main.main(map_width, map_height, screen, cell_size, clock)
                elif opcao_selecionada == 1: # Options
                    Config.gameConfigs(screen, screen_width, screen_height, fonte_opcao)
                elif opcao_selecionada == 2: # Exit
                    rodando = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()