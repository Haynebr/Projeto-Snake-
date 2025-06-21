# game/Snake.py

import pygame

class Snake: 
    def __init__(self):
        self.snake_pos = [(20, 20), (19, 20), (18, 20)]
        self.direction = (1, 0)

        # --- ADIÇÃO NECESSÁRIA 1: ATRIBUTO PARA PODER ---
        # Atributo que o poder "Fruta Duplicada" irá controlar.
        self.double_points_active = False


    def move(self, map_w, map_h):
        head_x, head_y = self.snake_pos[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)
        self.snake_pos = [new_head] + self.snake_pos[:-1]


    def out_of_bounds(self, map_w, map_h):
        head_x = self.snake_pos[0][0]
        head_y = self.snake_pos[0][1]

        if head_x < 0 or head_x >= map_w or head_y < 0 or head_y >= map_h:
            return 1
        else:
            return

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
            
    # --- ADIÇÃO NECESSÁRIA 2: MÉTODOS DO "CONTRATO" ---
    # Estes são os métodos que o PowerManager precisa chamar para funcionar.
    
    def set_double_points_active(self, is_active: bool):
        """Ativa ou desativa o efeito do poder Fruta Duplicada."""
        self.double_points_active = is_active
        # A lógica de crescimento e pontuação que usa este atributo
        # provavelmente ficará no main.py, onde as colisões são tratadas.

    def set_fps(self, new_fps):
        """
        Método placeholder. A lógica real que muda o FPS do jogo estará
        no main.py, mas o método precisa existir aqui para o PowerManager
        não dar erro ao tentar chamá-lo.
        """
        pass # Não faz nada, pois o main.py cuidará disso.