import pygame
import random
snowList = []
Black = (0,0,0)
White = (255,255,255)
pygame.init()
size = (300,300)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")

for i in range(50):
    x = random.randrange(0,300)
    y = random.randrange(0,300)
    snowList.append([x,y])

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(Black)
    for i in range(50):
        a = random.randrange(0,255)
        b = random.randrange(0,255)
        c = random.randrange(0,255)
        d = (a,b,c)
        pygame.draw.circle(screen,d,snowList[i],2)
        snowList[i][1]+=1
        if snowList[i][1] > 300:
            snowList[i][1]=-30
            snowList[i][0] = random.randrange(0,300)

    
    pygame.display.flip()
    clock.tick(100)
    
pygame.quit()