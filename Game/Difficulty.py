
def ajustar_dificuldade(pontos):
    if pontos < 10:
        return 0.5
    elif pontos < 20:
        return 0.3
    else:
        return 0.1
