import math
import pygame

# Scrolling speeds:
NUM_SCROLL_FAST = 0 # Normal scrolling speed
NUM_SCROLL_SLOW = 1 # Scrolling speed while guarding

# Scrolling states:
NUM_NOT_SCROLLING = 0
NUM_SCROLLING_DOWNWARDS = 1
NUM_SCROLLING_UPWARDS = 2

# Load images
scrollingNumberImages = []
for i in range(80):
        scrollingNumberImages.append(pygame.image.load("numbers/num%d.png" % i))

class NumDisplay(): # Class to display a 3-digit HP value and add scrolling through values
        def __init__(self, value, pos):
                self.currentVal = value
                # The current values of each digit
                # Format: [current value, scroll index, scroll state]
                self.digitHundreds = [math.floor(value / 100.0), 0, NUM_NOT_SCROLLING]
                self.digitTens = [math.floor((value % 100) / 10.0), 0, NUM_NOT_SCROLLING]
                self.digitOnes = [value % 10, 0, NUM_NOT_SCROLLING]
                self.targetVal = value
                self.speed = NUM_SCROLL_FAST
                self.x = pos[0]
                self.y = pos[1]
                self.timer = 0

        def begin_approach(self, target, speed=None):
                if target == self.currentVal:
                        return
                self.targetVal = target
                self.digitOnes[2] = (NUM_SCROLLING_UPWARDS if self.targetVal > self.currentVal else NUM_SCROLLING_DOWNWARDS)
                if speed is not None: # If speed is None, use current speed setting, otherwise override.
                        self.speed = speed
                        
        def approach_target(self):
                if self.speed == NUM_SCROLL_FAST or self.timer % 2 == 0: # Speed settings; skip a frame if setting is slow
                        # The code is duplicated because there are small differences in the structure of the code for increasing and decreasing, so the same code cannot be used for both.
                        # Scrolling upwards:
                        if self.digitOnes[2] == NUM_SCROLLING_UPWARDS:
                                # Check whether or not to begin scrolling up the tens and hundreds.
                                if self.digitOnes[0] == 9 and self.digitOnes[1] == 0:
                                        self.digitTens[2] = NUM_SCROLLING_UPWARDS
                                        if self.digitTens[0] == 9:
                                                self.digitHundreds[2] = NUM_SCROLLING_UPWARDS                                        
                                self.digitOnes[1] += 1
                                # Check whether to increase the number.
                                if self.digitOnes[1] > 7:
                                        self.currentVal += 1
                                        # See if the target has been reached.
                                        if self.currentVal == self.targetVal:
                                                self.digitOnes[2] = NUM_NOT_SCROLLING
                                                # Reset speed
                                                self.speed = NUM_SCROLL_FAST
                                        self.digitOnes[1] = 0
                                        self.digitOnes[0] += 1
                                        # Looping around
                                        if self.digitOnes[0] > 9:
                                                self.digitOnes[0] = 0
                                                
                        # Tens and hundreds differ from ones in that they can only count up one at a time and then stop.
                        if self.digitTens[2] == NUM_SCROLLING_UPWARDS:
                                self.digitTens[1] += 1
                                if self.digitTens[1] > 7:
                                        self.digitTens = [self.digitTens[0] + 1, 0, NUM_NOT_SCROLLING]
                                        # Tens loop around, hundreds don't.
                                        if self.digitTens[0] > 9:
                                                self.digitTens[0] = 0  
                                                
                        if self.digitHundreds[2] == NUM_SCROLLING_UPWARDS:
                                self.digitHundreds[1] += 1
                                if self.digitHundreds[1] > 7:
                                        self.digitHundreds = [self.digitHundreds[0] + 1, 0, NUM_NOT_SCROLLING]
                               
                                        
                        # Scrolling downwards:
                        if self.digitOnes[2] == NUM_SCROLLING_DOWNWARDS:
                                # Check whether or not to begin scrolling down the tens and hundreds.
                                if self.digitOnes[0] == 0 and self.digitOnes[1] == 0:
                                        self.digitTens[2] = NUM_SCROLLING_DOWNWARDS
                                        if self.digitTens[0] == 0:
                                                self.digitHundreds[2] = NUM_SCROLLING_DOWNWARDS                                        
                                self.digitOnes[1] -= 1
                                # See if the target has been reached.
                                if self.currentVal == self.targetVal and self.digitOnes[1] == 0:
                                        self.digitOnes[2] = NUM_NOT_SCROLLING
                                        # Reset speed
                                        self.speed = NUM_SCROLL_FAST                                        
                                # Check whether to decrease the number.
                                elif self.digitOnes[1] < 0:
                                        self.currentVal -= 1
                                        self.digitOnes[1] = 7
                                        self.digitOnes[0] -= 1
                                        # Looping around
                                        if self.digitOnes[0] < 0:
                                                self.digitOnes[0] = 9
                                                
                        if self.digitTens[2] == NUM_SCROLLING_DOWNWARDS:
                                self.digitTens[1] -= 1
                                # Check whether to decrease the number.
                                if self.digitTens[1] < 0:
                                        self.digitTens[1] = 7
                                        self.digitTens[0] -= 1
                                        # Looping around
                                        if self.digitTens[0] < 0:
                                                self.digitTens[0] = 9  
                                elif self.digitTens[1] == 0:
                                        self.digitTens[2] = NUM_NOT_SCROLLING
                                        
                        if self.digitHundreds[2] == NUM_SCROLLING_DOWNWARDS:
                                self.digitHundreds[1] -= 1
                                # Check whether to decrease the number.
                                if self.digitHundreds[1] < 0:
                                        self.digitHundreds[1] = 7
                                        self.digitHundreds[0] -= 1  
                                elif self.digitHundreds[1] == 0:
                                        self.digitHundreds[2] = NUM_NOT_SCROLLING
                

        def getimg(self, digitInfo):
                imageNum = digitInfo[0] * 8 + digitInfo[1]
                return scrollingNumberImages[imageNum]
        
        def display(self, gameScreen):
                if self.digitHundreds[0] != 0:
                        gameScreen.blit(self.getimg(self.digitHundreds), (self.x, self.y))
                        gameScreen.blit(self.getimg(self.digitTens), (self.x + 8, self.y))
                elif self.digitTens[0] != 0:
                        gameScreen.blit(self.getimg(self.digitTens), (self.x + 8, self.y))
                gameScreen.blit(self.getimg(self.digitOnes), (self.x + 16, self.y))
                
        def update(self, gameScreen):
                self.timer += 1
                self.approach_target()
                self.display(gameScreen)