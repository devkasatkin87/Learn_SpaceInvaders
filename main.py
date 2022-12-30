import pygame
import sys
from pygame.sprite import Group

from Gun import Gun
import controls

screen_size = (700, 800)

BLACK = (0,0,0)

FPS = 60

clock = pygame.time.Clock()

# run application
def run():
    pygame.init()
    
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Space Invaders")
    
    gun = Gun(screen)
    
    bullets = Group()
    
    inos = Group()
    controls.draw_army(screen, inos)
    
    while True:
        
        controls.events_listener(screen, gun,  bullets)
        gun.update_gun()
        controls.update(BLACK, screen, gun, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)
        
        clock.tick(FPS)
        
run()
    