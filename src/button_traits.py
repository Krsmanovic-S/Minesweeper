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
    def draw_button(self, window, mouse):
        if self.rect.collidepoint(mouse[0] - 5, mouse[1] - 5):
            window.blit(self.highlighted, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def is_mouse_over(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw_changing_button(self, window, mouse, button, check: bool):
        # This function is used for buttons which have multiple images
        # representing them, here we can decide which one to show.
        if not check:
            self.draw_button(window, mouse)
        else:
            button.draw_button(window, mouse)


# Main Menu Buttons
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
        return HIGHLIGHTED_GRID_SETTINGS

class Test2(Grid):
    y = int(325)

    @default('image')
    def _default_image(self):
        return TEST

    @default('highlighted')
    def _default_highlighted(self):
        return TEST


class Test1(Button):
    x = int(425)
    y = int(75)

    @default('image')
    def _default_image(self):
        return TEST

    @default('highlighted')
    def _default_highlighted(self):
        return TEST


class Test3(Test1):
    y = int(325)

    @default('image')
    def _default_image(self):
        return TEST

    @default('highlighted')
    def _default_highlighted(self):
        return TEST
