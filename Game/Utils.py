import pygame
from Game import Colors, Config, Rank

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

def player_wins(screen, screen_w, screen_h, big_font, medium_font, small_font, player, Tema, final_score, p1_score):
    Rank.add_to_rank(p1_score)
    # Define a posição do texto "Press ENTER" dependendo se há um vencedor ou não
    subtext_position_y = screen_h // 1.7

    gOver_surface = big_font.render("Game Over", False, Tema.cor_comida_padrão).convert_alpha()
    gOver_rect = gOver_surface.get_rect(center = (screen_w // 2, screen_h // 2.5))

    if player != 0:
        # Define a cor baseada em quem ganhou
        if player == 1:
            txt_color = Tema.cor_cabeca_P1
        elif player == 2:
            txt_color = Tema.cor_cabeca_P2
        else:
            txt_color = Tema.cor_letras  # Empate

        # Define o texto baseado em quem ganhou
        win_text = f"Player {player} Wins!" if player != 3 else "DRAW!"
        
        text_surface = medium_font.render(win_text, True, txt_color).convert_alpha()
        text_rect = text_surface.get_rect(center=(screen_w // 2, screen_h // 2))
    else:
        text_surface = None
        text_rect = None
        subtext_position_y = screen_h // 2.2

    # Score final
    if final_score:
        score_surf = small_font.render(final_score, True, Colors.BRANCO).convert_alpha()
        score_rect = score_surf.get_rect(center=(screen_w // 2, screen_h // 1.8))
        subtext_position_y += 30
    else:
        score_surf = None
        score_rect = None

    # Subtexto
    subtext_color = Tema.cor_selecao
    subtext_surface = small_font.render("* press ENTER to continue *", True, subtext_color).convert_alpha()
    subtext_rect = subtext_surface.get_rect(center=(screen_w // 2, subtext_position_y))

    # Calcula a área que envolve todos os textos
    text_rects = [r for r in [gOver_rect, text_rect, score_rect, subtext_rect] if r]
    bbox = text_rects[0].copy()
    for r in text_rects[1:]:
        bbox.union_ip(r)

    # Adiciona margem
    padding = 20
    bbox.inflate_ip(padding * 2, padding * 2)

    # Cria a borda da tela de Game Over
    fundo_box = pygame.Surface((bbox.width, bbox.height), pygame.SRCALPHA)
    cor_translucida = (0, 0, 0, 100)  # RGBA: preto com alfa 150
    pygame.draw.rect(fundo_box, cor_translucida, fundo_box.get_rect(), border_radius=15)

    # Desenha a borda
    screen.blit(fundo_box, bbox.topleft)

    # Desenha os textos
    screen.blit(gOver_surface, gOver_rect)
    if text_surface:
        screen.blit(text_surface, text_rect)
    if score_surf:
        screen.blit(score_surf, score_rect)
    screen.blit(subtext_surface, subtext_rect)



def wait_for_key():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    key_pressed = True