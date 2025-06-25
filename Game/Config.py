# Game/Config.py
import pygame
import sys
from . import Colors

dictConfigs = {
    "Enemies": 0, "Foods": 1, "Obstacles": 0, "Powers": False, "GameMode": 0,
    "Theme": 0, # 0: Dark, 1: Light, 2: Synthwave, 3: Forest, 4: Ocean
    "TimeLimit_InitialTime": 120, "TimeLimit_TimeGained": 5, "TimeLimit_TimeLost": 10
}

def gameConfigs(screen, screen_width, screen_height, textFont):
    clock = pygame.time.Clock()
    opcoes = ["Enemies", "Foods", "Obstacles", "Powers", "GameMode", "Theme", "Reset settings", "Back"]
    modos_jogo = ["Classic", "2 Players", "Limited Time"]
    # Lista de nomes de temas atualizada
    modos_tema = ["Dark", "Light", "Synthwave", "Forest", "Ocean"]
    opcao_selecionada = 0

    rodando = True
    while rodando:
        # A lógica para selecionar o tema dinamicamente
        if dictConfigs['Theme'] == 0: Tema = Colors.Tema_Base
        elif dictConfigs['Theme'] == 1: Tema = Colors.Tema_claro
        elif dictConfigs['Theme'] == 2: Tema = Colors.Tema_Synthwave
        elif dictConfigs['Theme'] == 3: Tema = Colors.Tema_Floresta
        elif dictConfigs['Theme'] == 4: Tema = Colors.Tema_Oceano
        else: Tema = Colors.Tema_Base
        
        screen.fill(Tema.cor_fundo_tela)

        # O resto do loop de eventos e desenho continua o mesmo da versão anterior...
        # ... (código para lidar com input e desenhar as opções)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP: opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
                if evento.key == pygame.K_DOWN: opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
                
                opcao_atual = opcoes[opcao_selecionada]
                change = 0
                if evento.key == pygame.K_RIGHT: change = 1
                if evento.key == pygame.K_LEFT: change = -1
                
                if change != 0:
                    if opcao_atual == "Enemies": dictConfigs["Enemies"] = max(0, dictConfigs["Enemies"] + change)
                    elif opcao_atual == "Foods": dictConfigs["Foods"] = max(1, dictConfigs["Foods"] + change)
                    elif opcao_atual == "Obstacles": dictConfigs["Obstacles"] = max(0, dictConfigs["Obstacles"] + change)
                    elif opcao_atual == "Powers": dictConfigs["Powers"] = not dictConfigs["Powers"]
                    elif opcao_atual == "GameMode": dictConfigs["GameMode"] = (dictConfigs["GameMode"] + change) % len(modos_jogo)
                    elif opcao_atual == "Theme": dictConfigs["Theme"] = (dictConfigs["Theme"] + change) % len(modos_tema)
                
                if evento.key == pygame.K_RETURN:
                    if opcoes[opcao_selecionada] == "Back": rodando = False
                    elif opcoes[opcao_selecionada] == "Reset settings":
                        # Reseta para os padrões
                        dictConfigs.update({"Enemies": 0, "Foods": 1, "Obstacles": 0, "Powers": False, "GameMode": 0, "Theme": 0})

        for i, opcao in enumerate(opcoes):
            cor = Colors.AMARELO if i == opcao_selecionada else Tema.cor_letras
            texto = ""
            if opcao == "Enemies": texto = f"Enemies: < {dictConfigs['Enemies']} >"
            elif opcao == "Foods": texto = f"Foods: < {dictConfigs['Foods']} >"
            elif opcao == "Obstacles": texto = f"Obstacles: < {dictConfigs['Obstacles']} >"
            elif opcao == "Powers": texto = f"Powers: < {'On' if dictConfigs['Powers'] else 'Off'} >"
            elif opcao == "GameMode": texto = f"Game Mode: < {modos_jogo[dictConfigs['GameMode']]} >"
            elif opcao == "Theme": texto = f"Theme: < {modos_tema[dictConfigs['Theme']]} >"
            elif opcao == "Reset settings": texto = "Reset settings"
            elif opcao == "Back": texto = "Back"
            
            label = textFont.render(texto, True, cor)
            rect = label.get_rect(center=(screen_width // 2, screen_height // 4 + i * 55))
            screen.blit(label, rect)

        pygame.display.flip()
        clock.tick(60)