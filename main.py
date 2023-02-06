import pygame
import sys
from pygame.locals import *
import map_file
import player_file
 

#initialization of variables
pygame.init()
vec = pygame.math.Vector2  
HEIGHT = 460
WIDTH = 460
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()
 
#display
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#creating a map
map = map_file.map(int(HEIGHT),WIDTH)
map.create_realistic()

#creating a group of all blocks 
blocks = pygame.sprite.Group()
blocks.add(map.getSprites())

#creating a player
P1 = player_file.Player(vec,ACC,FRIC,WIDTH,HEIGHT,blocks)

all_sprites = pygame.sprite.Group()
all_sprites.add(map.getSprites())
all_sprites.add(P1)

clicked =False

while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
        elif event.type == pygame.KEYUP:  
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()
        if event.type == pygame.MOUSEBUTTONUP:#deleting blocks
            clicked = True
        else: clicked = False
     
    #displaying all
    displaysurface.fill((0,0,0))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    for block in blocks:
        #highlighting blocks
        pos = pygame.mouse.get_pos()
        block.mouse_hover(pos,clicked)

        #moving "camera"
        if not P1.rect.top < HEIGHT / 3 and P1.vel.y > 0:#down
            block.rect.y -= abs(P1.vel.y) 
        elif P1.rect.top <= HEIGHT / 3 and P1.vel.y < 0: #up
            block.rect.y += abs(P1.vel.y)


    P1.move()
    P1.update()
 
    pygame.display.update()
    FramePerSec.tick(FPS)



