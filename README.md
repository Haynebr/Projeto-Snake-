snake_power/
│
├── main.py                → Arquivo principal que inicia o jogo
├── game/
│   ├── __init__.py        → Torna 'game' um pacote
│   ├── snake.py           → Lógica da cobrinha (movimentação, crescimento, etc.)
│   ├── food.py            → Lógica da comida (geração, posicionamento)
│   ├── powers.py          → Implementação dos poderes especiais
│   ├── modes.py           → Modos de jogo: clássico, caos, tempo limitado
│   ├── score.py           → Sistema de pontuação e recordes
│   ├── difficulty.py      → Dificuldade adaptativa
│   └── utils.py           → Funções auxiliares (por exemplo, detecção de colisão)
│
├── assets/
│   ├── skins/             → Arquivos de skins da cobrinha
│   └── sounds/            → Arquivos de trilha sonora e efeitos
│
├── README.md              → Descrição do projeto
└── requirements.txt       → Bibliotecas necessárias
