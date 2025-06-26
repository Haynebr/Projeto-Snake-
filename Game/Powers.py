# Game/Powers.py

import pygame
import random
import math

# CORREÇÃO: Usando importações relativas
from .Colors import Tema_Base, PRETO, AMARELO
from .Map import MapClass

GRID_SIZE = MapClass.cell_size
SCREEN_WIDTH = MapClass.map_width * GRID_SIZE
SCREEN_HEIGHT = MapClass.map_height * GRID_SIZE
BASE_FPS = 10 

class PowerBox(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.colors = Tema_Base.cores_animacao_powerbox
        self.color_index = 0
        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE])
        self.font = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)
        self.rect = self.image.get_rect(topleft=position)
        self.creation_time = pygame.time.get_ticks()
        self.last_color_swap = self.creation_time
        self._update_visuals()

    def _update_visuals(self):
        current_color = self.colors[self.color_index]
        self.image.fill(current_color)
        pygame.draw.rect(self.image, Tema_Base.cor_borda_power_box, self.image.get_rect(), 2)
        text_surf = self.font.render('?', True, Tema_Base.cor_letras)
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_color_swap > 500:
            self.last_color_swap = now
            self.color_index = (self.color_index + 1) % len(self.colors)
            self._update_visuals()

class PowerManager:
    def __init__(self):
        self.power_box_sprite = pygame.sprite.GroupSingle()
        self.power_effects = ['magnet_fruit', 'turbo', 'duplicate_fruit']
        self.spawn_interval = 15000 
        self.box_lifespan = 10000    
        self.next_spawn_time = pygame.time.get_ticks() + self.spawn_interval
        self.active_power_type = None
        self.power_start_time = 0
        self.power_duration = 7000
        self.font = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)
        self.power_names_map = {
            'magnet_fruit': 'Fruit Magnet',
            'turbo': 'Turbo',
            'duplicate_fruit': 'Double Fruit'
        }

    def update(self, snake, food, obstacles):
        now = pygame.time.get_ticks()
        
        box = self.power_box_sprite.sprite
        if box:
            box.update()
            if now - box.creation_time > self.box_lifespan:
                box.kill()
                self.next_spawn_time = now + self.spawn_interval
        else:
            if now >= self.next_spawn_time:
                self._spawn_power_box(snake, food.positions, obstacles.positions)

        if box:
            head_pos_grid = snake.snake_pos[0]
            snake_head_rect = pygame.Rect(
                head_pos_grid[0] * GRID_SIZE,
                head_pos_grid[1] * GRID_SIZE,
                GRID_SIZE,
                GRID_SIZE
            )
            if box.rect.colliderect(snake_head_rect):
                box.kill()
                self._activate_random_power(snake)
                self.next_spawn_time = now + self.spawn_interval
        
        if self.active_power_type:
            if now - self.power_start_time > self.power_duration:
                self._deactivate_current_power(snake)
            else:
                if self.active_power_type == 'magnet_fruit':
                    self._apply_magnet_effect(snake, food)
    
    def _spawn_power_box(self, snake, food_list, obstacle_list):
        possible_positions = set((x, y) for x in range(0, SCREEN_WIDTH, GRID_SIZE) for y in range(0, SCREEN_HEIGHT, GRID_SIZE))
        
        occupied_positions = set((pos[0] * GRID_SIZE, pos[1] * GRID_SIZE) for pos in snake.snake_pos)
        occupied_positions.update((pos[0] * GRID_SIZE, pos[1] * GRID_SIZE) for pos in food_list)
        occupied_positions.update((pos[0] * GRID_SIZE, pos[1] * GRID_SIZE) for pos in obstacle_list)

        safe_positions = list(possible_positions - occupied_positions)
        if safe_positions:
            position = random.choice(safe_positions)
            box = PowerBox(position)
            self.power_box_sprite.add(box)

    def _activate_random_power(self, snake):
        if self.active_power_type:
            self._deactivate_current_power(snake)
        self.active_power_type = random.choice(self.power_effects)
        self.power_start_time = pygame.time.get_ticks()
        if self.active_power_type == 'turbo':
            snake.set_fps(BASE_FPS * 2)
        elif self.active_power_type == 'duplicate_fruit':
            snake.set_double_points_active(True)

    def _deactivate_current_power(self, snake):
        if not self.active_power_type: return
        if self.active_power_type == 'turbo':
            snake.set_fps(BASE_FPS)
        elif self.active_power_type == 'duplicate_fruit':
            snake.set_double_points_active(False)
        self.active_power_type = None

    def _apply_magnet_effect(self, snake, food_object):
        head_grid_pos = snake.snake_pos[0]
        snake_head_pos_pixels = (head_grid_pos[0] * GRID_SIZE + GRID_SIZE // 2, 
                                 head_grid_pos[1] * GRID_SIZE + GRID_SIZE // 2)
        magnet_radius_pixels = 3 * GRID_SIZE
        
        # Itera sobre todas as comidas
        for i, food_pos in enumerate(food_object.positions):
            fruit_pos_pixels = (food_pos[0] * GRID_SIZE + GRID_SIZE // 2, 
                                food_pos[1] * GRID_SIZE + GRID_SIZE // 2)
            distance = math.hypot(snake_head_pos_pixels[0] - fruit_pos_pixels[0], 
                                  snake_head_pos_pixels[1] - fruit_pos_pixels[1])

            if distance <= magnet_radius_pixels:
                new_x, new_y = food_pos
                if food_pos[0] < head_grid_pos[0]: new_x += 1
                if food_pos[0] > head_grid_pos[0]: new_x -= 1
                if food_pos[1] < head_grid_pos[1]: new_y += 1
                if food_pos[1] > head_grid_pos[1]: new_y -= 1
                food_object.positions[i] = (new_x, new_y)

    def draw_ui(self, screen):
        if self.active_power_type:
            power_name = self.power_names_map.get(self.active_power_type, "")
            text_surf = self.font.render(f"Active Power: {power_name}", True, Tema_Base.cor_texto_nome_do_poder)
            text_rect = text_surf.get_rect(topright=(SCREEN_WIDTH - 15, 10))
            screen.blit(text_surf, text_rect)
        self.power_box_sprite.draw(screen)