import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
done = False

while not done:
        screen.fill((0, 0, 0)) # clear screen
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        clock.tick(60) # limit to 60 fps
        pygame.display.flip() # update display buffer