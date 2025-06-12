
import random

class Food:
    def __init__(self, grid_size):
        self.posicao = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))

    def nova_posicao(self, grid_size):
        self.posicao = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
