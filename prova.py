import pygame
width = 1000
height = 700
window_size = (width, height)
status_app = True 

pygame.init()

WHITE = (255,255,255)
larghezza_quadrato = 20
screen = pygame.display.set_mode(window_size)


class Figura:

    figura = [
        [1,5,9,13], [2,6,5,9],
        ]
    def __init__(self, x ,y ):
        self.x = x
        self.y = y
        

oggetto1 = Figura(20, 1)

start_griglia_x =  ((width/2)-(larghezza_quadrato*10)/2)
start_griglia_y = 20

while status_app:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status_app = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               status_app = False 
    # griglia
    for i in range(10) :
        for j in range(20):
            pygame.draw.rect(
                    screen, WHITE, 
                    ( larghezza_quadrato * i + start_griglia_x, 
                        larghezza_quadrato * j + start_griglia_y, 
                        larghezza_quadrato, larghezza_quadrato), 1)
    

    print(oggetto1.figura[1])
    for i in range(4):
        for j in range(4):
            p = i * 4 + j
            if p in oggetto1.figura[1] :
                x = larghezza_quadrato * (oggetto1.x + j )
                y = larghezza_quadrato * (oggetto1.y + i )
                pygame.draw.rect(screen, WHITE, 
                        (x, y, larghezza_quadrato , larghezza_quadrato ) )
            
    
    pygame.display.flip()

pygame.quit()
