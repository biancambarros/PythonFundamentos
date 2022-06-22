# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Forca:
    def __init__(self):
        pass

    def adivinhar(self):
        pass

    def checar_perdeu(self):
        pass

    def checar_ganhou(self):
        pass

    def esconder_palavra_quadro(self):
        pass

    def mostrar_status(self):
        pass

def sortear_palavra():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():
    # Objeto
    jogo = Forca(sortear_palavra())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    # Verifica o status do jogo
    jogo.mostrar_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if jogo.checar_ganhou():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

    # Executa o programa


if __name__ == "__main__":
    main()
