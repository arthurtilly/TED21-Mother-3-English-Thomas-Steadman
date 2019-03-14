import pygame

class TextArea():
    def __init__(self, text, x, y, updating=False, centered=False):
        self.text = text
        self.length = self.calculate_length(text)
        self.pos = x - ((self.length / 2 if centered else 0), y)
        self.surface = pygame.Surface((self.length, 8))
        if updating:
            pass
        else:
            pass
    
    def calculate_length(self, text):
        pass
    
    def update_display(self):
        pass
