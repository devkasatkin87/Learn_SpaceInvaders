import pygame
import sys

from Gun import Gun
from controls import *

screen_size = (800, 600)

BLACK = (0,0,0)

# run application
def run():
    pygame.init()
    
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Space Invaders")
    
    gun = Gun(screen)
    
    while True:
        
        events_listener(gun)
        
        screen.fill(BLACK)
        
        gun.update_gun()
        
        gun.draw()
        
        pygame.display.flip() 
        
run()
    