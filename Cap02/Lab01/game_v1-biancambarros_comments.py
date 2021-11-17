# Game Ping-Pong
##Importação de bibliotecas
from tkinter import *
import random
import time
##Variáveis definindo nível e largura da raquete conforme o nível selecionado pelo usuário
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 500/level

##Montando a tela a partir das bibliotecas importadas 
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
count = 0
lost = False
##Definindo classe com características e comportamentos da bolinha
class Bola:
    ##Método construtor, que inicializa a bolinha
    def __init__(self, canvas, Barra, color):
        ##São atribuídos valores padrão aos atributos do objeto Bola
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    ##Método que desenha e movimenta a bolinha na tela
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

#Definindo a classe com as características e o comportamento da raquete
class Barra:
    ##Método construtor, que inicializa a raquete
    def __init__(self, canvas, color):
        ##São definidos valores padrão aos atributos do objeto Barra
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
    ##Métodos que desenham e movimentam a barra na tela
    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

##Função (método) para iniciar o jogo 
def start_game(event):
    ##Variáveis inicializando os contadores de perda e pontuação
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")
    ##Funções que montam a tela para o usuário
    time.sleep(1)
    Barra.draw()
    Bola.draw()

##Função (método) para demonstrar a pontuação na tela
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))
##Função (método) para demonstrar a mensagem de Game over
def game_over():
    canvas.itemconfig(game, text="Game over!")

##Variáveis para determinar as cores da bola e da raquete
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

##Variáveis para determinar as coresda tela
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

#Métodos de inicialização da tela
canvas.bind_all("<Button-1>", start_game)

root.mainloop()



