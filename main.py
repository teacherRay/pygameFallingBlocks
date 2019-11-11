#https://www.youtube.com/watch?v=-8n91btt5d8
#git remote add origin https://github.com/teacherRay/pygameFallingBlocks.git
import sys
import pygame
import random

pygame.init()

SCREENWIDTH = 800
SCREENHEIGHT = 600
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

enemy_x = random.randint(50,SCREENWIDTH)
enemy_y = random.randint(50,300)

player_size = 50
player_pos = [SCREENWIDTH / 2, SCREENHEIGHT - 2 * player_size]
enemy_size = 50
enemy_pos = [enemy_x, enemy_y]
   
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

game_over = False

clock = pygame.time.Clock()

def spawn_enemy():
    enemy_x = random.randint(50,SCREENWIDTH)
    enemy_y = random.randint(50,300)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player_pos[0] -= 40
                elif event.key == pygame.K_RIGHT:
                    player_pos[0] += 40

    screen.fill((BLACK))  
  

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    
    if enemy_y >= 0 and enemy_y <= SCREENHEIGHT:
        enemy_y += 5

    if enemy_y >= SCREENHEIGHT:
       enemy_y = random.randint(50,300)
       enemy_x = random.randint(50,SCREENWIDTH-50)  

    pygame.draw.rect(screen, BLUE, (enemy_x, enemy_y, player_size, player_size))

    clock.tick(30)

    pygame.display.update()

