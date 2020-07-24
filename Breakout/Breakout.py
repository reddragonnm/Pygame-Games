import pygame as pg
import time, math
from pygame.locals import *

pg.init()

# frames per second setting
FPS = 30
fpsClock = pg.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# screen variables
screen_dim = (600, 600)
screen = pg.display.set_mode(screen_dim)
pg.display.set_caption('Breakout')

# general variables
boxes = []
running = True
tries = 3

# paddle variables
paddle_height = 25
paddle_width = 150
dist = int(screen_dim[1] / 8) * 7
paddle_x = int(screen_dim[0] / 2 - paddle_width / 2)
paddle_move_x = 0
speed = 20

# ball variables
ball_speed = 10
ball_x = int(screen_dim[0] / 2)
ball_y = dist - 20
ball_move_y = -ball_speed
ball_move_x = ball_speed

# box drawing variables
box_height = 30
box_width = 70
horiz_space = 30
vert_space = 30
space_between = 5
ball_space = int((screen_dim[1] / 8) * 5)


class Box():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bx = None

    def draw(self):
        self.bx = pg.draw.rect(screen, GREEN, (self.x, self.y, box_width, box_height))


for j in range(vert_space, ball_space, box_height + space_between):
    for i in range(horiz_space, screen_dim[0] - horiz_space, box_width + space_between):
        if i < screen_dim[0] - space_between - 100:
            boxes.append(Box(i, j))

while running:
    # getting mouse position
    mouse_x, mouse_y = pg.mouse.get_pos()

    # filling the back ground
    screen.fill(YELLOW)

    # drawing all the boxes
    for box in boxes:
        box.draw()

    # making and moving the paddle
    paddle = pg.draw.rect(screen, RED, (paddle_x, dist, paddle_width, paddle_height))
    paddle_x = mouse_x - int(paddle_width / 2)

    # making and moving the ball
    ball = pg.draw.circle(screen, BLUE, (math.ceil(ball_x), ball_y), 15, 0)
    ball_x += ball_move_x
    ball_y += ball_move_y

    # preventing the ball to go out of bounds
    if ball_x < 0:
        ball_x += 20
        ball_move_x *= -1
    elif ball_x > screen_dim[0]:
        ball_x -= 20
        ball_move_x *= -1
    elif ball_y < 0:
        ball_move_y *= -1
    elif ball_y > screen_dim[0]:
        tries -= 1
        if tries == 0:
            break
        else:
            ball_x = int(screen_dim[0] / 2)
            ball_y = dist - 20
            ball_move_y = -10
            ball_move_x = 10

    # checking ball collision
    if ball.colliderect(paddle):
        ball_move_y = -ball_speed
        deltaX = ball_x - (paddle_x + paddle_width / 2);
        ball_move_x = deltaX * 0.3
    for k in boxes:
        if ball.colliderect(k.bx):
            ball_move_x *= -1
            ball_move_y *= -1
            boxes.remove(k)

    # winning condition
    if not boxes:
        break

    # getting events
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

    # updating the screen
    pg.display.update()

    # defining the frames per second
    fpsClock.tick(FPS)

font = pg.font.Font('freesansbold.ttf', 32)
if tries == 0:
    screen.fill(RED)
    text = font.render("You lose! :(", True, GREEN)
    text_rect = text.get_rect()
    text_rect.center = (int(screen_dim[0] / 2), int(screen_dim[1] / 2))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(3)

elif not boxes:
    screen.fill(RED)
    text = font.render("You win! :)", True, GREEN)
    text_rect = text.get_rect()
    text_rect.center = (int(screen_dim[0] / 2), int(screen_dim[1] / 2))
    screen.blit(text, text_rect)
    pg.display.update()
    time.sleep(3)

pg.quit()
