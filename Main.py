import math
import pygame
from pygame.locals import *
from classes import Ball, Goal, Wall, scoreSheet
import Levels


def main():
    #Main Program "

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game name here') # maybe we should come up with a name
    framerate = 60 # I set this framerate to use later
    screenWidth, screenHeight = screen.get_size()

    #Create levels
    level_list = []
    level_list.append(Levels.Level_01(screen))
    level_list.append(Levels.Level_02(screen))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    # Keep track of scores
    strokes = 1
    sheet = scoreSheet(screen)

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
                current_level.click(mousePos)
                strokes += 1

        screen.fill(current_level.background) # set a background on top of everything that was drawn last frame

        # Update the physics
        current_level.update()
        # b.bounce(walls)
        # b.move()
        # g.hit(b)

        # Draw all the objects
        current_level.draw()
        # g.draw()
        # for wall in walls:
        #     wall.draw()
        # b.draw()

<<<<<<< HEAD
        if current_level.finished:
             # sheet.drawSheet(strokes)
             current_level_no += 1
             current_level = level_list[current_level_no]

        # Update the screen and wait for the next frame (without the delay the game runs way too fast)
        pygame.display.update()
        pygame.time.delay(int(1000/framerate)) # The delay function takes a time in milliseconds, the framerate is in frames per second so the delay time t = 1000/ framerate

=======
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
        if g.hit(b):
            sheet.drawSheet(strokes)
            current_level_no += 1
            current_level = level_list[current_level_no]
            b.level = current_level
    
        current_level.draw(screen)
   
        # Update the screen and wait for the next frame (without the delay the game runs way too fast)
        pygame.display.update()
        pygame.time.delay(int(1000/framerate)) # The delay function takes a time in milliseconds, the framerate is in frames per second so the delay time t = 1000/ framerate
    
>>>>>>> 012dfdd870d32364692fa8b9d7f4dfe7716825e0
    # If we leave the game loop; quit
    pygame.quit()

if __name__ == "__main__":
    main()
