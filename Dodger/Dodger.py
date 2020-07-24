import pygame as pg
import random
import time
from pygame.locals import *

pg.init()

# frames per second setting
FPS = 10
fpsClock = pg.time.Clock()

# fonts
font = pg.font.Font('freesansbold.ttf', 32)

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DEEPGREEN = (12, 235, 19)
BLUE = (0, 0, 255)
BROWN = (209, 53, 53)
YELLOW = (255, 255, 0)

# screen variables
screen_dim = (600, 600)
screen = pg.display.set_mode(screen_dim)
pg.display.set_caption('Dodger')

# general variables
running = True
obstacle_blocks = []
overcome = 0

class Block():
    def __init__(self):
        # obstacle_blocks.append(self)
        self.x = random.randint(0, screen_dim[0])
        self.y = 0
        self.blocksize = random.randint(10, 100)
        self.move_y = random.randint(1, 5)

    def draw(self):
        self.bl = pg.draw.rect(screen, GREEN, (self.x, self.y, self.blocksize, self.blocksize))
        self.x += random.randint(-10, 10)
        self.y += self.move_y
        if self.y == screen_dim[1]:
            obstacle_blocks.remove(self)
            global overcome
            overcome += 1

for i in range(10):
    obstacle_blocks.append(Block())

n = 0
while running:
    n += 1
    if n % 7 == 0:
        obstacle_blocks.append(Block())

    # filling the screen
    screen.fill(RED)

    mouse_x = pg.mouse.get_pos()[0]
    player = pg.draw.rect(screen, BLUE, (mouse_x, screen_dim[1]-70, 50, 50))

    # drawing the obstacle blocks
    for block in obstacle_blocks:
        block.draw()
        if player.colliderect(block.bl):
            running = False

    # getting events
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

    # updating the screen
    pg.display.update()

    # defining the frames per second
    fpsClock.tick(FPS)

screen.fill(YELLOW)
screen.blit(font.render("You got hit! Your score is: {}".format(overcome), True, GREEN),(100, int(screen_dim[1]/2)))
pg.display.update()
time.sleep(5)
pg.quit()
