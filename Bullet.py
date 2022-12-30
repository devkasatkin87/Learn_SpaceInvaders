import pygame

class Bullet(pygame.sprite.Sprite):
    
    #initialize bullet position
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = (34,177,77)
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
        
    
    #update bullet position
    def update(self):
        self.y += -self.speed
        self.rect.y = self.y
    
    #draw bullet on the screen
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)        
        