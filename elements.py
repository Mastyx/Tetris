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
    x = 0; y = 0; numero_figura = 0; numero_colore = 0;
    
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
        self.type = self.select_type()
        self.color = self.select_color()         
        # print(f"tipo: {self.type} colore : {self.color}")

        self.rotation = 0
    
    def select_type(self):
        type_figure = random.randint(0, len(self.figures) -1)
        return type_figure

    def select_color(self):
        type_color = random.randint(1, len(colori_figure) -1)
        return type_color


    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type] )



