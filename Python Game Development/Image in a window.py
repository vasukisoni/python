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

from pygame import *

pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Window")

black = (0,0,0)
blue= (0,0,200)
white = (255,255,255)

image=pygame.image.load("smiley.jpg").convert_alpha()

gameLoop=True
while gameLoop:
    for event in pygame.event.get():
         if (event.type==pygame.QUIT):
             gameLoop=False
         window.fill(white)
    window.blit(image, (200,200))
    pygame.display.flip()

pygame.quit()