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

pygame.display.set_caption("Animation")

white = (255,255,255)

clock = pygame.time.Clock()

# Mario sprites
m1 = pygame.image.load("smiley.jpg")
m2 = pygame.image.load("smiley1.jpg")

marioCurrentImage = 1

gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
            window.fill(white)
    if (marioCurrentImage==1):
        window.blit(m1, (10,10))
    if (marioCurrentImage==2):
        window.blit(m2, (10,10))
    if (marioCurrentImage==2):
        marioCurrentImage=1
    else:
        marioCurrentImage+=1;
    pygame.display.flip()
    clock.tick(10)

pygame.quit()