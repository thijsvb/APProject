import math
import pygame
from pygame.locals import *
from classes import Ball, Goal, Wall

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Test')
framerate = 60
screenWidth, screenHeight = screen.get_size()
b = Ball(screen, screenWidth/2, 500) #Roy: I changed the location of the ball to the middle of the bottom of the screen
g = Goal(screen, 400, 100) #Roy: And I added the goal on the top of the screen, also in the middle
distance = math.hypot(b.pos.x-g.pos.x,b.pos.y-g.pos.y) #Roy: This line calculates the distance between the ball and the goal
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
            distance = math.hypot(b.pos.x-g.pos.x,b.pos.y-g.pos.y)#Roy: I added this line so it updates the distance everytime we move the ball
        if distance <= (b.r+g.r): #Roy: This is the if-statement that checks for collision, e.g. if the ball hits the target
            g.color =  (0,0,255) #Roy: for now, I just told the code to change the color of the goal, we have to see what we want the program to do once the goal is hit
            

    screen.fill((0, 127, 50))
    b.bounce(walls)
    b.move()
    b.draw()
    g.draw()
    for wall in walls:
        wall.draw()
    pygame.display.update()
    pygame.time.delay(int(1000/framerate))

pygame.quit()
