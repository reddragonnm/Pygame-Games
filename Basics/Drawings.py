import pygame
from pygame.locals import *

dim = (500, 400)
SCREEN = pygame.display.set_mode(dim, 0, 32)
pygame.display.set_caption("Drawing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# fill(color)
SCREEN.fill(WHITE)

# pygame.draw.polygon(surface, color, pointlist(list or tuple), width)
pygame.draw.polygon(SCREEN, GREEN, [(146, 0), (291, 106), (236, 277),(56, 277), (0, 106)])

# pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.line(SCREEN, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(SCREEN, BLUE, (120, 60), (60, 120))
pygame.draw.line(SCREEN, BLUE, (60, 120), (120, 120), 4)

# pygame.draw.circle(surface, color, center_point, radius, width)
pygame.draw.circle(SCREEN, BLUE, (300, 50), 20, 0)

# pygame.draw.ellipse(surface, color, bounding_rectangle, width)
pygame.draw.ellipse(SCREEN, RED, (300, 250, 40, 80), 1)

# pygame.draw.rect(surface, color, rectangle_tuple, width)
pygame.draw.rect(SCREEN, RED, (200, 150, 200, 10))

pixObj = pygame.PixelArray(SCREEN)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        pygame.display.update()