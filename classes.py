import pygame
from pygame.locals import *
import math


class Ball:
    def __init__(self, surface, x, y, r = 10, color = (255, 255, 255)):
        # Keep track of the position and velocity in vectors, this makes the physics easier later on
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.r = r
        self.color = color

        self.screen = surface # pygame wants to know where to draw things, so I added the screen as an argument

        self.friction = 0.01 # this is just a constant to make the ball slow down over time, I put it here so it's easy to tweak if needed

    def draw(self):
        # The position x and y are not whole numbers (and pygame wants exact pixel locations), so cast them as ints
        x = int(self.pos.x)
        y = int(self.pos.y)
        pygame.draw.circle(self.screen, self.color, (x,y), self.r)

    def move(self):
        # If the velocity of the ball is super low, just kill it, otherwise it keeps going veeery slowly for forever
        if self.vel.magnitude() < 0.1:
            self.vel.xy = (0, 0)
        # If the velocity is high enough, move the ball
        else:
            self.vel *= (1-self.friction) # First decrease the velocity a tiny bit to model friction
            self.pos += self.vel # Then add the velocity vector to the position.
            # A bit more on the physics of this: normally the change in position dx = v * dt, but since our timestep dt is always the same here (the time between two frames). We can just do all our physics leaving that factor out.
            # Because position and velocity are both vector, the addition works for both x and y

    def accelerate(self, a):
        # Similair to the move function, for acceleration you add the acceleration vector to the velocity vector
        self.vel += a
        # If the ball goes to fast, it'll end up flying through walls and things like that
        # So here I limit the velocity so the ball will not move more then it's own radius in one frame
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
        # Thijs: your code correct, it was just in the wrong spot with the event handling, so I moved it over here and added returns.
        distance = math.hypot(ball.pos.x-self.pos.x,ball.pos.y-self.pos.y)#Roy: I added this line so it updates the distance everytime we move the ball
        if distance <= (ball.r+self.r): #Roy: This is the if-statement that checks for collision, e.g. if the ball hits the target
            self.color =  (0,0,255) #Roy: for now, I just told the code to change the color of the goal, we have to see what we want the program to do once the goal is hit
            return True
        else:
            return False
