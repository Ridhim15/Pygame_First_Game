import sys
import pygame
from pygame.locals import QUIT
import random
import time
pygame.init()
WIDTH,HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Fist Game')

PLAYER_HEIGHT,PLAYER_WIDTH = 100,80
PLAYER_VEL=10

BG=pygame.transform.scale(pygame.image.load("./assets/bg.jpg"),(WIDTH,HEIGHT)) 
def draw(player):
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,"red",player)
    pygame.display.update()
def main():
    run=True

    clock=pygame.time.Clock()
    
    
    player=pygame.Rect(350,HEIGHT-PLAYER_HEIGHT,
                       PLAYER_WIDTH,PLAYER_HEIGHT)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                run=False
                break
        draw(player)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x- PLAYER_VEL>=0:
            player.x-=PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x+=PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL - PLAYER_HEIGHT <=HEIGHT:
            player.y -=PLAYER_VEL
        if keys[pygame.K_DOWN] :
            player.y +=PLAYER_VEL

if __name__== "__main__":
    main()