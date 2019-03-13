import pygame
import math

pygame.init()

SCREEN_WIDTH = 240
SCREEN_HEIGHT = 160

display = pygame.display.set_mode((SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2))
gameScreen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
done = False

from numberdisplay import *
                
                
hp = NumDisplay(90, (10,10))
hp.begin_approach(120, NUM_SCROLL_SLOW)
while not done:
        gameScreen.fill((0, 0, 0)) # clear screen
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        hp.update(gameScreen)
        
        clock.tick(30) # limit to 60 fps
        display.blit(gameScreen, (0,0))
        pygame.display.flip() # update display buffer