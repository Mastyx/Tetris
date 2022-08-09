import pygame
width = 1000
height = 700
window_size = (width, height)
status_app = True 

pygame.init()

WHITE = (255,255,255)

screen = pygame.display.set_mode(window_size)

figura = [
        [1,5,9,13], 
        [2,6,5,9],
        ]
larghezza_quadrato = 20

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
                    ( larghezza_quadrato * i + ((width/2)-(larghezza_quadrato*10)/2), 
                        larghezza_quadrato * j + 50, 
                        larghezza_quadrato, larghezza_quadrato), 1)

    
    pygame.display.flip()

pygame.quit()
