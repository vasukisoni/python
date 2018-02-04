import pygame,sys
from pygame import *

pygame.init()  #initialise pygame


# Initialise the window for game
display =  pygame.display.set_mode((400,300)) 

# Setting the window title
pygame.display.set_caption('Hello Beta !!')

gameloop = True

# Main Game loop
while gameloop:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        
    
