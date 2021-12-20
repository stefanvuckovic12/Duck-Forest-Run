import random
import os
import pygame
pygame.init()



#creating a clock which regulates fps
clock= pygame.time.Clock()


#size of the game's window
width=800
height=400

collision_win=pygame.display.set_mode((width,height)).convert_alpha() #makes invisible background with drawn rectangles for collision
screen= pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")


#font
font=pygame.font.Font('game/font/Cave Story.ttf',40)


#back surfaces
woods= pygame.image.load('game/graphics/woods/woods.png')
ground= pygame.image.load('game/graphics/woods/ground.png')
ground_t= pygame.transform.scale(ground,(800,400))



#score surface
score_surface= font.render('Score:',False,'Pink').convert()
num='0'
score_num= font.render(num,False,'White').convert()

#projectile
projectile= pygame.image.load('game/sprites/projectiles/egg.png')


#enemy
enemy= [pygame.image.load('game/sprites/enemy/Idle/frame-1.png'),
        pygame.image.load('game/sprites/enemy/Idle/frame-2.png')]



hurt= pygame.image.load('game/sprites/main_char/hurt.png')
hop=   pygame.image.load('game/sprites/main_char/Jumping 001.png')
shoot=      pygame.image.load('game/sprites/main_char/Crouching 001.png')

#main_char and sprite
idle= pygame.image.load('game/sprites/main_char/R1.png')
list= [ pygame.image.load('game/sprites/main_char/R1.png'),
             pygame.image.load('game/sprites/main_char/R2.png'),
        pygame.image.load('game/sprites/main_char/blank.png'),
        shoot]






value=0


#enemy's position
enemy_x=1500
enemy_y=275


#main_char's postion
main_char_x=50
main_char_y=240

#projectile's pos
projectile_x= main_char_x+50
projectile_y= main_char_y+50
proj=False




#movement
vel_x=10
vel_y=15
jump=False
moving= False
att=False
stepIndex=0
stepIndex1=0
x=0





#keep the game running
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()


            #Showing images in game
    screen.blit(woods,(0,0))
    rel_x= x%ground.get_rect().width
    screen.blit(ground,(rel_x- ground.get_rect().width,325))
    if rel_x < width:
        screen.blit(ground, (rel_x,325))
    x-=5








    if att == True:
        stepIndex=3
        screen.blit(list[stepIndex],(main_char_x,main_char_y))
        screen.blit(shoot,(main_char_x,main_char_y))



    else: #regular walking if not shooting
        if stepIndex >= 2:
            stepIndex = 0
        if moving:
            screen.blit(list[stepIndex], (main_char_x, main_char_y))
            stepIndex += 1
        else:
            screen.blit(idle, (main_char_x, main_char_y))

    col=pygame.draw.rect(collision_win,(255,0,0),(main_char_x+20,main_char_y+45,45,40),1)
    cool=pygame.draw.rect(collision_win, (255,0,0),(enemy_x,enemy_y, 60,60),1)

    if pygame.Rect.colliderect(col,cool) is True:
        screen.blit(hurt,(main_char_x,main_char_y))



    if jump==True:
        stepIndex=0
        screen.blit(hop,(main_char_x,main_char_y))

    if moving:
        screen.blit(enemy[stepIndex1],(enemy_x,enemy_y))
        stepIndex1+=1
        if stepIndex1>1:
            stepIndex1=0




    if proj is True:
        cod = pygame.draw.rect(collision_win, (255, 0, 0), (projectile_x + 20, projectile_y + 45, 45, 40), 1)
        projectile_x += 5
        screen.blit(projectile,(cod.centerx,col.centery))
        cod.centerx+=5






#movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and main_char_x>0:
        main_char_x -=vel_x
        if att==False:
            moving= True
    if keys[pygame.K_RIGHT] and main_char_x<500:
        main_char_x +=vel_x
        if att==False:
            moving= True
    if jump is False and keys[pygame.K_UP]:
        jump=True
    if jump is True:
        main_char_y -=vel_y
        vel_y-=1
        if vel_y<-15:
            jump=False
            vel_y=15

    if att is False and keys[pygame.K_SPACE]:
        att=True
       #################
    if not keys[pygame.K_SPACE]:
        att=False

    if keys[pygame.K_SPACE]:
        proj=True
        if projectile_x>800:
            projectile_x= col.centerx



    #speed
    pygame.time.delay(15)
    enemy_x-=5

    if enemy_x<-100:
        enemy_x=800





#update the screen

    pygame.display.update()
    clock.tick(60)

