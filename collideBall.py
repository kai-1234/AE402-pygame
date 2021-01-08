import pygame
import random
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self,speed,srx,sry,r,color):
        super().__init__(self)
        self.x = srx
        self.y = sry
        self.image=pygame.Surface([2*r,2*r])
        self.image.fill(BLACK)
        pygame.draw.circle(self.image,color,(r,r),r)
        self.rect = self.image.get_rect()
        self.rect.center=(srx,sry)
        direction = random.randint(20,70)  #移動角度
        radian = math.radians(direction)  #角度轉為弳度
        self.dx = speed * math.cos(radian)  #球水平運動速度
        self.dy = speed * math.sin(radian)
    def update(self):
        self.x+=self.dx
        self.rect.x=self.x
        if self.rect.left<0 or self.rect.right>screen.get_width():
            self.dx*=-1
        self.y+=self.dy
        self.rect.y=self.y
        if self.rect.top<0 or self.rect.bottom>screen.get_height():
            self.dy*=-1
        
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

clock = pygame.time.Clock()
play = True

while play:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            play = False 

    screen.fill(WHITE)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
