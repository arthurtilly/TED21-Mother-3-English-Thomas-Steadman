import pygame

# Dictionary of letter images
fontImages = {}

# Images haven't been added to repository yet (todo)

# Letters where filename corresponds to character
#for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
#    if char.lower() != char: # Capitals (filenames with different capitalisation don't count as different so there needs to be a way to distinguish them)
#        fontImages[char] = pygame.image.load("font/font_%s_cap" % char.lower())
#    else: # Lowercase and numbers
#        fontImages[char] = pygame.image.load("font/font_%s" % char)

class TextArea():
    def __init__(self, text, pos, animated=False, centered=False, length_threshold=None):
        # Find out how much, if any, of the text needs to be placed on a new line
        # This will set self.text, self.nextline and self.length
        self.init_newlines(text, pos, animated, centered, length_threshold)
        
        self.pos = pos[0] - ((self.length / 2 if centered else 0), pos[1]) # calculate position if centered
        self.surface = pygame.Surface((self.length, 8))
        self.animated = animated
        if animated:
            self.displayedText = ""
        else:
            self.displayedText = self.text
    
    # Create additional text fields if necessary
    def init_newlines(self, text, pos, animated, centered, length_threshold):
        self.text, self.length, newlineText = self.calculate_length(text, length_threshold)
        if newlineText is not None:
            self.nextline = TextArea(newlineText, (pos[0], pos[1] - 10), animated, centered, length_threshold)
        else:
            self.nextline = None
        
        
    # Return values: current text up to threshold, length of current text, remaining text
    def calculate_length(self, text, length_threshold):
        length = -1 # compensate for the space that will be added at the end of each character
        for char_index in len(text):
            try:
                charlength = fontImages[text[char_index]].get_width() + 1 # +1 is to separate characters out slightly
                if length + charlength > length_threshold: # If past the length threshold, return everything so far 
                    return text[:char_index], length, text[char_index:]
                length += charlength
                
            # Non-supported character
            except KeyError:
                raise ValueError("Invalid character for text display: '%s'" % char)
        return text, length, None # If reached the end without hitting threshold, return entire text
            
    def animate_text(self):
        pass
    
    def update_display(self):
        pass