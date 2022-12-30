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
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        
        #flags for movement
        self.mright = False
        self.mleft = False
        
    # draw the objecr
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    #update the object's position
    def update_gun(self):
        # for right move keys
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 5
        # for left move keys    
        if self.mleft and self.rect.left > 0:
            self.center -= 5
            
        self.rect.centerx = self.center