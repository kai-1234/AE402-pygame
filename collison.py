import pygame
import random
import time
List = []
collideList=[]
fallList=[]
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pygame.init()
window_size = (800,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("collide game")
done = False
score = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None,50)
for i in range(20):
    block_x = random.randrange(80,720)
    block_y = random.randrange(60,540)
    List.append([block_x,block_y])
    collideList.append(False)
for z in range(20):
    x = List[i][0]
    y = List[i][1]
    fallList.append([x,y])
start_time = pygame.time.get_ticks()
block_w = 30
block_h = 30

player_x = 0
player_y = 0
player_w = 20
player_h = 20

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    player_x,player_y = pygame.mouse.get_pos()
    for l in range (20):
        fallList[i][0] = x
        fallList[i][1] = y
        pygame.draw.rect(screen,black,x,y,block_w,block_h)
    for i in range(20):
        x_collide = List[i][0]<player_x<List[i][0]+block_w or List[i][0]<player_x+player_w<List[i][0]+block_w        
        y_collide = List[i][1]<player_y<List[i][1]+block_h or List[i][1]<player_y+player_h<List[i][1]+block_h 
        if x_collide and y_collide and not collideList[i]:
            collideList[i] = True   
            score+=1
    now_time = pygame.time.get_ticks()-start_time
    now_time//=1000
    content = "score:"+str(score)
    text4 = font.render('Game over!', True, red)
    text3 = font.render(str(now_time), True, red)
    text2 = font.render('YOU WIN!!!',True,black)
    text = font.render(content,True,black)
    screen.fill(white)
    for z in range(20):
        fallList.append([x,y])
        fallList[z][1] -= 5
        if fallList[z][1] > 600:
            fallList[z][1]-=60
        screen.blit(text4,(400,300))
        pygame.display.flip()
        time.sleep(3)
        done = True
    if score >= 50:
        screen.blit(text2,(400,300))
        pygame.display.flip()
        time.sleep(3)
        done = True
    pygame.display.flip()
    clock.tick(100)
            
pygame.quit()
