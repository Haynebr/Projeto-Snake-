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

# Em Game/Utils.py

def player_wins(screen, screen_w, screen_h, medium_font, small_font, player, final_score=""):
    # Define a posição do texto "Press ENTER" dependendo se há um vencedor ou não
    subtext_position_y = screen_h // 1.7

    if player != 0:
        # Define a cor baseada em quem ganhou
        if player == 1: txt_color = Colors.VERDE
        elif player == 2: txt_color = Colors.CIANO
        else: txt_color = Colors.MAGENTA # Empate

        # Define o texto baseado em quem ganhou
        if player != 3:
            win_text = f"Player {player} Wins!"
        else:
            win_text = "DRAW!"
        
        text_surface = medium_font.render(win_text, True, txt_color).convert_alpha()
        text_rect = text_surface.get_rect(center = (screen_w // 2, screen_h // 2))
        screen.blit(text_surface, text_rect)
    else:
        # Se for single player (player 0), ajusta a posição do subtexto
        subtext_position_y = screen_h // 2.2
    
    # --- NOVO BLOCO PARA DESENHAR O SCORE FINAL ---
    if final_score: # Só desenha se uma string de score foi passada
        score_surf = small_font.render(final_score, True, Colors.BRANCO)
        score_rect = score_surf.get_rect(center = (screen_w // 2, screen_h // 1.8))
        screen.blit(score_surf, score_rect)
        # Ajusta a posição do "Press Enter" para não sobrepor o score
        subtext_position_y += 30

    # Desenha o subtexto "Press ENTER"
    subtext_color = Colors.AMARELO
    subtext_surface = small_font.render(f"* press ENTER to continue *", True, subtext_color).convert_alpha()
    subtext_rect = subtext_surface.get_rect(center = (screen_w // 2, subtext_position_y))
    screen.blit(subtext_surface, subtext_rect)