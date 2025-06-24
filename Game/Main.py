# Game/Main.py

import pygame
from . import Map, Snake, Foods, Utils, Score, Config, Modes
from .Obstacles import Obstacle
from .Enemies import Enemy
from .Powers import PowerManager
from .Colors import Tema_Base, BRANCO

# Game/Main.py

# ... (As importações no topo do arquivo estão corretas e não mudam)

def main(map_width, map_height, screen, cell_size, clock):
    # --- CORREÇÃO ADICIONADA AQUI ---
    # Recalcula as dimensões da tela para que sejam conhecidas dentro desta função
    screen_width = cell_size * map_width
    screen_height = cell_size * map_height

    gameConfigs = Config.dictConfigs # Acessa configurações do jogo
    mode = gameConfigs['GameMode'] # Salva o modo de jogo

    # Fontes
    big_txt_font = pygame.font.Font("Assets/text/Pixeltype.ttf", 120)
    medium_txt_font = pygame.font.Font("Assets/text/Pixeltype.ttf", 80)
    small_txt_font = pygame.font.Font("Assets/text/Pixeltype.ttf", 40)
    
    BASE_FPS = 10
    current_fps = BASE_FPS
    def set_game_fps(new_fps):
        nonlocal current_fps
        current_fps = new_fps

    # --- Inicialização dos Objetos ---
    Modes.start_mode(mode)
    
    secure_positions = [(16, 15), (17, 15), (18, 15), (19, 15), (15, 16), (15, 14), (20, 21), (20, 19), (21, 20), (22, 20), (23, 20), (24, 20)] # Para que não surjam obstáculos na frente dos players assim que o jogo inicia:
    snake_P1 = Snake.Snake() # Ciração do Player 1
    snakes = [snake_P1] # Lista de players
    if mode == 1:
        snake_P2 = Snake.Snake(start_pos=[(15, 15), (14, 15), (13, 15)]) # Criação do Player 2
        snakes.append(snake_P2)
    
    occupied_positions = Utils.get_snakes_positions(snakes) # Posições ocupadas pelos Players
    obstacles = Obstacle(map_width, map_height, occupied_positions, secure_positions, gameConfigs['Obstacles']) # Criação de obstáculos
    enemies = [Enemy(map_width, map_height, occupied_positions, obstacles.positions, secure_positions) for i in range(gameConfigs['Enemies'])] # Criação de inimigos
    score_obj = Score.Score() # Criação do Score
    
    all_occupied_start = Utils.get_snakes_positions(snakes) + obstacles.positions + [pos for e in enemies for pos in e.snake_pos] # Posições ocupadas no início do jogo
    food = Foods.Food(map_width, map_height, all_occupied_start, [], gameConfigs['Foods'])
    
    power_manager = PowerManager()
    snake_P1.set_fps = set_game_fps
    if mode == 1: snake_P2.set_fps = set_game_fps

    # --- LÓGICA DO MODO TEMPO LIMITADO ---
    time_limit_active = False
    if mode == 2:
        time_limit_active = True
        start_ticks = pygame.time.get_ticks()
        total_duration_ms = gameConfigs['TimeLimit_InitialTime'] * 1000

    running = True 
    while running:
        screen.fill(Tema_Base.cor_fundo_tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Volta para o menu
            elif event.type == pygame.KEYDOWN:
                # Controles P1
                if event.key == pygame.K_UP: snake_P1.change_direction((0, -1))
                elif event.key == pygame.K_DOWN: snake_P1.change_direction((0, 1))
                elif event.key == pygame.K_LEFT: snake_P1.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT: snake_P1.change_direction((1, 0))
                # Controles P2
                if mode == 1:
                    if event.key == pygame.K_w: snake_P2.change_direction((0, -1))
                    elif event.key == pygame.K_s: snake_P2.change_direction((0, 1))
                    elif event.key == pygame.K_a: snake_P2.change_direction((-1, 0))
                    elif event.key == pygame.K_d: snake_P2.change_direction((1, 0))

        if gameConfigs['Powers']:
            power_manager.update(snake_P1, food, obstacles)
            if mode == 1:
                power_manager.update(snake_P2, food, obstacles)

        # Atualiza e verifica o timer
        if time_limit_active:
            elapsed_ms = pygame.time.get_ticks() - start_ticks
            time_left_ms = total_duration_ms - elapsed_ms
            if time_left_ms < 0: time_left_ms = 0
            if time_left_ms <= 0:
                Utils.game_over(screen, screen_width, screen_height, big_txt_font)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 0, f"Score: {score_obj.p1_score}")
                running = False
                continue

        # Move Cobras e Inimigos
        snake_P1.move(map_width, map_height)
        if mode == 1: snake_P2.move(map_width, map_height)
        for enemy in enemies: enemy.move()
            
        # Lógica de comer comida para P1
        if snake_P1.snake_pos[0] in food.positions or snake_P1.snake_pos[1] in food.positions:
            if time_limit_active: total_duration_ms += gameConfigs['TimeLimit_TimeGained'] * 1000
            
            if snake_P1.snake_pos[0] in food.positions: eated_food_pos = snake_P1.snake_pos[0]
            else: eated_food_pos = snake_P1.snake_pos[1]

            growth_amount = 2 if snake_P1.double_points_active else 1
            score_to_add = 20 if snake_P1.double_points_active else 10
            
            score_obj.adicionar(score_to_add, 1)
            score_obj.exibir()

            eaten_food_index = food.positions.index(eated_food_pos)
            all_occupied_now = Utils.get_snakes_positions(snakes) + obstacles.positions + [pos for e in enemies for pos in e.snake_pos]
            food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(all_occupied_now, [])
            for _ in range(growth_amount): snake_P1.snake_pos.append(snake_P1.snake_pos[-1])

        # Lógica de comer comida para P2 (se aplicável)
        if mode == 1 and (snake_P2.snake_pos[0] in food.positions or snake_P2.snake_pos[1] in food.positions):
            if snake_P2.snake_pos[0] in food.positions: eated_food_pos = snake_P2.snake_pos[0]
            else: eated_food_pos = snake_P2.snake_pos[1]

            growth_amount = 2 if snake_P2.double_points_active else 1
            score_to_add = 20 if snake_P2.double_points_active else 10

            score_obj.adicionar(score_to_add, 2)
            score_obj.exibir()
            eaten_food_index = food.positions.index(eated_food_pos)
            
            all_occupied_now = Utils.get_snakes_positions(snakes) + obstacles.positions + [pos for e in enemies for pos in e.snake_pos]
            food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(all_occupied_now, [])
            for _ in range(growth_amount): snake_P2.snake_pos.append(snake_P2.snake_pos[-1])

        # Lógica de Colisões e Fim de Jogo
        p1_is_dead = (
            snake_P1.out_of_bounds(map_width, map_height) or
            snake_P1.snake_pos[0] in obstacles.positions or
            snake_P1.snake_pos[0] in snake_P1.snake_pos[1:] or
            (mode == 1 and snake_P1.snake_pos[0] in snake_P2.snake_pos)
        )
        
        for i, enemy in reversed(list(enumerate(enemies))):
            if snake_P1.snake_pos[0] in enemy.snake_pos:
                if time_limit_active:
                    total_duration_ms -= gameConfigs['TimeLimit_TimeLost'] * 1000
                    del enemies[i]
                else:
                    p1_is_dead = True
        
        p2_is_dead = False
        if mode == 1:
            p2_is_dead = (
                snake_P2.out_of_bounds(map_width, map_height) or
                snake_P2.snake_pos[0] in obstacles.positions or
                snake_P2.snake_pos[0] in snake_P2.snake_pos[1:] or
                snake_P2.snake_pos[0] in snake_P1.snake_pos or
                any(snake_P2.snake_pos[0] in e.snake_pos for e in enemies)
            )

        if p1_is_dead or p2_is_dead:
            winner = 0
            if mode == 1:
                if p1_is_dead and p2_is_dead: winner = 3 
                elif p1_is_dead: winner = 2 
                elif p2_is_dead: winner = 1
            
            final_score = f"P1: {score_obj.p1_score} | P2: {score_obj.p2_score}" if mode == 1 else f"Score: {score_obj.p1_score}"
            Utils.game_over(screen, screen_width, screen_height, big_txt_font)
            Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, winner, final_score)
            running = False
            continue
        
        # --- Seção de Desenho ---
        Map.MapClass.draw_grid(screen)
        
        cor_cabeca_P1 = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_cabeca_P1
        cor_corpo_P1 = Tema_Base.cor_corpo_cobra_turbo if power_manager.active_power_type == 'turbo' else Tema_Base.cor_corpo_P1
        
        Utils.draw_rect(screen, snake_P1.snake_pos[0], cor_cabeca_P1, cell_size)
        for segment in snake_P1.snake_pos[1:]: Utils.draw_rect(screen, segment, cor_corpo_P1, cell_size)

        if mode == 1:
            Utils.draw_rect(screen, snake_P2.snake_pos[0], Tema_Base.cor_cabeca_P2, cell_size)
            for segment in snake_P2.snake_pos[1:]: Utils.draw_rect(screen, segment, Tema_Base.cor_corpo_P2, cell_size)
        
        cor_comida = Tema_Base.cor_comida_dobro if snake_P1.double_points_active or (mode == 1 and snake_P2.double_points_active) else Tema_Base.cor_comida_padrão
        for pos in food.positions: Utils.draw_rect(screen, pos, cor_comida, cell_size)

        for obs in obstacles.positions: Utils.draw_rect(screen, obs, Tema_Base.cor_obstaculos, cell_size)
        for enemy in enemies:
            for segment in enemy.snake_pos: Utils.draw_rect(screen, segment, BRANCO, cell_size)

        if gameConfigs['Powers']: power_manager.draw_ui(screen)
        
        if time_limit_active:
            total_seconds = max(0, int(time_left_ms / 1000))
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            time_string = f"Time: {minutes:02d}:{seconds:02d}"
            text_surf = small_txt_font.render(time_string, True, Tema_Base.cor_letras)
            text_rect = text_surf.get_rect(topleft=(10, 10))
            screen.blit(text_surf, text_rect)

        pygame.display.flip()
        clock.tick(current_fps)

    pygame.display.update()
    Utils.wait_for_key()
    return