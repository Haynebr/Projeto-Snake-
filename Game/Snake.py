# game/Snake.py

import pygame

import pygame

class Snake: 
    def __init__(self, start_pos=None):
        if start_pos is None:
            self.snake_pos = [(20, 20), (19, 20), (18, 20)]
        else:
            self.snake_pos = start_pos
        
        self.direction = (1, 0)  # Direção inicial: direita
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
            return True
        return False

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def set_double_points_active(self, is_active: bool):
        self.double_points_active = is_active

    def set_fps(self, new_fps):
        pass