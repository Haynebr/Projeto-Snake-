import random

class Food:
    def __init__(self, grid_width, grid_height, snake_pos):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.posicao = self.gerar_nova_posicao(snake_pos)  # Gera posição inicial

    def gerar_nova_posicao(self, snake_pos):
        while True:
            pos = (
                random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_height - 1)
            )
            if pos not in snake_pos:   # Garante que não gera em cima da cobra
                return pos