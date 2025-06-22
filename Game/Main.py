# Main.py

import pygame
from Game import Map, Snake, Foods, Utils, Score, Config
from Game.Obstacles import Obstacle
from Game.Enemies import Enemy
from Game.Powers import PowerManager
from Game.Colors import Tema_Base, BRANCO # Importa o tema para usar as cores

def main(map_width, map_height, screen, cell_size, clock):
    pygame.init()
    gameConfigs = Config.dictConfigs

    cell_size = Map.MapClass.cell_size
    map_width = Map.MapClass.map_width
    map_height = Map.MapClass.map_height

    screen_width = cell_size * map_width
    screen_height = cell_size * map_height

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Projeto Snake Game")

    clock = pygame.time.Clock()
    
    BASE_FPS = 10
    current_fps = BASE_FPS
    def set_game_fps(new_fps):
        nonlocal current_fps
        current_fps = new_fps

    snake_obj = Snake.Snake()
    obstacles = Obstacle(map_width, map_height, snake_obj.snake_pos, gameConfigs['Obstacles'])
    enemies = [Enemy(map_width, map_height, snake_obj.snake_pos, obstacles.positions) for i in range(gameConfigs['Enemies'])]
    score_obj = Score.Score()
    food = Foods.Food(map_width, map_height, snake_obj.snake_pos, obstacles.positions, gameConfigs['Foods'])
    
    power_manager = PowerManager()
    snake_obj.set_fps = set_game_fps

    running = True 
    while running:
        screen.fill(Tema_Base.cor_fundo_tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: snake_obj.change_direction((0, -1))
                elif event.key == pygame.K_DOWN: snake_obj.change_direction((0, 1))
                elif event.key == pygame.K_LEFT: snake_obj.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT: snake_obj.change_direction((1, 0))
        
        if gameConfigs['Powers']:
            power_manager.update(snake_obj, food, obstacles)

        if snake_obj.out_of_bounds(map_width, map_height) or \
           snake_obj.snake_pos[0] in obstacles.positions or \
           snake_obj.snake_pos[0] in snake_obj.snake_pos[1:] or \
           any(snake_obj.snake_pos[0] in e.snake_pos for e in enemies):
            running = False 
            return

        if snake_obj.snake_pos[0] in food.positions:
            growth_amount = 2 if snake_obj.double_points_active else 1
            score_to_add = 20 if snake_obj.double_points_active else 10
            
            score_obj.adicionar(score_to_add)
            score_obj.exibir()

            eaten_food_index = food.positions.index(snake_obj.snake_pos[0])

            food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(snake_obj.snake_pos, obstacles.positions)
            
            for _ in range(growth_amount):
                snake_obj.snake_pos.append(snake_obj.snake_pos[-1])
        
        snake_obj.move(map_width, map_height)
        for enemy in enemies:
            enemy.move()
            
        # --- SEÇÃO DE DESENHO COMPLETA E CORRIGIDA ---
        Map.MapClass.draw_grid(screen)
        
        # EFEITO VISUAL DO TURBO: Muda a cor da cobra
        cor_cabeca = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_cabeca_snake
        cor_corpo = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_corpo_cobra
        Utils.draw_rect(screen, snake_obj.snake_pos[0], cor_cabeca, cell_size)
        for segment in snake_obj.snake_pos[1:]:
            Utils.draw_rect(screen, segment, cor_corpo, cell_size)

        # EFEITO VISUAL DA FRUTA DUPLICADA: Muda a cor da comida
        cor_comida = Tema_Base.cor_comida_dobro if snake_obj.double_points_active else Tema_Base.cor_comida_padrão
        for pos in food.positions:
            Utils.draw_rect(screen, pos, cor_comida, cell_size)

        # Desenha os obstáculos usando a cor do tema
        for obs in obstacles.positions:
            Utils.draw_rect(screen, obs, Tema_Base.cor_obstaculos, cell_size)
            
        # Desenha os inimigos (usando a cor BRANCO, como no código original)
        for enemy in enemies:
            for segment in enemy.snake_pos:
                Utils.draw_rect(screen, segment, BRANCO, cell_size)

        # Desenha a UI dos poderes por cima de tudo
        power_manager.draw_ui(screen)

        pygame.display.flip()
        
        clock.tick(current_fps)

    return

if __name__ == "__main__":
    main()