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
        self.type = random.randint(0, len(self.figure) -1)
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

