# Game/Config.py

import pygame
import sys
from . import Colors # Importação relativa

# CORREÇÃO: Adicionadas as chaves para o modo de tempo e a vírgula que faltava
dictConfigs = {
    "Enemies": 0,
    "Foods": 1,
    "Obstacles": 0,
    "Powers": False,
    "GameMode": 0, # 0: Classic, 1: 2 Players, 2: Limited Time
    "TimeLimit_InitialTime": 120, # Em segundos
    "TimeLimit_TimeGained": 5,    # Segundos ganhos por comida
    "TimeLimit_TimeLost": 10      # Segundos perdidos por colisão com inimigo
}

def gameConfigs(screen, screen_width, screen_height, textFont):
    # O resto do arquivo continua exatamente igual...
    clock = pygame.time.Clock()

    PRETO = Colors.PRETO
    BRANCO = Colors.BRANCO
    AMARELO = Colors.AMARELO
    CINZA = Colors.CINZA

    opcoes = ["Enemies", "Foods", "Obstacles", "Powers", "GameMode", "Back"]
    opcao_selecionada = 0

    modos_jogo = ["Classic", "2 Players", "Limited Time"]

    rodando = True

    while rodando:
        screen.fill(PRETO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
                if evento.key == pygame.K_DOWN:
                    opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)

                if evento.key == pygame.K_LEFT:
                    if opcoes[opcao_selecionada] == "Enemies":
                        dictConfigs["Enemies"] = max(0, dictConfigs["Enemies"] - 1)
                    elif opcoes[opcao_selecionada] == "Foods":
                        dictConfigs["Foods"] = max(1, dictConfigs["Foods"] - 1)
                    elif opcoes[opcao_selecionada] == "Obstacles":
                        dictConfigs["Obstacles"] = max(0, dictConfigs["Obstacles"] - 1)
                    elif opcoes[opcao_selecionada] == "Powers":
                        dictConfigs["Powers"] = not dictConfigs["Powers"]
                    elif opcoes[opcao_selecionada] == "GameMode":
                        dictConfigs["GameMode"] = (dictConfigs["GameMode"] - 1) % len(modos_jogo)

                if evento.key == pygame.K_RIGHT:
                    if opcoes[opcao_selecionada] == "Enemies":
                        dictConfigs["Enemies"] += 1
                    elif opcoes[opcao_selecionada] == "Foods":
                        dictConfigs["Foods"] += 1
                    elif opcoes[opcao_selecionada] == "Obstacles":
                        dictConfigs["Obstacles"] += 1
                    elif opcoes[opcao_selecionada] == "Powers":
                        dictConfigs["Powers"] = not dictConfigs["Powers"]
                    elif opcoes[opcao_selecionada] == "GameMode":
                        dictConfigs["GameMode"] = (dictConfigs["GameMode"] + 1) % len(modos_jogo)

                if evento.key == pygame.K_RETURN:
                    if opcoes[opcao_selecionada] == "Back":
                        rodando = False

        # Renderizar textos
        for i, opcao in enumerate(opcoes):
            cor = AMARELO if i == opcao_selecionada else BRANCO

            texto = ""
            if opcao == "Enemies":
                texto = f"Enemies: < {dictConfigs['Enemies']} >"
            elif opcao == "Foods":
                texto = f"Foods: < {dictConfigs['Foods']} >"
            elif opcao == "Obstacles":
                texto = f"Obstacles: < {dictConfigs['Obstacles']} >"
            elif opcao == "Powers":
                status = "On" if dictConfigs['Powers'] else "Off"
                texto = f"Powers: < {status} >"
            elif opcao == "GameMode":
                modo = modos_jogo[dictConfigs['GameMode']]
                texto = f"Game Mode: < {modo} >"
            elif opcao == "Back":
                texto = "Back"

            label = textFont.render(texto, True, cor)
            rect = label.get_rect(center=(screen_width // 2, screen_height // 3 + i * 60))
            screen.blit(label, rect)

        pygame.display.flip()
        clock.tick(60)