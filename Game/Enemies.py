import random

class Enemy:
    def __init__(self, map_width, map_height, snake_positions, obstacles_positions):
        self.map_width = map_width
        self.map_height = map_height
        self.direction = random.choice([(1,0), (-1,0), (0,1), (0,-1)])  # direção inicial aleatória
        self.snake_pos = self.generate_initial_position(snake_positions, obstacles_positions)

    def generate_initial_position(self, snake_positions, obstacles_positions):
        while True:
            # Posição aleatória para a geração do inimigo
            head_x = random.randint(2, self.map_width - 3)
            head_y = random.randint(2, self.map_height - 3)
            head = (head_x, head_y)

            # Cria corpo inicial (3 segmentos na direção contrária)
            body = [
                head,
                (head_x - self.direction[0], head_y - self.direction[1]),
                (head_x - 2*self.direction[0], head_y - 2*self.direction[1])
            ]

            # Verifica se não colide com cobra, comida ou obstáculos
            collision = any(pos in snake_positions or pos in obstacles_positions for pos in body)
            if not collision:
                return body

    def move(self):
        head_x, head_y = self.snake_pos[0]
        dx, dy = self.direction

        new_head = ((head_x + dx) % self.map_width, (head_y + dy) % self.map_height)

        self.snake_pos = [new_head] + self.snake_pos[:-1]  # move a cabeça e remove o último segmento

        if random.random() < 0.1:  # Chance de mudar de direção aleatoriamente (opcional)
            self.change_direction()

    def change_direction(self):
        possible_directions = [(1,0), (-1,0), (0,1), (0,-1)]
        opposite = (-self.direction[0], -self.direction[1])
        possible_directions.remove(opposite)  # Não deixa girar 180º
        self.direction = random.choice(possible_directions)
