# game/Snake.py
import pygame

class Snake:  # Módulo que cria a cobra (tanto para o Player1 quanto para Player2)
    def __init__(self, start_pos=None):
        if start_pos is None:
            self.snake_pos = [(20, 20), (19, 20), (18, 20)] # Posições iniciais da cobra se não for dada uma opção específica
        else:
            self.snake_pos = start_pos
        
        self.direction = (1, 0)  # Direção inicial: direita
        self.double_points_active = False

    def move(self, map_w, map_h): # Movimentação da cobra
        head_x, head_y = self.snake_pos[0]
        dx, dy = self.direction # dx e dy: casas que a cobra irá se mover no próximo frame (0 = Não se move, 1 = Avança uma casa, -1 = Retorna uma casa)

        new_head = (head_x + dx, head_y + dy) # Calcula a nova posição da cabeça da cobra com base na direção atual.
        self.snake_pos = [new_head] + self.snake_pos[:-1] # Atualiza a lista de posições da cobra (primeiro adiciona a nova cabeça, depois adiciona os seguimentos do corpo)

    def out_of_bounds(self, map_w, map_h): # Verifica se a cobra está além dos limites da tela
        head_x = self.snake_pos[0][0]
        head_y = self.snake_pos[0][1]

        if head_x < 0 or head_x >= map_w or head_y < 0 or head_y >= map_h:
            return True
        return False

    def change_direction(self, new_direction): # Altera a direção da cobra
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction: # Impede que ela se mova para a direção contrária (Ex: não pode mudar da direita para esquerda, e virse-versa)
            self.direction = new_direction

    def set_double_points_active(self, is_active: bool): # Ativa o duplicador de pontos se o PowerUp DoubleFruit estiver ativo
        self.double_points_active = is_active

    def set_fps(self, new_fps):
        pass