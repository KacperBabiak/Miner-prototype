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



all_sprites = pygame.sprite.Group()
all_sprites.add(map.getSprites())




while True:
   
    #displaying all
    displaysurface.fill((0,0,0))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    
    pygame.display.update()