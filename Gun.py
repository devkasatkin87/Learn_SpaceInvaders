import pygame

class Gun:
    
    #initialize gun object
    def __init__(self, screen):
        
        self.screen = screen
        self.image = pygame.image.load('images/gun_main.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # determine the center and bottom for the object
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    # draw the objecr
    def draw(self):
        self.screen.blit(self.image, self.rect)