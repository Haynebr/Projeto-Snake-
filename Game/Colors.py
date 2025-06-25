# Game/Colors.py

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
AZUL_ESCURO = (0, 20, 50) # Nova cor para o tema Oceano

class Tema_Base:
    # ... (conteúdo da classe não muda)
    cor_fundo_tela = PRETO
    cor_borda_tela = ROXO
    cor_obstaculos = CINZA
    cor_letras = BRANCO
    cor_comida_padrão = VERMELHO
    cor_cabeca_P1 = AMARELO
    cor_corpo_P1 = VERDE
    cor_cabeca_P2 = CIANO
    cor_corpo_P2 = AZUL
    cores_animacao_powerbox = [AZUL, VERMELHO, VERDE]
    cor_borda_power_box = cor_borda_tela
    cor_texto_nome_do_poder = AMARELO
    cor_borda_ima = cor_borda_tela
    cor_corpo_cobra_turbo = ROXO
    cor_comida_dobro = MAGENTA
    
class Tema_claro:
    # ... (conteúdo da classe não muda)
    cor_fundo_tela = BRANCO
    cor_borda_tela = PRETO
    cor_obstaculos = VERDE
    cor_letras = PRETO
    cor_comida_padrão = AMARELO
    cor_cabeca_P1 = PRETO
    cor_corpo_P1 = CIANO
    cor_cabeca_P2 = ROXO
    cor_corpo_P2 = CINZA
    cores_animacao_powerbox = [ROXO, LARANJA, CIANO]
    cor_borda_power_box = cor_borda_tela
    cor_texto_nome_do_poder = AMARELO
    cor_borda_ima = cor_borda_tela
    cor_corpo_cobra_turbo = ROXO
    cor_comida_dobro = VERMELHO

# --- NOVOS TEMAS ADICIONADOS ---
class Tema_Synthwave:
    cor_fundo_tela = ROXO
    cor_borda_tela = MAGENTA
    cor_obstaculos = CINZA
    cor_letras = CIANO
    cor_comida_padrão = AMARELO
    cor_cabeca_P1 = CIANO
    cor_corpo_P1 = AMARELO
    cor_cabeca_P2 = LARANJA
    cor_corpo_P2 = BRANCO
    cores_animacao_powerbox = [MAGENTA, AMARELO, CIANO]
    cor_borda_power_box = BRANCO
    cor_texto_nome_do_poder = AMARELO
    cor_corpo_cobra_turbo = MAGENTA
    cor_comida_dobro = VERDE

class Tema_Floresta:
    cor_fundo_tela = PRETO
    cor_borda_tela = VERDE
    cor_obstaculos = CINZA
    cor_letras = BRANCO
    cor_comida_padrão = VERMELHO
    cor_cabeca_P1 = AMARELO
    cor_corpo_P1 = LARANJA
    cor_cabeca_P2 = CIANO
    cor_corpo_P2 = AZUL
    cores_animacao_powerbox = [VERDE, AMARELO, LARANJA]
    cor_borda_power_box = BRANCO
    cor_texto_nome_do_poder = AMARELO
    cor_corpo_cobra_turbo = VERMELHO
    cor_comida_dobro = MAGENTA

class Tema_Oceano:
    cor_fundo_tela = AZUL_ESCURO
    cor_borda_tela = CIANO
    cor_obstaculos = CINZA
    cor_letras = BRANCO
    cor_comida_padrão = VERMELHO
    cor_cabeca_P1 = AMARELO
    cor_corpo_P1 = LARANJA
    cor_cabeca_P2 = BRANCO
    cor_corpo_P2 = VERDE
    cores_animacao_powerbox = [CIANO, AMARELO, VERMELHO]
    cor_borda_power_box = BRANCO
    cor_texto_nome_do_poder = AMARELO
    cor_corpo_cobra_turbo = CIANO
    cor_comida_dobro = MAGENTA