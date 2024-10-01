import pygame
import util


class Paddle:
    def __init__(self, posX, color):
        self.posX = posX
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 1.5)
        self.pos = pygame.Vector2(posX, util.height / 2)
        self.width = 10
        self.height = 100
        self.color = color
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)

    def resetPaddle(self):
        self.pos = pygame.Vector2(self.posX, util.height / 2)

    def drawPaddle(self):
        pygame.draw.rect(util.screen, self.color, self.rect)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)


    def movePaddle(self, up, down):

        if down:
            self.vel.y += self.acc.y
        if up:
            self.vel.y -= self.acc.y
        self.vel.y *= .9
        self.pos.y += self.vel.y

        self.drawPaddle()


