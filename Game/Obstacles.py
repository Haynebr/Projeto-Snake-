import random

class Obstacle:
    def __init__(self, map_width, map_height, snake_positions, food_position, num_obstacles=5):
        self.positions = self.generate_obstacles(map_width, map_height, snake_positions, food_position, num_obstacles)

    def generate_obstacles(self, width, height, snake_positions, food_position, count):
        obstacles = []
        while len(obstacles) < count:
            pos = (random.randint(0, width - 1), random.randint(0, height - 1))
            if pos not in obstacles and pos not in snake_positions and pos != food_position:
                obstacles.append(pos)
        return obstacles
