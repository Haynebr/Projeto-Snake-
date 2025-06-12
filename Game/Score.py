
class Score:
    def __init__(self):
        self.pontos = 0

    def adicionar(self, valor):
        self.pontos += valor

    def exibir(self):
        print(f"Pontuação: {self.pontos}")
