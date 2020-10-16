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
            fricVec = self.vel.normalize() * -self.friction
            self.vel += fricVec
            self.pos += self.vel

    def draw(self):
        x = int(self.pos.x)
        y = int(self.pos.y)
        pygame.draw.circle(self.screen, self.color, (x,y), self.r)

    def accelerate(self, a):
        self.vel += a

    def bounce(self, walls):
        # for wall in walls:
        #     # bounce
        return

class Wall:
    def __init__(self):
        # make a wall
        return

    def draw():
        # draw the wall
        return

class Target:
    def __init__(self):
        # make the target
        return

    def draw(self):
        #draw the target
        return

    def hit(self, ball):
        #return True if the ball is touching the target
        return
