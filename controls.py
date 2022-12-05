import pygame, sys
from Gun import Gun

#events listener
def events_listener(gun : Gun):
    for event in pygame.event.get():
        
        #for exit event
        if event.type == pygame.QUIT:
            sys.exit()
            
        # for move's events    
        elif event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_d:
                gun.mright = True
            #left    
            elif event.key == pygame.K_a:
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            #right
            if event.key == pygame.K_d:
                gun.mright = False
            #left    
            if event.key == pygame.K_a:
                gun.mleft = False