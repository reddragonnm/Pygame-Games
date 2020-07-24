import pygame as pg
import time, math
from pygame.locals import *

pg.init()

# frames per second setting
FPS = 20
fpsClock = pg.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up the window
screen_dim = (600, 600)
screen = pg.display.set_mode(screen_dim)
pg.display.set_caption('Pong')

# general game variables
running = True
winning_score = 5
player_score = 0
computer_score = 0

# general paddle variables
width_paddle = 25
height_paddle = 150

# ball's variables
ballX = 400
ballY = 400
moveX = 10
moveY = 10

# player's paddle variables
player_paddle_y = 350
move_paddle = 10

# fonts
font = pg.font.Font('freesansbold.ttf', 32)
font2 = pg.font.Font('freesansbold.ttf', 64)

# computer variables
computer_paddle_y = 350
computer_speed_y = 10


def countdown():
    for i in range(5, 0, -1):
        screen.fill(RED)
        count = font.render(str(i), True, GREEN)
        count_rect = count.get_rect()
        count_rect.center = (int(screen_dim[0] / 2), int(screen_dim[1] / 2))
        screen.blit(count, count_rect)
        pg.display.update()
        time.sleep(1)


countdown()
while running:
    # player score text
    player_score_text = font.render(str(player_score), True, GREEN)
    player_score_rect = player_score_text.get_rect()
    player_score_rect.center = (int(screen_dim[0] / 4), int(screen_dim[1] / 4))

    # computer score text
    computer_score_text = font.render(str(computer_score), True, GREEN)
    computer_score_rect = computer_score_text.get_rect()
    computer_score_rect.center = (int(screen_dim[0] / 4) * 3, int(screen_dim[1] / 4))

    # computer's paddle variable
    computer_center = computer_paddle_y + int(height_paddle / 2)
    if ballY > computer_paddle_y:
        computer_paddle_y += computer_speed_y
    elif ballY < computer_paddle_y + height_paddle:
        computer_paddle_y -= computer_speed_y

    # filling background
    screen.fill(RED)

    # drawing the net
    pg.draw.line(screen, YELLOW, (int(screen_dim[0] / 2), 0), (int(screen_dim[0] / 2), screen_dim[1]), 4)
    pg.draw.circle(screen, YELLOW, (int(screen_dim[0] / 2), int(screen_dim[1] / 2)), 100, 5)

    # control and restricting the computer paddle
    if computer_paddle_y > screen_dim[1] - height_paddle:
        computer_paddle = pg.draw.rect(screen, GREEN, (
        screen_dim[0] - width_paddle, screen_dim[1] - height_paddle, width_paddle, height_paddle))
    elif computer_paddle_y < 0:
        computer_paddle = pg.draw.rect(screen, GREEN, (screen_dim[0] - width_paddle, 0, width_paddle, height_paddle))
    else:
        computer_paddle = pg.draw.rect(screen, GREEN,
                                       (screen_dim[0] - width_paddle, computer_paddle_y, width_paddle, height_paddle))

    # moving and restricting the player's paddle
    player_paddle = pg.draw.rect(screen, GREEN, (0, player_paddle_y, width_paddle, height_paddle))
    if player_paddle_y == 0:
        player_paddle_y += 0
    elif player_paddle_y == screen_dim[1] - height_paddle:
        player_paddle_y += 0
    else:
        player_paddle_y += move_paddle

    # preventing ball to go out of bounds
    if ballX == screen_dim[0]:
        player_score += 1
        ballX = 400
        ballY = 400
        moveX *= -1
    elif ballX == 0:
        computer_score += 1
        ballX = 400
        ballY = 400
        moveX *= -1
    if ballY > screen_dim[1] or ballY < 0:
        moveY += -1
        if abs(moveY) > 5:
            moveY *= -1

    # moving the ball
    ball = pg.draw.circle(screen, BLUE, (ballX, ballY), 15, 0)
    ballX += int(math.ceil(moveX))
    ballY += int(math.ceil(moveY))

    # ball's collision detection
    if ball.colliderect(player_paddle):
        moveX = 10
        deltaY = ballY - (player_paddle_y + height_paddle / 2)
        moveY = deltaY * 0.35
    if ball.colliderect(computer_paddle):
        moveX = -10
        deltaY = ballY - (computer_paddle_y + height_paddle / 2)
        moveY = deltaY * 0.35

    screen.blit(player_score_text, player_score_rect)
    screen.blit(computer_score_text, computer_score_rect)

    # check win
    if computer_score == winning_score or player_score == winning_score:
        break

        # getting events
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if player_paddle_y != 0:
                    move_paddle = -10
                    player_paddle_y += move_paddle
            elif event.key == K_DOWN:
                if player_paddle_y != screen_dim[1] - height_paddle:
                    move_paddle = 10
                    player_paddle_y += move_paddle

    # updating the screen
    pg.display.update()

    # defining the frames per second
    fpsClock.tick(FPS)

if computer_score == winning_score:
    screen.fill(YELLOW)
    win_text = font.render("The Computer wins :(", True, GREEN)
    win_text_rect = player_score_text.get_rect()
    win_text_rect.center = (int(screen_dim[0] / 2), int(screen_dim[1] / 2))
    screen.blit(win_text, win_text_rect)
    pg.display.update()
    time.sleep(3)
elif player_score == winning_score:
    screen.fill(YELLOW)
    win_text = font.render("You win! :)", True, GREEN)
    win_text_rect = player_score_text.get_rect()
    win_text_rect.center = (int(screen_dim[0] / 3), int(screen_dim[1] / 2))
    screen.blit(win_text, win_text_rect)
    pg.display.update()
    time.sleep(3)

pg.quit()
