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
        self.field = []
        self.score = 0
        self.state = "start"
        self.number_figure = 0
        self.next_figure = []
        self.next_figure.append( Figure(3,0) )
        self.number_figure += 1
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.next_figure.append( Figure(3,0) )
        self.number_figure += 1
        print("self.next_figure numero : ", len(self.next_figure))
        
        self.figure = self.next_figure[len(self.next_figure)-2]

        if self.figure.type == 0:
            self.I+=1
        elif self.figure.type == 1:
            self.Z+=1
        elif self.figure.type == 2:
            self.S+=1
        elif self.figure.type == 3:
            self.L+=1
        elif self.figure.type == 4:
            self.J+=1
        elif self.figure.type == 5:
            self.T+=1
        elif self.figure.type == 6:
            self.O+=1

        print(f"n.{self.number_figure} - {self.figure.type}")


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
        if self.score > 30 and self.score < 49:
            self.level = 3
        elif self.score > 49 and self.score < 79 :
            self.level = 4
            
    
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
MYCOLOR1 = (107, 255, 139)


size = (800, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TETRIS - by mastyx ")
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(25, 10)
counter = 0 

pressing_down = False

mixer.music.load('tetris1.ogg')
mixer.music.play(-1)
#pygame.mixer.Channel(0).play(pygame.mixer.Sound('tetris1.ogg'),-1)
#ciclo del gioco 

def griglia_statistiche():

    # disegna il pezzo
    figura1 = Figure.figures[0][0]
    #print ("Figura 1 ", figura1 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura1:
                pygame.draw.rect(screen, colori_figure[1],[500 + 10 * (j),60 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10 * j, 60 + 10 * i, 10, 10 ], 1)
    # disegna il pezzo
    figura2 = Figure.figures[1][0]
    #print ("Figura 2 ", figura2 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura2:
                pygame.draw.rect(screen, colori_figure[7],[500 + 10 * (j),110 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10* j, 110 + 10 * i, 10, 10 ], 1)
    # disegna il pezzo
    figura3 = Figure.figures[2][0]
    #print ("Figura 3 ", figura3 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura3:
                pygame.draw.rect(screen, colori_figure[6],[500 + 10 * (j),160 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10* j, 160 + 10 * i, 10, 10 ], 1)
    # disegna il pezzo
    figura4 = Figure.figures[3][0]
    #print ("Figura 4 ", figura4 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura4:
                pygame.draw.rect(screen, colori_figure[3] ,[500 + 10 * (j),210 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10* j, 210 + 10 * i, 10, 10 ], 1)
    # disegna il pezzo
    figura5 = Figure.figures[4][0]
    #print ("Figura 5 ", figura5 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura5:
                pygame.draw.rect(screen, colori_figure[2] ,[500 + 10 * (j),260 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10* j, 260 + 10 * i, 10, 10 ], 1)
    # disegna il pezzo
    figura6 = Figure.figures[5][0]
    #print ("Figura 6 ", figura6 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura6:
                pygame.draw.rect(screen, colori_figure[4],[500 + 10 * (j),310 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10* j, 310 + 10 * i, 10, 10 ], 1)
    # disegna il pezzo
    figura7 = Figure.figures[6][0]
    #print ("Figura 7 ", figura7 )
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in figura7:
                pygame.draw.rect(screen, colori_figure[5],[500 + 10 * (j),360 + 10 * (i),10 , 10])
    # disegna la griglia 
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 500  + 10* j, 360 + 10 * i, 10, 10 ], 1)
     

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
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                print(f"I {game.I}\nS {game.S}\nL {game.L}\nJ {game.J}\nT {game.T}\nO {game.O}\nZ {game.Z}\n")
                done = True
    # eventi del rilasio del tasto
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False

    screen.fill(BLACK)
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

    


    #griglia del prossimo pezzo
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, GRAY, [ 350 + game.zoom * j, 60 + game.zoom * i, game.zoom, game.zoom ], 1)
    if game.next_figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if len(game.next_figure) >= 1:
                    if p in game.next_figure[len(game.next_figure)-1].image():
                        pygame.draw.rect(screen, MYCOLOR1,
                                         [350 + game.zoom * (j),
                                          60 + game.zoom * (i),
                                          game.zoom , game.zoom ])
    griglia_statistiche() 

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 45, True, False)
    text = font.render("Score: " + str(game.score), True, GRAY)
    pezzo_i = font.render(f"{game.I}", True, GRAY)  
    pezzo_z = font.render(f"{game.Z}", True, GRAY)
    pezzo_s = font.render(f"{game.S}", True, GRAY)
    pezzo_l = font.render(f"{game.L}", True, GRAY)
    pezzo_j = font.render(f"{game.J}", True, GRAY)
    pezzo_t = font.render(f"{game.T}", True, GRAY)
    pezzo_o = font.render(f"{game.O}", True, GRAY)
    next_text = font.render(f"NEXT", True, GRAY)

    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))
    screen.blit(text, [0, 0])
    screen.blit(pezzo_i, [550,65])
    screen.blit(pezzo_z, [550,115])
    screen.blit(pezzo_s, [550,165])
    screen.blit(pezzo_l, [550,215])
    screen.blit(pezzo_j, [550,265])
    screen.blit(pezzo_t, [550,315])
    screen.blit(pezzo_o, [550,365])
    screen.blit(next_text, [353,140])
    if game.state == "gameover":
        screen.blit(text_game_over, [60, 200])
        screen.blit(text_game_over1, [65, 265])

    pygame.display.flip()
    clock.tick(fps)
    
    
pygame.quit()

