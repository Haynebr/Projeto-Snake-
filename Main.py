
from game import modes

def main():
    print("Bem-vindo ao Snake Power!")
    modo = input("Escolha o modo: [1] Clássico [2] Caos [3] Tempo limitado: ")
    modes.iniciar_modo(modo)

if __name__ == "__main__":
    main()
