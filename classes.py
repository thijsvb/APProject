import pygame
from pygame.locals import *

friction = 0.01

class Ball:
    def __init__(self, surface, x, y, r = 10, color = (255, 255, 255)):
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.r = r
        self.color = color
        self.screen = surface

    def move(self):
        if self.vel.magnitude() < 0.1:
            self.vel.xy = (0, 0)
        else:
            fricVec = self.vel.normalize() * -friction
            self.vel += fricVec
            self.pos += self.vel

    def draw(self):
        x = int(self.pos.x)
        y = int(self.pos.y)
        pygame.draw.circle(self.screen, self.color, (x,y), self.r)

    def accelerate(self, a):
        self.vel += a
