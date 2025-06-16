import pygame
from Game import Map, Snake, Foods, Utils
from Game.Obstacles import Obstacle

def main():
    pygame.init()

    # Configurações do mapa
    cell_size = Map.MapClass.cell_size  # Tamanho de cada célula da grid (em px)
    map_width = Map.MapClass.map_width   # Nº de células na horizontal
    map_height = Map.MapClass.map_height  # Nº de células na vertical

    # Calcula o tamanho da janela em pixels com base no tamanho do grid
    screen_width = cell_size * map_width
    screen_height = cell_size * map_height

    # Cria a janela do jogo com o tamanho definido
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Projeto Snake Game")

    clock = pygame.time.Clock()
    snake_obj = Snake.Snake()
    food = Foods.Food(map_width, map_height, snake_obj.snake_pos)
    obstacles = Obstacle(map_width, map_height, snake_obj.snake_pos, food.posicao, num_obstacles=10)

    running = True 
    while running:  # loop principal do jogo
        screen.fill((0, 0, 0)) # Preenche o fundo da tela

        for event in pygame.event.get():  # Verifica os eventos do pygame (teclado, mouse, fechar janela, etc.)
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_obj.change_direction((0, -1))  # Cima
                elif event.key == pygame.K_DOWN:
                    snake_obj.change_direction((0, 1))   # Baixo
                elif event.key == pygame.K_LEFT:
                    snake_obj.change_direction((-1, 0))  # Esquerda
                elif event.key == pygame.K_RIGHT:
                    snake_obj.change_direction((1, 0))   # Direita        

        if snake_obj.out_of_bounds(map_width, map_height): # Verifica se a cobra está dentro da grid
            running = False

        if snake_obj.snake_pos[0] in obstacles.positions: # Verifica se a cobra colidiu com um obstáculo
            running = False  

        if snake_obj.snake_pos[0] == food.posicao: # verifica se a cobra está "em cima" de uma comida
            food = Foods.Food(map_width, map_height, snake_obj.snake_pos)
            snake_obj.snake_pos.append(snake_obj.snake_pos[-1])  # aumenta o tamanho da cobra
            snake_obj.posicao = food.gerar_nova_posicao(snake_obj.snake_pos)  # gera nova comida
        
        snake_obj.move(map_width, map_height) # Atualiza a posição da cobra
        Map.MapClass.draw_grid(screen)  # Desenha o grid do mapa na tela
        for segment in snake_obj.snake_pos[1:]:
            Utils.draw_rect(screen, segment, (0, 200, 0), cell_size)   # Desenha a cobra na tela
        Utils.draw_rect(screen, food.posicao, (255, 0, 0), cell_size)  # Desenha a comida

        for obs in obstacles.positions:
            Utils.draw_rect(screen, obs, (100, 100, 100), cell_size)  # desenha os obstáculos na tela
        pygame.display.flip() # Atualiza a tela
        clock.tick(10) # fps

    pygame.quit()

if __name__ == "__main__":
    main()
