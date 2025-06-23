# cores.py

# Cores RGB básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CIANO = (0, 255, 255)
MAGENTA = (255, 0, 255)
CINZA = (128, 128, 128)
LARANJA = (255, 165, 0)
ROXO = (128, 0, 128)

class Tema_Base:
    #Tela
    cor_fundo_tela = PRETO
    cor_borda_tela = ROXO
    cor_obstaculos = CINZA
    cor_letras = BRANCO
    cor_comida_padrão = VERMELHO
    #---------------------------------------
    #Snake
    cor_cabeca_P1 = AMARELO
    cor_corpo_P1 = VERDE
    cor_cabeca_P2 = CIANO
    cor_corpo_P2 = AZUL
    #---------------------------------------
    #Powers
    # Lista de cores para a animação da PowerBox
    cores_animacao_powerbox = [AZUL, VERMELHO, VERDE]
    cor_borda_power_box = cor_borda_tela
    cor_texto_nome_do_poder = AMARELO


    #1-Imã:
    cor_borda_ima = cor_borda_tela
    #2-Turbo:
    cor_corpo_cobra_turbo = ROXO
    #3-Frutas Dobro:
    cor_comida_dobro = MAGENTA

    
class Tema_claro:
    #Tela
    cor_fundo_tela = BRANCO
    cor_borda_tela = PRETO
    cor_obstaculos = VERDE
    cor_letras = PRETO
    cor_comida_padrão = AMARELO
    #---------------------------------------
    #Snake
    cor_cabeca_P1 = PRETO
    cor_corpo_P1 = CIANO
    cor_cabeca_P2 = ROXO
    cor_corpo_P2 = CINZA
    #---------------------------------------
    #Powers
    # Lista de cores para a animação da PowerBox
    cores_animacao_powerbox = [ROXO, LARANJA, CIANO]
    cor_borda_power_box = cor_borda_tela
    cor_texto_nome_do_poder = AMARELO



    #1-Imã:
    cor_borda_ima = cor_borda_tela
    #2-Turbo:
    cor_corpo_cobra_turbo = ROXO
    #3-Frutas Dobro:
    cor_comida_dobro = VERMELHO