import pygame
from pygame.locals import *
from classes import Ball, Goal, Wall, scoreSheet

class Level:
    #Generic super-class used to define a level. For each level with level"
    #specific info we should create a separate child class"

    def __init__(self, screen):

        # Lists of sprites used in all levels.
        self.background = None   #In parent class none; we can change this per level
        self.screen = screen
        self.finished = False
#        self.goal = goal

        framerate = 60 # I set this framerate to use later

        self.b = None#Ball(screen, screenWidth/2, 500)
        self.g = None#Goal(screen, 400, 100)
        self.walls = []

    def update(self):
        self.b.bounce(self.walls)
        self.b.move()
        if self.g.hit(self.b):
            self.finished = True

    def click(self, mousePos):
        acc = (mousePos - self.b.pos).normalize()
        acc *= 3
        self.b.accelerate(acc)

    def draw(self):
        self.g.draw()
        for wall in self.walls:
            wall.draw()
        self.b.draw()



class Level_01(Level):
    #definition for level 1

    def __init__(self, screen):
        Level.__init__(self, screen) # Call the parent constructor
        screenWidth, screenHeight = screen.get_size()
        self.background = (0, 127, 50)
        self.b = Ball(screen, screenWidth/2, 500)
        self.g = Goal(screen, 400, 100)

        self.walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
                 Wall(screen, 0, 0, "vertical", screenHeight),
                 Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
                 Wall(screen, 0, screenHeight-10, "horizontal", screenWidth),
                 Wall(screen, 0, screenHeight/3, "horizontal", screenWidth*2/3),
                 Wall(screen, screenWidth/3, screenHeight*2/3, "horizontal", screenWidth*2/3)]



class Level_02(Level):
    #definition for level 2

    def __init__(self, screen):
        Level.__init__(self, screen) # Call the parent constructor
        screenWidth, screenHeight = screen.get_size()
        self.background = (68, 87, 90)
        self.b = Ball(screen, screenWidth/2, 500)
        self.g = Goal(screen, 400, 100)

        self.walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
                 Wall(screen, 0, 0, "vertical", screenHeight),
                 Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
                 Wall(screen, 0, screenHeight-10, "horizontal", screenWidth)]
                #Only has surrounding walls now
