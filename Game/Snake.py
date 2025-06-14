import pygame

class Snake: 
    def __init__(self):
        # Lista de posições da cobra, onde tupla representa um bloco da cobra (x, y)
        self.snake_pos = [(20, 20), (19, 20), (18, 20)]  # Começa com 3 blocos no meio do mapa
        self.direction = (1, 0) # Direção inicial → direita (direção no X, direção no Y)


    def move(self, map_w, map_h):
        head_x, head_y = self.snake_pos[0]  # Pega a posição da cabeça
        dx, dy = self.direction  # Direção atual

        new_head = (head_x + dx, head_y + dy) # Calcula a nova posição da cabeça
        self.snake_pos = [new_head] + self.snake_pos[:-1] # Move a cabeça e empurra o corpo


    def out_of_bounds(self, map_w, map_h): # checa se a cobra está fora da grid
        head_x = self.snake_pos[0][0]
        head_y = self.snake_pos[0][1]

        if head_x < 0 or head_x >= map_w or head_y < 0 or head_y >= map_h:
            return 1  # fora dos limites
        else:
            return

    def change_direction(self, new_direction):
        # Impede que a cobra vá imediatamente na direção oposta
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction