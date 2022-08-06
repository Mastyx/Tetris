import pygame

window_size = (600, 400)
status_app = True 

pygame.init()

WHITE = (255,255,255)

screen = pygame.display.set_mode(window_size)

figura = [
        [1,5,9,13], 
        [2,6,5,9],
        ]
while status_app:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status_app = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               status_app = False 

    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, WHITE, (i+10,j+10, 20, 20) )  
            
    
    pygame.display.flip()

pygame.quit()
