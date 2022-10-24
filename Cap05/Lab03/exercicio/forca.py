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
        self.letras_erradas = []
        self.letras_certas = []

    def adivinhar(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
            return True
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
            return True
        else:
            return False

    def checar_perdeu(self):
        return self.checar_ganhou() or (len(self.letras_erradas) == 6)

    def checar_ganhou(self):
        if '_' not in self.esconder_palavra_quadro():
            return True
        else:
            return False

    def esconder_palavra_quadro(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                rtn += '_'
            else:
                rtn += letra
        return rtn

    def mostrar_status(self):
        print(board[len(self.letras_certas)])
        print('\nPalavra: ' + self.esconder_palavra_quadro())
        print('\nLetras erradas: ',)
        for letra in self.letras_erradas:
            print(letra, )
        print()
        print('\nLetras corretas: ', )
        for letra in self.letras_certas:
            print(letra, )
        print()


def sortear_palavra():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

def main():

    # Objeto
    jogo = Forca(sortear_palavra())

    # Verifica o status do jogo
    #jogo.mostrar_status()

    while not jogo.checar_perdeu():
        jogo.mostrar_status()
        letra = input('\nDigite uma letra: ')
        jogo.adivinhar(letra[0])

    jogo.mostrar_status()

    if jogo.checar_ganhou():
        print('\nParabéns! Você ganhou!!')
    else:
        print('\nGame over. Você perdeu. ')
        print('A palavra era ' + jogo.palavra)

if __name__ == "__main__":
    main()
