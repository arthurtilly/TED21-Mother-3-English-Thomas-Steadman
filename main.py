import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
done = False

HP_SCROLL_FAST = 0
HP_SCROLL_SLOW = 1

class HPDisplay(): # Class to display a 3-digit HP value and add scrolling through values
        def __init__(self, value, pos):
                self.currentHP = value
                self.digitHundreds = (math.floor(value / 100.0), 0)
                self.digitTens = (math.floor((value % 100) / 10.0), 0)
                self.digitOnes = (value % 10, 0)
                self.targetHP = value
                self.speed = HP_SCROLL_FAST
                self.x = pos[0]
                self.y = pos[1]

        def begin_approach(self, target, speed):
                self.targetHP = target
                self.speed = speed

        def getimg(self, digitInfo):
                imageNum = digitInfo[0] * 8 + digitInfo[1]
                return pygame.image.load("numbers/num%d.png" % imageNum)
        
        def display(self, gameScreen):
                gameScreen.blit(self.getimg(self.digitHundreds), (self.x, self.y))
                gameScreen.blit(self.getimg(self.digitTens), (self.x + 8, self.y))
                gameScreen.blit(self.getimg(self.digitOnes), (self.x + 16, self.y))
                
        def update(self, gameScreen):
                pass
                
                
hp = HPDisplay(234, (10,10))
while not done:
        screen.fill((0, 0, 0)) # clear screen
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        hp.display(screen)
        
        clock.tick(60) # limit to 60 fps
        pygame.display.flip() # update display buffer