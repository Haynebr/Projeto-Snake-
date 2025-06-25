# Game/Map.py

import pygame

class MapClass:
    cell_size = 25
    map_width = 45
    map_height = 30

    @classmethod
    def draw_grid(cls, screen, grid_color, border_color): # Adicionamos a cor da borda
        width_px = cls.cell_size * cls.map_width
        height_px = cls.cell_size * cls.map_height
        
        # Desenha as linhas do grid
        for x in range(0, width_px, cls.cell_size):
            pygame.draw.line(screen, grid_color, (x, 0), (x, height_px))
        for y in range(0, height_px, cls.cell_size):
            pygame.draw.line(screen, grid_color, (0, y), (width_px, y))

        # --- DESENHA A BORDA/MOLDURA ---
        border_rect = pygame.Rect(0, 0, width_px, height_px)
        pygame.draw.rect(screen, border_color, border_rect, 4) # Linha com 4 pixels de espessura