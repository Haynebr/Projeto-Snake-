# Game/Main.py

import pygame
from . import Map, Snake, Foods, Utils, Score, Config, Modes, Colors
from .Obstacles import Obstacle
from .Enemies import Enemy
from .Powers import PowerManager

def main(map_width, map_height, screen, cell_size, clock):
    # Recalcula as dimensões da tela
    screen_width = cell_size * map_width
    screen_height = cell_size * map_height
    
    # Seleciona o Tema com base na configuração
    gameConfigs = Config.dictConfigs
    if gameConfigs['Theme'] == 0: Tema = Colors.Tema_Base
    elif gameConfigs['Theme'] == 1: Tema = Colors.Tema_claro
    elif gameConfigs['Theme'] == 2: Tema = Colors.Tema_Synthwave
    elif gameConfigs['Theme'] == 3: Tema = Colors.Tema_Floresta
    elif gameConfigs['Theme'] == 4: Tema = Colors.Tema_Oceano
    else: Tema = Colors.Tema_Base
    
    mode = gameConfigs['GameMode']

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
    snake_P1 = Snake.Snake()
    snakes = [snake_P1]
    if mode == 1:
        snake_P2 = Snake.Snake(start_pos=[(15, 15), (14, 15), (13, 15)])
        snakes.append(snake_P2)

    occupied_positions = Utils.get_snakes_positions(snakes)
    secure_positions = [(16, 15), (17, 15), (18, 15), (19, 15), (15, 16), (15, 14), (20, 21), (20, 19), (21, 20), (22, 20), (23, 20), (24, 20)]
    obstacles = Obstacle(map_width, map_height, occupied_positions, secure_positions, gameConfigs['Obstacles'])
    
    all_occupied_start = Utils.get_snakes_positions(snakes) + obstacles.positions
    food = Foods.Food(map_width, map_height, all_occupied_start, [], gameConfigs['Foods'])
    
    enemies = [Enemy(map_width, map_height, all_occupied_start, food.positions, secure_positions) for i in range(gameConfigs['Enemies'])]
    
    score_obj = Score.Score()
    power_manager = PowerManager() # Acessa o módulos de poderes
    snake_P1.set_fps = set_game_fps # Manutenção do FPS quando o TURBO está ativo
    if mode == 1: snake_P2.set_fps = set_game_fps

    # --- LÓGICA DO MODO TEMPO LIMITADO ---
    time_limit_active = False
    if mode == 2:
        time_limit_active = True
        start_ticks = pygame.time.get_ticks()
        total_duration_ms = gameConfigs['TimeLimit_InitialTime'] * 1000

    running = True 
    while running:
        screen.fill(Tema.cor_fundo_tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
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

        if gameConfigs['Powers']: # Verifica se alguém pegou um poder
            power_manager.update(snake_P1, food, obstacles)

        if time_limit_active:
            elapsed_ms = pygame.time.get_ticks() - start_ticks
            time_left_ms = total_duration_ms - elapsed_ms
            if time_left_ms < 0: time_left_ms = 0
            if time_left_ms <= 0:
                Utils.game_over(screen, screen_width, screen_height, big_txt_font, Tema)
                Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, 0, Tema, f"Score: {score_obj.p1_score}")
                running = False
                continue

        snake_P1.move(map_width, map_height)
        if mode == 1: snake_P2.move(map_width, map_height)
        for enemy in enemies: enemy.move()
            
        if snake_P1.snake_pos[0] in food.positions or (len(snake_P1.snake_pos) > 1 and snake_P1.snake_pos[1] in food.positions):
            if time_limit_active: total_duration_ms += gameConfigs['TimeLimit_TimeGained'] * 1000
            
            eaten_food_pos = snake_P1.snake_pos[0] if snake_P1.snake_pos[0] in food.positions else snake_P1.snake_pos[1]
            growth_amount = 2 if snake_P1.double_points_active else 1
            score_to_add = 20 if snake_P1.double_points_active else 10
            score_obj.adicionar(score_to_add, 1)
            eaten_food_index = food.positions.index(eaten_food_pos)
            all_occupied_now = Utils.get_snakes_positions(snakes) + obstacles.positions + [pos for e in enemies for pos in e.snake_pos]
            food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(all_occupied_now, [])
            for _ in range(growth_amount): snake_P1.snake_pos.append(snake_P1.snake_pos[-1])

        if mode == 1 and (snake_P2.snake_pos[0] in food.positions or (len(snake_P2.snake_pos) > 1 and snake_P2.snake_pos[1] in food.positions)):
            eaten_food_pos = snake_P2.snake_pos[0] if snake_P2.snake_pos[0] in food.positions else snake_P2.snake_pos[1]
            growth_amount = 2 if snake_P2.double_points_active else 1
            score_to_add = 20 if snake_P2.double_points_active else 10
            score_obj.adicionar(score_to_add, 2)
            eaten_food_index = food.positions.index(eaten_food_pos)
            all_occupied_now = Utils.get_snakes_positions(snakes) + obstacles.positions + [pos for e in enemies for pos in e.snake_pos]
            food.positions[eaten_food_index] = food.gerar_uma_unica_posicao(all_occupied_now, [])
            for _ in range(growth_amount): snake_P2.snake_pos.append(snake_P2.snake_pos[-1])

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
                else: p1_is_dead = True
        
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
            Utils.game_over(screen, screen_width, screen_height, big_txt_font, Tema)
            Utils.player_wins(screen, screen_width, screen_height, medium_txt_font, small_txt_font, winner, Tema, final_score)
            running = False
            continue
        
        # --- Seção de Desenho Completa ---
        Map.MapClass.draw_grid(screen, (40,40,40), Tema.cor_borda_tela)
        
        # Desenha P1
        cor_cabeca_P1 = Tema.cor_corpo_cobra_turbo if gameConfigs['Powers'] and power_manager.active_power_type == 'turbo' else Tema.cor_cabeca_P1
        cor_corpo_P1 = Tema.cor_corpo_cobra_turbo if gameConfigs['Powers'] and power_manager.active_power_type == 'turbo' else Tema.cor_corpo_P1
        head_pos_P1 = snake_P1.snake_pos[0]
        Utils.draw_rect(screen, head_pos_P1, cor_cabeca_P1, cell_size)
        for segment in snake_P1.snake_pos[1:]: Utils.draw_rect(screen, segment, cor_corpo_P1, cell_size)
        
        # Desenha os olhos de P1
        head_pixel_x, head_pixel_y = Utils.grid_to_pixel(head_pos_P1, cell_size)
        eye_radius = cell_size // 8
        eye_1_pos = (head_pixel_x + cell_size // 4, head_pixel_y + cell_size // 3)
        eye_2_pos = (head_pixel_x + cell_size * 3 // 4, head_pixel_y + cell_size // 3)
        pygame.draw.circle(screen, Colors.PRETO, eye_1_pos, eye_radius)
        pygame.draw.circle(screen, Colors.PRETO, eye_2_pos, eye_radius)

        # Desenha P2
        if mode == 1:
            head_pos_P2 = snake_P2.snake_pos[0]
            Utils.draw_rect(screen, head_pos_P2, Tema.cor_cabeca_P2, cell_size)
            for segment in snake_P2.snake_pos[1:]: Utils.draw_rect(screen, segment, Tema.cor_corpo_P2, cell_size)
            
            head_pixel_x_p2, head_pixel_y_p2 = Utils.grid_to_pixel(head_pos_P2, cell_size)
            eye_1_pos_p2 = (head_pixel_x_p2 + cell_size // 4, head_pixel_y_p2 + cell_size // 3)
            eye_2_pos_p2 = (head_pixel_x_p2 + cell_size * 3 // 4, head_pixel_y_p2 + cell_size // 3)
            pygame.draw.circle(screen, Colors.PRETO, eye_1_pos_p2, eye_radius)
            pygame.draw.circle(screen, Colors.PRETO, eye_2_pos_p2, eye_radius)
        
        # Desenha Comida
        cor_comida = Tema.cor_comida_padrão
        if gameConfigs['Powers']:
            is_double_active = snake_P1.double_points_active or (mode == 1 and snake_P2.double_points_active)
            cor_comida = Tema.cor_comida_dobro if is_double_active else Tema.cor_comida_padrão
        for pos in food.positions: Utils.draw_rect(screen, pos, cor_comida, cell_size)

        # Desenha Obstáculos e Inimigos
        for obs in obstacles.positions: Utils.draw_rect(screen, obs, Tema.cor_obstaculos, cell_size)
        for enemy in enemies:
            for segment in enemy.snake_pos: Utils.draw_rect(screen, segment, Tema.cor_inimigo, cell_size)

        # Desenha UI
        if gameConfigs['Powers']: power_manager.draw_ui(screen)
        if time_limit_active:
            total_seconds = max(0, int(time_left_ms / 1000))
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            time_string = f"Time: {minutes:02d}:{seconds:02d}"
            text_surf = small_txt_font.render(time_string, True, Tema.cor_letras)
            text_rect = text_surf.get_rect(topleft=(10, 10))
            screen.blit(text_surf, text_rect)

        pygame.display.flip()
        clock.tick(current_fps)

    # Fim do loop 'while running:'
    pygame.display.update()
    Utils.wait_for_key()
    return