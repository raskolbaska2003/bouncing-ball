import pygame as pg
from pygame.locals import MOUSEBUTTONUP, MOUSEBUTTONDOWN, QUIT
import sys

#init
pg.init()

x=4
mouse_position=[0,0]
mouse_position_2=[0,0]
width,height = screen = 1600,900
clock=pg.time.Clock()
speed=[0,0] 
disp=pg.display.set_mode(screen) # create display
k_bounce=0.85 # coefficient of restitution

image=pg.image.load('ball.png') # load image
ball=image.get_rect() # get rect of image
while True:

    disp.fill((0,0,0)) # black background
    
    for event in pg.event.get(): # get events

        if event.type == MOUSEBUTTONDOWN and event.button == 1: # left mouse button is pressed
            mouse_position=pg.mouse.get_pos() # get mouse position when button is pressed

        if event.type == MOUSEBUTTONUP and event.button == 1: # left mouse button is released
            mouse_position_2=pg.mouse.get_pos() # get mouse position when button is released
            speed = [int((mouse_position_2[0]-mouse_position[0])/x),int((mouse_position_2[1]-mouse_position[1])/x)]
            print(speed) # print speed to console 

        if event.type == QUIT:
            sys.exit() # exit program

    

    if ball.left + speed[0] < 0:
        ball.left= speed[0] -ball.left # bounce off left wall
        speed[0] = -speed[0]*k_bounce # reduce speed by coefficient of restitution on bounce
    elif ball.right + speed[0] > width:
        ball.right = width - (ball.right + speed[0] - width) # bounce off right wall
        speed[0] = -speed[0]*k_bounce # reduce speed by coefficient of restitution on bounce
    elif ball.top + speed[1] < 0:
        ball.top = speed[1] - ball.top # bounce off top wall
        speed[1] = -speed[1]*k_bounce # reduce speed by coefficient of restitution on bounce
    elif ball.bottom + speed[1] > height:
        ball.bottom = height - (ball.bottom + speed[1] - height) # bounce off bottom wall
        speed[1] = -speed[1]*k_bounce # reduce speed by coefficient of restitution on bounce

    

    #gravity
    if ball.bottom < height-2 or abs(speed[1]) > 0.5: # if ball is not on the ground or speed is very low
        speed[1] += 0.5    
    else:
        ball.bottom = height
        speed[1] = 0
    print(speed[1]) # print speed to console

    ball = ball.move(speed) # move ball by speed

    disp.blit(image, ball) # draw image on display

    pg.display.update() # update display
    clock.tick(240) # set fps 


        
