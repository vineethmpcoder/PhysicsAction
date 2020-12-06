# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:32:01 2020

@author: vmpsk
"""

import pygame 
import numpy as np
import random
#import math  
#import sys
#import collections

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255), (0, 0, screen.get_width()// 1, screen.get_height()//1))
#Title and icon
pygame.display.set_caption("Hello world")
icon = pygame.image.load('RedCircle.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 20)

dt = 8

class Body():
    def __init__(self, r, v, a, circleImgFile):
        self.r = r # [x, y]
        self.v = v # [Vx, Vy]
        self.a = a# [Ax, Ay]
        self.shiftRegister = np.array([0.0, 0.0])
        self.circleImgFile = circleImgFile
        self.circle = pygame.image.load(self.circleImgFile + '.png')
        self.blank = pygame.image.load('blank.png')

    def draw(self):
        screen.blit(self.blank, (self.shiftRegister[0],self.shiftRegister[1]))
        screen.blit(self.circle, (self.r[0],self.r[1]))

    def move(self, body):
        self.shiftRegister[0] = self.r[0]
        self.shiftRegister[1] = self.r[1]
        self.v[1] = self.v[1] + self.a[1]*dt
        self.r[1] = self.r[1] + self.v[1]*dt
        self.v[0] = self.v[0] + self.a[0]*dt
        self.r[0] = self.r[0] + self.v[0]*dt
        
        # Define Elastic collision of body with walls of the space
        if self.r[0] >= 520:
            self.v[0] = -1*self.v[0]

        if self.r[1] >= 520:
            self.v[1] = -1*self.v[1]

        if self.r[0] <= 20:
            self.v[0] = -1*self.v[0]

        if self.r[1] <= 20:
            self.v[1] = -1*self.v[1]

        if(self.isCollision(body)): # Define Elastic collision between bodies
            print("Collision!")
            self.v, body.v = body.v, self.v


    def showData(self, posX, posY):
        screen.fill((255,255,255), (0, 0, screen.get_width()// 1, screen.get_height()//15))
        self.height = font.render("h = " + str(round(self.r[1],2)) + "; v =" + str(round(self.v[1],2)), True, (0,0,0))
        screen.blit(self.height,(posX,posY))

    def isCollision(self, body):
        return np.linalg.norm(self.r - body.r)<= 30


running = True
action = False
circle0 = Body(np.array([200.0, 100.0]), np.array([0.1, 0.1]), np.array([0.0, 0.0]), 'RedCircle')
circle1 = Body(np.array([400.0, 200.0]), np.array([0.1, 0.2]), np.array([0.0, 0.0]), 'GreyCircle')
circle2 = Body(np.array([300.0, 200.0]), np.array([0.1, 0.3]), np.array([0.0, 0.0]), 'GreyCircle')
circle0.draw()
circle1.draw()
circle2.draw()


# Game loop
while running:
    screen.fill((255,255,255)) # Fills the back ground of the screen with color
    # QUIT pygame application and windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            pygame.quit()
            exit()  ## not necessary as it restarts the console

    circle0.move(circle1)
    circle0.move(circle2)
    circle1.move(circle0)
    circle1.move(circle2)
    circle2.move(circle0)
    circle2.move(circle1)
    circle3.move(circle0)
    circle3.move(circle1)
    
    
    circle0.draw()
    circle1.draw()
    circle2.draw()

    pygame.time.delay(dt)
    pygame.display.update()



#        if not(action):
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_DOWN:
#                    action = True
#                    drop = True
