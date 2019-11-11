#https://www.youtube.com/watch?v=-8n91btt5d8
#git remote add origin https://github.com/teacherRay/pygameFallingBlocks.git
import sys
import pygame
pygame.init()

RED =(255,0,0)

player_pos = [400,300]
player_size = 50
    
SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()

