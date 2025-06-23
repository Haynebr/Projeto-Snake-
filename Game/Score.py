
class Score:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0

    def adicionar(self, valor, player):
        if player == 1: self.p1_score += valor
        else: self.p2_score += valor

    def exibir(self):
        print(f"Player 1 Score: {self.p1_score}")
        if self.p2_score > 0:
            print(f"Player 2 Score: {self.p2_score}")
