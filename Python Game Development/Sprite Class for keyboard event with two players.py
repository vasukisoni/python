#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kanha
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

moveX,moveY=0,0

clock = pygame.time.Clock()

class Sprite:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=50
        self.height=50
    def render(self):
        pygame.draw.rect(window,white,(self.x,self.y,self.width,self.height))


player=Sprite(100,150)
player2=Sprite(200,300)
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
    player.x+=moveX
    player.y+=moveY
    player.render()
    player2.render()
    clock.tick(50)
    pygame.display.flip()

pygame.quit()