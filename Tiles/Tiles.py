import pygame as pg
import random
from pygame.locals import *

pg.init()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SKYBLUE = (68, 234, 252)
WHITE = (255, 255, 255)

# screen variables
screen_dim = (600, 600)
screen = pg.display.set_mode(screen_dim)
pg.display.set_caption('Tiles')

# fonts
font = pg.font.Font('freesansbold.ttf', 32)

# general variables
running = True
sol = list(range(15)) + [" "]
puzzle = sol.copy()
random.shuffle(sol)

# block variables
blocks = []
blocksize = 100
boundary = 100
space = 2


class Block:
    def __init__(self, index):
        self.n = str(sol[index])
        self.index = index
        self.y = int(((index - (index % 4)) / 4 * blocksize) + boundary + (index - (index % 4)) * space)
        self.x = int(((index % 4) * blocksize) + boundary + ((index % 4) * space))

    def draw(self):
        if self.n != " ":
            self.bl = pg.draw.rect(screen, GREEN, (self.x, self.y, blocksize, blocksize))
        else:
            self.bl = pg.draw.rect(screen, SKYBLUE, (self.x, self.y, blocksize, blocksize))
        screen.blit(font.render(self.n, True, WHITE), (self.x + int(blocksize/2) - 10, self.y + int(blocksize/2) - 10))

    def check_mouse_click(self):
        # self.x - blocksize - space = another block
        # self.x + blocksize + space = another block
        # self.y - blocksize - space = another block
        # self.y + blocksize + space = another block

        self.adjacent_blocks = []
        for bx in blocks:
            if bx.x == self.x - blocksize - space and bx.y == self.y:
                self.adjacent_blocks.append(bx)
            if bx.x == self.x + blocksize + space and bx.y == self.y:
                self.adjacent_blocks.append(bx)

            if self.y - blocksize - space - 20 < bx.y < self.y - blocksize - space + 20 and bx.x == self.x:
                self.adjacent_blocks.append(bx)
            if self.y + blocksize + space - 20 < bx.y < self.y + blocksize + space + 20 and bx.x == self.x:
                self.adjacent_blocks.append(bx)

        mouse_x, mouse_y = pg.mouse.get_pos()
        if event.type == MOUSEBUTTONUP:
            if self.n != " ":
                if self.x < mouse_x < (self.x + blocksize) and self.y < mouse_y < (self.y + blocksize):
                    for b in self.adjacent_blocks:
                        if b.n == " ":
                            b.x, self.x = self.x, b.x
                            b.y, self.y = self.y, b.y
                            break
                        else:
                            continue



for i in range(16):
    blocks.append(Block(i))

while running:
    # filling the screen
    screen.fill(SKYBLUE)

    # drawing the blocks
    for block in blocks:
        block.draw()

    if puzzle == sol:
        break

    # getting the events
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        for block in blocks:
            block.check_mouse_click()

    # filling the screen
    pg.display.update()

pg.quit()
