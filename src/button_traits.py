from traitlets import HasTraits, Int, default, Any
from constants import *


class Button(HasTraits):
    x = Int()
    y = Int()
    highlighted = Any()
    image = Any()
    rect = Any()

    @default('rect')
    def _default_rect(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        return self.rect

    # Functions
    def draw_button(self, window: pygame.display, mouse: tuple):
        if self.rect.collidepoint(mouse[0] - 5, mouse[1] - 5):
            window.blit(self.highlighted, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def is_mouse_over(self, mouse_pos: tuple):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False


# Main Menu Buttons
class Git(Button):
    x = int(25)
    y = int(675)

    @default('image')
    def _default_image(self):
        return GIT_ICON

    @default('highlighted')
    def _default_highlighted(self):
        return HIGHLIGHTED_GIT


class LinkedIn(Git):
    x = int(675)

    @default('x')
    def _default_x(self):
        return WIDTH // 2 - 200

    @default('image')
    def _default_image(self):
        return LINKEDIN_ICON

    @default('highlighted')
    def _default_highlighted(self):
        return HIGHLIGHTED_LINKEDIN


class Smiley(Button):
    x = WIDTH // 2 - 40
    y = 13

    def update_smiley_picture(self, check: int):
        if check == 0:
            self.image = DEAD_SMILEY_BUTTON
            self.highlighted = HIGHLIGHTED_DEAD_SMILEY
        elif check == 1:
            self.image = SMILEY_BUTTON
            self.highlighted = HIGHLIGHTED_SMILEY
        else:
            self.image = WON_SMILEY_BUTTON
            self.highlighted = HIGHLIGHTED_WON_SMILEY


class Play(Button):
    y = int(100)

    @default('x')
    def _default_x(self):
        return WIDTH // 2 - 200

    @default('image')
    def _default_image(self):
        return PLAY_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HIGHLIGHTED_PLAY


class Settings(Play):
    y = int(380)

    @default('image')
    def _default_image(self):
        return SETTINGS_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HIGHLIGHTED_SETTINGS


class Exit(Play):
    y = int(580)

    @default('image')
    def _default_image(self):
        return EXIT_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HIGHLIGHTED_EXIT


# Settings Menu Buttons
class Grid(Button):
    x = int(25)
    y = int(75)

    @default('image')
    def _default_image(self):
        return GRID_SETTINGS_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return GRID_SETTINGS_BUTTON


class QuestionTile(Grid):
    y = int(325)

    def update_question_tile(self, check: bool):
        if not check:
            self.image = QUESTION_MARK_DISABLED
            self.highlighted = HIGHLIGHTED_DISABLED_QUESTION
        else:
            self.image = QUESTION_MARK_ENABLED
            self.highlighted = HIGHLIGHTED_ENABLED_QUESTION


class MineCount(Button):
    x = int(425)
    y = int(75)

    @default('image')
    def _default_image(self):
        return MINE_COUNT_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return MINE_COUNT_BUTTON


class Timer(MineCount):
    y = int(325)

    @default('image')
    def _default_image(self):
        return TEST

    @default('highlighted')
    def _default_highlighted(self):
        return TEST


class Back(Button):
    x = int(WIDTH // 2 - 175)
    y = int(550)

    @default('image')
    def _default_image(self):
        return BACK_BUTTON

    @default('highlighted')
    def _default_highlighted(self):
        return HIGHLIGHTED_BACK_BUTTON
