import pygame
import random 

colori_figure = [
    (83, 152, 155), #ciano
    (201, 58, 58), # rosso
    (68, 206, 86), #verde
    (86, 108, 196), #blu
    (176, 221, 70), #giallo
    (234, 123, 32), #arancio
    (232, 51, 213), #viola
]

class Figure:
    x = 0; y = 0;
    figures = [
        [[1,5,9,13], [4,5,6,7]],                            # figura I
        [[4,5,9,10], [2,6,5,9]],                            # figura Z
        [[6,7,9,10], [1,5,6,10]],                           # figura S
        [[1,2,5,9], [0,4,5,6], [1,5,9,8], [4,5,6,10]],      # figura L
        [[1,2,6,10], [5,6,7,9], [2,6,10,11], [3,5,6,7]], 
        [[1,4,5,6], [1,4,5,9], [4,5,6,9,], [1,5,6,9]],      # figura T
        [[1,2,5,6]]                                         # figura O  
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) -1)
        self.color = random.randint(1, len(colori_figure) -1)
        self.rotation = 0


    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type] )


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

    def __init__(self, height, width) :
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)

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
            sefl.figure.y += 1
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
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TETRIS - by mastyx ")
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0 

pressing_down = False

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
                

    pygame.display.flip()
    clock.tick(fps)
    screen.fill(WHITE)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score : ", True, BLACK)
    screen.blit(text, [0, 0])
pygame.quit()

