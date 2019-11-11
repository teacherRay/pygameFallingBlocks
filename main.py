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

        if event.type == pygame.KEYDOWN:

                x = player_pos[0]
                y = player_pos[1]

                if event.key == pygame.K_LEFT:
                    x -= 5
                elif event.key == pygame.K_RIGHT:
                    x += 5
                player_pos = [x,y]

    screen.fill((0,0,0))        

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()

