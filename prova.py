import pygame

window_size = (600, 400)
status_app = True 

pygame.init()


pygame.display.set_mode(window_size)


while status_app:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status_app = False


    pygame.display.flip()

pygame.quit()
