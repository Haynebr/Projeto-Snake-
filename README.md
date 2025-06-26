# 🐍 Snake Power

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/pygame-2.6.1-green.svg)](https://www.pygame.org/project/Pygame/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Uma releitura moderna e customizável do clássico jogo da Cobrinha, desenvolvido em Python com a biblioteca Pygame. Inclui múltiplos modos de jogo, Power-ups e Temas Visuais.

---
## 📸 Capturas de Tela

| Menu Principal | Gameplay em Ação |
| :---: | :---: |
* <img src="Assets\img\gameplay.jpg.jpg" alt="Gameplay do jogo em ação." width="450">

---

## ✨ Funcionalidades (Features)

* **Múltiplos Modos de Jogo:**
    * **Clássico:** A experiência tradicional de Snake.
    * **2 Players:** Compita contra um amigo no mesmo teclado.
    * **Tempo Limitado:** Corra contra o relógio! Coma frutas para ganhar tempo e desvie dos inimigos para não perder.

* **Sistema de Power-Ups:**
    * **Turbo:** Aumenta drasticamente a velocidade da cobra.
    * **Fruta Duplicada:** Frutas valem o dobro de pontos e crescimento.
    * **Imã de Frutas:** Atrai frutas próximas para a cabeça da cobra.

* **Sistema de Pontuação e Ranking:**
    * Acompanhe seu score em tempo real e desafie seus próprios recordes a cada partida. O jogo salva as melhores pontuações em um ranking local.
    * <img src="Assets\img\ranking.jpg.jpg" alt="Tela de Ranking com as melhores pontuações" width="450">

* **Obstáculos e Inimigos Desafiadores:**
    * Desvie de barreiras estáticas e enfrente cobras inimigas com inteligência artificial para testar seus reflexos.

* **Customização Completa:**
    * Ajuste o número de inimigos, obstáculos, comidas e ative ou desative os Power-Ups através do menu de opções.
    * <img src="Assets\img\menu-configuracoes.jpg.jpg" alt="Menu de Configurações do Jogo" width="450">

* **Temas Visuais:**
    * Escolha entre múltiplos temas de cores (Dark, Light, Synthwave, etc.) para personalizar a aparência do jogo.
---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** [Python 3.12](https://www.python.org/)
* **Biblioteca Gráfica:** [Pygame](https://www.pygame.org/)
* **Bibliotecas Padrão:** `random`, `sys`, `math`, `json`
* **Controle de Versão:** [Git](https://git-scm.com/) & [GitHub](https://github.com)

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o jogo em sua máquina local.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Instalação e Execução

1.  Clone o repositório para a sua máquina:
    ```bash
    git clone [https://github.com/Haynebr/Projeto-Snake-](https://github.com/Haynebr/Projeto-Snake-)
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd Projeto-Snake-
    ```
3.  (Recomendado) Crie e ative um ambiente virtual para isolar as dependências do projeto:
    ```bash
    # Cria o ambiente virtual
    python -m venv venv
    # Ativa o ambiente (no Windows)
    venv\Scripts\activate
    # No Mac/Linux, o comando seria: source venv/bin/activate
    ```
4.  Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```
    *(Lembre-se de criar o arquivo `requirements.txt` com o comando `pip freeze > requirements.txt` se ainda não o fez).*

5.  Execute o jogo a partir do menu principal:
    ```bash
    python Menu.py
    ```
---

## 👥 Contribuidores

Um projeto desenvolvido pela equipe:

* [Hayne René Campos de Andrade](https://github.com/Haynebr)
* [Aryendrew Arnold da Silva Oliveira](https://github.com/Aryendrew-Arnold)
* [Weverton Walter Dias Tomaz](https://github.com/Wevison)
* [Karlos Eduardo Saraiva da Silva](https://github.com/Karlos1766)
* [Rauê José Nobrega](https://github.com/rauejose)

---

## 📄 Licença

Este projeto está sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.