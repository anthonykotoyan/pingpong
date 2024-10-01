import math

import pygame
import random
import util


class Ball:
    gravity = .25
    hitDamp = .7
    floorFriction = .01
    paddleFriction = .25
    spinDamp = 1

    def __init__(self):
        self.spin = 0
        self.vel = pygame.Vector2((random.choice([-5, 5])), 0)
        self.pos = pygame.Vector2(util.width / 2, util.height / 2)
        self.size = 10

    def drawBall(self):
        pygame.draw.circle(util.screen, "white", self.pos, self.size)

    def wallColl(self):
        if self.pos.x <= self.size:
            return 0
        elif self.pos.x >= util.width - self.size:
            return 1
        else:
            return None

    def bounceColl(self):
        kickback = 2
        if self.pos.y <= self.size:
            self.pos.y = self.size+kickback
            self.vel.y *= -1
            frictionForce = - self.vel.x * Ball.floorFriction
            self.vel.x += frictionForce
            self.spin += -frictionForce

            self.vel.x += self.spin

        elif self.pos.y >= util.height - self.size:
            self.pos.y = util.height - self.size - kickback
            self.vel.y *= -1
            frictionForce = - self.vel.x * Ball.floorFriction
            self.vel.x += frictionForce
            self.spin += -frictionForce

            self.vel.x += self.spin



    def paddleColl(self, paddle0, paddle1):
        kickback = 2
        if paddle0.pos.x - self.size <= self.pos.x <= paddle0.pos.x + self.size + paddle0.width:

            if paddle0.pos.y + self.size <= self.pos.y <= paddle0.pos.y + paddle0.height - self.size:
                self.pos.x = paddle0.pos.x + self.size + paddle0.width + kickback
                self.vel.x *= -1
                self.vel.y += paddle0.vel.y*Ball.hitDamp
                frictionForce = - (self.vel.y+paddle0.vel.y) * Ball.paddleFriction
                self.vel.y += frictionForce
                self.spin += -frictionForce
                self.vel.y += self.spin


        elif paddle1.pos.x + self.size + paddle1.width >= self.pos.x >= paddle1.pos.x - self.size:

            if paddle1.pos.y + self.size <= self.pos.y <= paddle1.pos.y + paddle1.height - self.size:
                self.pos.x = paddle1.pos.x - self.size - kickback
                self.vel.x *= -1
                self.vel.y += paddle1.vel.y*Ball.hitDamp
                frictionForce = - (self.vel.y + paddle1.vel.y) * Ball.paddleFriction
                self.vel.y += frictionForce
                self.spin += -frictionForce
                self.vel.y += self.spin


    def updateForces(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.vel.y += Ball.gravity
        self.spin *= Ball.spinDamp

    def resetBall(self):
        self.vel = pygame.Vector2((random.choice([-7, 7])), 0)
        self.pos = pygame.Vector2(util.width / 2, util.height / 2)
        self.spin = 0



    def updateBall(self, paddle0, paddle1):
        self.updateForces()
        self.bounceColl()
        self.drawBall()
        self.paddleColl(paddle0, paddle1)

        return self.wallColl()
