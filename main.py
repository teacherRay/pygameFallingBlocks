#https://www.youtube.com/watch?v=-8n91btt5d8
#git remote add origin https://github.com/teacherRay/pygameFallingBlocks.git
import sys
import pygame
pygame.init()
SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

