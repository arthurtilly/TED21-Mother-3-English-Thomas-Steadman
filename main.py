import pygame
import math

pygame.init()

SCREEN_WIDTH = 240
SCREEN_HEIGHT = 160

SCALED_SCREEN_WIDTH = SCREEN_WIDTH * 3
SCALED_SCREEN_HEIGHT = SCREEN_HEIGHT * 3

display = pygame.display.set_mode((SCALED_SCREEN_WIDTH, SCALED_SCREEN_HEIGHT))
gameScreen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
done = False

from numberdisplay import *
                
                
stats = StatsDisplay(140, 103, (10,10))
stats.hurtHP(50)
stats.hurtPP(80)
while not done:
        gameScreen.fill((0, 0, 0)) # clear screen
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        stats.update(gameScreen)
        
        clock.tick(30) # limit to 60 fps
        display.blit(pygame.transform.scale(gameScreen, (SCALED_SCREEN_WIDTH, SCALED_SCREEN_HEIGHT)), (0,0))
        pygame.display.flip() # update display buffer