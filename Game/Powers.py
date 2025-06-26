# Game/Powers.py
# Este módulo gerencia toda a lógica de power-ups, desde o item que aparece na tela até os efeitos aplicados na cobra.

import pygame
import random
import math

from .Colors import Tema_Base, PRETO, AMARELO
from .Map import MapClass

# Constantes do módulo, definidas apartir das configurações do mapa
GRID_SIZE = MapClass.cell_size
SCREEN_WIDTH = MapClass.map_width * GRID_SIZE
SCREEN_HEIGHT = MapClass.map_height * GRID_SIZE
BASE_FPS = 10 

class PowerBox(pygame.sprite.Sprite):
    """
    Representa o item visual da "Caixa de Poder" que aparece na tela.
    É responsável por sua própria aparência e animação.
    """
    def __init__(self, position):
        """Inicializa o objeto PowerBox em uma posição específica."""
        super().__init__()
        
        # Atributos para a animação de troca de cor
        self.colors = Tema_Base.cores_animacao_powerbox
        self.color_index = 0
        
        # Criação da superfície e do retângulo de colisão (hitbox)
        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE])
        self.font = pygame.font.Font("Assets/text/Pixeltype.ttf", 30)
        self.rect = self.image.get_rect(topleft=position)
        
        # Timers para controlar o tempo de vida e a animação
        self.creation_time = pygame.time.get_ticks()
        self.last_color_swap = self.creation_time
        
        self._update_visuals()

    def _update_visuals(self):
        """Método interno para redesenhar a aparência da caixa (cor, borda e '?')."""
        current_color = self.colors[self.color_index]
        self.image.fill(current_color)
        pygame.draw.rect(self.image, Tema_Base.cor_borda_power_box, self.image.get_rect(), 2)
        text_surf = self.font.render('?', True, Tema_Base.cor_letras)
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect)

    def update(self):
        """Atualiza a animação de troca de cor da caixa a cada 500ms."""
        now = pygame.time.get_ticks()
        if now - self.last_color_swap > 500:
            self.last_color_swap = now
            self.color_index = (self.color_index + 1) % len(self.colors)
            self._update_visuals()

class PowerManager:
    """
    Gerencia o ciclo de vida completo dos poderes: quando e onde aparecem,
    seus efeitos na cobra e sua duração. É o "cérebro" do sistema.
    """
    def __init__(self):
        """Inicializa o gerenciador de poderes."""
        self.power_box_sprite = pygame.sprite.GroupSingle() # Grupo para garantir apenas uma PowerBox por vez
        self.power_effects = ['magnet_fruit', 'turbo', 'duplicate_fruit']
        
        # Parâmetros de tempo para o spawn e duração da caixa
        self.spawn_interval = 15000 
        self.box_lifespan = 10000    
        self.next_spawn_time = pygame.time.get_ticks() + self.spawn_interval
        
        # Variáveis para controlar o estado do poder ativo
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
        """Método principal do gerenciador, chamado a cada frame pelo Main.py."""
        now = pygame.time.get_ticks()
        box = self.power_box_sprite.sprite

        # 1. Gerencia o ciclo de vida da PowerBox (spawn e despawn por tempo)
        if box:
            box.update()
            if now - box.creation_time > self.box_lifespan:
                box.kill()
                self.next_spawn_time = now + self.spawn_interval
        else:
            if now >= self.next_spawn_time:
                self._spawn_power_box(snake, food.positions, obstacles.positions)

        # 2. Verifica a colisão da cabeça da cobra com a PowerBox
        if box:
            # Cria um hitbox temporário para a cabeça da cobra para a verificação
            head_pos_grid = snake.snake_pos[0]
            snake_head_rect = pygame.Rect(
                head_pos_grid[0] * GRID_SIZE, head_pos_grid[1] * GRID_SIZE,
                GRID_SIZE, GRID_SIZE
            )
            if box.rect.colliderect(snake_head_rect):
                box.kill()
                self._activate_random_power(snake)
                self.next_spawn_time = now + self.spawn_interval
        
        # 3. Gerencia a duração e os efeitos do poder ativo
        if self.active_power_type:
            if now - self.power_start_time > self.power_duration:
                self._deactivate_current_power(snake)
            elif self.active_power_type == 'magnet_fruit':
                self._apply_magnet_effect(snake, food)
    
    def _spawn_power_box(self, snake, food_list, obstacle_list):
        """Encontra um local seguro no mapa e cria uma novo lugar da PowerBox."""
        # Cria um conjunto de todas as posições possíveis e subtrai as já ocupadas
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
        """Sorteia um poder e aplica seu efeito inicial na cobra."""
        if self.active_power_type: self._deactivate_current_power(snake)
        
        self.active_power_type = random.choice(self.power_effects)
        self.power_start_time = pygame.time.get_ticks()
        
        # Aplica o efeito chamando o método correspondente no objeto 'snake'
        if self.active_power_type == 'turbo':
            snake.set_fps(BASE_FPS * 2)
        elif self.active_power_type == 'duplicate_fruit':
            snake.set_double_points_active(True)

    def _deactivate_current_power(self, snake):
        """Reverte o efeito do poder ativo na cobra ao final da sua duração."""
        if not self.active_power_type: return
        
        # Reverte o efeito específico que estava ativo
        if self.active_power_type == 'turbo':
            snake.set_fps(BASE_FPS)
        elif self.active_power_type == 'duplicate_fruit':
            snake.set_double_points_active(False)
        self.active_power_type = None

    def _apply_magnet_effect(self, snake, food_object):
        """Atrai comidas que estão dentro de um raio de 3 blocos da cabeça da cobra."""
        head_grid_pos = snake.snake_pos[0]
        snake_head_pos_pixels = (head_grid_pos[0] * GRID_SIZE + GRID_SIZE // 2, 
                                 head_grid_pos[1] * GRID_SIZE + GRID_SIZE // 2)
        magnet_radius_pixels = 3 * GRID_SIZE
        
        # Itera sobre todas as comidas para verificar a distância de cada uma
        for i, food_pos in enumerate(food_object.positions):
            fruit_pos_pixels = (food_pos[0] * GRID_SIZE + GRID_SIZE // 2, 
                                food_pos[1] * GRID_SIZE + GRID_SIZE // 2)
            
            # Calcula a distância em linha reta entre a cabeça e a fruta
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
        """Desenha os elementos visuais do gerenciador na tela."""
        # Desenha o texto do poder ativo, se houver
        if self.active_power_type:
            power_name = self.power_names_map.get(self.active_power_type, "")
            text_surf = self.font.render(f"Active Power: {power_name}", True, Tema_Base.cor_texto_nome_do_poder)
            text_rect = text_surf.get_rect(topright=(SCREEN_WIDTH - 15, 10))
            screen.blit(text_surf, text_rect)
            
        # Desenha a PowerBox se ela existir
        self.power_box_sprite.draw(screen)