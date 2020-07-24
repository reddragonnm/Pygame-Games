import pygame as pg
from pygame.locals import *
pg.init()

# Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

dim = (600, 800)
screen = pg.display.set_mode(dim)
running = True
background = GREEN

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                background = RED
            elif event.key == K_g:
                background = GREEN
            elif event.key == K_b:
                background = BLUE

            caption = 'background color = ' + str(background)
            pg.display.set_caption(caption)

    screen.fill(background)
    pg.display.update()
    
pg.quit()
