# import pygame
# import random
# List = []
# collideList=[]
# white = (255,255,255)
# black = (0,0,0)
# red = (255,0,0)
# pygame.init()
# window_size = (800,600)
# screen = pygame.display.set_mode(window_size)
# pygame.display.set_caption("collide game")
# done = False
# clock = pygame.time.Clock()
# for i in range(10):
#     block_x = random.randrange(80,720)
#     block_y = random.randrange(60,540)
#     List.append([block_x,block_y])

# block_w = 80
# block_h = 60

# player_x = 0
# player_y = 0
# player_w = 30
# player_h = 30
# collide = False

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     player_x,player_y = pygame.mouse.get_pos()
#     for j in range(10):
#         x_collide = List[i][0]<player_x<List[i][0]+block_w or List[i][0]<player_x+player_w<List[i][0]+block_w        
#         y_collide = List[i][1]<player_y<List[i][1]+block_h or List[i][1]<player_y+player_h<List[i][1]+block_h 
#         for k in range(10):
#             if x_collide and y_collide:
        
            
#                 collideList = True         
        
    
#     player_x,player_y = pygame.mouse.get_pos()
#     screen.fill(white)
#     if not collideList:
#         for l in range(10):
        
#             x=List[i][0]
#             y=List[i][1]
#             pygame.draw.rect(screen, black, [x,y,block_w,block_h])
#     pygame.draw.rect(screen, red, [player_x,player_y,player_w,player_h])
#     pygame.display.flip()
#     clock.tick(100)
            
# pygame.quit()
