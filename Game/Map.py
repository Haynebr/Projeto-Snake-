import pygame

class MapClass:
    cell_size = 25 # tamanho das células do grid (em pixels)
    map_width = 40  # largura em nº de célunas
    map_height = 40  # altura em nº de célunas

    @classmethod
    def draw_grid(cls, screen): # desenha o grid na tela
        # Desenha as linhas verticais do grid
        for x in range(0, cls.cell_size * cls.map_width, cls.cell_size):
            pygame.draw.line(               
                screen,  # onde será desenhado
                (40, 40, 40), # Cor da linha)
                (x, 0), # Ponto inicial da linha
                (x, cls.cell_size * cls.map_height)  # Ponto final da linha
            )

        # Desenha as linhas horizontais do grid
        for y in range(0, cls.cell_size * cls.map_height, cls.cell_size):
            pygame.draw.line(
                screen,
                (40, 40, 40),
                (0, y),
                (cls.cell_size * cls.map_width, y) 
            )