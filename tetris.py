import pygame
from pygame.locals import *
from pygame import mixer
import random 
from elements import colori_figure, Figure

class Tetris:
    level = 2
    score = 0
    state = "start"
    field = [] 
    height = 0
    width = 0
    x = 100
    y = 60 
    zoom = 20
    figure = None
    I=0;S=0; L=0; J=0; T=0; O=0; Z=0 

    def __init__(self, height, width) :
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        x = random.randint(5, 15)
        self.figure = Figure(x, 0)
        if self.figure.type == 0:
            self.I+=1
        elif self.figure.type == 1:
            self.S+=1
        elif self.figure.type == 2:
            self.L+=1
        elif self.figure.type == 3:
            self.J+=1
        elif self.figure.type == 4:
            self.T+=1
        elif self.figure.type == 5:
            self.O+=1
        elif self.figure.type == 6:
            self.Z+=1

        print(self.figure.type)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                                intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2
    
    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1 
        self.freeze()
   
    def go_down(self):
       self.figure.y += 1
       if self.intersects():
           self.figure.y -= 1
           self.freeze()

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation
    

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[ i + self.figure.y ][ j + self.figure.x ] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            game.state = "gameover"

pygame.init()
mixer.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)



size = (800, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TETRIS - by mastyx ")
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(30, 20)
counter = 0 

pressing_down = False

mixer.music.load('tetris1.ogg')
mixer.music.play(-1)

#ciclo del gioco 
while not done:
    
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0
    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == 'start':
            game.go_down()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #eventi della pressione dei tasti
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
                print("Sinistra")
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
                print("Destra")
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                print(f"I {game.I}\nS {game.S}\nL {game.L}\nJ {game.J}\nT {game.T}\nO {game.O}\nZ {game.Z}\n")
                done = True
    # eventi del rilasio del tasto
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False

    screen.fill(WHITE)
    # disegnamo la griglia
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colori_figure[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    
    if game.figure is not None:

        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colori_figure[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])
    
    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 45, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    pezzo_i = font.render(f"I : {game.I}", True, BLACK) 
    pezzo_s = font.render(f"S : {game.S}", True, BLACK)
    
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))
    screen.blit(text, [0, 0])
    screen.blit(pezzo_i, [600,10])
    screen.blit(pezzo_s, [600,30])
    if game.state == "gameover":
        screen.blit(text_game_over, [60, 200])
        screen.blit(text_game_over1, [65, 265])

    pygame.display.flip()
    clock.tick(fps)
    
    
pygame.quit()

