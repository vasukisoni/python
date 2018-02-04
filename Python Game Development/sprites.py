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

        self.i0 = pygame.image.load("m1.png")

        self.i1 = pygame.image.load("m2.png")

        self.timeTarget=10

        self.timeNum=0

        self.currentImage=0

    def update(self):

        self.timeNum+=1

        if (self.timeNum==self.timeTarget):

            if (self.currentImage==0):

                self.currentImage=1

            else:

                self.currentImage=0

            self.timeNum=0

        self.render()

    def render(self):

        if (self.currentImage==0):

            window.blit(self.i0, (self.x,self.y))

        else:

            window.blit(self.i1, (self.x,self.y))


player=Sprite(100,150)
gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

        if (event.type==pygame.KEYDOWN):

            if (event.key==pygame.K_LEFT):

                moveX = -3

            if (event.key==pygame.K_RIGHT):

                moveX = 3

            if (event.key==pygame.K_UP):

                moveY = -3

            if (event.key==pygame.K_DOWN):

                moveY = 3

        if (event.type==pygame.KEYUP):

            if (event.key==pygame.K_LEFT):

                moveX=0

            if (event.key==pygame.K_RIGHT):

                moveX=0

            if (event.key==pygame.K_UP):

                moveY=0

            if (event.key==pygame.K_DOWN):

                moveY=0

    window.fill(white)

    player.x+=moveX

    player.y+=moveY

    player.update()

    clock.tick(50)

    pygame.display.flip()

pygame.quit()
