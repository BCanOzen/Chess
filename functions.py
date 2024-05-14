import pygame
from constants import *

pygame.init()

# draw main game loop
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column*200) , row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column*200) , row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray' , [0,800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold' , [0,800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold' , [800,0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move !', 'White: Select a Destination!',
                       'Black: Select a Piece to Move !', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))

# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22,
                                     white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10,
                                              white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1,
                                                 white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, 
                                     black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10,
                                              black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1,
                                                  black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)