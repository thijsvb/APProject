import pygame
from pygame.locals import *


class Ball:
    def __init__(self, surface, x, y, r = 10, color = (255, 255, 255)):
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.r = r
        self.color = color
        self.screen = surface
        self.friction = 0.01

    def move(self):
        if self.vel.magnitude() < 0.1:
            self.vel.xy = (0, 0)
        else:
            fricVec = self.vel.normalize() * - self.friction
            self.vel += fricVec
            self.pos += self.vel

    def draw(self):
        x = int(self.pos.x)
        y = int(self.pos.y)
        pygame.draw.circle(self.screen, self.color, (x,y), self.r)

    def accelerate(self, a):
        self.vel += a
        if self.vel.magnitude() > self.r:
            self.vel.scale_to_length(self.r)
        
    def bounce(self, walls):
        for wall in walls:
            x, y = self.pos.xy
            left, top, right, bottom = wall.rect.topleft + wall.rect.bottomright
            centerx, centery = wall.rect.center

            if wall.orientation == "vertical":
                # left wall
                if y > top and y < bottom and x < centerx and x + self.r >= left:
                    self.pos.x = left - self.r
                    self.vel.x *= -1

                # right wall
                elif y > top and y < bottom and x > centerx and x - self.r <= right:
                    self.pos.x = right + self.r
                    self.vel.x *= -1

            elif wall.orientation == "horizontal":
                # top wall
                if x > left and x < right and y < centery and y + self.r >= top:
                    self.pos.y = top - self.r
                    self.vel.y *= -1

                # bottom wall
                elif x > left and x < right and y > centery and y - self.r <= bottom:
                    self.pos.y = bottom + self.r
                    self.vel.y *= -1

class Wall:
    def __init__(self, surface, x, y, orientation, length, thick=10, color=(255, 100, 0)):
        if orientation == "vertical":
            width = thick
            height = length
        elif orientation == "horizontal":
            width = length
            height = thick
        self.rect = Rect(x, y, width, height)
        self.orientation = orientation
        self.color = color
        self.screen = surface

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
class Goal:
    def __init__(self, surface, x, y, r = 10, color = (0,0,0)):
        self.pos = pygame.math.Vector2(x,y)
        self.r = r
        self.color = color
        self.screen = surface
    
    def draw(self):
        x = int(self.pos.x)
        y = int(self.pos.y)
        pygame.draw.circle(self.screen, self.color, (x,y), self.r)
        
    def hit(self,ball):
        #has to return True if the ball is touching the target
        #Roy: But now, I tried to do it in an if-statement in the game code
        #Roy: However, this doesn't work very well
        return
        
