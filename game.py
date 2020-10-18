import math
import pygame
from pygame.locals import *
from classes import Ball, Goal, Wall

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game name here') # maybe we should come up with a name
framerate = 60 # I set this framerate to use later
screenWidth, screenHeight = screen.get_size()

# Setting up game objects
b = Ball(screen, screenWidth/2, 500) #Roy: I changed the location of the ball to the middle of the bottom of the screen
g = Goal(screen, 400, 100) #Roy: And I added the goal on the top of the screen, also in the middle
# distance = math.hypot(b.pos.x-g.pos.x,b.pos.y-g.pos.y) #Roy: This line calculates the distance between the ball and the goal. Thijs: I commented this line out, cause I don't beleive the variable is used here
walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
         Wall(screen, 0, 0, "vertical", screenHeight),
         Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
         Wall(screen, 0, screenHeight-10, "horizontal", screenWidth),
         Wall(screen, 200, 200, "horizontal", 200),
         Wall(screen, 500, 200, "vertical", 300)]

# This is the game loop, as long as it's running the game is running
loop = True
while loop:
    # This for loop checks the pygame events: things like user inputs get turned into those events
    for event in pygame.event.get():
        # This event handles close the window
        if event.type == QUIT:
            loop = False
        # This event handles when the user quits
        if event.type == MOUSEBUTTONDOWN:
            mousePos = pygame.math.Vector2(event.pos)
            acc = (mousePos - b.pos).normalize()
            acc *= 3
            b.accelerate(acc)

    screen.fill((0, 127, 50)) # set a background on top of everything that was drawn last frame

    # Update the physics
    b.bounce(walls)
    b.move()
    g.hit(b)

    # Draw all the objects
    g.draw()
    for wall in walls:
        wall.draw()
    b.draw()

    # Update the screen and wait for the next frame (without the delay the game runs way too fast)
    pygame.display.update()
    pygame.time.delay(int(1000/framerate)) # The delay function takes a time in milliseconds, the framerate is in frames per second so the delay time t = 1000/ framerate

# If we leave the game loop; quit
pygame.quit()
