import pygame
pygame.init()

# WINDOW SETTINGS
HEIGHT = 1000
WIDTH = 1000
WINDOW_ICON = pygame.image.load('images/icon.png')

CELL_SIZE = 100

# COLORS
BORDER = (45.9, 45.9, 45.9)
GRAY = (72.5, 72.5, 72.5)
OPENED = (90.5, 90.5, 90.5)
RED = (255, 0, 0)

# IMAGES
EMPTY = pygame.image.load('images/empty_tile.png')
ONE = pygame.image.load('images/one.png')
TWO = pygame.image.load('images/two.png')
THREE = pygame.image.load('images/three.png')
FOUR = pygame.image.load('images/four.png')
FIVE = pygame.image.load('images/five.png')
SIX = pygame.image.load('images/six.png')
SEVEN = pygame.image.load('images/seven.png')
EIGHT = pygame.image.load('images/eight.png')
FLAG = pygame.image.load('images/flag.png')
MINE = pygame.image.load('images/mine.png')

# BUTTONS
TEST = pygame.image.load('images/buttons/button_template.png')

# DICTIONARY FOR DRAWING
DRAWING = {
    0: EMPTY,
    1: ONE,
    2: TWO,
    3: THREE,
    4: FOUR,
    5: FIVE,
    6: SIX,
    7: SEVEN,
    8: EIGHT,
    9: MINE,
    10: FLAG
}
