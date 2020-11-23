import pygame
pygame.init()
window = [800,600]
screen = pygame.display.set_mode(window)
white = (255,255,255)
black = (0,0,0)
pygame.display.set_caption("𝖇𝖗𝖚𝖍")
clock = pygame.time.Clock()
done = False
edge = True
player = pygame.image.load("player.png")
oo = pygame.image.load("space.png")
ooo = pygame.image.load("bullet.png")
ooo = pygame.transform.scale(ooo, (10,10))
ooo.set_colorkey
while not done:
    screen.fill(white)
    for event in pygame.event.get():
        x,y = pygame.mouse.get_pos()
        if edge == True:
            i,j = x,y
            i+=45
        
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            edge = False
                    
    
    screen.blit(oo,(0,0))
    if j <= 0 :
        edge = True
    if edge == False:
        j-=5
        screen.blit(ooo,(i,j))
    if edge == True:
        
        screen.blit(ooo,(x+45,y))
    
    screen.blit(player,(x,y))
    pygame.display.flip()        
    clock.tick(100)
pygame.quit()