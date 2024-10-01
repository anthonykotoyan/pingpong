from Paddle import Paddle
from Ball import Ball
import time
import util


class Game:
    paddleOffset = 50

    def __init__(self):
        self.score = [0, 0]

        self.paddle0 = Paddle(Game.paddleOffset, "green")

        self.paddle1 = Paddle(util.width - Game.paddleOffset, "blue")

        self.ball = Ball()

    def newRound(self):
        self.ball.resetBall()
        self.paddle0.resetPaddle()
        self.paddle1.resetPaddle()




    def updateGame(self, player0, player1, ):
        self.paddle0.movePaddle(player0[0], player0[1])
        self.paddle1.movePaddle(player1[0], player1[1])
        info = self.ball.updateBall(self.paddle0, self.paddle1)
        if info is not None:
            self.score[info] += 1
            self.newRound()
            return f'Player {(1-info)+1} Won!'
        return ''




