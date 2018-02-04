#-------------------------------------------------------------------------------
# Name:        Keyboard_control.py
# Purpose:     This program demonstrates the control of the events using
#              Keyboard
# Author:      Vasuki soni
#
# Created:     27/01/2014
# Copyright:   (c) kanha 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Window")

black = (0,0,0)
white=(255,255,255)

x,y=0,0

moveX,moveY=0,0

clock = pygame.time.Clock()

gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
    if (event.type==pygame.KEYDOWN):
        if (event.key==pygame.K_LEFT):
            moveX = -5
        if (event.key==pygame.K_RIGHT):
            moveX = 5
        if (event.key==pygame.K_UP):
            moveY = -5
        if (event.key==pygame.K_DOWN):
            moveY = 5
    if (event.type==pygame.KEYUP):
        if (event.key==pygame.K_LEFT):
            moveX=0
        if (event.key==pygame.K_RIGHT):
            moveX=0
        if (event.key==pygame.K_UP):
            moveY=0
        if (event.key==pygame.K_DOWN):
            moveY=0
    window.fill(black)
    x+=moveX
    y+=moveY
    pygame.draw.rect(window,white,(x,y,50,50))
    clock.tick(50)
    pygame.display.flip()

pygame.quit()