import pygame
from pygame.locals import *
from classes import Ball, Wall

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Test')
framerate = 60
screenWidth, screenHeight = screen.get_size()
b = Ball(screen, screenWidth/2, screenHeight/2)
walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
         Wall(screen, 0, 0, "vertical", screenHeight),
         Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
         Wall(screen, 0, screenHeight-10, "horizontal", screenWidth),
         Wall(screen, 200, 200, "horizontal", 200),
         Wall(screen, 500, 200, "vertical", 300)]


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
        if event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.math.Vector2(event.pos)
            acc = (mousePos - b.pos).normalize()
            acc *= 3
            b.accelerate(acc)

    screen.fill((0, 127, 50))
    b.bounce(walls)
    b.move()
    b.draw()
    for wall in walls:
        wall.draw()
    pygame.display.update()
    pygame.time.delay(int(1000/framerate))
