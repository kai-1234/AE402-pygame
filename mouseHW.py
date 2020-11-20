import pygame
import random
pygame.init()


windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)


count = 0
click = False 
limit = 30 
pos = (0, 0)

done = False
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
            a = random.randrange(0,255)
            b = random.randrange(0,255)
            c = random.randrange(0,255)
            d = a,b,c
            

        if event.type == pygame.QUIT:
            done = True
    if click:
        pygame.draw.circle(screen, d, pos, count)
        count += 1
        if count > 20:
            count = 0

    pygame.display.flip()
    clock.tick(60)
pygame.quit()