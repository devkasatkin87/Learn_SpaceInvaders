import pygame, sys
from Gun import Gun
from Bullet import Bullet
from Ino import Ino

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
def update(bg_color, screen, gun, inos, bullets):
        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw()
        gun.draw()
        inos.draw(screen)
        pygame.display.flip() 
        
#update bullet's process
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
 
#update invader's postion            
def update_inos(inos):
    inos.update()

# create army of invations
def draw_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)
    
    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)
    