import pygame as pg
import random
import time
from pygame.locals import *

pg.init()

# frames per second setting
FPS = 10
fpsClock = pg.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
NAVYBLUE = (60, 60, 100)

# general variables
running = True
shapes = ["donut", "square", "diamond", "lines", "oval"]
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]
column_boxes = 10
row_boxes = 7
space = 10
margin = 50
blocksize = 60
block_list = []
moves = 0
selected = []

# screen variables
screen_dim = (column_boxes * (blocksize + space) + margin * 2, (row_boxes * (blocksize + space) + margin * 2))
screen = pg.display.set_mode(screen_dim)
pg.display.set_caption('Memory Game')

all_combs = []
for i in colors:
    for j in shapes:
        all_combs.append((i, j))
all_combs = all_combs * 2
random.shuffle(all_combs)


class Blocks:
    def __init__(self, index, info):
        self.info = info
        self.shape = self.info[1]
        self.color = self.info[0]
        self.index = index
        self.x = int(margin + (self.index % column_boxes) * (space + blocksize))
        self.y = int(margin + ((self.index - (self.index % column_boxes))/column_boxes) * (blocksize + space))
        self.clicked = False

    def draw(self):
        if self.clicked == False:
            self.bl = pg.draw.rect(screen, WHITE, (self.x, self.y, blocksize, blocksize))
        else:
            self.bl = pg.draw.rect(screen, NAVYBLUE, (self.x, self.y, blocksize, blocksize))
            if self.shape == "donut":
                pg.draw.circle(screen, self.color, (self.x + int(blocksize/2), self.y + int(blocksize/2)), int(blocksize/2) - 5)
                pg.draw.circle(screen, NAVYBLUE, (self.x + int(blocksize/2), self.y + int(blocksize/2)), int(blocksize/4) - 5)
            elif self.shape == "square":
                pg.draw.rect(screen, self.color, (self.x + int(blocksize/4), self.y + int(blocksize/4), int(blocksize/2), int(blocksize/2)))
            elif self.shape == "diamond":
                pg.draw.polygon(screen, self.color, ((self.x + int(blocksize/2), self.y), (self.x + blocksize - 1, self.y + int(blocksize/2)), (self.x + int(blocksize/2), self.y + blocksize - 1), (self.x, self.y + int(blocksize/2))))
            elif self.shape == "lines":
                for a in range(0, blocksize, 4):
                    pg.draw.line(screen, self.color, (self.x, self.y + a), (self.x + a, self.y))
                    pg.draw.line(screen, self.color, (self.x + a, self.y + blocksize - 1), (self.x + blocksize - 1, self.y + a))
            else:
                pg.draw.ellipse(screen, self.color, (self.x, self.y + int(blocksize/4), blocksize, int(blocksize/2)))

    def hover_highlight(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x < mouse_x < self.x + blocksize and self.y < mouse_y < self.y + blocksize and not self.clicked:
            pg.draw.line(screen, BLUE, (self.x-4, self.y-4), (self.x-4, self.y+blocksize+4), 4)
            pg.draw.line(screen, BLUE, (self.x-4, self.y+blocksize+4), (self.x+blocksize+4, self.y+blocksize+4), 4)
            pg.draw.line(screen, BLUE, (self.x+blocksize+4, self.y-4), (self.x+blocksize+4, self.y+blocksize+4), 4)
            pg.draw.line(screen, BLUE, (self.x-4, self.y-4), (self.x+blocksize+4, self.y-4), 4)

    def on_click(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if event.type == MOUSEBUTTONUP:
            if self.x < mouse_x < self.x + blocksize and self.y < mouse_y < self.y + blocksize:
                global moves
                global selected
                self.clicked = True
                moves += 1
                selected.append(self)



for i in range(70):
    block_list.append(Blocks(i, all_combs[i]))

while running:
    # filling the screen
    screen.fill(NAVYBLUE)

    # drawing the blocks
    for block in block_list:
        block.draw()
        block.hover_highlight()

    if len(selected) == 2:
        if selected[0].info == selected[1].info:
            selected[0].clicked = True
            selected[1].clicked = True
        else:
            pg.display.update()
            time.sleep(0.5)
            selected[0].clicked = False
            selected[1].clicked = False
        selected = []

    # getting events
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        for b in block_list:
            b.on_click()

    # updating the screen
    pg.display.update()

    # defining the frames per second
    fpsClock.tick(FPS)

pg.quit()
