import pygame
import sys

from Gun import Gun

screen_size = (800, 600)

BLACK = (0,0,0)

# run application
def run():
    pygame.init()
    
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Space Invaders")
    
    gun = Gun(screen)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(BLACK)
        
        gun.draw()
        
        pygame.display.flip() 
        
run()
    