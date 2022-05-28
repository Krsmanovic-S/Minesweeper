import pygame
pygame.init()

# WINDOW SETTINGS
HEIGHT = 800
WIDTH = 800

# URLS
GIT_URL = 'https://github.com/Krsmanovic-S/'
LINKEDIN_URL = 'https://www.linkedin.com/in/stefan-krsmanovic-7698a4235/'

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER = (45.9, 45.9, 45.9)
GRAY = (72.5, 72.5, 72.5)
RED = (255, 0, 0)

# ICONS
WINDOW_ICON = pygame.image.load('images/icon.png')
GIT_ICON = pygame.image.load('images/buttons/git_button.png')
LINKEDIN_ICON = pygame.image.load('images/buttons/linkedin_button.png')

HIGHLIGHTED_GIT = pygame.image.load('images/buttons/highlighted_git.png')
HIGHLIGHTED_LINKEDIN = pygame.image.load('images/buttons/highlighted_linkedin.png')

# IMAGES
BG = pygame.image.load('images/background.png')
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
PLAY_BUTTON = pygame.image.load('images/buttons/play_button.png')
SETTINGS_BUTTON = pygame.image.load('images/buttons/settings_button.png')
EXIT_BUTTON = pygame.image.load('images/buttons/exit_button.png')

GRID_SETTINGS_BUTTON = pygame.image.load('images/buttons/grid_settings.png')
MINE_COUNT_BUTTON = pygame.image.load('images/buttons/mine_count_button.png')
TEST = pygame.image.load('images/buttons/button_template.png')

HIGHLIGHTED_PLAY = pygame.image.load('images/buttons/highlighted_play.png')
HIGHLIGHTED_SETTINGS = pygame.image.load('images/buttons/highlighted_settings.png')
HIGHLIGHTED_EXIT = pygame.image.load('images/buttons/highlighted_exit.png')
HIGHLIGHTED_GRID_SETTINGS = pygame.image.load('images/buttons/highlighted_grid_settings.png')
HIGHLIGHTED_MINE_COUNT = pygame.image.load('images/buttons/highlighted_mine_count.png')

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
