import pygame
from pygame.locals import *
from classes import Ball, Goal, Wall, scoreSheet

class Level:
    #Generic super-class used to define a level. For each level with level" 
    #specific info we should create a separate child class"
    
    def __init__(self, ball):
        
        # Lists of sprites used in all levels.
        self.background = None   #In parent class none; we can change this per level
        self.ball = ball
#        self.goal = goal
        
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Game name here') # maybe we should come up with a name
        framerate = 60 # I set this framerate to use later
        screenWidth, screenHeight = screen.get_size()
 
        b = Ball(screen, screenWidth/2, 500)
        g = Goal(screen, 400, 100)

#    def update(self):
#        self.wall_list.update() #Update everything in this level
#        
#    def draw(self, screen):
#        #Draw everything on this level
#        self.wall_list.draw(screen)



class Level_01(Level):
    #definition for level 1
    
    def __init__(self, ball):
        Level.__init__(self, ball) # Call the parent constructor
#        self.background = pygame.image.load("PUT BACKGROUND IMAGE HERE").convert()
#        self.background.set_colorkey(PUT COLOR HERE)
        
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Game name here') # maybe we should come up with a name
        framerate = 60 # I set this framerate to use later
        screenWidth, screenHeight = screen.get_size()
 
        b = Ball(screen, screenWidth/2, 500)
        g = Goal(screen, 400, 100)
        
        walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
                 Wall(screen, 0, 0, "vertical", screenHeight),
                 Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
                 Wall(screen, 0, screenHeight-10, "horizontal", screenWidth),
                 Wall(screen, 200, 200, "horizontal", 200),
                 Wall(screen, 500, 200, "vertical", 300)] 
       
        b.draw()
        g.draw()
        for wall in walls:
            wall.draw()
            b.draw()
            
            
            
class Level_02(Level):
    #definition for level 2
    
    def __init__(self, ball):
        Level.__init__(self, ball) # Call the parent constructor
#        self.background = pygame.image.load("PUT BACKGROUND IMAGE HERE").convert()
#        self.background.set_colorkey(PUT COLOR HERE)
        
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Game name here') # maybe we should come up with a name
        framerate = 60 # I set this framerate to use later
        screenWidth, screenHeight = screen.get_size()
 
        b = Ball(screen, screenWidth/2, 500)
        g = Goal(screen, 400, 100)
        
        walls = [Wall(screen, 0, 0, "horizontal", screenWidth),
                 Wall(screen, 0, 0, "vertical", screenHeight),
                 Wall(screen, screenWidth-10, 0, "vertical", screenHeight),
                 Wall(screen, 0, screenHeight-10, "horizontal", screenWidth)]
                #Only has surrounding walls now
        
        b.draw()
        g.draw()
        for wall in walls:
            wall.draw()
            b.draw()
