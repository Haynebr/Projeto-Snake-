import random

class Food: # Módulo que cria as comidas
    def __init__(self, grid_width, grid_height, snake_pos, obstacles_pos, food_count):
        self.grid_width = grid_width
        self.grid_height = grid_height
        
        self.positions = self.gerar_nova_posicao(snake_pos, obstacles_pos, food_count) # Gera posição inicial

    def gerar_nova_posicao(self, snake_pos, obstacles_pos, food_count): # Gera nova posição da comida após a Snake comer alguma
        foodPositions = [] # Lista de posições atuais das comidas
        while len(foodPositions) < food_count:
            pos = ( # Gera um X e um Y aleatórios dentro dos limites do mapa
                random.randint(0, self.grid_width - 1),
                random.randint(0, self.grid_height - 1)
            )
            if pos not in snake_pos and pos not in obstacles_pos:   # Garante que a comida não surja dentro da cobra ou de algum obstáculo
                foodPositions.append(pos) # Adiciona a nova posição à lista de posições
        return foodPositions
    
    def gerar_uma_unica_posicao(self, snake_pos, obstacles_pos):
        """Gera 1 nova posição, verificando se não colide com cobra ou obstáculos."""
        return self.gerar_nova_posicao(snake_pos, obstacles_pos, 1)[0]  # Retorna a posição, não a lista