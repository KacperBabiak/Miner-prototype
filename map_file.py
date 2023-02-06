import pygame
from pygame.locals import *
import sys
import random
from perlin_noise import PerlinNoise

class block(pygame.sprite.Sprite):
    r=0
    g=31
    b=0

    def __init__(self,x,y):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.r=random.randint(50,150)
        
        self.surf.fill((self.r,self.g,self.b))
        self.rect = self.surf.get_rect(center = (x, y))

    def mouse_hover(self,pos,clicked):
        if self.rect.collidepoint(pos[0], pos[1]):
            self.surf.fill((255,255,255))
            if clicked:
                self.kill()
        else:
            self.surf.fill((self.r,self.g,self.b))

        

 
class map:
    HEIGHT=0
    WIDTH=0
    sprites = pygame.sprite.Group()

    def __init__(self,h,w):
        self.HEIGHT=h
        self.WIDTH=w

    def create(self):
        for i in range (int(self.HEIGHT/2),self.HEIGHT*2,20):
            for j in range(10,self.WIDTH,20):
                bl = block(j,i)
                self.sprites.add(bl)

    def create_realistic(self):
        noise = PerlinNoise(octaves=1, seed=random.randint(1,1000))

        for i in range(0,self.HEIGHT,20):
            for j in range(0,self.WIDTH,20):
                print(noise([i/self.HEIGHT,j/self.WIDTH]))
                if(-0.15 <= noise([i/self.HEIGHT,j/self.WIDTH]) <= 0.15):
                   bl = block(j+10,i+self.HEIGHT/2)
                   self.sprites.add(bl) 
                

    def getSprites(self):
        return self.sprites

 


 
 
