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
    def __init__(self, palavra):
        self.palavra = palavra

    def adivinhar(self, letra):
        if letra in self.palavra:
            return True
        else:
            return False

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
    # Executa o programa
    n_tentativas = len(board)
    print(board[0])

    # Objeto
    jogo = Forca(sortear_palavra())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    for tentativa in range(len(board)):
        letra = input("Informe uma letra: ")
        status = jogo.adivinhar(letra)
        print(status)

    # Verifica o status do jogo
    jogo.mostrar_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    #if jogo.checar_ganhou():
    #    print('\nParabéns! Você venceu!!')
    #else:
    #    print('\nGame over! Você perdeu.')
    #    print('A palavra era ' + game.word)

    #print('\nFoi bom jogar com você! Agora vá estudar!\n')


if __name__ == "__main__":
    main()
