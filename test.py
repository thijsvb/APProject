import pygame
from pygame.locals import *

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Test')
screenWidth, screenHeight = screen.get_size()
pos = (int(screenWidth/2), int(screenHeight/2))


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos

    screen.fill((0, 127, 50))
    pygame.draw.circle(screen, (255,255,255), pos, 10)
    pygame.display.update()
