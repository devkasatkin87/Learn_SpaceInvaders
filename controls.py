import pygame, sys
from Gun import Gun
from Bullet import Bullet

#events listener
def events_listener(screen, gun : Gun, bullets):
    for event in pygame.event.get():
        
        #for exit event
        if event.type == pygame.QUIT:
            sys.exit()
            
        # for keyboards events    
        elif event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_d:
                gun.mright = True
            #left    
            elif event.key == pygame.K_a:
                gun.mleft = True
            #space
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                
        elif event.type == pygame.KEYUP:
            #right
            if event.key == pygame.K_d:
                gun.mright = False
            #left    
            if event.key == pygame.K_a:
                gun.mleft = False

#update game's process
def update(bg_color, screen, gun, bullets):
        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw()
        gun.draw()
        pygame.display.flip() 
        
#update bullet's process
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))