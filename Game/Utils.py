import pygame

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
