import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
purple = (255,0,255)
cyan = (0,255,255)
unknown = (43,103,247)
orange = (255,128,0)
q = (192,183,201)
w = (23,93,15)
e = random.randrange(0,255)
r = random.randrange(0,255)
t = random.randrange(0,255)
i = (e,r,t)
o = (r,t,e)
p = (t,e,r)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")
done = False
clock = pygame.time.Clock()
y = random.randrange(0,500)
x = random.randrange(-200,500)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)
    pygame.draw.circle(screen,white,(x,y),3)
    pygame.draw.circle(screen,red,(x,y),10,3)
    pygame.draw.circle(screen,blue,(x,y),17,3)
    pygame.draw.circle(screen,green,(x,y),24,3)
    pygame.draw.circle(screen,yellow,(x,y),31,3)
    pygame.draw.circle(screen,purple,(x,y),38,3)
    pygame.draw.circle(screen,cyan,(x,y),45,3)
    pygame.draw.circle(screen,unknown,(x,y),52,3)
    pygame.draw.circle(screen,orange,(x,y),59,3)
    pygame.draw.circle(screen,q,(x,y),66,3)
    pygame.draw.circle(screen,w,(x,y),73,3)
    pygame.draw.circle(screen,i,(x,y),80,3)
    pygame.draw.circle(screen,o,(x,y),87,3)
    pygame.draw.circle(screen,p,(x,y),94,3)
    y+=5
    x+=3
    if y>594:
        y=-144
        x = random.randrange(-200,500)
    pygame.display.flip()
    clock.tick(102)

pygame.quit()