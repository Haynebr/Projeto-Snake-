import pygame
import sys
from Game import Main, Map, Config, Colors

pygame.init()
# Tela
# Configurações do mapa
cell_size = Map.MapClass.cell_size  # Tamanho de cada célula da grid (em px)
map_width = Map.MapClass.map_width   # Nº de células na horizontal
map_height = Map.MapClass.map_height  # Nº de células na vertical

# Calcula o tamanho da janela em pixels com base no tamanho do grid
screen_width = cell_size * map_width
screen_height = cell_size * map_height

# Cria a janela do jogo com o tamanho definido
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Projeto Snake Game")

clock = pygame.time.Clock()
# Cores
PRETO = Colors.PRETO
BRANCO = Colors.BRANCO
AMARELO = Colors.AMARELO
CINZA = Colors.CINZA
# Fontes
fonte_titulo = pygame.font.Font("Assets/text\Pixeltype.ttf", 60)
fonte_opcao = pygame.font.Font("Assets/text\Pixeltype.ttf", 40)
# Opções
opcoes = ["Start", "Options", "Exit"]
opcao_selecionada = 0
# Retângulos dos botões
botoes = [
    pygame.Rect(screen_width // 2 - 100, screen_height // 3, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 90, 200, 50),
    pygame.Rect(screen_width // 2 - 100, screen_height // 3 + 180, 200, 50),
]
# Clock
clock = pygame.time.Clock()
rodando = True
#LOOP PRINCIPAL
while rodando:
    screen.fill(PRETO)
    # Título
    titulo = fonte_titulo.render("Snake Game",True,BRANCO)
    screen.blit(titulo, (screen_width //
                        2 - titulo.get_width() //
                        2, screen_height // 4))
    # POSICIONA O MOUSE
    mouse = pygame.mouse.get_pos()
    clicando = pygame.mouse.get_pressed()[0]
    # FORMATA O BOTÃO
    for i in range(len(botoes)):
        botao = botoes[i]
        # COR PADRÃO
        cor = BRANCO
        # HOVER DO MOUSE PARA PROVOCAR ANIMAÇÃO
        if botao.collidepoint(mouse):
            cor = AMARELO
            if clicando:
                cor = CINZA
                opcao_selecionada = i  
        # SELEÇÃO VIA TECLADO
        if i == opcao_selecionada:
            cor = AMARELO
        pygame.draw.rect(screen, cor, botao, border_radius=8)
        # TEXTO DO BOTÃO
        texto = fonte_opcao.render(opcoes[i], True, PRETO)
        screen.blit(texto, (botao.centerx - texto.get_width() // 2,
                        botao.centery - texto.get_height() // 2))
    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    #EVENTO DO BOTÃO DO MOUSE 
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(botoes)):
                if botoes[i].collidepoint(mouse):
                    if i == 0:
                        Main.main(map_width, map_height, screen, cell_size, clock)
                    elif i == 1:
                        Config.gameConfigs(screen, screen_width, screen_height, fonte_opcao)
                    elif i == 2:
                        rodando = False
    #EVENTO DO BOTÃO DO TECLADO(setinha pra cima,baixo e ENTER)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
            if evento.key == pygame.K_UP:
                opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
            if evento.key == pygame.K_RETURN:
                if opcao_selecionada == 0:
                    Main.main(map_width, map_height, screen, cell_size, clock)
                elif opcao_selecionada == 1:
                    Config.gameConfigs(screen, screen_width, screen_height, fonte_opcao)
                elif opcao_selecionada == 2:
                    rodando = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()