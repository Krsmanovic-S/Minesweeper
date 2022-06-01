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
GRAY = (30.5, 30.5, 30.5)

# ICONS
WINDOW_ICON = pygame.image.load('images/icon.png')
GIT_ICON = pygame.image.load('images/buttons/git_button.png')
LINKEDIN_ICON = pygame.image.load('images/buttons/linkedin_button.png')

HIGHLIGHTED_GIT = pygame.image.load('images/buttons/highlighted/highlighted_git.png')
HIGHLIGHTED_LINKEDIN = pygame.image.load('images/buttons/highlighted/highlighted_linkedin.png')

# IMAGES
BG = pygame.image.load('images/background.png')
EMPTY = pygame.image.load('images/tiles/empty_tile.png')
ONE = pygame.image.load('images/tiles/one.png')
TWO = pygame.image.load('images/tiles/two.png')
THREE = pygame.image.load('images/tiles/three.png')
FOUR = pygame.image.load('images/tiles/four.png')
FIVE = pygame.image.load('images/tiles/five.png')
SIX = pygame.image.load('images/tiles/six.png')
SEVEN = pygame.image.load('images/tiles/seven.png')
EIGHT = pygame.image.load('images/tiles/eight.png')
FLAG = pygame.image.load('images/tiles/flag.png')
MINE = pygame.image.load('images/tiles/mine.png')
CLOSED = pygame.image.load('images/tiles/closed_tile.png')
HIGHLIGHTED_CLOSED = pygame.image.load('images/tiles/highlighted_closed.png')
QUESTION_MARK = pygame.image.load('images/tiles/question_mark.png')

# BUTTONS
PLAY_BUTTON = pygame.image.load('images/buttons/play_button.png')
SETTINGS_BUTTON = pygame.image.load('images/buttons/settings_button.png')
EXIT_BUTTON = pygame.image.load('images/buttons/exit_button.png')

GRID_SETTINGS_BUTTON = pygame.image.load('images/buttons/grid_settings.png')
MINE_COUNT_BUTTON = pygame.image.load('images/buttons/mine_count_button.png')
QUESTION_MARK_ENABLED = pygame.image.load('images/buttons/enabled_question_mark.png')
QUESTION_MARK_DISABLED = pygame.image.load('images/buttons/disabled_question_mark.png')

BACK_BUTTON = pygame.image.load('images/buttons/back_button.png')

TEST = pygame.image.load('images/buttons/button_template.png')

SMILEY_BUTTON = pygame.image.load('images/buttons/smiley_tile.png')
WON_SMILEY_BUTTON = pygame.image.load('images/buttons/won_smiley_tile.png')
DEAD_SMILEY_BUTTON = pygame.image.load('images/buttons/dead_smiley_tile.png')

# HIGHLIGHTED BUTTONS
HIGHLIGHTED_PLAY = pygame.image.load('images/buttons/highlighted/highlighted_play.png')
HIGHLIGHTED_SETTINGS = pygame.image.load('images/buttons/highlighted/highlighted_settings.png')
HIGHLIGHTED_EXIT = pygame.image.load('images/buttons/highlighted/highlighted_exit.png')

HIGHLIGHTED_GRID_SETTINGS = pygame.image.load('images/buttons/highlighted/highlighted_grid_settings.png')
HIGHLIGHTED_MINE_COUNT = pygame.image.load('images/buttons/highlighted/highlighted_mine_count.png')
HIGHLIGHTED_ENABLED_QUESTION = pygame.image.load('images/buttons/highlighted/highlighted_enabled_question.png')
HIGHLIGHTED_DISABLED_QUESTION = pygame.image.load('images/buttons/highlighted/highlighted_disabled_question.png')

HIGHLIGHTED_BACK_BUTTON = pygame.image.load('images/buttons/highlighted/highlighted_back_button.png')

HIGHLIGHTED_SMILEY = pygame.image.load('images/buttons/highlighted/highlighted_smiley.png')
HIGHLIGHTED_WON_SMILEY = pygame.image.load('images/buttons/highlighted/highlighted_won_smiley.png')
HIGHLIGHTED_DEAD_SMILEY = pygame.image.load('images/buttons/highlighted/highlighted_dead_smiley.png')

# CLOCK IMAGES
CLOCK_0 = pygame.image.load('images/clock/clock_0.png')
CLOCK_1 = pygame.image.load('images/clock/clock_1.png')
CLOCK_2 = pygame.image.load('images/clock/clock_2.png')
CLOCK_3 = pygame.image.load('images/clock/clock_3.png')
CLOCK_4 = pygame.image.load('images/clock/clock_4.png')
CLOCK_5 = pygame.image.load('images/clock/clock_5.png')
CLOCK_6 = pygame.image.load('images/clock/clock_6.png')
CLOCK_7 = pygame.image.load('images/clock/clock_7.png')
CLOCK_8 = pygame.image.load('images/clock/clock_8.png')
CLOCK_9 = pygame.image.load('images/clock/clock_9.png')

# DICTIONARY FOR CLOCK DIGITS
CLOCK_DIGITS = {
    0: CLOCK_0,
    1: CLOCK_1,
    2: CLOCK_2,
    3: CLOCK_3,
    4: CLOCK_4,
    5: CLOCK_5,
    6: CLOCK_6,
    7: CLOCK_7,
    8: CLOCK_8,
    9: CLOCK_9,
}

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
    10: FLAG,
    11: CLOSED,
    12: HIGHLIGHTED_CLOSED,
    13: QUESTION_MARK
}
