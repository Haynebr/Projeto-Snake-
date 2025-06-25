import pygame                                              #pygame: BIBLIOTECA USADA PARA CRIAR JOGOS 2D EM PYTHON           
import sys                                                 #sys   : PPERMITE SAIR DO PROGRAMA COM sys.exit().
from Game import Colors                                    #Colors: MÓDULO PERSONALIZADO COM CORES TEMÁTICA

# Inicialização
pygame.init()

# Configurações de resolução da tela
largura, altura = 1225, 750 #AQUI ELE ESTÁ APENAS DEFININDO QUAL VAI SER O TAMANHO DA TELA 
tela = pygame.display.set_mode((largura, altura))  #AQUI ELE VAI CRIAR UMA JANELA COM O TAMANHO DEFINIDO ANTERIORMENTE 
pygame.display.set_caption("Cadastro do Jogador")  #AQUI ELE VAI DEFINIR O TÍTULO DA JANELA ( QUE APARECE NA BARRA DO TOPO DA JANELA )
# CORES PADRONIZADA DO TEMA EM QUE ESCOLHEMOS
fundo = Colors.Tema_Base.cor_fundo_tela #COR DE FUNDO
texto_cor = Colors.Tema_Base.cor_letras #COR DE TEXTO
destaque = Colors.Tema_Base.cor_texto_nome_do_poder #COR DE TEXTO DESTACADO (TITULO)
borda = Colors.Tema_Base.cor_borda_tela #COR DA BORDA

# Fonte
fonte = pygame.font.Font("Assets/text/Pixeltype.ttf", 48) #CARREGA UMA FONTE EXTERNA NO FORMATO .TTF NO TAMANHO 48 QUE É USADA PARA EXIBIR OS TEXTOS DE FORMA PIXELADA

#VARIAVEIS DE ENTRADA 
entrada_texto = ""    #ISSO VAI GUARDAR O NOME DIGITADO PELO USUARIO
nome_cadastrado = None #VAI SER PREENCHIDO AO FINAL DO CADASTRO 

# LOOP DE CADASTRO PARA NOVOS JOGADORES 
cadastro_ativo = True  
while cadastro_ativo:  #O LOOP VAI SE MANTER ENQUANTO O JOGADOR NAO TIVER SE CADASTRADO
    tela.fill(fundo) #ISSO FAZ COM QUE A TELA DE FUNDO SEJA PINTADA A CADA FRAME

    # AQUI SÃO TEXTOS DE INSTRUÇÕES 
    titulo = fonte.render("Digite seu nome e pressione Enter:", True, destaque) #INSTRUÇÃO DE COMO SE CADASTRAR
    rect_titulo = titulo.get_rect(center=(largura // 2, altura // 3))  #RESPONSAVEL PELO POSICIONAMENTO DA INSTRUÇÃO ( CENTRALIZADO NA PARTE SUPERIOR DA TELA )
    tela.blit(titulo, rect_titulo)  #O BLIT É RESPONSÁVEL POR GERAR O TEXTO NA TELA

    # Nome cadastrado
    texto = fonte.render(entrada_texto, True, texto_cor)  #FUNÇÃO DE RENDERIZAR O TEXTO DIGITADO ATÉ O MOMENTO
    rect_texto = texto.get_rect(center=(largura // 2, altura // 2))  #RESPONSÁVEL POR MANTER A ESCRITA SEMPRE NO MEIO DA DELA 
    tela.blit(texto, rect_texto)  #APENAS DESENHO 

    # Borda visual 
    pygame.draw.rect(tela, borda, rect_texto.inflate(20, 20), 2) #AUMENTA LEVEMENTE O RETÂNGULO PARA DAR ESPAÇO VISUAL E A ESPESURA DA BORDA

    pygame.display.update()  #ATUALIZA A TELA PARA QUE TUDO QUE FOI DESENHADO APAREÇA PARA O JOGADOR

#TRATAMENTO DE EVENTOS 
    for evento in pygame.event.get(): #ALTERA SOBRE TODOS OS EVENTOS COMO "MOUSE, TECLADO, ETC" 

        if evento.type == pygame.QUIT:  #ENCERRA O PROGRAMA QUANDO O JOGADOR CLICA NO "X" DA JANELA
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.KEYDOWN:  #DETECTA SE UMA TECLA FOI PRESSIONADA
            if evento.key == pygame.K_RETURN:   #SE PRESSIONAR ENTER E O NOME NÃO ESTIVER VAZIO, O NOME É SALVO E O LOOP DE CADASTRO TERMINA
                if entrada_texto.strip() != "":
                    nome_cadastrado = entrada_texto.strip()
                    cadastro_ativo = False
            elif evento.key == pygame.K_BACKSPACE: #REMOVE O ULTIMO CARACTERE DIGITADO 
                entrada_texto = entrada_texto[:-1]
            else:
                if len(entrada_texto) < 20:  #ENQUANTO O NOME TIVER MENOS DE 20 CARACTERES, PODE-SE ADICIONAR +1 ELEMENTO
                    entrada_texto += evento.unicode

# Exibe no terminal 
print(f"Jogador cadastrado: {nome_cadastrado}")  #QUANDO O JOGADOR TERMINA DE DIGITAR E APERTA ENTER, O NOME É EXIBIDO NO TERMINAL
pygame.quit() #O PYGAME É ENCERRADO
