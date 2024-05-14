import pygame
from constants import *
from functions import *

 
# MAIN GAME LOOP

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()    
    
pygame.quit()