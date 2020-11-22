# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:52:32 2020
Bouncing ball
@author: vmpsk
"""

import pygame
import random
import math  

pygame.init()

screen = pygame.display.set_mode((600,600))
#Title and icon
pygame.display.set_caption("Hello world")
icon = pygame.image.load('RedCircle.png')
pygame.display.set_icon(icon)

cirlceImage = pygame.image.load('RedCircle.png')
circleX = 100
circleY = 15
circleXChange = 0
circleYChange = 0

def circle(x,y):
    screen.blit(cirlceImage, (x,y))

running = True
drop = False
bounce = False
action = False
# Game loop
while running:
    screen.fill((255,255,255))
    
    # QUIT pygame application and windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #pygame.display.quit(); #exit()  ## not necessary as it restarts the console
            running = False
        
        if not(action):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    action = True
                    drop = True

    
    if drop:
        circleY += circleYChange
        circleYChange = math.sqrt((circleYChange)**2 + 2*1e-7*circleY)
        
    if bounce:
        circleY -= 0.8*circleYChange
        if (circleYChange)**2 <= 2*1e-7*circleY:
            circleYChange = math.sqrt((circleYChange)**2 - 2*1e-7*circleY)
    
        
#    if circleY <=0:
#        circleY = 0
#        drop = True
#        bounce = False
##        circleYChange = 0.3
        
    if circleYChange <=0:
        #circleY = 0
        drop = True
        bounce = False
#        circleYChange = 0.3
        
    if circleY >= 570:
        circleY = 570
        drop = False
        bounce = True
#        circleYChange = -0.3 

    circle(circleX, circleY)
    pygame.display.update()
