import random

class Obstacle:
    def __init__(self, map_width, map_height, snake_positions, num_obstacles):
        self.positions = self.generate_obstacles(map_width, map_height, snake_positions, num_obstacles)

    def generate_obstacles(self, width, height, snake_positions, count):
        obstacles = []
        while len(obstacles) < count:
            pos = (random.randint(0, width - 1), random.randint(0, height - 1))
            if pos not in obstacles and pos not in snake_positions:
                obstacles.append(pos)
        return obstacles
