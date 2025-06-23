import pygame
from Game import Colors

def grid_to_pixel(position, cell_size):
    x = position[0] * cell_size
    y = position[1] * cell_size
    return (x, y)

def draw_rect(screen, position, color, cell_size):
    pygame.draw.rect(
        screen,
        color,
        (*grid_to_pixel(position, cell_size), cell_size, cell_size)
    )

def verificar_colisao(pos1, pos2):
    return pos1 == pos2

def get_snakes_positions(snakes): # Pega as posições de ambas as cobras
    positions = []
    for snake in snakes:
        positions += snake.snake_pos
    return positions

def is_head_at_position(position, snakes): # verifica se a cabeça de alguma cobra está na posição enviada
    return any(snake.snake_pos[0] == position for snake in snakes)

def game_over(screen, screen_w, screen_h, font):
    gOver_surface = font.render("Game Over", False, (255, 0, 0)).convert_alpha()
    gOver_rect = gOver_surface.get_rect(center = (screen_w // 2, screen_h // 2.5))
    screen.blit(gOver_surface, gOver_rect)

def player_wins(screen, screen_w, screen_h, medium_font, small_font, player):
    if player != 0:
        subtext_position = screen_h // 1.7
        if player == 1:
            txt_color = Colors.VERDE
        if player == 2:
            txt_color = Colors.CIANO
        if player == 3:
            txt_color = Colors.MAGENTA
        if player != 3: text_surface = medium_font.render(f"Player {player} Wins!", False, txt_color).convert_alpha()
        else: text_surface = medium_font.render(f"DRAW!", False, txt_color).convert_alpha()
        text_rect = text_surface.get_rect(center = (screen_w // 2, screen_h // 2))
        screen.blit(text_surface, text_rect)
    else: subtext_position = screen_h // 2.2

    subtext_color = Colors.AMARELO
    subtext_surface = small_font.render(f"*  press ENTER to continue  *", False, subtext_color).convert_alpha()
    subtext_rect = subtext_surface.get_rect(center = (screen_w // 2, subtext_position))
    screen.blit(subtext_surface, subtext_rect)

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False