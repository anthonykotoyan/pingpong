# Example file showing a basic pygame "game loop"
import pygame
import util
from Game import Game
import time

# pygame setup
pygame.init()
screen = util.screen
clock = pygame.time.Clock()
running = True

pygame.font.init()
score_font = pygame.font.SysFont('Comic Sans MS', 30)
endRound_font = pygame.font.SysFont('Futura Bold', 50)


game = Game()
ScoreColor = "white"
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    keys = pygame.key.get_pressed()
    player0Keys = [keys[pygame.K_w], keys[pygame.K_s]]
    player1Keys = [keys[pygame.K_UP], keys[pygame.K_DOWN]]
    ScoreText = game.updateGame(player0Keys, player1Keys)

    score_text = score_font.render(f'{game.score[1]} | {game.score[0]}', True, (255, 255, 255))
    screen.blit(score_text, (util.width/2-30, 50))
    if "1" in ScoreText:
        ScoreColor = "green"
    elif "2" in ScoreText:
        ScoreColor = "blue"
    endRound_text = endRound_font.render(f'{ScoreText}', True, ScoreColor)
    screen.blit(endRound_text, (util.width / 2 - 115, 100))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    if ScoreText != '':
        time.sleep(1)

pygame.quit()