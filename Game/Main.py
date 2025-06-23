# Main.py

import pygame
from Game import Map, Snake, Foods, Utils, Score, Config, Modes
from Game.Obstacles import Obstacle
from Game.Enemies import Enemy
from Game.Powers import PowerManager
from Game.Colors import Tema_Base, BRANCO # Importa o tema para usar as cores

def main(map_width, map_height, screen, cell_size, clock):
    pygame.init()

    gameConfigs = Config.dictConfigs
    mode = gameConfigs['GameMode']

    cell_size = Map.MapClass.cell_size
    map_width = Map.MapClass.map_width
    map_height = Map.MapClass.map_height

    screen_width = cell_size * map_width
    screen_height = cell_size * map_height

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Projeto Snake Game")

    clock = pygame.time.Clock()

    big_txt_font = pygame.font.Font("Assets/text\Pixeltype.ttf", 120)
    medium_txt_font = pygame.font.Font("Assets/text\Pixeltype.ttf", 80)
    small_txt_font = pygame.font.Font("Assets/text\Pixeltype.ttf", 40)
    
    BASE_FPS = 10
    current_fps = BASE_FPS
    def set_game_fps(new_fps):
        nonlocal current_fps
        current_fps = new_fps

    Modes.start_mode(mode)
    # Para que não surjam obstáculos na frente dos players assim que ele spawna:
    secure_positions = [(16, 15), (17, 15), (18, 15), (19, 15), (15, 16), (15, 14), (20, 21), (20, 19), (21, 20), (22, 20), (23, 20), (24, 20)]
    snake_P1 = Snake.Snake()
    if mode == 1:
        snake_P2 = Snake.Snake(start_pos=[(15, 15), (14, 15), (13, 15)])
    snakes = [snake_P1]
    if mode == 1:
        snakes.append(snake_P2)
    occupied_positions = Utils.get_snakes_positions(snakes)

    obstacles = Obstacle(map_width, map_height, occupied_positions, secure_positions, gameConfigs['Obstacles'])
    enemies = [Enemy(map_width, map_height, occupied_positions, obstacles.positions, secure_positions) for i in range(gameConfigs['Enemies'])]
    score_obj = Score.Score()
    food = Foods.Food(map_width, map_height, occupied_positions, obstacles.positions, gameConfigs['Foods'])
    
    power_manager = PowerManager()
    snake_P1.set_fps = set_game_fps
    if mode == 1 and current_fps == BASE_FPS:
        snake_P2.set_fps = set_game_fps

    running = True 
    while running:
        screen.fill(Tema_Base.cor_fundo_tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: snake_P1.change_direction((0, -1))
                elif event.key == pygame.K_DOWN: snake_P1.change_direction((0, 1))
                elif event.key == pygame.K_LEFT: snake_P1.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT: snake_P1.change_direction((1, 0))
                if mode == 1:
                    if event.key == pygame.K_w: snake_P2.change_direction((0, -1))
                    elif event.key == pygame.K_s: snake_P2.change_direction((0, 1))
                    elif event.key == pygame.K_a: snake_P2.change_direction((-1, 0))
                    elif event.key == pygame.K_d: snake_P2.change_direction((1, 0))

        if gameConfigs['Powers']:
            power_manager.update(snake_P1, food, obstacles)
            if mode == 1:
                power_manager.update(snake_P2, food, obstacles)

        if snake_P1.snake_pos[0] in food.positions:
            growth_amount = 2 if snake_P1.double_points_active else 1
            score_to_add = 20 if snake_P1.double_points_active else 10
            
            score_obj.adicionar(score_to_add, 1)
            score_obj.exibir()

            eaten_food_index = food.positions.index(snake_P1.snake_pos[0])

            food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(snake_P1.snake_pos, obstacles.positions)
            
            for _ in range(growth_amount):
                snake_P1.snake_pos.append(snake_P1.snake_pos[-1])

        if mode == 1: # P2
            if snake_P2.snake_pos[0] in food.positions:
                growth_amount = 2 if snake_P2.double_points_active else 1
                score_to_add = 20 if snake_P2.double_points_active else 10

                score_obj.adicionar(score_to_add, 2)
                score_obj.exibir()

                eaten_food_index = food.positions.index(snake_P2.snake_pos[0])

                food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(snake_P2.snake_pos, obstacles.positions)

                for _ in range(growth_amount):
                    snake_P2.snake_pos.append(snake_P2.snake_pos[-1])
        
        snake_P1.move(map_width, map_height)
        if mode == 1: # P2
            snake_P2.move(map_width, map_height)
        for enemy in enemies:
            enemy.move()
            
        # --- SEÇÃO DE DESENHO COMPLETA E CORRIGIDA ---
        Map.MapClass.draw_grid(screen)
        
        # EFEITO VISUAL DO TURBO: Muda a cor da cobra
        cor_cabeca_P1 = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_cabeca_P1
        cor_corpo_P1 = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_corpo_P1
        Utils.draw_rect(screen, snake_P1.snake_pos[0], cor_cabeca_P1, cell_size)
        for segment in snake_P1.snake_pos[1:]:
            Utils.draw_rect(screen, segment, cor_corpo_P1, cell_size)

        cor_comida = Tema_Base.cor_comida_dobro if snake_P1.double_points_active else Tema_Base.cor_comida_padrão

        if mode == 1: # P2
            cor_cabeca_P2 = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_cabeca_P2
            cor_corpo_P2 = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_corpo_P2
            Utils.draw_rect(screen, snake_P2.snake_pos[0], cor_cabeca_P2, cell_size)
            for segment in snake_P2.snake_pos[1:]:
                Utils.draw_rect(screen, segment, cor_corpo_P2, cell_size)
            if snake_P2.double_points_active:
                cor_comida = Tema_Base.cor_comida_dobro

        # EFEITO VISUAL DA FRUTA DUPLICADA: Muda a cor da comida
        
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


        if mode == 1: # empate se as duas baterem na borda ao msm tempo
            if snake_P1.out_of_bounds(map_width, map_height) and snake_P2.out_of_bounds(map_width, map_height):
                Utils.game_over(screen, screen_width, screen_height, big_txt_font)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 3)
                running = False
                continue

        if snake_P1.out_of_bounds(map_width, map_height) or \
           snake_P1.snake_pos[0] in obstacles.positions or \
           snake_P1.snake_pos[0] in snake_P1.snake_pos[1:] or \
           any(snake_P1.snake_pos[0] in e.snake_pos for e in enemies):
            Utils.game_over(screen, screen_width, screen_height, big_txt_font)
            if mode == 1:
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 2)
            else: Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 0)
            running = False 
            continue
        if mode == 1: # P2
            if snake_P2.out_of_bounds(map_width, map_height) or \
            snake_P2.snake_pos[0] in obstacles.positions or \
            snake_P2.snake_pos[0] in snake_P2.snake_pos[1:] or \
            any(snake_P2.snake_pos[0] in e.snake_pos for e in enemies):
                Utils.game_over(screen, screen_width, screen_height, big_txt_font)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 1)
                running = False 
                continue

            # Checar se P1 bateu no corpo de P2
            if snake_P1.snake_pos[0] in snake_P2.snake_pos[1:]:
                Utils.game_over(screen, screen_width, screen_height, big_txt_font)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 2)
                running = False
                continue

            # Checar se P2 bateu no corpo de P1
            elif snake_P2.snake_pos[0] in snake_P1.snake_pos[1:]:
                Utils.game_over(screen, screen_width, screen_height, big_txt_font)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 1)
                running = False
                continue

            # Checar se houve colisão de cabeça com cabeça (empate)
            elif snake_P1.snake_pos[0] == snake_P2.snake_pos[0]:
                Utils.game_over(screen, screen_width, screen_height, big_txt_font)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 3)
                running = False
                continue

        pygame.display.flip()
        
        clock.tick(current_fps)

    pygame.display.update()
    Utils.wait_for_key()
    return

if __name__ == "__main__":
    main()