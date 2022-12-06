import pygame
import sys
from pygame.sprite import Group

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
    
    bullets = Group()
    
    while True:
        
        events_listener(screen, gun,  bullets)
        gun.update_gun()
        update(BLACK, screen, gun, bullets)
        update_bullets(bullets)
        
run()
    